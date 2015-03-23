// DomemasterStereo Vray Shader v0.3
// 2014-12-24 
// ---------------------------------
// Ported to Vray 2.0 by Andrew Hazelden
// Based upon the mental ray shader domeAFL_FOV_Stereo  
// by Roberto Ziche

// Todo:
// Work out the return black color code if the check for "if (r < 1.0)" comes back as false

//**************************************************
//**************************************************

#include "vrayplugins.h"
#include "vrayinterface.h"
#include "vrayrenderer.h"
#include "misc_ray.h"
#include "mcsampler.h"

#include "globalnewdelete.cpp"

using namespace VR;

struct DomemasterStereo_ParamsStruct {
  int   camera;
  float fov_angle; 
  float zero_parallax_sphere;
  float separation;
  float forward_tilt;
  int   tilt_compensation;
  int   vertical_mode;
  float separation_map;
  float head_turn_map;
  float head_tilt_map;
  int   flip_x;
  int   flip_y;
};

#define CENTERCAM    0
#define LEFTCAM      1
#define RIGHTCAM     2

#define DOME_PI  3.141592653589793238
#define DOME_DTOR  0.0174532925199433 
#define DOME_PIOVER2 1.57079632679489661923 
#define DOME_EPSILON	0.00001

//**************************************************
// The actual camera
class DomemasterStereoImpl: public VRayCamera2 {
  DomemasterStereo_ParamsStruct *params;
  VRayRenderer *vray;

public:
  // From VRayCamera
  virtual int getScreenRay(   double xs, double ys, 
  double time, 
  float dof_uc, float dof_vc, 
  TraceRay &ray, 
  Ireal &mint, Ireal &maxt, 
  RayDeriv &rayDeriv, 
  VR::Color &multResult) const;

  virtual int getScreenRays(  VR::RayBunchCamera& raysbunch,
  const double* xs,   const double* ys, 
  const float* dof_uc, const float* dof_vc, 
  bool calcDerivs = false ) const;

  int canDoDOF(void) { return false; }
  Vector2 mapToScreen(const Vector &p) { return Vector2(p.x, p.y); }

  void renderBegin(VRayRenderer *vray) {}
  void renderEnd(VRayRenderer *vray) {}
  void frameBegin(VR::VRayRenderer *vray);
  void frameEnd(VRayRenderer *vray) {}

  // From VRayCamera2
  void frameBeginImpl(VR::VRayRenderer *vray, const VR::VRaySequenceData &sdata, const VR::VRayFrameData &fdata) { frameBegin(vray); }

  // Other methods
  void init(DomemasterStereo_ParamsStruct &params);
  Vector getDir(double xs, double ys, int rayVsOrgReturnMode) const;
};

void DomemasterStereoImpl::init(DomemasterStereo_ParamsStruct &p) {
  params=&p;
}

void DomemasterStereoImpl::frameBegin(VR::VRayRenderer *vray) {
  this->vray=vray;
}

