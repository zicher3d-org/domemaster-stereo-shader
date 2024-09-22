/**********************************************************************
  FILE: vraylatlongstereo.cpp
  
  V-Ray LatLongStereo Shader v1.0

  2023-09-21
  V-Ray 6.2 for 3ds max 2024 update by Andrew Hazelden/Roberto Ziche

  2023-06-24
  V-Ray 6.1 for 3ds max 2023 update by Andrew Hazelden/Roberto Ziche

  2018-06-21
  Ported to V-Ray 3.0 by Andrew Hazelden/Roberto Ziche
  Based upon the mental ray shader LatLong_Stereo by Roberto Ziche

  Todo:
  [rz] Bitmap to Texmap
  [rz] Bool parameters (from int)
  [rz] Remove pb_fov (pb2 enum)
  [rz] Adjust default parameter values based on scene units?
  [rz] enable/disable controls - adjust start/end angles in UI
  [rz] Use parallax distance to draw cam target
  
**********************************************************************/


#include "vrayplugins.h"
#include "vrayinterface.h"
#include "vrayrenderer.h"
#include "misc_ray.h"
#include "mcsampler.h"

#include "max_compat.h"
#include "gencam.h"
#include "macrorec.h"
#include "decomp.h"
#include "iparamb2.h"
#include "iparamm2.h"
#include "vassert.h"
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
#include "vraylatlongstereo.h"
#include "vraylatlongstereoparamblockwidget.h"

#include "resource.h"

// no param block script access for VRay free
#ifdef _FREE_
#define _FT(X) _T("")
#define IS_PUBLIC 0
#else
#define _FT(X) _T(X)
#define IS_PUBLIC 1
#endif // _FREE_

using namespace VRayLatLongStereo;

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

#define GETDIR        0
#define GETORG        1

#define PLUGIN_CLASSID Class_ID(0x5b6d4650, 0x21e1666f)

#define STR_CLASSNAME _T("VRayLatLongStereo")
#define STR_INTERNALNAME _T("VRayLatLongStereo")
#define STR_LIBDESC _T("VRayLatLongStereo plugin")
#define STR_DLGTITLE _T("VRayLatLongStereo Parameters")
#define STR_CATEGORY _T("VRay")


