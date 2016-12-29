# Linux - Domemaster3D Mental Ray Shader Makefile
# by Andrew Hazelden  andrew@andrewhazelden.com
# http://www.andrewhazelden.com

CC = gcc

#MAYA_DIR=/usr/autodesk/maya8.5-x64
#MAYA_DIR=/usr/autodesk/maya2011-x64
#MAYA_DIR=/usr/autodesk/maya2012-x64
#MAYA_DIR=/usr/autodesk/maya2013-x64
#MAYA_DIR=/usr/autodesk/mentalrayForMaya2014
#MAYA_DIR=/usr/autodesk/mentalrayForMaya2015
#MAYA_DIR=/usr/autodesk/mentalrayForMaya2016
MAYA_DIR=/usr/autodesk/mentalrayForMaya2016.5
#MAYA_DIR=/opt/nvidia/mentalray-3.14-for-Maya-2016
#MAYA_DIR=/opt/nvidia/mentalray-3.14-for-Maya-2017

DOMEMASTER_DIR = /opt/Domemaster3D/maya/shaders

#INC = -I$(MAYA_DIR)/devkit/mentalray/include
INC = -I$(MAYA_DIR)/devkit/include
LIB = 
LIB_STATIC = 
CFLAGS = -c -O3 -fPIC -Bsymbolic -DBIT64
LIBTOOL = ld

OBJS = domeAFL_FOV_Stereo.o domeAFL_FOV.o domeAFL_WxH.o test_texture.o
SRCS = domeAFL_FOV_Stereo.c domeAFL_FOV.c domeAFL_WxH.c test_texture.c

all: domeAFL_FOV_Stereo.so

$(OBJS): 
	$(CC) $(CFLAGS) $(INC) $(LIB) $(SRCS) $(LIB_STATIC)

domeAFL_FOV_Stereo.so : $(OBJS) 
	$(LIBTOOL) -export-dynamic -shared -o domeAFL_FOV_Stereo.so $(OBJS)

clean: 
	rm -f $(OBJS) 
	rm -f domeAFL_FOV_Stereo.so

install:
# Maya 2013 and Earlier MR Shaders
#	cp domeAFL_FOV_Stereo.so $(MAYA_DIR)/mentalray/lib
#	cp domeAFL_FOV_Stereo.mi $(MAYA_DIR)/mentalray/include

# Maya 2014+ MR Shaders
	cp domeAFL_FOV_Stereo.so $(MAYA_DIR)/shaders
	cp domeAFL_FOV_Stereo.mi $(MAYA_DIR)/shaders/include

# Domemaster3D MR Shaders
#	cp domeAFL_FOV_Stereo.so $(DOMEMASTER_DIR)
#	cp domeAFL_FOV_Stereo.mi $(DOMEMASTER_DIR)/include

go: clean all install
