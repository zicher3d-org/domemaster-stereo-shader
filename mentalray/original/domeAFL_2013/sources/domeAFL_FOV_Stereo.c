/******************************************************************************
 *	domeAFL_FOV_Stereo
 *	by Roberto Ziche
 *	(based on the Angular Fisheye Lens (AFL) Shader by Daniel F. Ott
 *	
 *	Versions:
 *	0.1.0	First version released to public. No Offset and Flip options.
 * 
 *  0.1.1 [Andrew Hazelden] modification adding flip controls. Aug 4, 2012
 *  0.1.2 [Roberto Ziche] Fixed Flip X/Y and ray conversion order
 *  
 *****************************************************************************/

#include <stdio.h>
#include <math.h>
#include "shader.h"

#define _VER_	"domeAFL_FOV_Stereo ver: 0.1.2"

#define	CENTERCAM	0
#define	LEFTCAM		1
#define	RIGHTCAM	2

#define EPSILON	0.00001

// static evaluate-once shader parameters
static	miScalar	fov_angle;
static	miVector	viewport_offset;
static	miInteger	camera;
static	miScalar	dome_radius;
static	miScalar	dome_tilt;
static	miScalar	cameras_separation;
static	miBoolean	dome_tilt_compensation;
static	miBoolean	vertical_mode;

// Parameters data structure
struct dsDomeAFL_FOV_Stereo {
	miScalar	FOV_Angle;		/* Fisheye FOV angle in degrees */
	miVector	View_Offset;	/* View offset location x,y,z [-1,1] */
	miBoolean	Flip_Ray_X;		/* Flag for flipping image about the x-axis */
	miBoolean	Flip_Ray_Y;		/* Flag for flipping image about the y-axis */
	
	miInteger	Camera;			// 0=center, 1=Left, 2=Right
	miScalar	Dome_Radius;
	miScalar	Dome_Tilt;
	miScalar	Cameras_Separation;
	miScalar	Cameras_Separation_Map;
	miScalar	Head_Turn_Map;
	miScalar	Head_Tilt_Map;
	miBoolean	Dome_Tilt_Compensation;
	miBoolean	Vertical_Mode;
};

DLLEXPORT int domeAFL_FOV_Stereo_version(void) {return(1);}

DLLEXPORT miBoolean domeAFL_FOV_Stereo(
									   miColor	*result,
									   miState	*state,
									   struct dsDomeAFL_FOV_Stereo *params)
{
	miScalar	cameras_separation_multiplier = *mi_eval_scalar(&params->Cameras_Separation_Map);
	miScalar	head_turn_multiplier = *mi_eval_scalar(&params->Head_Turn_Map);
	miScalar	head_tilt = *mi_eval_scalar(&params->Head_Tilt_Map);
	
	miVector	org, ray, target, htarget;
	miMatrix	tilt;
	double		x, y, r, phi, theta, rot, tmp, tmpY, tmpZ;
	double		sinP, cosP, sinT, cosT, sinR, cosR;
	
   	// normalize image coordinates btwn [-1,1]...
	// [rz] swap X-Y to match camera view and apply a vertical symmetry
	// [rz] basically, we rotate the cartesian axis 90deg CW
	x = -2.0*state->raster_y/state->camera->y_resolution+1.0;
	y = 2.0*state->raster_x/state->camera->x_resolution-1.0;
	
	// Calculate the radius value
	r = MI_SQRT((x*x)+(y*y));
	