//************************************************************
// The definition of the VRayCamera
//************************************************************

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
  float fov_vert_angle;
  float fov_horiz_angle;
  float parallax_distance;
  float separation;
  PBBitmap *separation_map;
  float neck_offset;
  int   zenith_mode;
  int   flip_x;
  int   flip_y;
  bool  zenith_fov;
  bool  horiz_neck;
  bool  poles_corr;
  float poles_corr_start = 0.785f;
  float poles_corr_end = 1.483f;
  bool  parallel_cams;

  // Constructor/destructor
  VRayCamera(void);
  ~VRayCamera(void) override;

  // From GenCamera
  GenCamera* NewCamera(int type) override { return new VRayCamera; }
  void SetConeState(int s) override {}
  int GetConeState(void) override { return FALSE; }
  void SetHorzLineState(int s) override {}
  int GetHorzLineState(void) override { return FALSE; }
  void Enable(int onOff) override {}
  BOOL SetFOVControl(Control *c) override {
#if MAX_RELEASE<13900
    // [rz] pblock->SetController(pblock->IDtoIndex(pb_fov), 0, c);
#else
    // [rz] pblock->SetControllerByID((ParamID) pb_fov, 0, c);
#endif
    return TRUE;
  }
  Control *GetFOVControl() override {
#if MAX_RELEASE<13900
    return pblock->GetController((ParamID) pb_fov);
#else
    return pblock->GetControllerByID((ParamID) pb_fov);
#endif
  }
  void SetFOVType(int ft) override {}
  int GetFOVType(void) override { return 0; } // FOV_W
  int Type(void) override { return FREE_CAMERA; }
  void SetType(int type) override {}

  // From CameraObject
  RefResult EvalCameraState(TimeValue time, Interval &valid, CameraState *cs) override;
  void SetOrtho(BOOL b) override {}
  BOOL IsOrtho(void) override { return FALSE; }
  void SetFOV(TimeValue t, float f) override { /* [rz] pblock->SetValue(pb_fov, t, f);*/ }
  float GetFOV(TimeValue t, Interval &valid) override { float res; /* [rz] pblock->GetValue(pb_fov, t, res, valid);*/ res = 1.0f; return res; }
  void SetTDist(TimeValue t, float f) override {}
  float GetTDist(TimeValue t, Interval &valid) override { return 100.0f; }
  int GetManualClip(void) override { return FALSE; }
  void SetManualClip(int onOff) override {}
  float GetClipDist(TimeValue t, int which, Interval &valid) override { return (which==CAM_HITHER_CLIP)? 0.0f : 1e6f; }
  void SetClipDist(TimeValue t, int which, float val) override {}
  void SetEnvRange(TimeValue t, int which, float f) override {}
  float GetEnvRange(TimeValue t, int which, Interval &valid) override { return (which==ENV_NEAR_RANGE)? 0.0f: 1e6f; }
  void SetEnvDisplay(BOOL b, int notify) override {}
  BOOL GetEnvDisplay(void) override { return FALSE; }
  void RenderApertureChanged(TimeValue t) override {}
  void UpdateTargDistance(TimeValue t, INode *node) override {}

  // From Object
  ObjectState Eval(TimeValue time) override { return ObjectState(this); }
  void InitNodeName(TSTR& s) override { s=STR_CLASSNAME; }
  int DoOwnSelectHilite() override { return TRUE; }
  Interval ObjectValidity(TimeValue time) override { Interval res=FOREVER; pblock->GetValidity(time, res); return res; }
  BOOL UsesWireColor() override { return TRUE; }
  int CanConvertToType(Class_ID obtype) override { return FALSE; }
  Object* ConvertToType(TimeValue t, Class_ID obtype) override { vassert(0); return NULL; }

  void GetWorldBoundBox(TimeValue t, INode *mat, ViewExp *vpt, Box3& box) override;
  void GetLocalBoundBox(TimeValue t, INode *mat, ViewExp *vpt, Box3& box) override;

  // From BaseObject
  int HitTest(TimeValue t, INode* inode, int type, int crossing, int flags, IPoint2 *p, ViewExp *vpt) override;
  void Snap(TimeValue t, INode* inode, SnapInfo *snap, IPoint2 *p, ViewExp *vpt) override;
  void SetExtendedDisplay(int flags) override { extendedDisplayFlags=flags; }
  int Display(TimeValue t, INode* inode, ViewExp *vpt, int flags) override;

#if MAX_RELEASE >= 14850
	const TCHAR *GetObjectName(NO_ARG_LOCALIZED) CONST_MAX2022 override { return STR_CLASSNAME; }
#else
	TCHAR *GetObjectName(void) { return STR_CLASSNAME; }
#endif
	CreateMouseCallBack* GetCreateMouseCallBack() override;

  void BeginEditParams(IObjParam *ip, ULONG flags, Animatable *prev) override;
  void EndEditParams(IObjParam *ip, ULONG flags, Animatable *next) override;
  void InvalidateUI(void);

  // From ReferenceTarget
#if GET_MAX_RELEASE(VERSION_3DSMAX) < 8900
  RefTargetHandle Clone(RemapDir& remap=NoRemap());
#else
  RefTargetHandle Clone(RemapDir& remap) override;
