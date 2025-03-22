#pragma once

#include "qtuiutils.h"
#include "vrenderdll.h"
#include "vrender_uilang.h"

#include "resource.h"

#ifdef USE_MAX_QT_BASED_UI

class VRayDomemasterStereoParamBlockWidget : public VRayParamBlockWidget {
	Q_OBJECT

public:
	VRayDomemasterStereoParamBlockWidget(
		ReferenceMaker& owner,
		IParamBlock2& paramBlock,
		const MapID paramMapID,
		MSTR& rollupTitle,
		int& rollupFlags,
		int& rollupCategory
	);
};


#endif