/******************************************************************************
 *	LatLong_Stereo
 *	by Roberto Ziche
 *	
 *	
 *	Versions:
 *  0.1.0	First version for test only - 2014-09-16
 *  0.1.1	Added horizontal/Zenith orientation option - 2014-10-21 
 *           Cleaned code
 *
 *****************************************************************************/

#include <stdio.h>
#include <math.h>
#include "shader.h"

#define _VER_	"LatLong_Stereo ver: 0.1.1"

#define	CENTERCAM	0
#define	LEFTCAM		1
#define	RIGHTCAM	2

#define EPSILON	0.00001

// static evaluate-once shader parameters
static	miScalar	fov_vert_angle, fov_horiz_angle;
static	miInteger	camera;
static	miScalar	parallax_distance;
static	miScalar	cameras_separation;

// Parameters data structure
struct dsLatLong_Stereo {
	miScalar	FOV_Vert_Angle;		// Fisheye vertical FOV angle in degrees
	miScalar	FOV_Horiz_Angle;	// Fisheye horizontal FOV angle in degrees
	miBoolean	Flip_Ray_X;			// Flag for flipping image about the x-axis
	miBoolean	Flip_Ray_Y;			// Flag for flipping image about the y-axis

	miInteger	Camera;				// 0=center, 1=Left, 2=Right
	miScalar	Parallax_Distance;
	miScalar	Cameras_Separation;
	miScalar	Cameras_Separation_Map;
	miScalar	Head_Tilt_Map;

	miBoolean	Zenith_Mode;		// Flag for orientation compatibility with Domemaster camera
};

DLLEXPORT int LatLong_Stereo_version(void) {return(1);}

DLLEXPORT miBoolean LatLong_Stereo(
	miColor	*result,
	miState	*state,
	struct dsLatLong_Stereo *params)
{
	miScalar	cameras_separation_multiplier = *mi_eval_scalar(&params->Cameras_Separation_Map);
	miScalar	head_tilt = *mi_eval_scalar(&params->Head_Tilt_Map);

	miVector	org, ray, target, htarget;
	miMatrix	tilt;
	double		x, y, phi, theta, tmp;
	double		sinP, cosP, sinT, cosT;

	miBoolean	zenithMode = *mi_eval_boolean(&params->Zenith_Mode);

   	// normalize image coordinates btwn [-1,-1] and [1,1]...
	x = 2.0*state->raster_x/state->camera->x_resolution-1.0;
	y = 2.0*state->raster_y/state->camera->y_resolution-1.0;

	// Calculate phi and theta...
	phi = x*(fov_horiz_angle/2.0);
	if (zenithMode)
		theta = M_PI_2-y*(fov_vert_angle/2.0);
	else
		theta = y*(fov_vert_angle/2.0);

	// start by matching camera (center camera)
	// mi_point_to_camera(state, &org, &state->org);
	org.x = org.y = org.z = 0.0;

	// saves common used values for performance reasons
	sinP = sin(phi); cosP = cos(phi);
	sinT = sin(theta); cosT = cos(theta);

	// center camera target vector (normalized)
	if (zenithMode) {
		target.x = (miScalar)(sinP*sinT);
		target.y = (miScalar)(-cosP*sinT);
		target.z = (miScalar)(-cosT);
	} else {
		target.x = (miScalar)(sinP*cosT);
		target.y = (miScalar)(sinT);
		target.z = (miScalar)(-cosP*cosT);
	}

	if (camera != CENTERCAM) {
		// camera selection and initial position
		if (camera == LEFTCAM) {
			org.x = (miScalar)(-cameras_separation*cameras_separation_multiplier/2);
		} else if (camera == RIGHTCAM) {
			org.x = (miScalar)(cameras_separation*cameras_separation_multiplier/2);
		}


		// head rotation = phi
		// rotate camera
		if (zenithMode) {
			tmp = org.x*cosP-org.y*sinP;
			org.y = (miScalar)(org.y*cosP+org.x*sinP);
			org.x = (miScalar)tmp;
		} else {
			tmp = org.x*cosP-org.z*sinP;
			org.z = (miScalar)(org.z*cosP+org.x*sinP);
			org.x = (miScalar)tmp;
		}

		// calculate head target
		htarget.x = (miScalar)(sinP*sinT);
		htarget.y = (miScalar)(-cosP*sinT);
		htarget.z = (miScalar)target.z;

		// head tilt
		head_tilt = (miScalar)((head_tilt-0.5)*M_PI);
		mi_matrix_ident(tilt);
		mi_matrix_rotate_axis(tilt, &htarget, head_tilt);
		mi_vector_transform(&org, &org, tilt);

		// calculate ray from camera to target
		target.x *= parallax_distance;
		target.y *= parallax_distance;
		target.z *= parallax_distance;
		ray.x = target.x-org.x;
		ray.y = target.y-org.y;
		ray.z = target.z-org.z;
		mi_vector_normalize(&ray);

	} else {		// center camera

		ray = target;

	}

//mi_debug("II->,Phi=%f,Theta=%f,rot=%f,camx=%f,camy=%f", (miScalar)phi, (miScalar)theta, (miScalar)rot, (miScalar)org.x, (miScalar)org.y);

	// Flip the X ray direction about the Y-axis
	if(*mi_eval_boolean(&params->Flip_Ray_X)) { 
		org.x = (-org.x);
		ray.x = (-ray.x);
	}
	// Flip the Y ray direction about the X-axis
	if(*mi_eval_boolean(&params->Flip_Ray_Y)) {
		if (zenithMode) {
			org.z = (-org.z);
			ray.z = (-ray.z);
		} else {
			org.y = (-org.y);
			ray.y = (-ray.y);
		}
	}

	// Convert ray from camera space
	mi_vector_from_camera(state, &ray, &ray);
	mi_point_from_camera(state, &org, &org);

	// Trace new ray...
	return(mi_trace_eye(result, state, &org, &ray));

}

DLLEXPORT void LatLong_Stereo_init(
	miState	*state,
	struct dsLatLong_Stereo *params,
	miBoolean *inst_init_req)
{
	if (!params) {
		// version output
		mi_info(_VER_);
		*inst_init_req = miTRUE;
	} else {
		fov_vert_angle = *mi_eval_scalar(&params->FOV_Vert_Angle);
		fov_horiz_angle = *mi_eval_scalar(&params->FOV_Horiz_Angle);
		camera = *mi_eval_integer(&params->Camera);
		parallax_distance = *mi_eval_scalar(&params->Parallax_Distance);
		cameras_separation = *mi_eval_scalar(&params->Cameras_Separation);
//mi_info("II-> fovV=%f,fovH=%f,cam=%i,rad=%f,sep=%f",fov_vert_angle,fov_horiz_angle,camera,parallax_distance,cameras_separation);

		// Convert input angles from degrees to radians...
		fov_vert_angle = (miScalar)(fov_vert_angle*M_PI/180.0);
		fov_horiz_angle = (miScalar)(fov_horiz_angle*M_PI/180.0);
	}
}

DLLEXPORT void LatLong_Stereo_exit(
	miState	*state,
	void *params)
{
}
