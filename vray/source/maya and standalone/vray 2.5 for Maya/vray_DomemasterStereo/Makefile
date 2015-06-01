# Linux - DomemasterStereo Vray Shader Makefile
# 2015-06-01 09.50 am
# by Andrew Hazelden  andrew@andrewhazelden.com
# http://www.andrewhazelden.com

# You can compile this file from the command line using:
# make -f Makefile

# Note: In order to compile the lens shaders, you have to copy your Vray for Maya Lib & Include files into the folders "../lib" and "../include".

.SUFFIXES:

all: libvray_DomemasterStereo.so

libvray_DomemasterStereo.so:  vray_DomemasterStereo.obj
	g++  -lpthread -lrt -lc -lz  -Wl,--gc-sections  -fPIC      -Wl,--no-as-needed   "-Wl,-(" -lvutils_s  -ldl -lvray -lplugman_s -shared -Wl,--export-dynamic -o "./libvray_DomemasterStereo.so" -L"../lib"    -O "./vray_DomemasterStereo.obj"  "-Wl,-)" -pthread -lrt


vray_DomemasterStereo.obj: ./vray_DomemasterStereo.cpp
	g++ -O0 -g -DENABLE_DEBUG_PRINTF -fPIC -Wreturn-type -Werror=return-type -DREQUIRE_IOSTREAM -DHAVE_EXR -D_LIBRARY_ALEMBIC -DHAVE_OPENSUBDIV -DHAVE_EMBREE -DDEBUG_OPT -DVASSERT_ENABLED -D__VRAY4MAYA30__ -DBits64_ -D_REENTRANT  -fvisibility=hidden -DVRAY_EXPORTS      -fexceptions    -I "../include"  -D "NDEBUG"     -c -o "./vray_DomemasterStereo.obj" "./vray_DomemasterStereo.cpp"

