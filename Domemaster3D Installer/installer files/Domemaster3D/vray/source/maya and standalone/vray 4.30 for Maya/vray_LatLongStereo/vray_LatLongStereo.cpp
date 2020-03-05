// vray_LatLongStereo Shader v0.5
// 2015-04-01 11.38 pm
// ---------------------------------
// Ported to Vray 3.0 by Andrew Hazelden/Roberto Ziche
// Based upon the mental ray shader LatLong_Stereo  
// by Roberto Ziche

//**************************************************
//**************************************************

#include "vrayplugins.h"
#include "vrayinterface.h"
#include "vrayrenderer.h"
#include "misc_ray.h"
#include "mcsampler.h"

using namespace VR;

struct LatLongStereo_ParamsStruct {
  int   camera;
  float fov_vert_angle; 
  float fov_horiz_angle;
  float parallax_distance;
  float separation;
  int   zenith_mode;
  float separation_map;
  float head_tilt_map;
  int   flip_x;
  int   flip_y;
  int   poles_corr;
  float poles_corr_start;
  float poles_corr_end;
  float neck_offset;
  int   zenith_fov;
};

#define CENTERCAM    0
#define LEFTCAM      1
#define RIGHTCAM     2

#define DOME_PI  3.141592653589793238
#define DOME_DTOR  0.0174532925199433
#define DOME_PIOVER2 1.57079632679489661923

#define GETDIR        0
#define GETORG        1

//**************************************************
// The actual camera
class LatLongStereoImpl : public VRayCamera {
	LatLongStereo_ParamsStruct *params;
	VRayRenderer *vray;

	VR::VRayFrameDataCameraFilmTrans* cameraFilmTrans;
public:
	LatLongStereoImpl() : cameraFilmTrans(NULL) {}

	// From VRayCamera
	int getScreenRay(
		double xs,
		double ys,
		double time,
		const float *rnds,
		int numRnds,
		TraceRay &ray,
		Ireal &mint,
		Ireal &maxt,
		RayDeriv &rayDeriv,
		ShadeCol &multResult,
		uint32 flags
	) const override;

	/// Returns camera flags @see VRayCameraFlags enum
	uint32 getFlags(void) const override {
		return vrayCameraFlags_empty;
	}

	void renderBegin(VRayRenderer *vray) {}
	void renderEnd(VRayRenderer *vray) {}
	void frameBegin(VR::VRayRenderer *vray);
	void frameEnd(VRayRenderer *vray) {}

	// From VRayCamera2
	void frameBeginImpl(VR::VRayRenderer *vray, const VR::VRaySequenceData &sdata, const VR::VRayFrameData &fdata) { frameBegin(vray); }

	// Other methods
	void init(LatLongStereo_ParamsStruct &params);
	simd::Vector3f getDir(double xs, double ys, int rayVsOrgReturnMode) const;
};

void LatLongStereoImpl::init(LatLongStereo_ParamsStruct &p) {
	params = &p;
}

void LatLongStereoImpl::frameBegin(VR::VRayRenderer *vray) {
	this->vray = vray;

	const VR::VRayFrameData &_fdata = vray->getFrameData();
	VR::VRayFrameData &fdata = const_cast<VR::VRayFrameData&>(_fdata);

	VR::VRayFrameDataCameraFilmTrans* filmTrans = static_cast<VR::VRayFrameDataCameraFilmTrans*>(fdata.newInterface(EXT_FRAME_DATA_CAMERA_FILM_TRANS));

	if (filmTrans && filmTrans->params.enabled) {
		cameraFilmTrans = filmTrans;
	}
}

