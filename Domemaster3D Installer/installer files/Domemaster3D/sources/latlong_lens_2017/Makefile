# Linux - latlong_lens Mental Ray Shader Makefile
# by Andrew Hazelden  andrew@andrewhazelden.com
# http://www.andrewhazelden.com

# You can compile this file from the command line using:
# make

# You can install the files using the command:
# sudo make install

# Note: If you don't have g++ on your CentOS system use the command:
# sudo yum install gcc-c++

CC=g++

#MAYA_DIR=/usr/autodesk/maya8.5-x64
#MAYA_DIR=/usr/autodesk/maya2011-x64
#MAYA_DIR=/usr/autodesk/maya2012-x64
#MAYA_DIR=/usr/autodesk/maya2013-x64
#MAYA_DIR=/usr/autodesk/mentalrayForMaya2014
#MAYA_DIR=/usr/autodesk/mentalrayForMaya2015
#MAYA_DIR=/usr/autodesk/mentalrayForMaya2016
#MAYA_DIR=/usr/autodesk/mentalrayForMaya2016.5
MAYA_DIR=/opt/nvidia/mentalray-for-maya-2017-3.14

# Domemaster3D Maya 2016-2016 Shaders
#DOMEMASTER_DIR=/opt/Domemaster3D/maya/shaders

# Domemaster3D Maya 2016.5-2017 Shaders
DOMEMASTER_DIR=/opt/Domemaster3D/maya/shaders/mr3.14

# Maya 2012's mental ray directory:
#MENTALRAY_DEV_DIR=/devkit/mentalray/include

# Maya 2013's mental ray directory:
#MENTALRAY_DEV_DIR=/mentalray/devkit/include

# Maya 2014/2015's mental ray devkit directory:
MENTALRAY_DEV_DIR=/devkit/include

INC=-I$(MAYA_DIR)$(MENTALRAY_DEV_DIR)
LIB= 
LIB_STATIC = 
CFLAGS=-c -O3 -fPIC -Bsymbolic -DBIT64
LIBTOOL=ld
LDEXECFLAGS=

OBJS=latlong_lens.o
SRCS=latlong_lens.cpp

all: latlong_lens.so

$(OBJS): 
	$(CC) $(CFLAGS) $(INC) $(LIB) $(SRCS) $(LIB_STATIC)

latlong_lens.so : $(OBJS) 
	$(LIBTOOL) -export -shared $(LDEXECFLAGS) -o latlong_lens.so $(OBJS)

clean: 
	rm -rf $(OBJS) 
	rm -rf latlong_lens.so

install:	
	# Maya 2013 and Earlier MR Shaders
	#cp ./latlong_lens.so $(MAYA_DIR)/mentalray/shaders
	#cp ./latlong_lens.mi $(MAYA_DIR)/mentalray/shaders/include
  
	# Maya 2014+ MR Shaders
	#	cp latlong_lens.so $(MAYA_DIR)/shaders
	#	cp latlong_lens.mi $(MAYA_DIR)/shaders/include

	# Domemaster3D Shaders Folder
	cp ./latlong_lens.so $(DOMEMASTER_DIR)
	cp ./latlong_lens.mi $(DOMEMASTER_DIR )/include

go: clean all install

