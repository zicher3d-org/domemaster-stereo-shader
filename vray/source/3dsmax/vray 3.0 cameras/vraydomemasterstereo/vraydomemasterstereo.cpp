/**********************************************************************
  FILE: vraydomemasterstereo.cpp
  
  vray DomemasterStereo Shader v0.5
  2015-02-07

  Ported to Vray 3.0 by Andrew Hazelden/Roberto Ziche
  Based upon the mental ray shader domeAFL_FOV_Stereo by Roberto Ziche

  Todo:
  [rz] Bitmap to Texmap
  [rz] Relocate bCol definition
  [rz] Bool parameters (from int)
  [rz] Remove pb_fov (pb2 enum)
  [rz] Adjust default parameter values based on scene units?
  [rz] Black outer frame.
          Return false by GetScreenRay() does not work. Ray computed no matter what. Should render black.

**********************************************************************/

#include "max.h"
#include "gencam.h"
#include "macrorec.h"
#include "decomp.h"
#include "iparamb2.h"
#include "iparamm2.h"
#include "utils.h"
#include "pb2template_generator.h"
#include "imtl.h"
#include "bitmap.h"
#include "maxscript\maxscript.h"

#include "vraybase.h"
#include "vrayinterface.h"
#include "shadedata_new.h"
#include "tomax.h"
#include "vrayrenderer.h"
#include "vraycam.h"
#include "rayserver.h"
#include "vraygeom.h"
#include "raybunchcamera.h"
#include "vraydomemasterstereo.h"

#include "resource.h"

// no param block script access for VRay free
#ifdef _FREE_
#define _FT(X) _T("")
#define IS_PUBLIC 0
#else
#define _FT(X) _T(X)
#define IS_PUBLIC 1
#endif // _FREE_

using namespace VRayDomemasterStereo;

//************************************************************
// #defines
//************************************************************

#define CENTERCAM     0
#define LEFTCAM       1
#define RIGHTCAM      2

#define DOME_PI       3.141592653589793238
#define DOME_DTOR     0.0174532925199433
#define DOME_RTOD     57.295779513082321
#define DOME_PIOVER2  1.57079632679489661923
#define DOME_EPSILON  0.00001

#define GETDIR        0
#define GETORG        1

#define PLUGIN_CLASSID Class_ID(0x511a5e3e, 0x61393d01)

#define STR_CLASSNAME _T("VRayDomemasterStereo")
#define STR_INTERNALNAME _T("VRayDomemasterStereo")
#define STR_LIBDESC _T("VRayDomemasterStereo plugin")
#define STR_DLGTITLE _T("VRayDomemasterStereo Parameters")
#define STR_CATEGORY _T("VRay")

//************************************************************
// The definition of the VRayCamera
//************************************************************

// [rz] relocate?
BMM_Color_64 bCol;

#define REFNO_PBLOCK 0

class VRayCamera: public GenCamera, public VR::VRayCamera {
  IParamMap2 *pmap;
  static Mesh mesh;
  static int meshBuilt;
  int extendedDisplayFlags;

  void buildMesh(void);
  void getTM(TimeValue t, INode *node, ViewExp *vpt, Matrix3 &tm);
  void drawLine(TimeValue t, INode *node, ViewExp *vpt);

  // Cached parameters during rendering
  float fov;
  float targetDist;
  float aperture;

  VR::PinholeCamera camera;
  VR::VRayRenderer *vray;

public:
  IParamBlock2 *pblock;

  int suspendSnap; // TRUE only during creation

  int   stereo_camera;
  float fov_angle; 
  float parallax_distance;
  float separation;
  float forward_tilt;
  int   tilt_compensation;
  int   vertical_mode;
  PBBitmap *separation_map;
  PBBitmap *head_turn_map;
  PBBitmap *head_tilt_map;
  float neck_offset;
  int   flip_x;
  int   flip_y;

  // Constructor/destructor
  VRayCamera(void);
  ~VRayCamera(void);

  // From GenCamera
  GenCamera* NewCamera(int type) { return new VRayCamera; }
  void SetConeState(int s) {}
  int GetConeState(void) { return FALSE; }
  void SetHorzLineState(int s) {}
  int GetHorzLineState(void) { return FALSE; }
  void Enable(int onOff) {}
  BOOL SetFOVControl(Control *c) {
#if MAX_RELEASE<13900
    // [rz] pblock->SetController(pblock->IDtoIndex(pb_fov), 0, c);
#else
    // [rz] pblock->SetControllerByID((ParamID) pb_fov, 0, c);
#endif
    return TRUE;
  }
  Control *GetFOVControl() {
#if MAX_RELEASE<13900
    return pblock->GetController((ParamID) pb_fov);
#else
    return pblock->GetControllerByID((ParamID) pb_fov);
#endif
  }
  void SetFOVType(int ft) {}
  int GetFOVType(void) { return 0; } // FOV_W
  int Type(void) { return FREE_CAMERA; }
  void SetType(int type) {}

  // From CameraObject
  RefResult EvalCameraState(TimeValue time, Interval &valid, CameraState *cs);
  void SetOrtho(BOOL b) {}
  BOOL IsOrtho(void) { return FALSE; }
  void SetFOV(TimeValue t, float f) { /* [rz] pblock->SetValue(pb_fov, t, f);*/ }
  float GetFOV(TimeValue t, Interval &valid) { float res; /* [rz] pblock->GetValue(pb_fov, t, res, valid);*/ res = 1.0f; return res; }
  void SetTDist(TimeValue t, float f) {}
  float GetTDist(TimeValue t, Interval &valid=FOREVER) { return 100.0f; }
  int GetManualClip(void) { return FALSE; }
  void SetManualClip(int onOff) {}
  float GetClipDist(TimeValue t, int which, Interval &valid) { return (which==CAM_HITHER_CLIP)? 0.0f : 1e6f; }
  void SetClipDist(TimeValue t, int which, float val) {}
  void SetEnvRange(TimeValue t, int which, float f) {}
  float GetEnvRange(TimeValue t, int which, Interval &valid) { return (which==ENV_NEAR_RANGE)? 0.0f: 1e6f; }
  void SetEnvDisplay(BOOL b, int notify) {}
  BOOL GetEnvDisplay(void) { return FALSE; }
  void RenderApertureChanged(TimeValue t) {}
  void UpdateTargDistance(TimeValue t, INode *node) {}

