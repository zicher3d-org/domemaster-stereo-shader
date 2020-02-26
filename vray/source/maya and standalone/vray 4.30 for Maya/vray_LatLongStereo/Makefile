# Linux - LatLongStereo Vray Shader Makefile
# 2015-06-05 1.59pm
# by Andrew Hazelden  andrew@andrewhazelden.com
# http://www.andrewhazelden.com

# You can compile this file from the command line using:
# make -f Makefile

# Note: In order to compile the lens shaders, you have to copy your Vray for Maya Lib & Include files into the folders "../lib" and "../include".

.SUFFIXES:

all: libvray_LatLongStereo.so

libvray_LatLongStereo.so:  vray_LatLongStereo.obj
	g++  -std=c++11 -lpthread -lrt -lc -lz  -Wl,--gc-sections  -fPIC      -Wl,--no-as-needed   "-Wl,-(" -lvutils_s  -ldl -lvray -lplugman_s -shared -Wl,--export-dynamic -o "./libvray_LatLongStereo.so" -L"../lib" -L"../lib/gcc-4.8" -O "./vray_LatLongStereo.obj"  "-Wl,-)" -pthread -lrt


vray_LatLongStereo.obj: ./vray_LatLongStereo.cpp
	g++ -std=c++11 -O0 -g -DENABLE_DEBUG_PRINTF -fPIC -Wreturn-type -Werror=return-type -DREQUIRE_IOSTREAM -DHAVE_EXR -D_LIBRARY_ALEMBIC -DHAVE_OPENSUBDIV -DHAVE_EMBREE -DDEBUG_OPT -DVASSERT_ENABLED -D__VRAY4MAYA30__ -DBits64_ -D_REENTRANT  -fvisibility=hidden -DVRAY_EXPORTS      -fexceptions    -I "../include"  -D "NDEBUG"     -c -o "./vray_LatLongStereo.obj" "./vray_LatLongStereo.cpp"