#endif

	// From ReferenceMaker
	RefResult NotifyRefChanged(NOTIFY_REF_CHANGED_ARGS) override;
	int NumRefs(void) override { return 1; }
	RefTargetHandle GetReference(int i) override { return (i==0)? pblock : NULL; }
	void SetReference(int i, RefTargetHandle rtarg) override { if (i==0) pblock=(IParamBlock2*) rtarg; }

	// IOResult Load(ILoad *load);
	// IOResult Save(ISave *save);

	// From Animatable
	void DeleteThis() override { delete this; }
	Class_ID ClassID() override { return PLUGIN_CLASSID; }
	void GetClassName(ARG1_LOCALIZED(TSTR &s)) CONST_MAX2022 override { s=STR_CLASSNAME; }
	int IsKeyable() { return 0; }

	int NumParamBlocks() override { return 1; }
	IParamBlock2* GetParamBlock(int i) override { return pblock; }
	IParamBlock2* GetParamBlockByID(BlockID id) override { return (pblock->ID() == id) ? pblock : NULL; }

	int NumSubs() override { return 1; }
	Animatable* SubAnim(int i) override { return (i==0)? pblock : NULL; }
	TSTR SubAnimName(ARG1_LOCALIZED(int i)) override { return (i==0)? STR_DLGTITLE : _T("<???>"); }
	
	void* GetInterface(ULONG id) override { return (id==I_VRAYCAMERA)? (VR::VRayCamera*) this : GenCamera::GetInterface(id); }
	void ReleaseInterface(ULONG id, void *ip) override {
		if (id==I_VRAYCAMERA);
		else GenCamera::ReleaseInterface(id, ip);
	}

	// From VRayCamera
	uint32 getFlags(void) const override { return uint32(VR::vrayCameraFlags_empty); }
	int getScreenRay(
		double xs,
		double ys,
		double time,
		const float *rnds,
		int numRnds,
		VR::TraceRay &ray,
		VR::Ireal &mint,
		VR::Ireal &maxt,
		VR::RayDeriv &rayDeriv,
		VR::ShadeCol &multResult,
		uint32 flags
	) const VRAY_OVERRIDE;

	void renderBegin(VR::VRayRenderer *vray) VRAY_OVERRIDE;
	void renderEnd(VR::VRayRenderer *vray) VRAY_OVERRIDE;
	void frameBegin(VR::VRayRenderer *vray) VRAY_OVERRIDE;
	void frameEnd(VR::VRayRenderer *vray) VRAY_OVERRIDE;
	
	void frameBeginImpl(VR::VRayRenderer *vray, const VR::VRaySequenceData &sdata, const VR::VRayFrameData &fdata) VRAY_OVERRIDE { frameBegin(vray); }
	
    VR::Vector getDir(double xs, double ys, int rayVsOrgReturnMode) const;
	/* [ah] TODO - Check out "int *valid=false" revision */
	float getTDist(TimeValue t) {
		Interval valid=FOREVER;
		return GetTDist(t, valid);
	}
};

//************************************************************
// Class descriptor
//************************************************************

class CameraClassDesc:public ClassDescriptor {
public:
  int IsPublic() override { return IS_PUBLIC; }
  void* Create(BOOL loading) override { return new VRayCamera; }
  const TCHAR* ClassName() override { return STR_CLASSNAME; }
  SClass_ID SuperClassID() override { return CAMERA_CLASS_ID; }
  Class_ID ClassID() override { return PLUGIN_CLASSID; }
  const TCHAR* Category() override { return STR_CATEGORY; }

  // Hardwired name, used by MAX Script as unique identifier
  const TCHAR*  InternalName() override { return STR_INTERNALNAME; }
  HINSTANCE HInstance() override { return hInstance; }

#ifdef USE_MAX_QT_BASED_UI
	// Qt UI
	MaxSDK::QMaxParamBlockWidget* CreateQtWidget(
		ReferenceMaker& owner,
		IParamBlock2& paramBlock,
		const MapID paramMapID,
		MSTR& rollupTitle,
		int& rollupFlags,
		int& rollupCategory
	) override {
		UIThreadLanguageSwitchRAII switchLang;

		return new VRayLatLongStereoParamBlockWidget(
			owner,
			paramBlock,
			paramMapID,
			rollupTitle,
			rollupFlags,
			rollupCategory
		);
	}
#endif // USE_MAX_QT_BASED_UI
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
  if (hInstance) return LoadString(hInstance, id, buf, COUNT_OF(buf)) ? buf : NULL;
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
        }
        break;
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

#ifdef USE_MAX_QT_BASED_UI
#define PBLOCK_FLAGS P_AUTO_CONSTRUCT+P_AUTO_UI_FLAG
#define WINAPI_UI(...)
#else
#define PBLOCK_FLAGS P_AUTO_CONSTRUCT
#define WINAPI_UI(...) __VA_ARGS__
#endif