  // From Object
  ObjectState Eval(TimeValue time) { return ObjectState(this); }
  void InitNodeName(TSTR& s) { s=STR_CLASSNAME; }
  int DoOwnSelectHilite() { return TRUE; }
  Interval ObjectValidity(TimeValue time) { Interval res=FOREVER; pblock->GetValidity(time, res); return res; }
  BOOL UsesWireColor() { return TRUE; }
  int CanConvertToType(Class_ID obtype) { return FALSE; }
  Object* ConvertToType(TimeValue t, Class_ID obtype) { assert(0); return NULL; }

  void GetWorldBoundBox(TimeValue t, INode *mat, ViewExp *vpt, Box3& box);
  void GetLocalBoundBox(TimeValue t, INode *mat, ViewExp *vpt, Box3& box);

  // From BaseObject
  int HitTest(TimeValue t, INode* inode, int type, int crossing, int flags, IPoint2 *p, ViewExp *vpt);
  void Snap(TimeValue t, INode* inode, SnapInfo *snap, IPoint2 *p, ViewExp *vpt);
  void SetExtendedDisplay(int flags) { extendedDisplayFlags=flags; }
  int Display(TimeValue t, INode* inode, ViewExp *vpt, int flags);

#if MAX_RELEASE >= 14850
  const TCHAR *GetObjectName(void) { return STR_CLASSNAME; }
#else
  TCHAR *GetObjectName(void) { return STR_CLASSNAME; }
#endif
  CreateMouseCallBack* GetCreateMouseCallBack();

  void BeginEditParams(IObjParam *ip, ULONG flags, Animatable *prev);
  void EndEditParams(IObjParam *ip, ULONG flags, Animatable *next);
  void InvalidateUI(void);

  // From ReferenceTarget
#if GET_MAX_RELEASE(VERSION_3DSMAX) < 8900
  RefTargetHandle Clone(RemapDir& remap=NoRemap());
#else
  RefTargetHandle Clone(RemapDir& remap=DefaultRemapDir());
#endif

  // From ReferenceMaker
  RefResult NotifyRefChanged(NOTIFY_REF_CHANGED_ARGS);
  int NumRefs(void) { return 1; }
  RefTargetHandle GetReference(int i) { return (i==0)? pblock : NULL; }
  void SetReference(int i, RefTargetHandle rtarg) { if (i==0) pblock=(IParamBlock2*) rtarg; }

  // IOResult Load(ILoad *load);
  // IOResult Save(ISave *save);

  // From Animatable
  void DeleteThis() { delete this; }
  Class_ID ClassID() { return PLUGIN_CLASSID; }
  void GetClassName(TSTR& s) { s=STR_CLASSNAME; }
  int IsKeyable() { return 0; }

  int NumParamBlocks() { return 1; }  
  IParamBlock2* GetParamBlock(int i) { return pblock; }
  IParamBlock2* GetParamBlockByID(BlockID id) { return (pblock->ID() == id) ? pblock : NULL; }

  int NumSubs() { return 1; }  
  Animatable* SubAnim(int i) { return (i==0)? pblock : NULL; }
  TSTR SubAnimName(int i) { return (i==0)? STR_DLGTITLE : _T("<???>"); }
  void* GetInterface(ULONG id) { return (id==I_VRAYCAMERA)? (VR::VRayCamera*) this : GenCamera::GetInterface(id); }
  void ReleaseInterface(ULONG id, void *ip) {
    if (id==I_VRAYCAMERA);
    else GenCamera::ReleaseInterface(id, ip);
  }

  // From VRayCamera
  virtual int getScreenRay(double xs, double ys, double time, float dof_uc, float dof_vc, VR::TraceRay &ray, VR::Ireal &mint, VR::Ireal &maxt, VR::RayDeriv &rayDeriv, VR::Color &multResult) const;
  virtual int getScreenRays(  VR::RayBunchCamera& raysbunch,
                              const double* xs,   const double* ys, 
                              const float* dof_uc, const float* dof_vc, 
                              bool calcDerivs = false ) const;
  void renderBegin(VR::VRayRenderer *vray);
  void renderEnd(VR::VRayRenderer *vray);
  void frameBegin(VR::VRayRenderer *vray);
  void frameEnd(VR::VRayRenderer *vray);
  
  VR::Vector getDir(double xs, double ys, int rayVsOrgReturnMode) const;
};

//************************************************************
// Class descriptor
//************************************************************

class CameraClassDesc:public ClassDesc2 {
public:
  int IsPublic() { return IS_PUBLIC; }
  void* Create(BOOL loading) { return new VRayCamera; }
  const TCHAR* ClassName() { return STR_CLASSNAME; }
  SClass_ID SuperClassID() { return CAMERA_CLASS_ID; }
  Class_ID ClassID() { return PLUGIN_CLASSID; }
  const TCHAR* Category() { return STR_CATEGORY; }

  // Hardwired name, used by MAX Script as unique identifier
  const TCHAR*  InternalName() { return STR_INTERNALNAME; }
  HINSTANCE HInstance() { return hInstance; }
};

static CameraClassDesc cameraClassDesc;

//************************************************************
// DLL stuff
//************************************************************

HINSTANCE hInstance;
int controlsInit=FALSE;

BOOL WINAPI DllMain(HINSTANCE hinstDLL,ULONG fdwReason,LPVOID lpvReserved) {
  hInstance=hinstDLL;

  if (!controlsInit) {
    controlsInit=TRUE;
#if MAX_RELEASE<13900
    InitCustomControls(hInstance);
#endif
    InitCommonControls();
  }
  return(TRUE);
}

