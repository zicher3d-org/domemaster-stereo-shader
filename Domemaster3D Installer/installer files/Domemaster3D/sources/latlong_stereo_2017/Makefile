# Linux - LatLong_Stereo Mental Ray Shader Makefile
# by Andrew Hazelden  andrew@andrewhazelden.com
# http://www.andrewhazelden.com

# You can compile this file from the command line using:
# make

# You can install the files using the command:
# sudo make install

# Note: If you don't have gcc on your CentOS system use the command:
# sudo yum install gcc

CC = gcc

#MAYA_DIR=/usr/autodesk/maya8.5-x64
#MAYA_DIR=/usr/autodesk/maya2011-x64
#MAYA_DIR=/usr/autodesk/maya2012-x64
#MAYA_DIR=/usr/autodesk/maya2013-x64
#MAYA_DIR=/usr/autodesk/mentalrayForMaya2014
#MAYA_DIR=/usr/autodesk/mentalrayForMaya2015
#MAYA_DIR=/usr/autodesk/mentalrayForMaya2016
#MAYA_DIR=/usr/autodesk/mentalrayForMaya2016.5
#MAYA_DIR=/opt/nvidia/mentalray-3.14-for-Maya-2016
MAYA_DIR=/opt/nvidia/mentalray-3.14-for-Maya-2017

# Domemaster3D Maya 2016-2016 Shaders
#DOMEMASTER_DIR=/opt/Domemaster3D/maya/shaders

# Domemaster3D Maya 2016.5-2017 Shaders
DOMEMASTER_DIR=/opt/Domemaster3D/maya/shaders/mr3.14

#INC=-I$(MAYA_DIR)/devkit/mentalray/include
INC=-I$(MAYA_DIR)/devkit/include
LIB = 
LIB_STATIC = 
CFLAGS = -c -O3 -fPIC -Bsymbolic -DBIT64
LIBTOOL = ld

OBJS = latlong_stereo.o
SRCS = latlong_stereo.c

all: LatLong_Stereo.so

$(OBJS): 
	$(CC) $(CFLAGS) $(INC) $(LIB) $(SRCS) $(LIB_STATIC)

LatLong_Stereo.so : $(OBJS) 
	$(LIBTOOL) -export-dynamic -shared -o LatLong_Stereo.so $(OBJS)

clean: 
	rm -f $(OBJS) 
	rm -f LatLong_Stereo.so

install:
	# Maya 2013 and Earlier MR Shaders
	#cp LatLong_Stereo.so $(MAYA_DIR)/mentalray/lib
	#cp LatLong_Stereo.mi $(MAYA_DIR)/mentalray/include

	# Maya 2014+ MR Shaders
	#cp LatLong_Stereo.so $(MAYA_DIR)/shaders
	#cp LatLong_Stereo.mi $(MAYA_DIR)/shaders/include

	# Domemaster3D MR Shaders
	cp LatLong_Stereo.so $(DOMEMASTER_DIR)
	cp LatLong_Stereo.mi $(DOMEMASTER_DIR)/include

go: clean all install
