// LatLongStereo Arnold Shader
// 2014-10-31 4.23 pm
// ---------------------------------
// Ported to Arnold by Andrew Hazelden
// Based upon the mental ray shader LatLong_Stereo  
// by Roberto Ziche

#include <stdio.h>
#include <math.h>
#include <cstring>
#include <ai.h>
#include <ai_cameras.h>
#include <ai_nodes.h>
#include <ai_metadata.h>

// For use with the Windows Visual Studio compiler and strcpy_s()
//#include <string>

AI_CAMERA_NODE_EXPORT_METHODS(LatLongStereo_Methods);

#define camera                     (params[0].INT)
#define fovVertDegrees             (params[1].FLT)
#define fovHorizDegrees            (params[2].FLT)
#define ParallaxDistance           (params[3].FLT)
#define separation                 (params[4].FLT)
#define zenithMode                 (params[5].FLT)
#define separationMap              (params[6].FLT)
#define headTiltMap                (params[7].FLT)
#define flipRayX                   (params[8].FLT)
#define flipRayY                   (params[9].FLT)

#define CENTERCAM    0
#define LEFTCAM      1
#define RIGHTCAM     2

// Link to the external (Softimage SPDL / Maya + Houdini Metadata GUI) parameters
node_parameters {
  AiParameterInt("camera", 0);
  AiParameterFlt("fov_vert_angle", 180.f);
  AiParameterFlt("fov_horiz_angle", 360.f);
  AiParameterFlt("parallax_distance", 360.f);
  AiParameterFlt("separation", 6.5f);
  AiParameterBool("zenith_mode", false);
  AiParameterFlt("separation_map", 1.f);
  AiParameterFlt("head_tilt_map", 1.f);
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
  double x, y, phi, theta, tmp;
  double sinP, cosP, sinT, cosT;
  //double head_tilt;
  AtVector org, ray, target, htarget;
  //AtMatrix tilt;
  
  // Get camera parameters
  const AtParamValue* params = AiNodeGetParams(node); 
  
  //head_tilt = headTiltMap;
  
  // Convert FOV from degrees to radians
  double fovVert = fovVertDegrees * AI_DTOR;  
  double fovHoriz = fovHorizDegrees * AI_DTOR;  
  
  // Get the image coordinates
  x = input->sx;
  y = input->sy;

  // Calculate phi and theta...
  phi = x * (fovHoriz / 2.0);
  if(zenithMode){
    theta = AI_PIOVER2 - y * (fovVert / 2.0);
  } else {
   theta = y * (fovVert / 2.0);
  }  
  
  // Calculate phi and theta...
  //phi = x * (fovHoriz / 2.0);
  //if(zenithMode) {
  //  theta = AI_PIOVER2 - y * (fovVert);
  //} else {
  //  theta = y * (fovVert);
  //}  
  
  // Start by matching camera (center camera)
  org = 0.0;
  
  // Compute commonly used values
  sinP = sin(phi);
  cosP = cos(phi);
  sinT = sin(theta);
  cosT = cos(theta);
  
  // Center camera target vector (normalized)
  if(zenithMode) {
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
  if (camera != CENTERCAM) {
    // camera selection and initial position
    if (camera == LEFTCAM) {
      org.x = (float)(-separation * separationMap / 2.0);
    } else if (camera == RIGHTCAM) {
      org.x = (float)(separation * separationMap / 2.0);
    }
    
    // head rotation = phi
    // rotate camera
    if(zenithMode) {
      tmp = (float)((org.x * cosP) - (org.y * sinP));
      org.y = (float)((org.y * cosP) + (org.x * sinP));
      org.x = (float)tmp;
    } else {
      tmp = (float)((org.x * cosP) - (org.z * sinP));
      org.z = (float)((org.z * cosP) + (org.x * sinP));
      org.x = (float)tmp;
    }
    
    // calculate head target
    htarget.x = (float)(sinP * sinT);
    htarget.y = (float)(-cosP * sinT);
    htarget.z = (float)target.z;
    
    // head tilt
    //head_tilt = (double)((head_tilt - 0.5) * AI_PI);
    
    // Rotate vector
    //AiM4Identity(tilt);
    
    //Todo: Find the Arnold replacement for this mental ray line:
    //mi_matrix_rotate_axis(tilt, &htarget, head_tilt);
    
    //AiM4VectorByMatrixMult(&org, tilt, &org);
    
    // Compute ray from camera to target
    target *= ParallaxDistance;
    ray = target - org;
    ray = AiV3Normalize(ray);
  } else {
    ray = target;
  }
  
  // Flip the X ray direction about the Y-axis
  // if(flipRayX) {
    // org.x = (-org.x);
    // ray.x = (-ray.x);
  // }
  
  // Flip the Y ray direction about the X-axis
  // if(flipRayY) {
    // if (zenithMode) {
      // org.z = (-org.z);
      // ray.z = (-ray.z);
    // } else {
      // org.y = (-org.y);
      // ray.y = (-ray.y);
    // }
  // }
  
  // Convert ray from camera space
  // TODO: adapt mental ray code snippet
  //mi_vector_from_camera(state, &ray, &ray);
  //mi_point_from_camera(state, &org, &org);
  
  // output
  output->origin = org;
  output->dir = ray;
  output->weight = 1.0;
}

node_loader {
  if (i > 0) return false;
  node->methods       = LatLongStereo_Methods;
  node->output_type  = AI_TYPE_NONE;
  node->name           = "LatLongStereo";
  node->node_type    = AI_NODE_CAMERA;
  
  // Note: Visual Studio prefers strcpy_s which will remove the compiler warning message
  #if defined _WIN32 || defined _WIN64
  strcpy_s(node->version, AI_VERSION);
  #else
  strcpy(node->version, AI_VERSION);
  #endif
  
  return true;
}