__declspec(dllexport) const TCHAR* LibDescription() { return STR_LIBDESC; }
__declspec(dllexport) int LibNumberClasses() { return 1; }

__declspec( dllexport ) ClassDesc* LibClassDesc(int i) {
  switch(i) { case 0: return &cameraClassDesc; }
  return NULL;
}

__declspec( dllexport ) ULONG LibVersion() { return VERSION_3DSMAX; }

TCHAR *GetString(int id) {
  static TCHAR buf[256];
  if (hInstance) return LoadString(hInstance, id, buf, sizeof(buf)) ? buf : NULL;
  return NULL;
}

//************************************************************
// Parameter block
//************************************************************

class VRayCamera_PBAccessor : public PBAccessor
{
  void Set(PB2Value& v, ReferenceMaker* owner, ParamID id, int tabIndex, TimeValue t)
  {
    VRayCamera *cam = (VRayCamera*)owner;
    IParamMap2* pmap = cam->pblock->GetMap();
    TSTR p, f, e, name;

    switch (id) {
      case pb_separation_map: {
        if (pmap) {
          TSTR sepname(v.bm->bi.Name());
          SplitFilename(sepname, &p, &f, &e);
          name = f + e;
          pmap->SetText(pb_separation_map, name.data());
        } break;
      }
      case pb_head_turn_map: {
        if (pmap) {
          TSTR sepname(v.bm->bi.Name());
          SplitFilename(sepname, &p, &f, &e);
          name = f + e;
          pmap->SetText(pb_head_turn_map, name.data());
        } break;
      }
      case pb_head_tilt_map: {
        if (pmap) {
          TSTR sepname(v.bm->bi.Name());
          SplitFilename(sepname, &p, &f, &e);
          name = f + e;
          pmap->SetText(pb_head_tilt_map, name.data());
        } break;
      }
      default: break;
    }
  }
};

static VRayCamera_PBAccessor pb_accessor;

// Paramblock2 name
enum { camera_params }; 

static int ctrlID = 100;
int nextID(void) { return ctrlID++; }

static ParamBlockDesc2 camera_param_blk(camera_params, STR_DLGTITLE,  0, &cameraClassDesc,
  P_AUTO_CONSTRUCT + P_AUTO_UI, REFNO_PBLOCK, IDD_DOMEMASTERUI, IDS_DOMEMASTERROLL, 0, 0, NULL,
  // Params

  pb_camera, _FT("stereo_camera"), TYPE_INT, 0, IDS_DLG_CAMERA,
    p_default, 0,
    p_ui, TYPE_INTLISTBOX, IDC_CAMERA, 3, IDS_CAMCENTER, IDS_CAMLEFT, IDS_CAMRIGHT,
    p_range, 0, 2,
    p_tooltip, "Select Center, Left, or Right Camera Views",
  PB_END,

  pb_fov_angle, _FT("fov_angle"), TYPE_ANGLE, P_ANIMATABLE + P_RESET_DEFAULT, IDS_DLG_FOV,
    p_default, DOME_PI,
    p_range, 0.0f, 360.0f,
    p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, IDC_FOV_EDIT, IDC_FOV_SPIN, SPIN_AUTOSCALE,
    p_tooltip, "Field of View",
  PB_END,

  pb_separation, _FT("separation"), TYPE_FLOAT, P_ANIMATABLE, IDS_DLG_SEPARATION,
    p_default, 6.5f,
    p_range, 0.0f, 999999.0f,
    p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, IDC_CAMSEP_EDIT, IDC_CAMSEP_SPIN, SPIN_AUTOSCALE,
    p_tooltip, "Camera Separation",
  PB_END,

  pb_neck_offset, _FT("neck_offset"), TYPE_FLOAT, P_ANIMATABLE, IDS_DLG_NECK,
    p_default, 0.0f,
    p_range, -999999.0f, 999999.0f,
    p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, IDC_NECK_EDIT, IDC_NECK_SPIN, SPIN_AUTOSCALE,
    p_tooltip, "Neck Offset",
  PB_END,

  pb_separation_map, _FT("separation_map"), TYPE_BITMAP, P_SHORT_LABELS, IDS_DLG_SEPMAP,
    //p_default, 1.0f,
    p_ui, TYPE_BITMAPBUTTON, IDC_SEPMAP,
    p_accessor, &pb_accessor,
    p_tooltip, "Separation Map",
  PB_END,

  pb_head_turn_map, _FT("head_turn_map"), TYPE_BITMAP, P_SHORT_LABELS, IDS_DLG_HEADMAP,
    //p_default, 1.0f,
    p_ui, TYPE_BITMAPBUTTON, IDC_HEADTURNMAP,
    p_accessor, &pb_accessor,
    p_tooltip, "Head Turn map",
  PB_END,

  pb_parallax_distance, _FT("parallax_distance"), TYPE_FLOAT, P_ANIMATABLE + P_RESET_DEFAULT, IDS_DLG_PARALLAX,
    p_default, 400.0f,    // [rz] is there a way to adjust this based on the current scene unit?
    p_range, 0.0f, 999999.0f,
    p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, IDC_PLAX_EDIT, IDC_PLAX_SPIN, SPIN_AUTOSCALE,
    p_tooltip, "Zero Parallax Distance",
  PB_END,

  pb_forward_tilt, _FT("forward_tilt"), TYPE_ANGLE, P_ANIMATABLE + P_RESET_DEFAULT, IDS_DLG_FORWARD_TILT,
    p_default, 0.0f,
    p_range, 0.0f, 180.0f,
    p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, IDC_DOMETILT_EDIT, IDC_DOMETILT_SPIN, SPIN_AUTOSCALE,
    p_tooltip, "Forward Tilt",
  PB_END,

  pb_tilt_compensation, _FT("tilt_compensation"), TYPE_BOOL, 0, IDS_DLG_TILT_COMPENSATION,
    p_default, FALSE,
    p_ui, TYPE_SINGLECHEKBOX, IDC_DOMETILTCOMP,
    p_tooltip, "Tilt Compensation Mode",
  PB_END,

  pb_head_tilt_map, _FT("head_tilt_map"), TYPE_BITMAP, P_SHORT_LABELS, IDS_DLG_TILTMAP,
    //p_default, 0.5f,
    p_ui, TYPE_BITMAPBUTTON, IDC_HEADTILTMAP,
    p_accessor, &pb_accessor,
    p_tooltip, "Head Tilt map",
  PB_END,

  pb_vertical_mode, _FT("vertical_mode"), TYPE_BOOL, 0, IDS_DLG_VERTICAL_MODE,
    p_default, FALSE,
    p_ui, TYPE_SINGLECHEKBOX, IDC_VERTICAL,
    p_tooltip, "Vertical Mode",
  PB_END,

  pb_flip_x, _FT("flip_x"), TYPE_BOOL, 0, IDS_DLG_FLIP_X,
    p_default, FALSE,
    p_ui, TYPE_SINGLECHEKBOX, IDC_FLIPX,
    p_tooltip, "Flip X",
  PB_END,

  pb_flip_y, _FT("flip_y"), TYPE_BOOL, 0, IDS_DLG_FLIP_Y,
    p_default, FALSE,
    p_ui, TYPE_SINGLECHEKBOX, IDC_FLIPY,
    p_tooltip, "Flip Y",
  PB_END,

PB_END
);

