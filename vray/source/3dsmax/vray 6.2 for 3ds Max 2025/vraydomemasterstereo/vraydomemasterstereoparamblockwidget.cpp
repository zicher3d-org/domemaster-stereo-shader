#ifdef USE_MAX_QT_BASED_UI

#include "vraydomemasterstereo.h"
#include "vraydomemasterstereoparamblockwidget.h"
#include "vraydomemasterstereoparamblockwidget.h.moc"
#include "vrender_imgfile_dragdrop_helper.h"

VRayDomemasterStereoParamBlockWidget::VRayDomemasterStereoParamBlockWidget(
	ReferenceMaker& owner,
	IParamBlock2& paramBlock,
	const MapID paramMapID,
	MSTR& rollupTitle,
	int& rollupFlags,
	int& rollupCategory
): VRayParamBlockWidget(owner, paramBlock, Dlg_Geo, paramMapID) {
	ImgFileDNDHelper& dndHelper=getImgFileDNDHelper();
	autoGenUserInterface(&dndHelper);
	rollupTitle=loadStringResource(idtr_grp_params);
}

#endif //USE_MAX_QT_BASED_UI
