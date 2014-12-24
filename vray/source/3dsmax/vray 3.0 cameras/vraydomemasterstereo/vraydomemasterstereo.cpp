/**********************************************************************
  FILE: vraydomemasterstereo.cpp

  vray DomemasterStereo Shader v0.3
  2014-12-24 

  Ported to Vray 3.0 by Andrew Hazelden
  Based upon the mental ray shader domeAFL_FOV_Stereo by Roberto Ziche

  Todo:
  Work out the return black color code if the check for "if (r < 1.0)" comes back as false

**********************************************************************/

#include "math.h"

#include "max.h"
#include "gencam.h"
#include "macrorec.h"
#include "decomp.h"
#include "iparamb2.h"
#include "iparamm2.h"

#include "utils.h"
#include "pb2template_generator.h"

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

// no param block script access for VRay free
#ifdef _FREE_
#define _FT(X) _T("")
#define IS_PUBLIC 0
#else
#define _FT(X) _T(X)
#define IS_PUBLIC 1
#endif // _FREE_

using namespace VRayDomemasterStereo;

#define CENTERCAM    0
#define LEFTCAM      1
#define RIGHTCAM     2

#define DOME_PI  3.141592653589793238
#define DOME_DTOR  0.0174532925199433 
#define DOME_PIOVER2 1.57079632679489661923 
#define DOME_EPSILON	0.00001

//************************************************************
// #defines
//************************************************************

#define	PLUGIN_CLASSID Class_ID(0x1d04418d, 0x4e486c84)

#define STR_CLASSNAME _T("VRayDomemasterStereo")
#define STR_INTERNALNAME _T("VRayDomemasterStereo")
#define STR_LIBDESC _T("VRayDomemasterStereo plugin")
#define STR_DLGTITLE _T("VRayDomemasterStereo Parameters")
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
  float fov_angle; 
  float zero_parallax_sphere;
  float separation;
  int   forward_tilt;
  int   tilt_compensation;
  int   vertical_mode;
  float separation_map;
  float head_turn_map;
  float head_tilt_map;
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
		pblock->SetController(pblock->IDtoIndex(pb_fov), 0, c);
#else
		pblock->SetControllerByID((ParamID) pb_fov, 0, c);
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
	void SetFOV(TimeValue t, float f) { pblock->SetValue(pb_fov, t, f); }
	float GetFOV(TimeValue t, Interval &valid) { float res; pblock->GetValue(pb_fov, t, res, valid); return res; }
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

	void BeginEditParams(IObjParam *ip, ULONG flags,Animatable *prev);
	void EndEditParams(IObjParam *ip, ULONG flags,Animatable *next);
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

	int	NumParamBlocks() { return 1; }	
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
	const TCHAR*	InternalName() { return STR_INTERNALNAME; }
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

__declspec( dllexport ) const TCHAR* LibDescription() { return STR_LIBDESC; }
__declspec( dllexport ) int LibNumberClasses() { return 1; }

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

// Paramblock2 name
enum { camera_params, }; 

static int ctrlID=100;

int nextID(void) { return ctrlID++; }

