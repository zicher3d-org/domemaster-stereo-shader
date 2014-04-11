/******************************************************************************
* latlong_lens for mental ray by Ralf Habel 
* ralf.habel@vi-motion.de
******************************************************************************/

#include <math.h>
#include <shader.h>

#include "latlong_lens.h"

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

	mi_vector_from_camera(state, &raydir_internal, &raydir);

  return (mi_trace_eye(out_pResult, state, &state->org, &raydir_internal));


	
}


DLLEXPORT void latlong_lens_exit(
	miState * state,
	latlong_lens_params * in_pParams)
{
}
