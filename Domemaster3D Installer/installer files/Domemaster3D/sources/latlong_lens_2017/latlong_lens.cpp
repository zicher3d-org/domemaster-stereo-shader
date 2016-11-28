/******************************************************************************
* latlong_lens for mental ray by Ralf Habel 
* ralf.habel@vi-motion.de
* 
*  Added ray differential based sampling to support mr 3.14 - July 22, 2016
******************************************************************************/

#include <math.h>
#include <shader.h>

#include "latlong_lens.h"


/*
 * Return in 'rot_transform' a transform matrix that rotates 'old_dir' to 'new_dir'
 * around an axis that is perpendicular to both directions.
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
 * Apply to the ray differentials a rotation transform that corresponds to the rotation
 * from the old direction ('state->dir', which is in world space) to the new one ('new_dir',
 * which is in camera space). The transform to apply has to be in world space, so it will
 * be built from the product of world-to-camera, rotation and camera-to-world transforms.
 */

static void rotate_ray_differentials(
    miState *state,
    miVector new_dir)
{
    /* Compute the old direction in camera space */
    miVector old_dir;
    mi_vector_to_camera(state, &old_dir, &state->dir);
    mi_vector_normalize(&old_dir);

    /* Normalize the new direction as well */
    mi_vector_normalize(&new_dir);

    /* Compute the transform matrix in camera space from 'old_dir' to 'new_dir' */
    miMatrix cs_rot_transform;
    build_rot_matrix(&old_dir, &new_dir, cs_rot_transform);

    /* Get pointers to the world-to-camera and camera-to-world transforms */
    miScalar *p_world_to_camera;
    mi_query(miQ_TRANS_WORLD_TO_CAMERA, state, 0, &p_world_to_camera);

    miScalar *p_camera_to_world;
    mi_query(miQ_TRANS_CAMERA_TO_WORLD, state, 0, &p_camera_to_world);

    /* Compute the complete transform matrix in world space   */
    /* (world-to-camera, then rotation, then camera-to-world) */
    miMatrix rot_transform;
    mi_matrix_prod(rot_transform, p_world_to_camera, cs_rot_transform);
    mi_matrix_prod(rot_transform, rot_transform, p_camera_to_world);

    /* Applies the computed transform to the ray differentials */
    mi_ray_differential_transform(state, rot_transform);
}


DLLEXPORT int latlong_lens_version(void)
{
	return 1;
}

DLLEXPORT void latlong_lens_init(
	miState * state,
	latlong_lens_params * in_pParams,
	miBoolean *inst_req)
{
	if(!in_pParams) 
	{		
		*inst_req = miFALSE;		
	} 
}

DLLEXPORT miBoolean latlong_lens
(
	miColor * out_pResult,
	miState * state,
	latlong_lens_params * in_pParams
)
{

	miBoolean vmirror;

	miScalar uval, vval, rayx, rayy, rayz;
	miVector raydir, raydir_internal; 

	vmirror = *mi_eval_boolean(&(in_pParams->m_vmirror));

	if (vmirror==miTRUE)
	{
    uval = (state->camera->x_resolution - state->raster_x) / state->camera->x_resolution;
	}
	else
	{
    uval = state->raster_x / state->camera->x_resolution;	
	}

	vval = (state->camera->y_resolution - state->raster_y) / state->camera->y_resolution;

	rayx = (float)(sin(vval*M_PI)*cos(M_PI*(2*uval+0.5))); 
	rayy = (float)(cos(vval*M_PI));
	rayz = (float)(sin(vval*M_PI)*sin(M_PI*(2*uval+0.5)));

	raydir.x = rayx; raydir.y = rayy; raydir.z = rayz;
  
  #if 1
    /* Adjust the ray differentials */
    rotate_ray_differentials(state, raydir);
  #endif
  
	mi_vector_from_camera(state, &raydir_internal, &raydir);

  return (mi_trace_eye(out_pResult, state, &state->org, &raydir_internal));
}


DLLEXPORT void latlong_lens_exit(
	miState * state,
	latlong_lens_params * in_pParams)
{
}