static ParamBlockDesc2 camera_param_blk(camera_params, STR_DLGTITLE,  0, &cameraClassDesc, P_AUTO_CONSTRUCT, REFNO_PBLOCK, 
	// Params
  
  pb_camera, _FT("stereo_camera"), TYPE_INT, P_ANIMATABLE, 0,
		p_default, 0,
		p_ui, TYPE_INTLISTBOX, nextID(), 0, SPIN_AUTOSCALE,
    p_prompt, "Center, Left, Right Camera Views",
	PB_END,
  
  pb_fov_angle, _FT("fov_angle"), TYPE_ANGLE, P_ANIMATABLE, 0,
		p_default, 180.0f,
		p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, nextID(), nextID(), SPIN_AUTOSCALE,
    p_prompt, "Field of View",
	PB_END,
    
  pb_zero_parallax_sphere, _FT("zero_parallax_sphere"), TYPE_FLOAT, P_ANIMATABLE, 0,
		p_default, 360.0f,
		p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, nextID(), nextID(), SPIN_AUTOSCALE,
    p_prompt, "Zero Parallax Sphere",
	PB_END,
  
  pb_separation, _FT("separation"), TYPE_FLOAT, P_ANIMATABLE, 0,
		p_default, 6.5f,
		p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, nextID(), nextID(), SPIN_AUTOSCALE,
    p_prompt, "Camera Separation",
	PB_END,
  
  pb_forward_tilt, _FT("forward_tilt"), TYPE_FLOAT, P_ANIMATABLE, 0,
		p_default, 0.0f,
	  p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, nextID(), nextID(), SPIN_AUTOSCALE,
    p_prompt, "Forward Tilt",
	PB_END,
  
  pb_tilt_compensation, _FT("tilt_compensation"), TYPE_BOOL, P_ANIMATABLE, 0,
		p_default, FALSE,
		p_ui, TYPE_SINGLECHEKBOX, nextID(),
    p_prompt, "Tilt Compensation Mode",
	PB_END,
  
  pb_vertical_mode, _FT("vertical_mode"), TYPE_BOOL, P_ANIMATABLE, 0,
		p_default, FALSE,
		p_ui, TYPE_SINGLECHEKBOX, nextID(),
    p_prompt, "Vertical Mode",
	PB_END,
  
  pb_separation_map, _FT("separation_map"), TYPE_TEXMAPBUTTON, P_ANIMATABLE, 0,
		p_default, 1.0f,
		p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, nextID(), nextID(), SPIN_AUTOSCALE,
    p_prompt, "Separation Map",
	PB_END,
  
  pb_head_turn_map, _FT("head_turn_map"), TYPE_TEXMAPBUTTON, P_ANIMATABLE, 0,
		p_default, 1.0f,
    p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, nextID(), nextID(), SPIN_AUTOSCALE,
    p_prompt, "Head Turn map",
	PB_END,

  pb_head_tilt_map, _FT("head_tilt_map"), TYPE_TEXMAPBUTTON, P_ANIMATABLE, 0,
		p_default, 0.5f,
    p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, nextID(), nextID(), SPIN_AUTOSCALE,
    p_prompt, "Head Tilt map",
	PB_END,
  
	pb_flip_x, _FT("flip_x"), TYPE_BOOL, P_ANIMATABLE, 0,
		p_default, FALSE,
		p_ui, TYPE_SINGLECHEKBOX, nextID(),
    p_prompt, "Flip X",
	PB_END,
  
	pb_flip_y, _FT("flip_y"), TYPE_BOOL, P_ANIMATABLE, 0,
		p_default, FALSE,
		p_ui, TYPE_SINGLECHEKBOX, nextID(),
    p_prompt, "Flip Y",
	PB_END,
  
	// pb_fov, _FT("fov"), TYPE_ANGLE, P_ANIMATABLE, 0,
		// p_default, 45.0f*pi/180.0f,
		// p_ui, TYPE_SPINNER, EDITTYPE_FLOAT, nextID(), nextID(), SPIN_AUTOSCALE,
	//PB_END,
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
	pblock->GetValue(pb_fov, time, cs->fov, valid);
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
	DLGTEMPLATE* tmp=templateGenerator.GenerateTemplate(pblock, STR_DLGTITLE, 108);
	pmap=CreateCPParamMap2(pblock, ip, hInstance, tmp, STR_DLGTITLE, 0);
	templateGenerator.ReleaseDlgTemplate(tmp);
}

void VRayCamera::EndEditParams(IObjParam *ip, ULONG flags, Animatable *next) {
	DestroyCPParamMap2(pmap);
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
}

// This is called at the end of the animation
void VRayCamera::renderEnd(VR::VRayRenderer *vray) {
}

// Called at the start of each frame
void VRayCamera::frameBegin(VR::VRayRenderer *vray) {
	const VR::VRayFrameData &fdata=vray->getFrameData();

	TimeValue t=fdata.t;

	stereo_camera=pblock->GetInt(pb_camera, t);
	fov_angle=pblock->GetFloat(pb_fov_angle, t);
	zero_parallax_sphere=pblock->GetFloat(pb_zero_parallax_sphere, t);
	separation=pblock->GetFloat(pb_separation, t);
	forward_tilt=pblock->GetFloat(pb_forward_tilt, t);
	tilt_compensation=pblock->GetInt(pb_tilt_compensation, t);
	separation_map=pblock->GetFloat(pb_separation_map, t);
	head_turn_map=pblock->GetFloat(pb_head_turn_map, t);
	head_tilt_map=pblock->GetFloat(pb_head_tilt_map, t);
	flip_x=pblock->GetInt(pb_flip_x, t);
	flip_y=pblock->GetInt(pb_flip_y, t);

	fov=pblock->GetFloat(pb_fov, fdata.t);
	targetDist=GetTDist((TimeValue) fdata.t);
	aperture=0.0f;

	camera.SetPos(fdata.camToWorld.offs, -fdata.camToWorld.m[2], fdata.camToWorld.m[1], fdata.camToWorld.m[0]);
	camera.Init(fdata.imgWidth, fdata.imgHeight, fov, 1.0f, aperture, targetDist);

	this->vray=vray;
}

// Called at the end of each frame
void VRayCamera::frameEnd(VR::VRayRenderer *vray) {
}