simd::Vector3f LatLongStereoImpl::getDir(double xs, double ys, int rayVsOrgReturnMode) const {

	const VR::VRayFrameData &fdata=vray->getFrameData();
	
  double rx = 2.0f * xs / fdata.imgWidth - 1.0f;
  double ry = -2.0f * ys / fdata.imgHeight + 1.0f;

  double phi, theta, tmp;
  double sinP, cosP, sinT, cosT;
  //double head_tilt = params->head_tilt_map;
  
  VR::Vector org, ray, target, htarget;
  
  // Check the stereo camera view for 0=center, 1=Left, 2=Right
  int stereo_camera = params->camera;
  
  double fov_vert_angle = params->fov_vert_angle * DOME_DTOR;  
  double fov_horiz_angle = params->fov_horiz_angle * DOME_DTOR; 
  float parallax_distance = params->parallax_distance;
  float separation = params->separation;
  int zenith_mode = params->zenith_mode;
  int flip_x = params->flip_x;
  int flip_y = params->flip_y;
  int poles_corr = params->poles_corr;
  float poles_corr_start = params->poles_corr_start * DOME_DTOR;
  float poles_corr_end = params->poles_corr_end * DOME_DTOR;
  float neck_offset = params->neck_offset;
  int zenith_fov = params->zenith_fov;

  // check poles correction angles
  if (poles_corr_end < poles_corr_start)
    poles_corr_end = poles_corr_start;
  
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
  org.x = org.y = org.z = 0.0;
  
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
  } else {
    target.x = (float)(sinP * cosT);
    target.y = (float)(sinT);
    target.z = (float)(-cosP * cosT);
  }
  
  // Camera selection and initial position
  // 0=center, 1=Left, 2=Right
  if (stereo_camera != CENTERCAM) {
  
    //float separation_mult = params->separation_map;
    float separation_mult = 1.0f;// TODO separation map
    float separation_mult_auto = 1.0f;

    // Additional automatic separation fade
    if (poles_corr) {
      float tmpTheta;
      if (zenith_mode)
        tmpTheta = abs(DOME_PIOVER2 - theta);
      else 
        tmpTheta = abs(theta);
      if (tmpTheta > poles_corr_start) {
        if (tmpTheta < poles_corr_end) {
          float fadePos = (tmpTheta - poles_corr_start) / (poles_corr_end - poles_corr_start);
            separation_mult_auto = (cos(fadePos*DOME_PI) + 1.0f) / 2.0f;
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
    return simd::Vector3f(ray);
  } else {  
    // GETORG
    return simd::Vector3f(org);
  }
}

int LatLongStereoImpl::getScreenRay(
		double xs,
		double ys,
		double time,
		const float *rnds,
		int numRnds,
		TraceRay &ray,
		Ireal &mint,
		Ireal &maxt,
		RayDeriv &rayDeriv,
		ShadeCol &multResult,
		uint32 flags
) const {
	if (cameraFilmTrans) {
		const VR::VRayFrameData& fdata = vray->getFrameData();
		cameraFilmTrans->transformScreenRay(xs, ys, fdata.rgnLeft, fdata.rgnTop, fdata.imgWidth, fdata.imgHeight);
	}

  simd::Vector3f dir = getDir(xs, ys, GETDIR);   //Return the dir data from the getDir function
  simd::Vector3f org = getDir(xs, ys, GETORG);   //Return the org data from the getDir function
  
  rayDeriv.dPdx.makeZero();
  rayDeriv.dPdy.makeZero();

  double delta=0.01f;
  rayDeriv.dDdx = (getDir(xs + delta, ys, GETDIR) - getDir(xs - delta, ys, GETDIR)) / float(delta*2.0f);
  rayDeriv.dDdy = (getDir(xs, ys + delta, GETDIR) - getDir(xs, ys - delta, GETDIR)) / float(delta*2.0f);
  
  const VR::VRayFrameData &fdata=vray->getFrameData();
  ray.p = fdata.camToWorld.offs + fdata.camToWorld.m*org;
  ray.dir = fdata.camToWorld.m*dir;

  mint = 0.0f;
  maxt = LARGE_FLOAT;

  return true;
}

//**************************************************
// Plugin stuff

// This structure describes the parameters of the plugin; the parameters must be of the
// exact same type and in the same order as in the LatLongStereo_ParamsStruct structure.
struct LatLongStereo_Params: VRayParameterListDesc {
  LatLongStereo_Params(void) {
    addParamInt("camera", 0, -1, "Center, Left, Right Camera Views");
    addParamFloat("fov_vert_angle", 180.0f, -1, "Field of View Vertical");
    addParamFloat("fov_horiz_angle", 360.0f, -1, "Field of View Horizontal");
    addParamFloat("parallax_distance", 360.0f, -1, "Zero Parallax Distance");
    addParamFloat("separation", 6.5f, -1, "Camera Separation");
    addParamBool("zenith_mode", false, -1, "Zenith Mode");
    addParamFloat("separation_map", 1.0f, -1, "Separation Map");
    addParamFloat("head_tilt_map", 0.5f, -1, "Head Tilt map");
    addParamBool("flip_x", false, -1, "Flip X");
    addParamBool("flip_y", false, -1, "Flip Y");
	addParamBool("poles_corr", true, -1, "Poles Correction");
	addParamFloat("poles_corr_start", 45.f, -1, "Poles Correction Start Angle");
	addParamFloat("poles_corr_end", 85.f, -1, "Poles Correction End Angle");
    addParamFloat("neck_offset", 0.0f, -1, "Neck Offset");
    addParamBool("zenith_fov", false, -1, "Hemi-equirectangular");
	}
};

class LatLongStereo: public VRayRenderSettings {
  // The actual camera that will be used
  LatLongStereoImpl camera;

  // Cached parameters
  LatLongStereo_ParamsStruct params;
public:
  LatLongStereo(VRayPluginDesc *pluginDesc):VRayRenderSettings(pluginDesc) {
    // We want the parameters to be cached to the params structure
    paramList->setParamCache("camera", &params.camera);
    paramList->setParamCache("fov_vert_angle", &params.fov_vert_angle);
    paramList->setParamCache("fov_horiz_angle", &params.fov_horiz_angle);
    paramList->setParamCache("parallax_distance", &params.parallax_distance);
    paramList->setParamCache("separation", &params.separation);
    paramList->setParamCache("zenith_mode", &params.zenith_mode);
    paramList->setParamCache("separation_map", &params.separation_map);
    paramList->setParamCache("head_tilt_map", &params.head_tilt_map);
    paramList->setParamCache("flip_x", &params.flip_x);
    paramList->setParamCache("flip_y", &params.flip_y);
    paramList->setParamCache("poles_corr", &params.poles_corr);
    paramList->setParamCache("poles_corr_start", &params.poles_corr_start);
    paramList->setParamCache("poles_corr_end", &params.poles_corr_end);
    paramList->setParamCache("neck_offset", &params.neck_offset);
    paramList->setParamCache("zenith_fov", &params.zenith_fov);
  }

	// From RenderSettingsExtension
	void setupSequenceData(VR::VRaySequenceData &sdata) {
		// Note that this method is called before frameBegin(), and so parameters have not been cached
		// Therefore, cache the parameters here - computes the actual parameter values from the scene
		// description
		paramList->cacheParams();

    // Initialize the camera
    camera.init(params);

		// Set the camera into the sequence data so that VRay can use it
		sdata.cameraRaySampler=static_cast<VRayCamera*>(&camera);
	}
	
	void setupFrameData(VR::VRayFrameData &fdata) {
		paramList->cacheParams(fdata.t);
		// The field of view may be specified by a SettingsCamera plug-in, so only set it here if explicitly specified;
		//if (paramList->getParam("fov")) fdata.fov=params.fov;
	}
	void renderEnd(VR::VRayRenderer *vray) {
		VRayRenderSettings::renderEnd(vray);
		
		VRaySequenceData &sdata=const_cast<VR::VRaySequenceData&>(vray->getSequenceData());
		VR::VRayCamera *cameraSampler=static_cast<VR::VRayCamera*>(&camera);
		vray->setCameraRaySampler(NULL, 1, cameraSampler);
	}
};


#define LatLongStereo_PluginID PluginID(LARGE_CONST(1185226))

PLUGIN_LIBRARY("Cameras", "V-Ray Cameras");
PLUGIN_DESC(LatLongStereo_PluginID, "LatLongStereo", "LatLongStereo plugin for V-Ray", LatLongStereo, LatLongStereo_Params, EXT_RENDER_SETTINGS);

