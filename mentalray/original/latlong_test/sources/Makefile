# Linux - LatLong_Stereo Mental Ray Shader Makefile
# by Andrew Hazelden  andrew@andrewhazelden.com
# http://www.andrewhazelden.com

CC = gcc

#MAYA_DIR=/usr/autodesk/maya8.5-x64
#MAYA_DIR=/usr/autodesk/maya2011-x64
#MAYA_DIR=/usr/autodesk/maya2012-x64
#MAYA_DIR=/usr/autodesk/maya2013-x64
MAYA_DIR=/usr/autodesk/mentalrayForMaya2014

#INC = -I$(MAYA_DIR)/devkit/mentalray/include
INC = -I$(MAYA_DIR)/devkit/include
LIB = 
LIB_STATIC = 
CFLAGS = -c -O3 -fPIC -Bsymbolic -DBIT64
LIBTOOL = ld

OBJS = LatLong_Stereo.o
SRCS = LatLong_Stereo.c

all: LatLong_Stereo.so

$(OBJS): 
	$(CC) $(CFLAGS) $(INC) $(LIB) $(SRCS) $(LIB_STATIC)

LatLong_Stereo.so : $(OBJS) 
	$(LIBTOOL) -export-dynamic -shared -o LatLong_Stereo.so $(OBJS)

clean: 
	rm -f $(OBJS) 
	rm -f LatLong_Stereo.so

install:
#	cp LatLong_Stereo.so $(MAYA_DIR)/mentalray/lib
#	cp LatLong_Stereo.mi $(MAYA_DIR)/mentalray/include
	cp LatLong_Stereo.so $(MAYA_DIR)/shaders
	cp LatLong_Stereo.mi $(MAYA_DIR)/shaders/include
