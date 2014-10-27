// DomemasterStereo Arnold Shader
// 2014-09-06 10:12 am 

#include <ai.h>
#include <cstring>

// For use with the Windows Visual Studio compiler and strcpy_s()
//#include <string>

AI_CAMERA_NODE_EXPORT_METHODS(DomemasterStereo_Methods);

#define camera				(params[0].INT)
#define fovDegrees		(params[1].FLT)
#define separation		(params[2].FLT)
#define zeroParallaxSphere		(params[3].FLT)
#define separationMap	(params[4].FLT)
#define headTurnMap		(params[5].FLT)
#define headRollMap		(params[6].FLT)
#define flipRayX		(params[7].FLT)
#define flipRayY		(params[8].FLT)

#define LEFTCAM	0
#define RIGHTCAM	1
#define EPSILON	0.00001

// Link to the external (Softimage SPDL / Maya+Houdini Metadata GUI) parameters
node_parameters
{
	AiParameterInt("camera", 0);
	AiParameterFlt("fov", 180.f);
	AiParameterFlt("separation", 6.5f);
	AiParameterFlt("zero_parallax_sphere", 360.f);
	AiParameterFlt("forward_tilt", 0.0f);
	AiParameterFlt("separation_map", 1.f);
	AiParameterFlt("head_turn_map", 1.f);
	AiParameterFlt("head_roll_map", 0.5f);
	AiParameterInt("flip_ray_x", 0);
	AiParameterInt("flip_ray_y", 0);
}

node_initialize
{
	AiCameraInitialize(node, NULL);
}

node_update
{
	AiCameraUpdate(node, false);
}

node_finish
{
	AiCameraDestroy(node);
}

camera_create_ray
{
	double x, y, r, phi, theta, offset, rot, tmp;
	double sinP, cosP, sinT, cosT, sinR, cosR;
	AtVector org, ray, target;
	
	const AtParamValue* params = AiNodeGetParams(node);	// get camera parameters
	
	float fov = fovDegrees * AI_DTOR;	// convert FOV from degrees to radians
	
	// Swap X-Y and apply a vertical symmetry
	x = - input->sy;
	y = input->sx;
	
	// Compute radius
	r = sqrt((x * x) + (y * y));
	
	if (r < 1.0)
	{
		// Compute phi angle
		if ((r > -EPSILON) && (r < EPSILON))
		{
			phi = 0.0;
		}
		else
		{
			phi = atan2(y,x);
		}
		
		// Compute theta angle
		theta = r * (fov / 2.0);
		
		// Compute commonly used values
		sinP = sin(phi);
		cosP = cos(phi);
		sinT = sin(theta);
		cosT = cos(theta);
		
		// Initialize camera position
		org.x = org.y = org.z = 0.0;
		
		// Camera target
		target.x = (float)(sinP * sinT);
		target.y = (float)(-cosP * sinT);
		target.z = (float)(-cosT);
		
		// Set camera offset
		offset = separation * separationMap / 2.0;

		if (camera == LEFTCAM)
		{
			org.x = (float)(- offset);
		}
		if (camera == RIGHTCAM)
		{
			org.x = (float)offset;
		}
		
		// Head rotation
		rot = phi * headTurnMap;
		sinR = sin(rot);
		cosR = cos(rot);
		
		// Rotate camera
		tmp = org.x * cosR - org.y * sinR;
		org.y = (float)(org.y * cosR + org.x * sinR);
		org.x = (float)tmp;
		
		// Compute ray from camera to target
		target *= zeroParallaxSphere;
		ray = target - org;
		ray = AiV3Normalize(ray);
		
		// output
		output->origin = org;
		output->dir = ray;
		output->weight = 1.0;
	}
	else
	{
		output->weight = 0.0;
	}
}

node_loader
{
   if (i != 0) return false;
   node->methods     = DomemasterStereo_Methods;
   node->output_type = AI_TYPE_UNDEFINED;
   node->name        = "DomemasterStereo";
   node->node_type   = AI_NODE_CAMERA;
   //strcpy_s(node->version, AI_VERSION);
   strcpy(node->version, AI_VERSION);
   return true;
}