static ParamBlockDesc2 camera_param_blk(camera_params, loadStringResource(idtr_grp_params, false).data(), 0, &cameraClassDesc,
  PBLOCK_FLAGS, REFNO_PBLOCK,
    WINAPI_UI(IDD_LATLONGUI, IDS_LATLONGROLL, 0, 0 , NULL,)
  // Params

  pb_camera, _FT("stereo_camera"), TYPE_INT, 0, IDS_DLG_CAMERA,
    p_default, 0,
    p_ui, TYPE_INTLISTBOX, IDC_CAMERA, 3, IDS_CAMCENTER, IDS_CAMLEFT, IDS_CAMRIGHT,
    p_range, 0, 2,
    p_tooltip, "Select Center, Left, or Right Camera Views",
  PB_END,

  pb_fov_vert_angle, _FT("fov_vert_angle"), TYPE_ANGLE, P_ANIMATABLE + P_RESET_DEFAULT, IDS_DLG_FOV_V,
    p_default, DOME_PI,
    p_range, 0.0f, 180.0f, 
    p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, IDC_FOVV_EDIT, IDC_FOVV_SPIN, SPIN_AUTOSCALE,
    p_tooltip, "Field of View - Vertical",
  PB_END,

  pb_zenithfov, _FT("hemirect"), TYPE_BOOL, 0, IDS_DLG_ZENITHFOV,
    p_default, FALSE,
    p_ui, TYPE_SINGLECHEKBOX, IDC_ZENITHFOV,
    p_tooltip, "Hemi-equirectangular (Zenith FOV)",
  PB_END,

  pb_fov_horiz_angle, _FT("fov_horiz_angle"), TYPE_ANGLE, P_ANIMATABLE + P_RESET_DEFAULT, IDS_DLG_FOV_H,
    p_default, DOME_PI*2,
    p_range, 0.0f, 360.0f,
    p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, IDC_FOVH_EDIT, IDC_FOVH_SPIN, SPIN_AUTOSCALE,
    p_tooltip, "Field of View - Horizontal",
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

  pb_parallax_distance, _FT("parallax_distance"), TYPE_FLOAT, P_ANIMATABLE + P_RESET_DEFAULT, IDS_DLG_PARALLAX,
    p_default, 400.0f,    // [rz] is there a way to adjust this based on the current scene unit?
    p_range, 0.0f, 999999.0f,
    p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, IDC_PLAX_EDIT, IDC_PLAX_SPIN, SPIN_AUTOSCALE,
    p_tooltip, "Zero Parallax Distance",
  PB_END,

  pb_zenith_mode, _FT("zenith_mode"), TYPE_BOOL, 0, IDS_DLG_ZENITH,
    p_default, FALSE,
    p_ui, TYPE_SINGLECHEKBOX, IDC_ZENITH,
    p_tooltip, "Zenith Mode",
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

  pb_poles_corr, _FT("poles_corr"), TYPE_BOOL, 0, IDS_DLG_POLES_CORR,
    p_default, TRUE,
    p_ui, TYPE_SINGLECHEKBOX, IDC_POLES,
    p_tooltip, "Poles Correction",
  PB_END,

  pb_poles_corr_start, _FT("poles_corr_start"), TYPE_ANGLE, P_ANIMATABLE + P_RESET_DEFAULT, IDS_DLG_POLES_ST,
    p_default, 0.785398163397448,   // 45 deg
    p_range, 0.0f, 90.0f,
    p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, IDC_POLEST_EDIT, IDC_POLEST_SPIN, SPIN_AUTOSCALE,
    p_tooltip, "Poles Correction Start Angle",
  PB_END,

  pb_poles_corr_end, _FT("poles_corr_end"), TYPE_ANGLE, P_ANIMATABLE + P_RESET_DEFAULT, IDS_DLG_POLES_EN,
    p_default, 1.48352986419518,   // 85 deg
    p_range, 45.0f, 90.0f,
    p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, IDC_POLEEN_EDIT, IDC_POLEEN_SPIN, SPIN_AUTOSCALE,
    p_tooltip, "Poles Correction End Angle",
  PB_END,

  pb_horiz_neck, _FT("horiz_neck"), TYPE_BOOL, 0, IDS_DLG_HORIZ_NECK,
    p_default, TRUE,
    p_ui, TYPE_SINGLECHEKBOX, IDC_HORIZN,
    p_tooltip, "Horizontal Neck",
  PB_END,

  pb_parall_cams, _FT("parall_cams"), TYPE_BOOL, 0, IDS_DLG_PARALL_CAMS,
    p_default, TRUE,
    p_ui, TYPE_SINGLECHEKBOX, IDC_PARALL,
    p_tooltip, "Parallel Cameras",
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
  cameraClassDesc.MakeAutoParamBlocks(this); // Make and initialize the parameter block
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
  pblock->GetValue(pb_fov_vert_angle, time, cs->fov, valid); // [rz] better formula? [interactive viewport]
  cs->fov = abs(cs->fov) * 0.75f; // [rz] can I make this one flip the camera 90 deg when negative? (zenith view)
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
#ifdef USE_MAX_QT_BASED_UI
		IParamMap2* map=pblock->GetMap();
		if (map) {
			MaxSDK::QMaxParamBlockWidget* mapWidget=map->GetQWidget();
			if (mapWidget) {
				const TimeValue t=GetCOREInterface()->GetTime();
				const ParamID paramID=pblock->LastNotifyParamID();
				mapWidget->UpdateParameterUI(t, paramID, 0);
			}
		}
#endif
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

  box+=node->GetObjectTM(t)*Point3(0.0f, 0.0f, -getTDist(t));
}