//************************************************************
// VRayCamera implementation
//************************************************************

Mesh VRayCamera::mesh;
int VRayCamera::meshBuilt=false;

VRayCamera::VRayCamera(void) {
  // Initialize parameter block names for TrackView;
  // this approach takes the names from the parameter block itself.
  // If you want custom names for the parameters in TrackView,
  // check the 3ds Max API documentation.
  static int pblockDesc_inited=false;
  if (!pblockDesc_inited) {
    initPBlockDesc(camera_param_blk);
    pblockDesc_inited=true;
  }

  pblock=NULL;
  pmap=NULL;
  suspendSnap=FALSE;
  buildMesh();
  cameraClassDesc.MakeAutoParamBlocks(this); // Make and intialize the parameter block
}

VRayCamera::~VRayCamera(void) {
}

RefTargetHandle VRayCamera::Clone(RemapDir& remap) {
  VRayCamera *mnew=new VRayCamera();
  BaseClone(this, mnew, remap);
  mnew->ReplaceReference(REFNO_PBLOCK, remap.CloneRef(pblock));
  return (RefTargetHandle) mnew;
}

RefResult VRayCamera::EvalCameraState(TimeValue time, Interval &valid, CameraState *cs) {
  cs->isOrtho=FALSE;
  // [rz] pblock->GetValue(pb_fov, time, cs->fov, valid);
  // [rz] cs->fov = 1.0f;
  pblock->GetValue(pb_fov_angle, time, cs->fov, valid); // [rz] better formula? [interactive viewport]
  cs->fov = cs->fov * 0.75f;
  if (cs->fov > DOME_PI * 0.75f) cs->fov = DOME_PI * 0.75f;
  cs->tdist=100.0f;
  cs->horzLine=FALSE;
  cs->manualClip=FALSE;
  cs->hither=0.0f;
  cs->yon=1e6f;
  cs->nearRange=0.0f;
  cs->farRange=1e6f;
  return REF_SUCCEED;
}

RefResult VRayCamera::NotifyRefChanged(NOTIFY_REF_CHANGED_ARGS) {
  if (hTarget==pblock) 
  {
    camera_param_blk.InvalidateUI();
    NotifyDependents(FOREVER, PART_ALL, REFMSG_CHANGE);
  }
  return REF_SUCCEED;
}

void VRayCamera::getTM(TimeValue t, INode *node, ViewExp *vpt, Matrix3 &tm) {
  tm=node->GetObjectTM(t);

  AffineParts ap;
  decomp_affine(tm, &ap);
  tm.IdentityMatrix();
  tm.SetRotate(ap.q);
  tm.SetTrans(ap.t);

  float scaleFactor=vpt->NonScalingObjectSize()*vpt->GetVPWorldWidth(tm.GetTrans())/360.0f;
  tm.Scale(Point3(scaleFactor,scaleFactor,scaleFactor));
}

void VRayCamera::GetWorldBoundBox(TimeValue t, INode *node, ViewExp *vpt, Box3& box) {
  int i,nv;
  Matrix3 tm;
  Point3 pt;

  getTM(t, node, vpt, tm);
  nv=mesh.getNumVerts();
  box.Init();
  if (!(extendedDisplayFlags & EXT_DISP_ZOOM_EXT)) for (i=0; i<nv; i++) box+=tm*mesh.getVert(i);
  else box+=tm.GetTrans();

  box+=node->GetObjectTM(t)*Point3(0.0f, 0.0f, -GetTDist(t));
}

void VRayCamera::GetLocalBoundBox(TimeValue t, INode *node, ViewExp *vpt, Box3& box) {
  Matrix3 m=node->GetObjectTM(t);
  float scaleFactor=vpt->NonScalingObjectSize()*vpt->GetVPWorldWidth(m.GetTrans())/360.0f;
  box=mesh.getBoundingBox();
  box.Scale(scaleFactor);

  if (extendedDisplayFlags & EXT_DISP_ONLY_SELECTED) box+=Point3(0.0f, 0.0f, -GetTDist(t));
}

void VRayCamera::drawLine(TimeValue t, INode *node, ViewExp *vpt) {
  GraphicsWindow *gw=vpt->getGW();

  gw->setTransform(node->GetObjectTM(t));
  Point3 pt[3];
  pt[0]=Point3(0,0,0);
  pt[1]=Point3(0.0f, 0.0f, -GetTDist(t));
  gw->polyline(2, pt, NULL, NULL, false, NULL);
  gw->marker(&pt[1], HOLLOW_BOX_MRKR);
}

