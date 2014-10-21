# Linux - LatLong_Stereo Mental Ray Shader Makefile
# by Andrew Hazelden  andrew@andrewhazelden.com
# http://www.andrewhazelden.com

CC = gcc

#MAYA_DIR=/usr/autodesk/maya8.5-x64
#MAYA_DIR=/usr/autodesk/maya2011-x64
#MAYA_DIR=/usr/autodesk/maya2012-x64
#MAYA_DIR=/usr/autodesk/maya2013-x64
MAYA_DIR=/usr/autodesk/mentalrayForMaya2014
#MAYA_DIR=/usr/autodesk/mentalrayForMaya2015

DOMEMASTER_DIR = /opt/Domemaster3D/maya/shaders

#INC = -I$(MAYA_DIR)/devkit/mentalray/include
INC = -I$(MAYA_DIR)/devkit/include
LIB = 
LIB_STATIC = 
CFLAGS = -c -O3 -fPIC -Bsymbolic -DBIT64
LIBTOOL = ld

OBJS = latlong_stereo.o
SRCS = latlong_stereo.c

all: latlong_stereo.so

$(OBJS): 
	$(CC) $(CFLAGS) $(INC) $(LIB) $(SRCS) $(LIB_STATIC)

latlong_stereo.so : $(OBJS) 
	$(LIBTOOL) -export-dynamic -shared -o latlong_stereo.so $(OBJS)

clean: 
	rm -f $(OBJS) 
	rm -f latlong_stereo.so

install:
#Rename the file to have proper capitalization
	mv latlong_stereo.so LatLong_Stereo.so

# Maya 2013 and Earlier MR Shaders
#	cp LatLong_Stereo.so $(MAYA_DIR)/mentalray/lib
#	cp LatLong_Stereo.mi $(MAYA_DIR)/mentalray/include

# Maya 2014+ MR Shaders
#	cp LatLong_Stereo.so $(MAYA_DIR)/shaders
#	cp LatLong_Stereo.mi $(MAYA_DIR)/shaders/include

# Domemaster3D MR Shaders
	cp LatLong_Stereo.so $(DOMEMASTER_DIR)
	cp LatLong_Stereo.mi $(DOMEMASTER_DIR)/include

go: clean all install