Vector DomemasterStereoImpl::getDir(double xs, double ys, int rayVsOrgReturnMode) const {
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
  //double head_tilt = params->head_tilt_map;
  
  Vector org, ray, target, htarget;
  //Matrix tilt;
  
  // Convert FOV from degrees to radians
  double fov_angle = params->fov_angle * DOME_DTOR; 
  double forward_tilt = params->forward_tilt * DOME_DTOR;
  

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
    theta = r * (fov_angle / 2.0);

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
    switch (params->camera) {
    case CENTERCAM:
      ray = target;
      break;
      
    case LEFTCAM:
      // Use the separation texture map
      org.x = (float)((-params->separation) * (params->separation_map) / 2.0);
      // Debugging Alternate: use a constant separation map value
      //org.x = (float)(-params->separation * 1.0 / 2.0);
      break;
      
    case RIGHTCAM:
      // Use the separation texture map
      org.x = (float)((params->separation) * (params->separation_map) / 2.0);
      // Debugging Alternate: use a constant separation map value
      //org.x = (float)(params->separation * 1.0 / 2.0);
      break;
      
    default:
      ray = target;
      break;
    }
    

    // horizontal mode
    if (params->camera != CENTERCAM) {
      
      // Tilted dome mode ON
      if(params->tilt_compensation) {
        
        // head rotation
        tmpY = target.y * cos(-forward_tilt) - target.z * sin(-forward_tilt);
        tmpZ = target.z * cos(-forward_tilt) + target.y * sin(-forward_tilt);
        rot = atan2(target.x,-tmpY) * params->head_turn_map;
        
        if (params->vertical_mode) {
          rot *= fabs(sinP);
        }
        
        sinR = sin(rot); 
        cosR = cos(rot);
        sinD = sin(params->forward_tilt);
        cosD = cos(params->forward_tilt);
        
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
        if (params->vertical_mode) {
          
          // head rotation
          rot = atan2(target.x,-target.z) * params->head_turn_map * fabs(sinP);
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
          rot = phi * params->head_turn_map;
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
      target *= params->zero_parallax_sphere;
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
    if(params->flip_x) {
      org.x = -org.x;
      ray.x = -ray.x;
    }
    
    // Flip the Y ray direction about the X-axis
    if(params->flip_y) {
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
}


int DomemasterStereoImpl::getScreenRay(double xs, double ys, double time, float dof_uc, float dof_vc, TraceRay &ray, Ireal &mint, Ireal &maxt, RayDeriv &rayDeriv, VR::Color &multResult) const {
  Vector dir=getDir(xs, ys, 0);   //Return the dir data from the getDir function
  Vector org=getDir(xs, ys, 1);   //Return the org data from the getDir function
  
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


int DomemasterStereoImpl::getScreenRays(  
VR::RayBunchCamera& raysbunch,
const double* xs,   const double* ys, 
const float* dof_uc, const float* dof_vc, 
bool calcDerivs /*= false*/ ) const
{
  for( uint32 i = 0; i < raysbunch.getCount(); i++ ) raysbunch.mints()[i] = 0.0f;
  for( uint32 i = 0; i < raysbunch.getCount(); i++ ) raysbunch.maxts()[i] = LARGE_FLOAT;

  // This should be SingleOrigin for pinhole cameras for better performance
  raysbunch.setType( RayBunchBaseParams<RAYS_IN_BUNCH>::MultipleOrigins );

  bool success = true;

  // By default call single rays versions
  for( unsigned int i = 0 ; i < raysbunch.getCount(); i++ )
  {
    TraceRay ray;
    RayDeriv deriv;
    Color multResult( 1.0f, 1.0f, 1.0f );
    bool res = getScreenRay( xs[i], ys[i], 
    raysbunch.times()[ i ], 
    dof_uc[i], dof_vc[i], 
    ray, 
    raysbunch.mints()[i],
    raysbunch.maxts()[i],
    deriv,
    multResult );

    success &= res;

    if (res) {
      // Scatter
      raysbunch.origins(0)[i] = ray.p.x;
      raysbunch.origins(1)[i] = ray.p.y;
      raysbunch.origins(2)[i] = ray.p.z;
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


//**************************************************
// Plugin stuff

// This structure describes the parameters of the plugin; the parameters must be of the
// exact same type and in the same order as in the DomemasterStereo_ParamsStruct structure.
struct DomemasterStereo_Params: VRayParameterListDesc {
  DomemasterStereo_Params(void) {
    addParamInt("camera", 0, -1, "Center, Left, Right Camera Views");
    addParamFloat("fov_angle", 180.0f, -1, "Field of View");
    addParamFloat("zero_parallax_sphere", 360.0f, -1, "Zero Parallax Sphere");
    addParamFloat("separation", 6.5f, -1, "Camera Separation Distance");
    addParamFloat("forward_tilt", 0.0f, -1, "Forward Tilt");
    addParamBool("tilt_compensation", false, -1, "Tilt Compensation Mode");
    addParamBool("vertical_mode", false, -1, "Vertical Mode");
    addParamFloat("separation_map", 1.0f, -1, "Separation Map");
    addParamFloat("head_turn_map", 1.0f, -1, "Head Turn Map");
    addParamFloat("head_tilt_map", 0.5f, -1, "Head Tilt map");
    addParamBool("flip_x", false, -1, "Flip X");
    addParamBool("flip_y", false, -1, "Flip Y");
  }
};


class DomemasterStereo: public VRayRenderSettings {
  // The actual camera that will be used
  DomemasterStereoImpl camera;

  // Cached parameters
  DomemasterStereo_ParamsStruct params;
public:
  DomemasterStereo(VRayPluginDesc *pluginDesc):VRayRenderSettings(pluginDesc) {
    // We want the parameters to be cached to the params structure
    paramList->setParamCache("camera", &params.camera);
    paramList->setParamCache("fov_angle", &params.fov_angle);
    paramList->setParamCache("zero_parallax_sphere", &params.zero_parallax_sphere);
    paramList->setParamCache("separation", &params.separation);
    paramList->setParamCache("forward_tilt", &params.forward_tilt);
    paramList->setParamCache("tilt_compensation", &params.tilt_compensation);
    paramList->setParamCache("vertical_mode", &params.vertical_mode);
    paramList->setParamCache("separation_map", &params.separation_map);
    paramList->setParamCache("head_turn_map", &params.head_turn_map);
    paramList->setParamCache("head_tilt_map", &params.head_tilt_map);
    paramList->setParamCache("flip_x", &params.flip_x);
    paramList->setParamCache("flip_y", &params.flip_y);
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

#define DomemasterStereo_PluginID PluginID(LARGE_CONST(1185227))
SIMPLE_PLUGIN_LIBRARY(DomemasterStereo_PluginID, EXT_RENDER_SETTINGS, "DomemasterStereo", "DomemasterStereo plugin for V-Ray", DomemasterStereo, DomemasterStereo_Params);

