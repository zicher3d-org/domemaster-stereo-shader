/******************************************************************************
* latlong_lens for mental ray by Ralf Habel 
* ralf.habel@vi-motion.de
******************************************************************************/

#ifndef _LATLONG_LENS_H_
#define _LATLONG_LENS_H_

#include <math.h>
#include <shader.h>


typedef struct
{

	miBoolean m_vmirror;

} latlong_lens_params;

extern "C" {
DLLEXPORT int latlong_lens_version(void);

DLLEXPORT miBoolean latlong_lens(
	miColor *out_pResult,
	miState *state,
	latlong_lens_params *in_pParams
);

DLLEXPORT void latlong_lensp_init(
	miState * state,
	latlong_lens_params * in_pParams,
	miBoolean *inst_req
);

DLLEXPORT void latlong_lens_exit(
	miState * state,
	latlong_lens_params * in_pParams);
}
#endif
