// DomemasterStereo Arnold Shader
// 2014-10-31 4.31 pm
// --------------------------------------
// Ported to Arnold by Andrew Hazelden and Luis Silva
// Based upon the mental ray shader domeAFL_FOV_Stereo  
// by Roberto Ziche

#include <stdio.h>
#include <math.h>
#include <cstring>
#include <ai.h>
#include <ai_cameras.h>
#include <ai_nodes.h>
#include <ai_metadata.h>

// For use with the Windows Visual Studio compiler and strcpy_s()
// #include <string>

AI_CAMERA_NODE_EXPORT_METHODS(DomemasterStereo_Methods);

#define camera                     (params[0].INT)
#define fovDegrees                 (params[1].FLT)
#define zeroParallaxSphere         (params[2].FLT)
#define separation                 (params[3].FLT)
#define forwardTilt                (params[4].FLT)
#define tiltCompensation           (params[5].FLT)
#define verticalMode               (params[6].FLT)
#define separationMap              (params[7].FLT)
#define headTurnMap                (params[8].FLT)
#define headTiltMap                (params[9].FLT)
#define flipRayX                   (params[10].FLT)
#define flipRayY                   (params[11].FLT)

#define CENTERCAM    0
#define LEFTCAM      1
#define RIGHTCAM     2

// Link to the external (Softimage SPDL / Maya + Houdini Metadata GUI) parameters
node_parameters {
  AiParameterInt("camera", 0);
  AiParameterFlt("fov_angle", 180.f);
  AiParameterFlt("zero_parallax_sphere", 360.f);
  AiParameterFlt("separation", 6.5f);
  AiParameterFlt("forward_tilt", 0.0f);
  AiParameterBool("tilt_compensation", false);
  AiParameterBool("vertical_mode", false);
  AiParameterFlt("separation_map", 1.f);
  AiParameterFlt("head_turn_map", 1.f);
  AiParameterFlt("head_tilt_map", 0.5f);
  AiParameterBool("flip_ray_x", false);
  AiParameterBool("flip_ray_y", false);
}

node_initialize {
  AiCameraInitialize(node, NULL);
}

node_update {
  AiCameraUpdate(node, false);
}

node_finish {
  AiCameraDestroy(node);
}

camera_create_ray {
  double x, y, r, phi, theta, rot, tmp, tmpY, tmpZ;
  //double offset;
  double sinP, cosP, sinT, cosT, sinR, cosR, sinD, cosD;
  //double headTiltMap;
  AtVector org, ray, target, htarget;
  //AtMatrix tilt;
  
  // Get camera parameters
  const AtParamValue* params = AiNodeGetParams(node); 
  
  // Convert fov and dome_tilt from degrees to radians
  float fov_angle = fovDegrees * AI_DTOR; 
  float dome_tilt = forwardTilt * AI_DTOR;
  
  //AiMsgInfo("II-> fov=%f,cam=%d,rad=%f,tilt=%f,sep=%f,comp=%d,vert=%d", fovDegrees, camera, zeroParallaxSphere, forwardTilt, separation, tiltCompensation, verticalMode);

  // Swap X-Y and apply a vertical symmetry
  x = - input->sy;
  y = input->sx;
  
  // Compute radius
  // Todo: compare sqrt() performance with AI_SQRT2()
  r = sqrt((x * x) + (y * y));
  
  if (r < 1.0) {
  
    // Compute phi angle
    if ((r > -AI_EPSILON) && (r < AI_EPSILON)) {
      phi = 0.0;
    } else {
      phi = atan2(y,x);
    }
    
    // Compute theta angle
    theta = r * (fov_angle / 2.0);
    
    // Todo: Port this MR code
    // Start by matching the camera (center camera)
    // Tip: internal point to camera space
    // mi_point_to_camera(state, &org, &state->org);
    
    // Initialize camera position
    org = 0.0;
    
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
    switch (camera) {
    case CENTERCAM:
      ray = target;
      break;
      
    case LEFTCAM:
      org.x = (float)(-separation * separationMap / 2.0);
      break;
      
    case RIGHTCAM:
      org.x = (float)(separation * separationMap / 2.0);
      break;
      
    default:
      ray = target;
      break;
    }
    
    // horizontal mode
    if (camera != CENTERCAM) {
      
      // Tilted dome mode ON
      if(tiltCompensation) {
        
        // head rotation
        tmpY = target.y * cos(-dome_tilt) - target.z * sin(-dome_tilt);
        tmpZ = target.z * cos(-dome_tilt) + target.y * sin(-dome_tilt);
        rot = atan2(target.x,-tmpY) * headTurnMap;
        
        if (verticalMode) {
          rot *= fabs(sinP);
        }
        
        sinR = sin(rot); 
        cosR = cos(rot);
        sinD = sin(dome_tilt);
        cosD = cos(dome_tilt);
        
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
        if (verticalMode) {
          
          // head rotation
          rot = atan2(target.x,-target.z) * headTurnMap * fabs(sinP);
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
          rot = phi * headTurnMap;
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
      
      // head tilt
      //headTiltMap = (double)((headTiltMap - 0.5) * AI_PI);
      
      // Rotate vector
      //AiM4Identity(tilt);
      
      //Todo: Find the Arnold replacement for this mental ray line:
      // Rotate the tilt matrix, around axis htarget, by a point headTiltMap radians
      //mi_matrix_rotate_axis(tilt, &htarget, headTiltMap);
      
      //AiM4VectorByMatrixMult(&org, tilt, &org);
      
      // Compute ray from camera to target
      target *= zeroParallaxSphere;
      ray = target - org;
      ray = AiV3Normalize(ray);
    }
    
    //AiMsgInfo("II->,Phi=%f,Theta=%f,rot=%f,camx=%f,camy=%f", (float)phi, (float)theta, (float)rot, (float)org.x, (float)org.y);
    
    // Flip the X ray direction about the Y-axis
    // if(flipRayX) {
      // org.x = (-org.x);
      // ray.x = (-ray.x);
    // }
    
    // Flip the Y ray direction about the X-axis
    // if(flipRayY) {
      // org.z = (-org.z);
      // ray.z = (-ray.z);
    // }
    
    // Convert ray from camera space
    // Todo: Port this MR code
    
    // Tip: camera vector to internal space
    //mi_vector_from_camera(state, &ray, &ray);
    
    // Tip: camera point to internal space
    //mi_point_from_camera(state, &org, &org);
    
    //Optional Todo: look at the code to implement the Arnold data->calculateDerivatives functions
    
    // output
    output->origin = org;
    output->dir = ray;
    output->weight = 1.0;
  } else  {
    output->weight = 0.0;
  }
}

node_loader {
  if (i > 0) return false;
  node->methods      = DomemasterStereo_Methods;
  node->output_type = AI_TYPE_NONE;
  node->name          = "DomemasterStereo";
  node->node_type   = AI_NODE_CAMERA;
  
  // Note: Visual Studio prefers strcpy_s which will remove the compiler warning message
  #if defined _WIN32 || defined _WIN64
  strcpy_s(node->version, AI_VERSION);
  #else
  strcpy(node->version, AI_VERSION);
  #endif
  
  return true;
}