int VRayCamera::HitTest(TimeValue t, INode* node, int type, int crossing, int flags, IPoint2 *p, ViewExp *vpt) {
  static HitRegion hitRegion;
  MakeHitRegion(hitRegion,type,crossing,4,p);

  GraphicsWindow *gw=vpt->getGW();

  DWORD savedLimits=gw->getRndLimits();
  gw->setRndLimits((savedLimits|GW_PICK)&~GW_ILLUM);

  Matrix3 tm;
  getTM(t, node, vpt, tm);
  gw->setTransform(tm);

  int res=mesh.select(gw, gw->getMaterial(), &hitRegion, flags & HIT_ABORTONHIT);
  if (!res) {
    gw->clearHitCode();
    drawLine(t, node, vpt);
    res=gw->checkHitCode();
  }

  gw->setRndLimits(savedLimits);

  return res;
}

void VRayCamera::Snap(TimeValue t, INode* inode, SnapInfo *snap, IPoint2 *p, ViewExp *vpt) {
}

int VRayCamera::Display(TimeValue t, INode* node, ViewExp *vpt, int flags) {
  GraphicsWindow *gw=vpt->getGW();

  DWORD savedLimits=gw->getRndLimits();
#if MAX_RELEASE > 4000
  gw->setRndLimits(GW_WIREFRAME | GW_EDGES_ONLY | GW_BACKCULL| (gw->getRndMode() & GW_Z_BUFFER));
#else
  gw->setRndLimits(GW_WIREFRAME | GW_BACKCULL| (gw->getRndMode() & GW_Z_BUFFER));
#endif

  Matrix3 tm;
  getTM(t, node, vpt, tm);
  gw->setTransform(tm);

  if (node->Selected()) gw->setColor(LINE_COLOR, GetSelColor());
  else if (!node->IsFrozen() && !node->Dependent()) {
    Color color(node->GetWireColor());
    gw->setColor(LINE_COLOR, color);
  }

  mesh.render(gw, gw->getMaterial(), NULL, COMP_ALL);
  drawLine(t, node, vpt);
  gw->setRndLimits(savedLimits);
  return 1;
}

class CreateCallback: public CreateMouseCallBack {
  VRayCamera *obj;
  IPoint2 sp0;
  Point3 p0;
public:
  void setObj(VRayCamera *obj) { this->obj = obj; }

  int proc(ViewExp *vpt, int msg, int point, int flags, IPoint2 m, Matrix3& mat) {
    Point3 p1, center;

    if (msg==MOUSE_FREEMOVE) vpt->SnapPreview(m, m, NULL, SNAP_IN_3D);

    if (msg==MOUSE_POINT || msg==MOUSE_MOVE) {
      switch(point) {
      case 0:
        obj->suspendSnap=TRUE;
        sp0=m;
        p0=vpt->SnapPoint(m, m, NULL, SNAP_IN_3D);
        mat.SetTrans(p0);

        if (msg==MOUSE_POINT) {
          obj->suspendSnap=FALSE;
          return CREATE_STOP;
        }
        break;
      }
    } else {
      if (msg==MOUSE_ABORT) return CREATE_ABORT;
    }
    return TRUE;
  }
};

CreateMouseCallBack* VRayCamera::GetCreateMouseCallBack() {
  static CreateCallback createCallback;
  createCallback.setObj(this);
  return &createCallback;
}

static Pb2TemplateGenerator templateGenerator;

void VRayCamera::BeginEditParams(IObjParam *ip, ULONG flags, Animatable *prev) {
  pmap = CreateCPParamMap2(pblock, ip, hInstance, MAKEINTRESOURCE(IDD_DOMEMASTERUI), GetString(IDS_DOMEMASTERROLL), 0);
}

void VRayCamera::EndEditParams(IObjParam *ip, ULONG flags, Animatable *next) {
  DestroyCPParamMap2(pmap);
  pmap = NULL;
}

void VRayCamera::InvalidateUI(void) {
  camera_param_blk.InvalidateUI(pblock->LastNotifyParamID());
}

static void MakeQuad(Face *f, int a,  int b , int c , int d, int sg, int dv = 0) {
  f[0].setVerts( a+dv, b+dv, c+dv);
  f[0].setSmGroup(sg);
  f[0].setEdgeVisFlags(1,1,0);
  f[1].setVerts( c+dv, d+dv, a+dv);
  f[1].setSmGroup(sg);
  f[1].setEdgeVisFlags(1,1,0);
}

