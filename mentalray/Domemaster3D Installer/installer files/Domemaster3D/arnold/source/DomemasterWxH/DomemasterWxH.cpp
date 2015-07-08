// DomemasterWxH Arnold Shader
// 2014-11-06 10.16 pm
// --------------------------------------
// Ported to Arnold by Andrew Hazelden
// Based upon the mental ray shader domeAFL_WxH by Daniel Ott

#include <stdio.h>
#include <math.h>
#include <cstring>
#include <ai.h>
#include <ai_cameras.h>
#include <ai_nodes.h>
#include <ai_metadata.h>

// For use with the Windows Visual Studio compiler and strcpy_s()
// #include <string>

AI_CAMERA_NODE_EXPORT_METHODS(DomemasterWxH_Methods);

#define diameter                   (params[0].FLT)
#define height                     (params[1].FLT)
//#define view_offset                (params[2].VEC)
#define flipRayX                   (params[2].FLT)
#define flipRayY                   (params[3].FLT)

// Link to the external (Softimage SPDL / Maya + Houdini Metadata GUI) parameters
node_parameters {
  AiParameterFlt("diameter", 1.0f);
  AiParameterFlt("height", 0.5f);
  //AiParameterVec("view_offset", 0.0f, 0.0f, 0.0f);
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
  double fov, radius;
  double x, y, r, phi, theta;
  AtVector viewpt_offset;
  AtVector ray, org;
  
  // Get camera parameters
  const AtParamValue* params = AiNodeGetParams(node); 
  
  // Init the view offset value with zero until I figure out the AiParameterVec setting.
  viewpt_offset = AiVector(0.0f, 0.0f, 0.0f);
  
  //AiMsgInfo("II-> diameter=%f, height=%f, fov=%f,radius=%f", diameter, height, fov, radius );

  // Swap X-Y and apply a vertical symmetry
  x = -input->sy;
  y = input->sx;
  
  //Calculate FOV for given Diameter & height of dome
	// Equations obtained from:
	// http://mathforum.org/dr.math/faq/faq.circle.segment.html#8
	radius =  ((diameter * diameter) + (4 * height * height)) / (8 * height);
	fov = 2 * asin(diameter / (2 * radius));
  
  // Compute radius
  // Todo: compare sqrt() performance with AI_SQRT2()
  r = sqrt((x * x) + (y * y));
  
  if (r < 1.0) {
  
    // Compute phi angle
    if ((r > -AI_EPSILON) && (r < AI_EPSILON)) {
      phi = 0.0;
    } else {
      phi = atan2(x, y);
    }
    
    // Compute theta angle
    theta = r * (fov / 2.0);
    
    // Initialize camera position
    org = 0.0;
    
    // Calculate Ray direction vector
    ray.x = (float)(sin(theta) * cos(phi));
    ray.y = (float)(-sin(theta) * sin(phi));
	  // -Z is the look at direction
		ray.z = (float)(-cos(theta));
		
		// Account for the view offset
    // Offset is added to the y & z components because they are negative values
		ray.x = ray.x - viewpt_offset.x;
		ray.y = ray.y + viewpt_offset.y; 
		// Add because MR uses -Z as Look At
		ray.z = ray.z + viewpt_offset.z;
 
    ray = AiV3Normalize(ray);
    
    //AiMsgInfo("II->,Phi=%f,Theta=%f,rot=%f,camx=%f,camy=%f", (float)phi, (float)theta, (float)rot, (float)org.x, (float)org.y);
    
    // Flip the X ray direction about the Y-axis
    // if(flipRayX) {
      // ray.x = (-ray.x);
    // }
    
    // Flip the Y ray direction about the X-axis
    // if(flipRayY) {
      // ray.y = (-ray.y);
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
  node->methods      = DomemasterWxH_Methods;
  node->output_type = AI_TYPE_NONE;
  node->name          = "DomemasterWxH";
  node->node_type   = AI_NODE_CAMERA;
  
  // Note: Visual Studio prefers strcpy_s which will remove the compiler warning message
  #if defined _WIN32 || defined _WIN64
  strcpy_s(node->version, AI_VERSION);
  #else
  strcpy(node->version, AI_VERSION);
  #endif
  
  return true;
}