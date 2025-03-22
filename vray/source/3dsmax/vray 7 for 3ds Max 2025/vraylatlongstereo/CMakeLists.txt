#
# CGREPO CMake-based build system
# Copyright, legal, contacts: see build_scripts/cmake/build_copyright.txt
#

cgr_plugin_project(vraylatlongstereo)

set(HEADERS
	vraylatlongstereo.h
	resource.h
)

set(SOURCES
	plugin.def
	vraylatlongstereo.cpp
	vraylatlongstereo.rc
)

set(LINK_LIBS
	maxutils
	pluginlib_includes
)

cgr_3dsmax_vrayplugin(
	NAME ${PROJECT_NAME}
	SOURCES "${SOURCES};${HEADERS}"
	LINK_LIBS ${LINK_LIBS}
	EXT "dlo"
)

cgr_use_max_qt_based_ui(${PROJECT_NAME}
	HEADERS "vraylatlongstereoparamblockwidget.h"
	SOURCES "vraylatlongstereoparamblockwidget.cpp"
)

cgr_warnings_as_errors(TARGET ${PROJECT_NAME})

cgr_finalize_options(${PROJECT_NAME})