void VRayCamera::buildMesh(void) {
  if (meshBuilt) return;
  int nverts = 16;
  int nfaces = 24;
  mesh.setNumVerts(nverts);
  mesh.setNumFaces(nfaces);
  float len = (float)5.0;
  float w = (float)8.0;
  float d = w*(float).8;
  float e = d*(float).5;
  float f = d*(float).8;
  float l = w*(float).8;

  mesh.setVert(0, Point3( -d, -d, -len));
  mesh.setVert(1, Point3(  d, -d, -len));
  mesh.setVert(2, Point3( -d,  d, -len));
  mesh.setVert(3, Point3(  d,  d, -len));
  mesh.setVert(4, Point3( -d, -d,  len));
  mesh.setVert(5, Point3(  d, -d,  len));
  mesh.setVert(6, Point3( -d,  d,  len));
  mesh.setVert(7, Point3(  d,  d,  len));
  MakeQuad(&(mesh.faces[ 0]), 0,2,3,1,  1);
  MakeQuad(&(mesh.faces[ 2]), 2,0,4,6,  2);
  MakeQuad(&(mesh.faces[ 4]), 3,2,6,7,  4);
  MakeQuad(&(mesh.faces[ 6]), 1,3,7,5,  8);
  MakeQuad(&(mesh.faces[ 8]), 0,1,5,4, 16);
  MakeQuad(&(mesh.faces[10]), 4,5,7,6, 32);

  mesh.setVert(8+0, Point3( -e, -e, len));
  mesh.setVert(8+1, Point3(  e, -e, len));
  mesh.setVert(8+2, Point3( -e,  e, len));
  mesh.setVert(8+3, Point3(  e,  e, len));
  mesh.setVert(8+4, Point3( -f, -f, len+l));
  mesh.setVert(8+5, Point3(  f, -f, len+l));
  mesh.setVert(8+6, Point3( -f,  f, len+l));
  mesh.setVert(8+7, Point3(  f,  f, len+l));

  Face* fbase = &mesh.faces[12];
  MakeQuad(&fbase[0],0,2,3,1,   1, 8);
  MakeQuad(&fbase[2], 2,0,4,6,  2, 8);
  MakeQuad(&fbase[4], 3,2,6,7,  4, 8);
  MakeQuad(&fbase[6], 1,3,7,5,  8, 8);
  MakeQuad(&fbase[8], 0,1,5,4, 16, 8);
  MakeQuad(&fbase[10],4,5,7,6, 32, 8);

  // whoops- rotate 180 about x to get it facing the right way
  Matrix3 mat;
  mat.IdentityMatrix();
  mat.RotateX(DegToRad(180.0));
  for (int i=0; i<nverts; i++) mesh.getVert(i)=mat*mesh.getVert(i);
  mesh.buildNormals();
  mesh.EnableEdgeList(1);
  meshBuilt = true;
}

//************************************************************
// What this is all about: the camera
//************************************************************

// This is called at the start of the animation
void VRayCamera::renderBegin(VR::VRayRenderer *vray) {

  // [rz] evaluate non-animatable parameters here?
}

// This is called at the end of the animation
void VRayCamera::renderEnd(VR::VRayRenderer *vray) {
}

// Called at the start of each frame
void VRayCamera::frameBegin(VR::VRayRenderer *vray) {
  const VR::VRayFrameData &fdata = vray->getFrameData();

  TimeValue t = fdata.t;

  stereo_camera=pblock->GetInt(pb_camera, t);

  // angles in paramblock are automatically converted to radians, so no need to convert here
  fov_angle = pblock->GetFloat(pb_fov_angle, t);
  parallax_distance = pblock->GetFloat(pb_parallax_distance, t);
  separation = pblock->GetFloat(pb_separation, t);
  neck_offset = pblock->GetFloat(pb_neck_offset, t);
  forward_tilt = pblock->GetFloat(pb_forward_tilt, t);
  tilt_compensation = pblock->GetInt(pb_tilt_compensation, t);

  separation_map = pblock->GetBitmap(pb_separation_map, t);
  if (separation_map != NULL) {
    separation_map->Load();
    if (separation_map->bm != NULL) {
      separation_map->bm->SetFilter(BMM_FILTER_PYRAMID);
    }
  }
  head_turn_map = pblock->GetBitmap(pb_head_turn_map, t);
  if (head_turn_map != NULL) {
    head_turn_map->Load();
    if (head_turn_map->bm != NULL) {
      head_turn_map->bm->SetFilter(BMM_FILTER_PYRAMID);
    }
  }
  head_tilt_map = pblock->GetBitmap(pb_head_tilt_map, t);
  if (head_tilt_map != NULL) {
    head_tilt_map->Load();
    if (head_tilt_map->bm != NULL) {
      head_tilt_map->bm->SetFilter(BMM_FILTER_PYRAMID);
    }
  }

  vertical_mode = pblock->GetInt(pb_vertical_mode, t);
  flip_x = pblock->GetInt(pb_flip_x, t);
  flip_y = pblock->GetInt(pb_flip_y, t);
  //fov=pblock->GetFloat(pb_fov, fdata.t);
  fov = 1.0; // fov_angle/ 2.0f; // [rz] testing only. Need better approximation formula.
  targetDist = GetTDist((TimeValue) fdata.t);
  aperture = 0.0f;

  camera.SetPos(fdata.camToWorld.offs, -fdata.camToWorld.m[2], fdata.camToWorld.m[1], fdata.camToWorld.m[0]);
  camera.Init(fdata.imgWidth, fdata.imgHeight, fov, 1.0f, aperture, targetDist);

  this->vray = vray;
}

// Called at the end of each frame
void VRayCamera::frameEnd(VR::VRayRenderer *vray) {
}

