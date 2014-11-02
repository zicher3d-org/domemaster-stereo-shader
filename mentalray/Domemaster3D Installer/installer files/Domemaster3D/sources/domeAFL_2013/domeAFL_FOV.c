/******************************************************************************
 * Author:	Daniel F. Ott (dott@thedott.net)
 * Created:	05.17.04
 * Module:	
 * Purpose:	Angular Fisheye Lens (AFL) Shader
 *
 * Exports:
 *	domeAFL_FOV_version
 *	domeAFL_FOV
 *
 * History:
 *
 * 08.23.2004 - Added an EPSILON test for the radius and corrected phi, 
 *              which should be 0 when the radius is 0.
 * 
 * 07.06.2010 - [Roberto Ziche] Changed phi calculation to use atan2
 *
 * 11.04.2012 - [Andrew Hazelden] Added view rotation code to correct
 *              for atan2 changes
 *
 * Description:
 *	This shader uses the angular fisheye method discussed in Paul Bourke's   
 *	__Computer_Generated_Angular_Fisheye_Projection__
 *	at http://astronomy.swin.edu.au/~pbourke/projection/fisheye/
 *
 *	It requires two pieces of external data, which is obtained from
 *	the MR declaration file: field of view (fovangle) and 
 *	view axis offset (viewoffset).
 *
 *****************************************************************************/

#include <stdio.h>
#include <math.h>
#include "shader.h"
 
#define EPSILON 0.00001

/* Data Structure used store attribute values from Maya...*/
struct dsDomeAFL_FOV {
	miScalar	FOV_Angle;	/* Fisheye FOV angle in degrees */
	miVector	View_Offset;	/* View offset location x,y,z 
	        			   are members of [-1,1] */
    
	miBoolean	Flip_Ray_X; /* Flag for flipping image about the x-axis */
	miBoolean	Flip_Ray_Y; /* Flag for flipping image about the y-axis */
};

DLLEXPORT int domeAFL_FOV_version(void) {return(1);}

DLLEXPORT miBoolean domeAFL_FOV(
	miColor	*result,
	miState	*state,
	register struct dsDomeAFL_FOV *params)
{
	miScalar	fov_angle_deg = *mi_eval_scalar(&params->FOV_Angle);
	miGeoScalar	fov_angle_rad;

	miVector	viewpt_offset = *mi_eval_vector(&params->View_Offset);
	miVector	ray;

	miGeoScalar x, y, r, phi, theta;

   	/* normalize image coordinates btwn [-1,1]... */
	/* [ah] Rotate the cartesian axis 90 deg CW   */
	x = -2.0*state->raster_y/state->camera->y_resolution+1.0;
	y = 2.0*state->raster_x/state->camera->x_resolution-1.0;
	
	/* Calcaulate the radius value */
	r = MI_SQRT( ( x * x ) + ( y * y ) );

	if ( r < 1.0 ) {

		/* Calculate phi... */
		if ( (r > -EPSILON) && (r < EPSILON) ) {
			phi = 0.0;
		} else {
			phi = atan2(x,y);	// [rz] using atan2 instead of original if-then formula
		}

		/* Convert FOV angle of fisheye from degrees to radians... */
		fov_angle_rad = fov_angle_deg * M_PI / 180.0;

		/* Calculate theta... */
		
		theta = r * ( fov_angle_rad / 2.0 );

		/* Calculate Ray direction vector... */
		ray.x = (float)(sin(theta) * cos(phi));
		ray.y = (float)(-sin(theta) * sin(phi));
			/* -Z is Look At Direction*/
		ray.z = (float)(-cos(theta));

		/* Account for view offset... */
   		/* Offset is added to y & z components because 
   		   they are negative values...*/
		ray.x = ray.x - viewpt_offset.x;
		ray.y = ray.y + viewpt_offset.y;
			/* Add because MR uses -Z as Look At */
		ray.z = ray.z + viewpt_offset.z;
	
 		/* Flip the ray direction about the y-axis */
		if(*mi_eval_boolean(&params->Flip_Ray_X)) { 
			ray.x = (-ray.x);
		}

        	/* Flip the ray direction about the x-axis */
		if(*mi_eval_boolean(&params->Flip_Ray_Y)) {
			ray.y = (-ray.y);		
		}

		/* Convert ray from camera space */
		mi_vector_from_camera(state, &ray, &ray);

		/* Trace new ray... */
	        return(mi_trace_eye(result, state, &state->org, &ray));          
	
	} else {

		/* Set the return colors to Black */
		result->r = result->g =
		result->b = result->a = 0;
		return(miFALSE);
	}

} /* end of dome_FOV_AFL() */

