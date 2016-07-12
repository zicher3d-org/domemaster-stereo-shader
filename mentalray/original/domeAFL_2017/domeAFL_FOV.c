/******************************************************************************
 * Author:  Daniel F. Ott (dott@thedott.net)
 * Created: 05.17.04
 * Module:
 * Purpose: Angular Fisheye Lens (AFL) Shader
 *
 * Exports:
 *  domeAFL_FOV_version
 *  domeAFL_FOV
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
 * 12.07.2016 - Added ray differential based sampling to support mr 3.14
 * 
 * Description:
 *  This shader uses the angular fisheye method discussed in Paul Bourke's   
 *  __Computer_Generated_Angular_Fisheye_Projection__
 *  at http://astronomy.swin.edu.au/~pbourke/projection/fisheye/
 *
 *  It requires two pieces of external data, which is obtained from
 *  the MR declaration file: field of view (fovangle) and 
 *  view axis offset (viewoffset).
 *
 *****************************************************************************/

#include <stdio.h>
#include <math.h>
#include "shader.h"
 
#define EPSILON 0.00001

/* Data Structure used store attribute values from Maya... */
struct dsDomeAFL_FOV {
  miScalar  FOV_Angle;  /* Fisheye FOV angle in degrees */
  miVector  View_Offset;  /* View offset location x,y,z are members of [-1,1] */
    
  miBoolean Flip_Ray_X; /* Flag for flipping image about the x-axis */
  miBoolean Flip_Ray_Y; /* Flag for flipping image about the y-axis */
};

DLLEXPORT int domeAFL_FOV_version(void) {return(1);}

/*
 * return in 'rot_transform' a transform matrix that rotates 'old_dir' to 'new_dir'
 * around an axis that is perpendicular to both directions
 */

static void build_rot_matrix(
    miVector *old_dir,
    miVector *new_dir,
    miMatrix rot_transform)
{
    miVector rot_axis;
    mi_vector_prod(&rot_axis, old_dir, new_dir);
    mi_vector_normalize(&rot_axis);

    float cos_theta = mi_vector_dot(old_dir, new_dir);
    float theta = (float) acos(cos_theta);

    mi_matrix_rotate_axis(rot_transform, &rot_axis, theta);
}

/*
 * apply to the ray differentials a rotation transform that corresponds to the rotation
 * from the old direction ('state->dir', which is in world space) to the new one ('new_dir',
 * which is in camera space). The transform to apply has to be in world space, so it will
 * be built from the product of world-to-camera, rotation and camera-to-world transforms
 */

static void rotate_ray_differentials(
    miState *state,
    miVector new_dir)
{
    /* compute the old direction in camera space */
    miVector old_dir;
    mi_vector_to_camera(state, &old_dir, &state->dir);
    mi_vector_normalize(&old_dir);

    /* normalize the new direction as well */
    mi_vector_normalize(&new_dir);

    /* compute the transform matrix in camera space from 'old_dir' to 'new_dir' */
    miMatrix cs_rot_transform;
    build_rot_matrix(&old_dir, &new_dir, cs_rot_transform);

    /* get pointers to the world-to-camera and camera-to-world transforms */
    miScalar *p_world_to_camera;
    mi_query(miQ_TRANS_WORLD_TO_CAMERA, state, 0, &p_world_to_camera);

    miScalar *p_camera_to_world;
    mi_query(miQ_TRANS_CAMERA_TO_WORLD, state, 0, &p_camera_to_world);

    /* compute the complete transform matrix in world space   */
    /* (world-to-camera, then rotation, then camera-to-world) */
    miMatrix rot_transform;
    mi_matrix_prod(rot_transform, p_world_to_camera, cs_rot_transform);
    mi_matrix_prod(rot_transform, rot_transform, p_camera_to_world);

    /* applies the computed transform to the ray differentials */
    mi_ray_differential_transform(state, rot_transform);
}

DLLEXPORT miBoolean domeAFL_FOV(
  miColor *result,
  miState *state,
  register struct dsDomeAFL_FOV *params)
{
  miScalar  fov_angle_deg = *mi_eval_scalar(&params->FOV_Angle);
  miGeoScalar fov_angle_rad;

  miVector  viewpt_offset = *mi_eval_vector(&params->View_Offset);
  miVector  ray;

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
      phi = atan2(x,y); // [rz] using atan2 instead of original if-then formula
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
    /* Offset is added to y & z components because they are negative values... */
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

#if 1
    /* adjust the ray differentials */
    rotate_ray_differentials(state, ray);
#endif

    /* Convert ray from camera space */
    mi_vector_from_camera(state, &ray, &ray);

    /* Trace new ray... */
    return(mi_trace_eye(result, state, &state->org, &ray));          
  } else {
    /* Set the return colors to Black */
    result->r = result->g = result->b = result->a = 0;
    return(miFALSE);
  }

} /* end of dome_FOV_AFL() */