VR::Vector VRayCamera::getDir(double xs, double ys, int rayVsOrgReturnMode) const {

  const VR::VRayFrameData &fdata = vray->getFrameData();
  
  // Swap X-Y to rotate the cartesian axis 90 degrees CW
  double ry = (xs-fdata.imgWidth*0.5f)/(fdata.imgWidth*0.5f);
  double rx = (ys-fdata.imgHeight*0.5f)/(fdata.imgHeight*0.5f);
  
  double r, phi, theta, rot, tmp, tmpY, tmpZ;
  double sinP, cosP, sinT, cosT, sinR, cosR, sinD, cosD;

  VR::Vector org, ray, target, htarget;

  // Head tilt transform matrix
  VR::Matrix tilt(1);

  // Compute radius
  r = sqrt((rx * rx) + (ry * ry));

  // Check if the shader should return black
  if (r < 1.0) {
    // Compute phi angle
    if ((r > -DOME_EPSILON) && (r < DOME_EPSILON)) {
      phi = 0.0;
    } else {
      phi = atan2(ry,rx);
    }
    // Compute theta angle
    theta = r * (fov_angle/ 2.0);
    
    // Start by matching camera (center camera)
    org.x = org.y = org.z = 0.0;

    // Compute commonly used values
    sinP = sin(phi);
    cosP = cos(phi);
    sinT = sin(theta);
    cosT = cos(theta);
    
    // Center camera target vector (normalized)
    target.x = (float)(sinP * sinT);
    target.y = (float)(-cosP * sinT);
    target.z = (float)(-cosT);

    // Camera selection and initial position
    // 0=center, 1=Left, 2=Right
    if (stereo_camera != CENTERCAM) {

      float separation_mult = 1.0f;
      float head_turn_mult = 1.0f;
      float head_tilt = 0.5f;

      // [rz] these could be moved to per-frame calculation
      float dx1 = 1.0f / (fdata.imgWidth * 2.0f);
      float dy1 = 1.0f / (fdata.imgHeight * 2.0f);
      float rx1 = xs / fdata.imgWidth - dx1;
      float ry1 = ys / fdata.imgHeight - dy1;

      // [rz] not the right grayscale conversion formula, but ok assuming all input bitmaps are grayscale
      if (separation_map != NULL) {
        separation_map->bm->GetFiltered(rx1, ry1, dx1, dy1, &bCol);
        separation_mult = (bCol.r + bCol.g + bCol.b) / 3.0f / 65535.0f;
      }

      if (head_turn_map != NULL) {
        head_turn_map->bm->GetFiltered(rx1, ry1, dx1, dy1, &bCol);
        head_turn_mult = (bCol.r + bCol.g + bCol.b) / 3.0f / 65535.0f;
      }

      if (head_tilt_map != NULL) {
        head_tilt_map->bm->GetFiltered(rx1, ry1, dx1, dy1, &bCol);
        head_tilt = (bCol.r + bCol.g + bCol.b) / 3.0f / 65535.0f;
      }

      // camera selection and initial position
      if (stereo_camera == LEFTCAM) {
        org.x = (float)(-separation * separation_mult / 2.0);
      }
      else if (stereo_camera == RIGHTCAM) {
        org.x = (float)(separation * separation_mult / 2.0);
      }

      // Tilted dome mode ON
      if(tilt_compensation) {
        // head rotation
        tmpY = target.y * cos(-forward_tilt) - target.z * sin(-forward_tilt);
        tmpZ = target.z * cos(-forward_tilt) + target.y * sin(-forward_tilt);
        rot = atan2(target.x,-tmpY) * head_turn_mult;
        
        if (vertical_mode) {
          rot *= fabs(sinP);
        }
        
        sinR = sin(rot); 
        cosR = cos(rot);
        sinD = sin(forward_tilt);
        cosD = cos(forward_tilt);
        
        // rotate camera
        tmp = org.x * cosR - org.y * sinR;
        org.y = (float)(org.y * cosR + org.x * sinR);
        org.x = (float)tmp;
        
        // compensate for dome tilt
        tmp = org.y * cosD - org.z * sinD;
        org.z = (float)(org.z * cosD + org.y * sinD);
        org.y = (float)tmp;

        // calculate head target
        tmp = sqrt(target.x * target.x + tmpY * tmpY);
        htarget.x = (float)(sinR * tmp);
        htarget.y = (float)(-cosR * tmp);
        htarget.z = (float)tmpZ;
        
        // dome rotation again on head target
        tmp = htarget.y * cosD - htarget.z * sinD;
        htarget.z = (float)(htarget.z * cosD + htarget.y * sinD);
        htarget.y = (float)tmp;
      } else {
        // Tilted dome mode OFF
        
        // Vertical Mode ON
        if (vertical_mode) {
          // head rotation
          rot = atan2(target.x,-target.z) * head_turn_mult * fabs(sinP);
          sinR = sin(rot);
          cosR = cos(rot);
          
          // rotate camera
          tmp = org.x * cosR - org.z * sinR;
          org.z = (float)(org.z * cosR + org.x * sinR);
          org.x = (float)tmp;
          
          // calculate head target
          tmp = sqrt(target.x * target.x + target.z * target.z);
          htarget.x = (float)(sinR * tmp);
          htarget.y = (float)target.y;
          htarget.z = (float)(-cosR * tmp);
        } else {            
          // Vertical Mode OFF  (horizontal dome mode)
          
          // Head rotation
          rot = phi * head_turn_mult;
          sinR = sin(rot);
          cosR = cos(rot);
          
          // Rotate camera
          tmp = (org.x * cosR) - (org.y * sinR);
          org.y = (float)((org.y * cosR) + (org.x * sinR));
          org.x = (float)tmp;
          
          // calculate head target
          htarget.x = (float)(sinR * sinT);
          htarget.y = (float)(-cosR * sinT);
          htarget.z = (float)target.z;
        }
      }

      // head tilt (in rad)
      head_tilt = (float)((head_tilt - 0.5) * DOME_PI);

      float cT = cos(head_tilt);
      float sT = sin(head_tilt);
      tilt[0][0] = cT + htarget.x*htarget.x*(1 - cT);
      tilt[0][1] = htarget.x*htarget.y*(1 - cT) - htarget.z*sT;
      tilt[0][2] = htarget.x*htarget.z*(1 - cT) + htarget.y*sT;
      tilt[1][0] = htarget.y*htarget.x*(1 - cT) + htarget.z*sT;
      tilt[1][1] = cT + htarget.y*htarget.y*(1 - cT);
      tilt[1][2] = htarget.y*htarget.z*(1 - cT) - htarget.x*sT;
      tilt[2][0] = htarget.z*htarget.x*(1 - cT) - htarget.y*sT;
      tilt[2][1] = htarget.z*htarget.y*(1 - cT) + htarget.x*sT;
      tilt[2][2] = cT + htarget.z*htarget.z*(1 - cT);

      org = org * tilt;
      
      // Adjust org for Neck offset
      org = org + target * neck_offset;

      // Compute ray from camera to target
      target *= parallax_distance;
      ray = target - org;
      ray = normalize(ray);

    } else {

      // center cam
      ray = target;

    }
    
    // Flip the X ray direction about the Y-axis
    if(flip_x) {
      org.x = -org.x;
      ray.x = -ray.x;
    }
    
    // Flip the Y ray direction about the X-axis
    if(flip_y) {
      org.y = -org.y;
      ray.y = -ray.y;
    }

    if (rayVsOrgReturnMode == GETDIR){
      return ray;
    }
    else {  // GETORG
      return org;
    }

  } else {
    // Outside image circular space
    ray.x = ray.y = ray.z = 0.0f;
    return ray;
  } 
}