	if (r < 1.0) {
		
		// Calculate phi...
		if ((r > -EPSILON) && (r < EPSILON) ) {
			phi = 0.0;
		} else {
			phi = atan2(y,x);
		}
		// Calculate theta...
		theta = r*(fov_angle/2.0);
		
		// start by matching camera (center camera)
		// mi_point_to_camera(state, &org, &state->org);
		org.x = org.y = org.z = 0.0;
		
		// saves common used values for performance reasons
		sinP = sin(phi); cosP = cos(phi);
		sinT = sin(theta); cosT = cos(theta);
		
		// center camera target vector (normalized)
		target.x = (miScalar)(sinP*sinT);
		target.y = (miScalar)(-cosP*sinT);
		target.z = (miScalar)(-cosT);
		
		// camera selection and initial position
		switch (camera)
		{
			case CENTERCAM:
				ray = target;
				break;
				
			case LEFTCAM:
				org.x = (miScalar)(-cameras_separation*cameras_separation_multiplier/2);
				break;
				
			case RIGHTCAM:
				org.x = (miScalar)(cameras_separation*cameras_separation_multiplier/2);
				break;
				
			default:
				ray = target;
				break;
		}
		
		
		if (camera != CENTERCAM)
		{
			if (dome_tilt_compensation) {		// tilted dome mode
				
				// head rotation
				// @@@ need to check atan2 params for 0 values?
				// @@@ save values of sin/cos
				tmpY = target.y*cos(-dome_tilt)-target.z*sin(-dome_tilt);
				tmpZ = target.z*cos(-dome_tilt)+target.y*sin(-dome_tilt);
				rot = atan2(target.x,-tmpY)*head_turn_multiplier;
				if (vertical_mode)
					rot *= fabs(sinP);
				sinR = sin(rot); cosR = cos(rot);
				
				// rotate camera
				tmp = org.x*cosR-org.y*sinR;
				org.y = (miScalar)(org.y*cosR+org.x*sinR);
				org.x = (miScalar)tmp;
				
				// compensate for dome tilt
				// @@@ save values of sin/cos
				tmp = org.y*cos(dome_tilt)-org.z*sin(dome_tilt);
				org.z = (miScalar)(org.z*cos(dome_tilt)+org.y*sin(dome_tilt));
				org.y = (miScalar)tmp;
				
				// calculate head target
				tmp = sqrt(target.x*target.x+tmpY*tmpY);
				htarget.x = (miScalar)(sin(rot)*tmp);
				htarget.y = (miScalar)(-cos(rot)*tmp);
				htarget.z = (miScalar)tmpZ;
				
				// dome rotation again on head target
				tmp = htarget.y*cos(dome_tilt)-htarget.z*sin(dome_tilt);
				htarget.z = (miScalar)(htarget.z*cos(dome_tilt)+htarget.y*sin(dome_tilt));
				htarget.y = (miScalar)tmp;
				
			} else {
				
				if (vertical_mode) {			// vertical mode
					
					// head rotation
					// @@@ need to check atan2 params for 0 values?
					rot = atan2(target.x,-target.z)*head_turn_multiplier*fabs(sinP);
					sinR = sin(rot); cosR = cos(rot);
					
					// rotate camera
					tmp = org.x*cosR-org.z*sinR;
					org.z = (miScalar)(org.z*cosR+org.x*sinR);
					org.x = (miScalar)tmp;
					
					// calculate head target
					tmp = sqrt(target.x*target.x+target.z*target.z);
					htarget.x = (miScalar)(sin(rot)*tmp);
					htarget.y = (miScalar)target.y;
					htarget.z = (miScalar)(-cos(rot)*tmp);
					
				} else {						// horizontal mode
					
					// head rotation
					rot = phi*head_turn_multiplier;
					sinR = sin(rot); cosR = cos(rot);
					
					// rotate camera
					tmp = org.x*cosR-org.y*sinR;
					org.y = (miScalar)(org.y*cosR+org.x*sinR);
					org.x = (miScalar)tmp;
					
					// calculate head target
					htarget.x = (miScalar)(sin(rot)*sinT);
					htarget.y = (miScalar)(-cos(rot)*sinT);
					htarget.z = (miScalar)target.z;
					
				}
			}
			
			// head tilt
			head_tilt = (miScalar)((head_tilt-0.5)*M_PI);
			mi_matrix_ident(tilt);
			mi_matrix_rotate_axis(tilt, &htarget, head_tilt);
			mi_vector_transform(&org, &org, tilt);
			
			
			// calculate ray from camera to target
			target.x *= dome_radius;
			target.y *= dome_radius;
			target.z *= dome_radius;
			
			
			ray.x = target.x-org.x;
			ray.y = target.y-org.y;
			ray.z = target.z-org.z;
			mi_vector_normalize(&ray);
			
		}
		
		
		// Account for view offset...
   		// Offset is added to y & z components because they are negative values...
		// @@@ ray.x = ray.x - viewport_offset.x;
		// @@@ ray.y = ray.y + viewport_offset.y;
		// @@@ ray.z = ray.z + viewport_offset.z;
		
		//mi_debug("II->,Phi=%f,Theta=%f,rot=%f,camx=%f,camy=%f", (miScalar)phi, (miScalar)theta, (miScalar)rot, (miScalar)org.x, (miScalar)org.y);
		

		// Flip the X ray direction about the Y-axis
		if(*mi_eval_boolean(&params->Flip_Ray_X)) { 
			org.x = (-org.x);
			ray.x = (-ray.x);
		}
		// Flip the Y ray direction about the X-axis
		if(*mi_eval_boolean(&params->Flip_Ray_Y)) {
			org.z = (-org.z);
			ray.z = (-ray.z);
		}

		// Convert ray from camera space
		mi_vector_from_camera(state, &ray, &ray);
		mi_point_from_camera(state, &org, &org);

		// Trace new ray...
		return(mi_trace_eye(result, state, &org, &ray));
		
	} else {
		
		// Set the return colors to Black
		result->r = result->g = result->b = result->a = 0;
		return(miFALSE);
	}
	
}

DLLEXPORT void domeAFL_FOV_Stereo_init(
									   miState	*state,
									   struct dsDomeAFL_FOV_Stereo *params,
									   miBoolean *inst_init_req)
{
	if (!params) {
		// version output
		mi_info(_VER_);
		*inst_init_req = miTRUE;
	} else {
		fov_angle = *mi_eval_scalar(&params->FOV_Angle);
		viewport_offset = *mi_eval_vector(&params->View_Offset);
		camera = *mi_eval_integer(&params->Camera);
		dome_radius = *mi_eval_scalar(&params->Dome_Radius);
		dome_tilt = *mi_eval_scalar(&params->Dome_Tilt);
		cameras_separation = *mi_eval_scalar(&params->Cameras_Separation);
		dome_tilt_compensation = *mi_eval_boolean(&params->Dome_Tilt_Compensation);
		vertical_mode = *mi_eval_boolean(&params->Vertical_Mode);
		//mi_info("II-> fov=%f,cam=%i,rad=%f,tilt=%f,sep=%f,comp=%i,vert=%i",fov_angle,camera,dome_radius,dome_tilt,cameras_separation,dome_tilt_compensation,vertical_mode);
		
		// Convert input angles from degrees to radians...
		fov_angle = (miScalar)(fov_angle*M_PI/180.0);
		dome_tilt = (miScalar)(dome_tilt*M_PI/180.0);
	}
}

DLLEXPORT void domeAFL_FOV_Stereo_exit(
									   miState	*state,
									   void *params)
{
}