void VRayCamera::GetLocalBoundBox(TimeValue t, INode *node, ViewExp *vpt, Box3& box) {
  Matrix3 m=node->GetObjectTM(t);
  float scaleFactor=vpt->NonScalingObjectSize()*vpt->GetVPWorldWidth(m.GetTrans())/360.0f;
  box=mesh.getBoundingBox();
  box.Scale(scaleFactor);

  if (extendedDisplayFlags & EXT_DISP_ONLY_SELECTED) box+=Point3(0.0f, 0.0f, -getTDist(t));
}

void VRayCamera::drawLine(TimeValue t, INode *node, ViewExp *vpt) {
  GraphicsWindow *gw=vpt->getGW();

  gw->setTransform(node->GetObjectTM(t));
  Point3 pt[3];
  pt[0]=Point3(0,0,0);
  pt[1]=Point3(0.0f, 0.0f, -getTDist(t));
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

  int proc(ViewExp *vpt, int msg, int point, int flags, IPoint2 m, Matrix3& mat) override {
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

#ifndef USE_MAX_QT_BASED_UI
static Pb2TemplateGenerator templateGenerator;
#endif

void VRayCamera::BeginEditParams(IObjParam *ip, ULONG flags, Animatable *prev) {
#ifdef USE_MAX_QT_BASED_UI
	cameraClassDesc.BeginEditParams(ip, this, flags, prev);
#else
  pmap = CreateCPParamMap2(pblock, ip, hInstance, MAKEINTRESOURCE(IDD_LATLONGUI), GetString(IDS_LATLONGROLL), 0);
#endif
}

void VRayCamera::EndEditParams(IObjParam *ip, ULONG flags, Animatable *next) {
#ifdef USE_MAX_QT_BASED_UI
	cameraClassDesc.EndEditParams(ip, this, flags, next);
#else
  DestroyCPParamMap2(pmap);
  pmap = NULL;
#endif
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
  MakeQuad(&fbase[0], 0,2,3,1,  1, 8);
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

  TimeValue t=TimeValue(fdata.t);

  stereo_camera=pblock->GetInt(pb_camera, t);

  // angles in paramblock are automatically converted to radians, so no need to convert here
  fov_vert_angle = pblock->GetFloat(pb_fov_vert_angle, t);
  zenith_fov = pblock->GetInt(pb_zenithfov, t);
  fov_horiz_angle = pblock->GetFloat(pb_fov_horiz_angle, t);
  parallax_distance = pblock->GetFloat(pb_parallax_distance, t);
  separation = pblock->GetFloat(pb_separation, t);
  neck_offset = pblock->GetFloat(pb_neck_offset, t);
  zenith_mode = pblock->GetInt(pb_zenith_mode, t);

  separation_map = pblock->GetBitmap(pb_separation_map, t);
  if (separation_map != NULL) {
    separation_map->Load();
    if (separation_map->bm != NULL) {
      separation_map->bm->SetFilter(BMM_FILTER_PYRAMID);
    }
  }
 
  flip_x = pblock->GetInt(pb_flip_x, t);
  flip_y = pblock->GetInt(pb_flip_y, t);

  horiz_neck = pblock->GetInt(pb_horiz_neck, t);;
  poles_corr = pblock->GetInt(pb_poles_corr, t);;
  poles_corr_start = pblock->GetFloat(pb_poles_corr_start, t);
  poles_corr_end = pblock->GetFloat(pb_poles_corr_end, t);
  parallel_cams = pblock->GetInt(pb_parall_cams, t);

  // check poles corr angles
  if (poles_corr_end < poles_corr_start)
    poles_corr_end = poles_corr_start;

  //zenith_fov = (fov_vert_angle < 0.0f) ? TRUE : FALSE;
  //fov_vert_angle = abs(fov_vert_angle);

  //fov=pblock->GetFloat(pb_fov, TimeValue(fdata.t));
  fov = 1.0; // fov_vert_angle / 2.0f;  // [rz] testing only. Need better approximation formula.
  targetDist = getTDist((TimeValue) fdata.t);
  aperture = 0.0f;

  camera.setPos(
    fdata.camToWorld.offs,
    -fdata.camToWorld.m[2],
    fdata.camToWorld.m[1],
    fdata.camToWorld.m[0]
  );
  camera.init(float(fdata.imgWidth), float(fdata.imgHeight), fov, 1.0f, aperture, targetDist);

  this->vray = vray;
}

// Called at the end of each frame
void VRayCamera::frameEnd(VR::VRayRenderer *vray) {
}

VR::Vector VRayCamera::getDir(double xs, double ys, int rayVsOrgReturnMode) const {
  const VR::VRayFrameData &fdata = vray->getFrameData();

  double rx = 2.0f * xs / fdata.imgWidth - 1.0f;
  double ry = -2.0f * ys /fdata.imgHeight + 1.0f;

  double phi, theta, tmp;
  double sinP, cosP, sinT, cosT;

  VR::Vector org, ray, target, neckTarget;
  
  // Calculate phi and theta...
  phi = rx * (fov_horiz_angle / 2.0);
  if (zenith_fov) {
    // zenith FOV
    if (zenith_mode){
      theta = -(ry - 1.0f) * (fov_vert_angle / 2.0);
      if (flip_y) theta = theta + (DOME_PI - fov_vert_angle);
    }
    else {
      theta = DOME_PIOVER2 + (ry - 1.0f) * (fov_vert_angle / 2.0);
      if (flip_y) theta = theta - (DOME_PI - fov_vert_angle);
    }
  } else {
    // horizontal FOV
    if (zenith_mode){
      theta = DOME_PIOVER2 - ry * (fov_vert_angle / 2.0);
    }
    else {
      theta = ry * (fov_vert_angle / 2.0);
    }
  }

  // Start by matching camera (center camera)
  org.x = 0.0;
  org.y = 0.0;
  org.z = 0.0;

  // Compute commonly used values
  sinP = sin(phi);
  cosP = cos(phi);
  sinT = sin(theta);
  cosT = cos(theta);

  // Center camera target vector (normalized)
  if (zenith_mode) {
    target.x = (float)(sinP * sinT);
    target.y = (float)(-cosP * sinT);
    target.z = (float)(-cosT);
    if (horiz_neck) {
      neckTarget.x = (float)sinP;
      neckTarget.y = (float)-cosP;
      neckTarget.z = 0.0f;
    } else
      neckTarget = target;
  } else {
    target.x = (float)(sinP * cosT);
    target.y = (float)(sinT);
    target.z = (float)(-cosP * cosT);
    if (horiz_neck) {
      neckTarget.x = (float)sinP;
      neckTarget.y = 0.0f;
      neckTarget.z = (float)-cosP;
    } else
      neckTarget = target;
  }

  // Camera selection and initial position
  // 0=center, 1=Left, 2=Right
  if (stereo_camera != CENTERCAM) {

    float separation_mult = 1.0f;
    float separation_mult_auto = 1.0f;

    // get separation multiplier from map
    if (separation_map != NULL && separation_map->bm != NULL) {
      // [rz] these could be moved to per-frame calculation
      float dx1 = 1.0f / (fdata.imgWidth * 2.0f);
      float dy1 = 1.0f / (fdata.imgHeight * 2.0f);
      float rx1 = float(xs / fdata.imgWidth - dx1);
      float ry1 = float(ys / fdata.imgHeight - dy1);

      BMM_Color_64 bCol;
      separation_map->bm->GetFiltered(rx1,ry1,dx1,dy1, &bCol);
      //if (separation_map->bm->HasFilter()) {
        //separation_map->bm->GetFiltered(rx1,ry1,dx1,dy1, &bCol);
      //}

      // [rz] not the right grayscale conversion formula, but ok assuming all input bitmaps are grayscale
      separation_mult = (bCol.r + bCol.g + bCol.b) / 3.0f / 65535.0f;
    }

    // Additional automatic separation fade
    if (poles_corr) {
      double tmpTheta;
      if (zenith_mode)
        tmpTheta = abs(DOME_PIOVER2 - theta);
      else 
        tmpTheta = abs(theta);
      if (tmpTheta > poles_corr_start) {
        if (tmpTheta < poles_corr_end) {
          double fadePos = (tmpTheta - poles_corr_start) / (poles_corr_end - poles_corr_start);
            separation_mult_auto = float((cos(fadePos*DOME_PI) + 1.0f) / 2.0f);
        } else
          separation_mult_auto = 0.0f;
      }
    }
    // combine both separation values
    separation_mult *= separation_mult_auto;

    // camera selection and initial position
    if (stereo_camera == LEFTCAM) {
      org.x = (float)(-separation * separation_mult / 2.0);
    } else {  // RIGHTCAM
      org.x = (float)(separation * separation_mult / 2.0);
    }

    // head rotation = phi
    // rotate camera
    if (zenith_mode) {
      tmp = (float)((org.x * cosP) - (org.y * sinP));
      org.y = (float)((org.y * cosP) + (org.x * sinP));
      org.x = (float)tmp;
    } else {
      tmp = (float)((org.x * cosP) - (org.z * sinP));
      org.z = (float)((org.z * cosP) + (org.x * sinP));
      org.x = (float)tmp;
    }

    // Adjust org for Neck offset
    org = org + neckTarget * neck_offset;

    // Compute ray from camera to target
    if (parallel_cams) {
      ray = target;
    } else {
      target *= parallax_distance;
      ray = target - org;
      ray = normalize(ray);
    }

  } else {

    // center cam
    ray = target;

  }

  // Flip the X ray direction about the Y-axis
  if (flip_x) {
    org.x = -org.x;
    ray.x = -ray.x;
  }

  // Flip the Y ray direction about the X-axis
  if (flip_y) {
    if (zenith_mode) {
      org.z = -org.z;
      ray.z = -ray.z;
    } else {
      org.y = -org.y;
      ray.y = -ray.y;
    }
  }

  if (rayVsOrgReturnMode == GETDIR){
    return ray;
  } else {  
    // GETORG
    return org;
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
///  multResult - A filter by which this pixel value should be multiplied (used for e.g. vignetting or exposure effects).
//   flags - A combination of OR'ed members of the GetScreenRayFlags enum.
int VRayCamera::getScreenRay(
	double xs,
	double ys,
	double time,
	const float *rnds,
	int numRnds,
	VR::TraceRay &ray,
	VR::Ireal &mint,
	VR::Ireal &maxt,
	VR::RayDeriv &rayDeriv,
	VR::ShadeCol &multResult,
	uint32 flags
) const {
  VR::Vector dir = getDir(xs, ys, GETDIR);   //Return the dir data from the getDir function
  VR::Vector org = getDir(xs, ys, GETORG);   //Return the org data from the getDir function

  rayDeriv.dPdx.makeZero();
  rayDeriv.dPdy.makeZero();

  double delta = 0.01f;
  rayDeriv.dDdx = VR::toShadeVec((getDir(xs + delta, ys, GETDIR) - getDir(xs - delta, ys, GETDIR)) / float(delta * 2.0f));
  rayDeriv.dDdy = VR::toShadeVec((getDir(xs, ys + delta, GETDIR) - getDir(xs, ys - delta, GETDIR)) / float(delta * 2.0f));

  const VR::VRayFrameData &fdata = vray->getFrameData();
  ray.p = VR::toShadeVec(fdata.camToWorld.offs + fdata.camToWorld.m * VR::toShadeVec(org));
  ray.dir = VR::toShadeVec(fdata.camToWorld.m * VR::toShadeVec(dir));

  mint = 0.0f;
  maxt = LARGE_FLOAT;

  return true;
}
