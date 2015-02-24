# Linux - Domemaster3D Arnold Shader Makefile
# by Andrew Hazelden  andrew@andrewhazelden.com
# http://www.andrewhazelden.com

# You can compile this file from the command line using:
# Make -f Makefile

# You can install the files using the command
# sudo Make -f Makefile install

CC=g++

# Which version of Maya you are running with Arnold?
#MAYA_VERSION=2012
#MAYA_VERSION=2013
# Current Build Version = 2014
MAYA_VERSION=2014
#MAYA_VERSION=2015

MTOA_SHADERS_DIR=/opt/solidangle/mtoa/$(MAYA_VERSION)/shaders
MTOA_TEMPLATE_DIR=/opt/solidangle/mtoa/$(MAYA_VERSION)/scripts/mtoa/ui/ae

# Which version of the Arnold API Devkit are you using?
MTOA_API_VERSION=4.2.3.1

MTOA_DEV_DIR=/opt/solidangle/Arnold-$(MTOA_API_VERSION)-linux
MTOA_INCLUDE_DIR=$(MTOA_DEV_DIR)/include

INC = -I$(MTOA_INCLUDE_DIR)/
LIB =
LIB_STATIC = 
CFLAGS = -c -O3 -fPIC -Bsymbolic -DBIT64
LIBTOOL = ld
LDEXECFLAGS=

OBJS = DomemasterWxH.o
SRCS = DomemasterWxH.cpp

all: DomemasterWxH.so

$(OBJS): 
	$(CC) $(CFLAGS) $(INC) $(LIB) $(SRCS) $(LIB_STATIC)

DomemasterWxH.so : $(OBJS) 
	$(LIBTOOL) -export -dynamic -shared $(LDEXECFLAGS) -o DomemasterWxH.so $(OBJS)

clean: 
	rm -f $(OBJS) 
	rm -f DomemasterWxH.so

install:
	# Arnold Shader and Metadata File
	# ---------------------------------
	cp ./DomemasterWxH.so $(MTOA_SHADERS_DIR)
	cp ./DomemasterWxH.mtd $(MTOA_SHADERS_DIR)

	# Arnold Maya AE Template File
	# ------------------------------
	cp ./DomemasterWxHTemplate.py $(MTOA_TEMPLATE_DIR)
	
go: clean all install