// This is called to compute the actual ray:
//   xs, ys - the point in screen (pixel) coordinates
//   time - the time in the motion blur interval (0-1); VRay will do automatic moblur for camera motion, use this for the other camera params
//   dof_uc, dof_vc - if DOF is on, these are additional lens sampling vars
//   ray - this is where the computed ray must be stored; it's good to make the direction a unit direction
//   mint - this is the start point along the ray (typically 0.0f)
//   maxt - this is the end point along the ray (typically a large value, 1e18f)
//   rayDeriv - derivatives of the point and direction with respect to xs and ys, may be computed numerically if there is no other way

int VRayCamera::getScreenRay(double xs, double ys, double time, float dof_uc, float dof_vc, VR::TraceRay &ray, VR::Ireal &mint, VR::Ireal &maxt, VR::RayDeriv &rayDeriv, VR::Color &multResult) const {

  VR::Vector dir = getDir(xs, ys, GETDIR);   //Return the dir data from the getDir function
  if (dir.x == 0.0f && dir.y == 0.0f && dir.z == 0.0f)  // outside circular image
    return false;   // [rz] Not working. Does not render as black.

  VR::Vector org = getDir(xs, ys, GETORG);   //Return the org data from the getDir function
  
  rayDeriv.dPdx.makeZero();
  rayDeriv.dPdy.makeZero();

  double delta = 0.01f;
  rayDeriv.dDdx = (getDir(xs+delta, ys, GETDIR) - getDir(xs-delta, ys, GETDIR)) / float(delta*2.0f);
  rayDeriv.dDdy = (getDir(xs, ys+delta, GETDIR) - getDir(xs, ys-delta, GETDIR)) / float(delta*2.0f);
  
  const VR::VRayFrameData &fdata = vray->getFrameData();
  ray.p = fdata.camToWorld.offs + fdata.camToWorld.m*org;
  ray.dir = fdata.camToWorld.m*dir;;

  mint = 0.0f;
  maxt = LARGE_FLOAT;

  return true;
}

int VRayCamera::getScreenRays(  
    VR::RayBunchCamera& raysbunch,
        const double* xs,   const double* ys, 
        const float* dof_uc, const float* dof_vc, 
        bool calcDerivs /*= false*/ ) const
{
  for( uint32 i = 0; i < raysbunch.getCount(); i++ ) raysbunch.mints()[i] = 0.0f;
  for( uint32 i = 0; i < raysbunch.getCount(); i++ ) raysbunch.maxts()[i] = LARGE_FLOAT;

  // This should be SingleOrigin for pinhole cameras for better performance
  raysbunch.setType( VR::RayBunchBaseParams<RAYS_IN_BUNCH>::MultipleOrigins );

  bool success = true;

  // By default call single rays versions
  for( unsigned int i = 0 ; i < raysbunch.getCount(); i++ )
  {
    VR::TraceRay ray;
    VR::RayDeriv deriv;
    VR::Color multResult( 1.0f, 1.0f, 1.0f );
    bool res = getScreenRay( xs[i], ys[i], 
    raysbunch.times()[ i ], 
    dof_uc[i], dof_vc[i], 
    ray, 
    raysbunch.mints()[i],
    raysbunch.maxts()[i],
    deriv,
    multResult );

    // Scatter
    success &= res;

    if (res)
    {
      raysbunch.origins(0)[i] = (VR::real) ray.p.x;
      raysbunch.origins(1)[i] = (VR::real) ray.p.y;
      raysbunch.origins(2)[i] = (VR::real) ray.p.z;
      raysbunch.dirs(0)[i] = ray.dir.x;
      raysbunch.dirs(1)[i] = ray.dir.y;
      raysbunch.dirs(2)[i] = ray.dir.z;

      raysbunch.currMultResults(0)[i] = multResult[0];
      raysbunch.currMultResults(1)[i] = multResult[1];
      raysbunch.currMultResults(2)[i] = multResult[2];

      // Restructure derivatives
      *(raysbunch.dPds( 0, 0 ) + i) = deriv.dPdx.x;
      *(raysbunch.dPds( 0, 1 ) + i) = deriv.dPdx.y;
      *(raysbunch.dPds( 0, 2 ) + i) = deriv.dPdx.z;

      *(raysbunch.dPds( 1, 0 ) + i) = deriv.dPdy.x;
      *(raysbunch.dPds( 1, 1 ) + i) = deriv.dPdy.y;
      *(raysbunch.dPds( 1, 2 ) + i) = deriv.dPdy.z;

      *(raysbunch.dDds( 0, 0 ) + i) = deriv.dDdx.x;
      *(raysbunch.dDds( 0, 1 ) + i) = deriv.dDdx.y;
      *(raysbunch.dDds( 0, 2 ) + i) = deriv.dDdx.z;

      *(raysbunch.dDds( 1, 0 ) + i) = deriv.dDdy.x;
      *(raysbunch.dDds( 1, 1 ) + i) = deriv.dDdy.y;
      *(raysbunch.dDds( 1, 2 ) + i) = deriv.dDdy.z;
    } else {
      // This could be further optimized not to trace those rays
      raysbunch.mints()[i] = -LARGE_FLOAT;
      raysbunch.maxts()[i] = -LARGE_FLOAT;

      raysbunch.currMultResults(0)[i] = 0.0f;
      raysbunch.currMultResults(1)[i] = 0.0f;
      raysbunch.currMultResults(2)[i] = 0.0f;
    }
  }

  return success;
}
