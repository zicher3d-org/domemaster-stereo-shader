#include <stdio.h>
#include <math.h>
#include "shader.h"

struct rob_lookup_background {
    miVector        zoom;
    miVector        pan;
    miBoolean       torus_u;
    miBoolean       torus_v;
	//miTag			tex;
	miScalar		tex;
};

DLLEXPORT int rob_lookup_background_version(void) {return(1);}

DLLEXPORT miBoolean rob_lookup_background(
    miColor         *result,
    miState         *state,
    struct rob_lookup_background *paras)
{
    miVector        *zoom;
    miVector        *pan;
    miVector        coord;
	//miTag			tex = *mi_eval_tag(&paras->tex);
	miScalar		tex = *mi_eval_scalar(&paras->tex);

    if (!tex) {
            result->r = result->g = result->b = result->a = 0;
            return(miFALSE);
    }
    zoom = mi_eval_vector(&paras->zoom);
    pan  = mi_eval_vector(&paras->pan);
    coord.x = (miScalar)(state->raster_x / state->camera->x_resolution * .9999);
    coord.y = (miScalar)(state->raster_y / state->camera->y_resolution * .9999);
    coord.z = 0;
    coord.x = pan->x + (zoom->x ? zoom->x * coord.x : coord.x);
    coord.y = pan->y + (zoom->y ? zoom->y * coord.y : coord.y);
    if (*mi_eval_boolean(&paras->torus_u))
            coord.x -= (miScalar)floor(coord.x);
    if (*mi_eval_boolean(&paras->torus_v))
            coord.x -= (miScalar)floor(coord.y);
    if (coord.x < 0 || coord.y < 0 || coord.x >= 1 || coord.y >= 1) {
            result->r = result->g = result->b = result->a = 0;
            return(miTRUE);
	} else {
            //return(mi_lookup_color_texture(result, state, tex, &coord));
			result->r = result->g = result->b = result->a = tex;
			return(miTRUE);
	}
}