VR::Vector VRayCamera::getDir(double xs, double ys, int rayVsOrgReturnMode) const {
  // Note: rayVsOrgReturnMode == 0 means ray, rayVsOrgReturnMode == 1 means org data is returned

	const VR::VRayFrameData &fdata=vray->getFrameData();
	
  // Get the image coordinates
  //double rx=(xs-fdata.imgWidth*0.5)/(fdata.imgWidth*0.5f);
  //double ry=(fdata.imgHeight*0.5-ys)/(fdata.imgHeight*0.5f);
  
  // Swap X-Y to rotate the cartesian axis 90 degrees CW
  double ry=(xs-fdata.imgWidth*0.5f)/(fdata.imgWidth*0.5f);
  double rx=(ys-fdata.imgHeight*0.5f)/(fdata.imgHeight*0.5f);
  
  double r, phi, theta, rot, tmp, tmpY, tmpZ;
  //double offset;
  double sinP, cosP, sinT, cosT, sinR, cosR, sinD, cosD;
  //double head_tilt = head_tilt_map;
  
  VR::Vector org, ray, target, htarget;
  //Matrix tilt;
  
  // Convert FOV from degrees to radians
  double fov_angle_rad = fov_angle * DOME_DTOR; 
  double forward_tilt_rad = forward_tilt * DOME_DTOR;
  

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
    theta = r * (fov_angle_rad / 2.0);

    // Todo: Port this MR code
    // Start by matching the camera (center camera)
    // Tip: internal point to camera space
    // mi_point_to_camera(state, &org, &state->org);

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
    target.x = (float)(sinP * sinT);
    target.y = (float)(-cosP * sinT);
    target.z = (float)(-cosT);
    

    // Camera selection and initial position
    // 0=center, 1=Left, 2=Right
    switch (stereo_camera) {
    case CENTERCAM:
      ray = target;
      break;
      
    case LEFTCAM:
      // Use the separation texture map
      org.x = (float)((-separation) * (separation_map) / 2.0);
      // Debugging Alternate: use a constant separation map value
      //org.x = (float)(-separation * 1.0 / 2.0);
      break;
      
    case RIGHTCAM:
      // Use the separation texture map
      org.x = (float)((separation) * (separation_map) / 2.0);
      // Debugging Alternate: use a constant separation map value
      //org.x = (float)(separation * 1.0 / 2.0);
      break;
      
    default:
      ray = target;
      break;
    }
    

    // horizontal mode
    if (stereo_camera != CENTERCAM) {
      
      // Tilted dome mode ON
      if(tilt_compensation) {
        
        // head rotation
        tmpY = target.y * cos(-forward_tilt_rad) - target.z * sin(-forward_tilt_rad);
        tmpZ = target.z * cos(-forward_tilt_rad) + target.y * sin(-forward_tilt_rad);
        rot = atan2(target.x,-tmpY) * head_turn_map;
        
        if (vertical_mode) {
          rot *= fabs(sinP);
        }
        
        sinR = sin(rot); 
        cosR = cos(rot);
        sinD = sin(forward_tilt_rad);
        cosD = cos(forward_tilt_rad);
        
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
          rot = atan2(target.x,-target.z) * head_turn_map * fabs(sinP);
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
          rot = phi * head_turn_map;
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
      
      // Compute ray from camera to target
      target *= zero_parallax_sphere;
      ray = target - org;
      ray = normalize(ray);
    } 
    
    // head tilt
    //head_tilt = (double)((head_tilt - 0.5) * DOME_PI);
    
    // Rotate vector tilt
    
    //Todo: Find the vray replacement for this mental ray line:
    //mi_matrix_rotate_axis(tilt, &htarget, head_tilt);
    
    //vector_by_matirx_mult(&org, tilt, &org);
    
    
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
    
    // Convert ray from camera space
    // Todo: Port this MR code

    // Tip: camera vector to internal space
    //mi_vector_from_camera(state, &ray, &ray);

    // Tip: camera point to internal space
    //mi_point_from_camera(state, &org, &org);

    // Note: rayVsOrgReturnMode == 0 means ray, rayVsOrgReturnMode == 1 means org data is returned
    if(rayVsOrgReturnMode == 0){
      return fdata.camToWorld.m*ray;
    } else if (rayVsOrgReturnMode == 1){
      return fdata.camToWorld.offs-org;
    }
    
  //This is connected to the if( r> 1.0) code
  } else {
    // Todo Work out the return black color code
    //Note: rayVsOrgReturnMode == 0 means ray, rayVsOrgReturnMode == 1 means org data is returned
    if(rayVsOrgReturnMode == 0){
      //return fdata.camToWorld.m*ray;
      ray.x=0.0;
      ray.y=0.0;
      ray.z=0.0;
      return ray;
    } else if (rayVsOrgReturnMode == 1){
      //return fdata.camToWorld.offs;

      org.x=0.0;
      org.y=0.0;
      org.z=0.0;
      return org;
    }
    

  } 
  //fallback return option to eliminate VS2010 "not all control paths return a value" warning
  return org;
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
  VR::Vector dir=getDir(xs, ys, 0);   //Return the dir data from the getDir function
  VR::Vector org=getDir(xs, ys, 1);   //Return the org data from the getDir function
  
  rayDeriv.dPdx.makeZero();
  rayDeriv.dPdy.makeZero();

  double delta=0.01f;
  rayDeriv.dDdx=(getDir(xs+delta, ys, 0)-getDir(xs-delta, ys, 0))/float(delta*2.0f);
  rayDeriv.dDdy=(getDir(xs, ys+delta, 0)-getDir(xs, ys-delta, 0))/float(delta*2.0f);
  
  const VR::VRayFrameData &fdata=vray->getFrameData();
  ray.p=org;
  ray.dir=dir;

  mint=0.0f;
  maxt=1e18f;

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
		}
		else
		{
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
