"""
Domemaster3D Camera Setup Script V1.6
2014-10-21 04.42 pm
Created by Andrew Hazelden  andrew@andrewhazelden.com

This script makes it easy to start creating fulldome stereoscopic content in Autodesk Maya.
-------------------------------------------------------------------------------------------------------

Version History

Version 1.6
---------------
Sept 17, 2014

Added LatLong_Stereo support

Version 1.5
---------------
July 12, 2014

Added a new "FulldomeIBL" tool to the Maya shelf. This allows you to use a file texture with a circular domemaster 180 degree FOV image as the image based lighting environment map in the scene, and as the source of final gather IBL, and Maya 2015 "emit light" based lighting. The fulldome texture is applied using a mentalrayTexture with an image sequence expression. The FulldomeIBL tool supports domemaster frame masking. 

The new "HemirectIBL" tool (hemirect = half height equirectangular 360x90 degree image) tool creates a custom mentalrayTexture based shading network that lets you feed in an image with the top half of an equirectangular panorama into the mental ray IBL's spherical texture input. Note: This mode requires your batch rendering software to distribute the rendering job using 1 frame per packet/render slice so a new image is loaded for each from of the sequence. The HemirectIBL tool works with Maya 2015's newly improved "emit light" IBL lighting system.

A remapColor node is connected to the FulldomeIB and HemirectIBL shading networks to make it easier to adjust the color correction and exposure on the imagery before it is used with final gathering or light emission.

Updated the dome version "update" button URL to use GitHub

Changed the openGL viewport default focal length from 4 mm (160 degree FOV) to 18 mm (90 degree FOV)

Updated the code that makes sure mental ray is loaded and active before adding mental ray lens shaders to the scene

Added display smoothing to the AutoMagic fulldome sphere test shape

Updated the order of the DomeGrid Extra Attributes.

Version 1.4 B10
-------------------
Dec 18, 2013

Added the latlong_lens shader

Version 1.4 B9
-----------------
Dec 7, 2013

Updated Linux install path to:
/opt/Domemaster3D

Version 1.4 B8
-----------------
Nov 20, 2013

Added flexible changeRenderRes(1024) render resolution tool to match 0.5k, 1k, 2k, 4k, 8k shelf items

Version 1.4 B6
-----------------
Oct 27, 2013

Updated Grid defaults and worked on Maya 2010 support.

Version 1.4 B5
-----------------
Oct 24, 2013

Updated PreRenderMel and PostRenderMel code for the DomeAFL_FOV_Stereo shader.

Version 1.4 B4
---------------
Oct 21, 2013

Upgraded the DomeGrid with new radius controls, color controls, paintFX toon line thickness controls, and custom display modes


Version 1.4 B1
---------------
Oct 6, 2013

Renamed the fulldome rig creation script to domeCamera.py for clarity.
This script is compatible with the new StereoRigEditor based stereo fulldome rig


Version 1.3.5
---------------
Sept 27, 2013
Added features for previewing the dome radius (zero parallax zone), field of view, and safe viewing volumes

Reorganized the python scripts to put the domeAFL_FOV code with the domeAFL_FOV_Stereo camera code 


Version 1.3.4
---------------
Released June 27, 2013
Updated the the Automagic tool's dome grid color to a brighter yellow value. This makes the grid more visible in a Physical Sun & Sky scene.

Added a new HELP icon to the Maya Shelf toolset. This shelf item loads the domemaster stereo shader wiki page.


Version 1.3.3
---------------
Released May 30, 2013
Updated the default locator scale.

Fixed the dome ramp shelf tool item so the default ramp texture preset is applied when the tool is run multiple times.

Updated source image paths for Maya 2010 compatibility

Version 1.3.2
---------------
Released April 16, 2013
Edited the default camera connections for the lens shaders to work with the modified versions of the maya createMentalRayIndirectLightingTab.mel & AEmia_physicalskyTemplate.mel scripts. This fixes the problem of the Physical Sky & Sun system overwriting the first .miLensShader input on cameras in the scene.

The location of the default domemaster control map textures is now in the Program Files\Domemaster3D\sourceimages folder on Windows or the /Applications/Domemaster3D/sourceimages folder on Mac OS X. The Domemaster3D shelf tools have been updated to link to the new sourceimages folder.

Version 1.3
------------
Released Nov 4, 2012
Moved FOV and WxH functions into domeMaterial.py, changed the default lens shader connections to support the mental ray sky and sun system.


Version 1.1
------------
Released Aug 14, 2012
Improved python code and made it Maya 2010 compatible.


Version 1.0
------------
Released Aug 6, 2012
First release of the Domemaster3D auto-setup python scripts.


------------------------------------------------------------------------------

Domemaster3D AutoSetup
A python function to create a fulldome stereo rig and test grid in Maya.

Run using the command:
import domeCamera as domeCamera
reload(domeCamera)
domeCamera.autosetup()

------------------------------------------------------------------------------

Domemaster3D Fulldome Stereo Rig
A python function to create a fulldome stereo rig in Maya.

Run using the command:
import domeCamera as domeCamera
reload(domeCamera)
domeCamera.createFulldomeStereoRig()

------------------------------------------------------------------------------

Domemaster3D createLatLong_Camera
A python function to create a latitude longitude lens shader and attach it to a camera.

Run using the command:
import domeCamera as domeCamera
reload(domeCamera)
domeCamera.createLatLong_Camera():
------------------------------------------------------------------------------

Domemaster3D createLatLongStereoRig
A python function to create a stereoscopic latitude longitude lens shader and attach it to a camera.

Run using the command:
import domeCamera as domeCamera
reload(domeCamera)
domeCamera.createLatLongStereoRig():

------------------------------------------------------------------------------

Domemaster3D createDomeAFL_WxH_Camera
A python function to create a domeAFL_WxH lens shader and attach it to a camera.

Run using the command:
import domeCamera as domeCamera
reload(domeCamera)
domeCamera.createDomeAFL_WxH_Camera()

------------------------------------------------------------------------------

Domemaster3D createDomeAFL_FOV_Camera
A python function to create a domeAFL_FOV lens shader and attach it to a camera.

Run using the command:
import domeCamera as domeCamera
reload(domeCamera)
domeCamera.createDomeAFL_FOV_Camera()

------------------------------------------------------------------------------

Domemaster3D DomeGrid test background 
A python function to create a hemispherical yellow test grid in Maya. 

Run using the command:
import domeCamera as domeCamera
reload(domeCamera)
domeCamera.createDomeGrid()

------------------------------------------------------------------------------

Domemaster3D createTestShapes
A python function to create a test sphere and cube in Maya. 

Run using the command:
import domeCamera as domeCamera
reload(domeCamera)
domeCamera.createTestShapes()

------------------------------------------------------------------------------

Domemaster3D createRobLookup
A python function to create a mental ray screen space texture 
and connect it to a robLookupBackground lens shader. 

Run using the command:
import domeCamera as domeCamera
reload(domeCamera)
domeCamera.createRobLookup()
------------------------------------------------------------------------------

Domemaster3D createDomeRampTexture
A python function to create a mental ray screen space ramp texture 
and connect it to a robLookupBackground lens shader.

Run using the command:
import domeCamera as domeCamera
reload(domeCamera)
domeCamera.createDomeRampTexture()

------------------------------------------------------------------------------

Domemaster3D setRenderRes
A python function to setup the basic mental ray 2K x 2K square render settings. 

Run using the command:
import domeCamera as domeCamera
reload(domeCamera)
domeCamera.setRenderRes()
------------------------------------------------------------------------------

Domemaster3D setDomeSamplingQuality
A python function to setup the mental ray AA sampling quality. 

Run using the command:
import domeCamera as domeCamera
reload(domeCamera)
domeCamera.setDomeSamplingQuality()

------------------------------------------------------------------------------

Domemaster3D changeRenderRes
A python function to change the basic mental ray resolution square render settings. 

Run using the command:
import domeCamera
reload(domeCamera)
domeCamera.changeRenderRes(1024)

------------------------------------------------------------------------------

Domemaster3D Force Mental Ray to load
A python function to make sure mental ray is active and the MR shading nodes are read to be used.

Run using the command:
import domeCamera
reload(domeCamera)
domeCamera.forceMentalRayLoad()

------------------------------------------------------------------------------

Domemaster3D createFulldomeIBL
A python function to create a mental ray texture and connect it to an mental ray mentalrayIbl node.

The this function will offset the texture coordinates so a 180 degree fisheye image would sit in the center of the mental ray IBL system's 360 degree angular fisheye input.

Run using this command:
import domeCamera
reload(domeCamera)
domeCamera.createFulldomeIBL()


------------------------------------------------------------------------------

Domemaster3D getMayaVersionDome

A python function to check what Maya version is active.

import domeCamera
reload(domeCamera)
domeCamera.getMayaVersionDome()

------------------------------------------------------------------------------

"""


"""
Show the Domemaster Wiki
--------------------------------
Loads the wiki page in your default web browser

Run using the command:
print("Open the Domemaster Wiki Page")
import domeCamera as domeCamera
domeCamera.openDomemasterWiki()

print("Open the Domemaster NING Group")
import domeCamera as domeCamera
domeCamera.openDomemasterNing()

print("Open the Domemaster Downloads Page")
import domeCamera as domeCamera
domeCamera.openDomemasterDownloads()

print("Open the Domemaster Bug Reporter")
import domeCamera as domeCamera
domeCamera.openDomemasterBugReport()


"""

def openDomemasterWiki():
  import webbrowser
  
  # Domemaster Stereo Shader - Wiki Page
  url = 'https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages'
  
  # Open URL in new window, raising the window if possible.
  webbrowser.open_new(url)
  
  
def openDomemasterNing():
  import webbrowser
  
  # Domemaster NING Group
  url = 'http://fulldome.ning.com/forum/topics/stereoscopic-domemaster-images'
  
  # Open URL in new window, raising the window if possible.
  webbrowser.open_new(url)


def openDomemasterDownloads():
  import webbrowser
  
  # Domemaster Stereo Shader - Download Page
  url = 'https://github.com/zicher3d-org/domemaster-stereo-shader/releases'

  # Open URL in new window, raising the window if possible.
  webbrowser.open_new(url)
  
def openDomemasterBugReport():
  import webbrowser
  
  # Domemaster Stereo Shader - Bug Report Page
  url = 'https://github.com/zicher3d-org/domemaster-stereo-shader/issues'
  
  # Open URL in new window, raising the window if possible.
  webbrowser.open_new(url)
  

"""
Find out the path to the sourceimages folder
----------------------
A python function to check the operating system platform and the source images folder. 

"""
def getSourceImagesPath(imageFileName):
  import os
  import maya.cmds as cmds
  import maya.mel as mel
  # ---------------------------------------------------------------------
  #Set up the base folder path for the Domemaster3D control maps
  # ---------------------------------------------------------------------

  #Check OS platform for Windows/Mac/Linux Paths
  import platform

  #This is the base path for the images folder
  baseImagesFolder = ""
  
  # Try and read the value from the current Maya.env file's environment variables
  baseImagesFolder = os.environ.get('DOMEMASTER3D_SOURCEIMAGES_DIR') + "/"
  # Typical Result: C:/Program Files/Domemaster3D/sourceimages/ 
  
  # Use a fixed value if the env var is empty
  if baseImagesFolder == None:
    if platform.system()=='Windows':
      #Check if the program is running on Windows 
      baseImagesFolder = "C:/Program Files/Domemaster3D/sourceimages/"
    elif platform.system()== 'win32':
      #Check if the program is running on Windows 32
      baseImagesFolder = "C:/Program Files (x86)/Domemaster3D/sourceimages/"
    elif platform.system()== 'Darwin':
      #Check if the program is running on Mac OS X
      baseImagesFolder = "/Applications/Domemaster3D/sourceimages/"
    elif platform.system()== 'Linux':
      #Check if the program is running on Linux
      baseImagesFolder = "/opt/Domemaster3D/sourceimages/"
    elif platform.system()== 'Linux2':
      #Check if the program is running on Linux
      baseImagesFolder = "/opt/Domemaster3D/sourceimages/"
    else:
      # Create the empty variable as a fallback mode
      baseImagesFolder = ""

  combinedFileAndImagePath = baseImagesFolder + imageFileName

  print "[Domemaster3D is running on a " + platform.system() + " System]"
  print "[Requesting the image file]: " + combinedFileAndImagePath

  return combinedFileAndImagePath



"""
Domemaster3D AutoSetup
----------------------
A python function to create a fulldome stereo rig and test grid in Maya. 

"""
def autosetup():
  setRenderRes()
  setDomeSamplingQuality()
  createFulldomeStereoRig()
  createDomeGrid()
  createTestShapes()




"""
Domemaster3D setDomeSamplingQuality
----------------------
A python function to setup the mental ray AA sampling quality. 

"""
def setDomeSamplingQuality():
  import maya.cmds as cmds
  import maya.mel as mel
  #---------------------------------------------------------------------
  # Render AA Quality Settings
  # ---------------------------------------------------------------------

  #Add the mental ray miDefaultOptions settings to the scene before accessing MR indirect lighting features
  mel.eval("miCreateDefaultNodes();")

  # Gaussian AA Filtering
  cmds.setAttr( 'miDefaultOptions.filter', 2)

  # Filter Size 3x3
  cmds.setAttr( 'miDefaultOptions.filterWidth', 1)
  cmds.setAttr( 'miDefaultOptions.filterHeight', 1)

  #Sample Adjustments
  cmds.setAttr( 'miDefaultOptions.maxSamples', 2)
  cmds.setAttr( 'miDefaultOptions.minSamples', 0)

  #Production Quality Settings
  cmds.setAttr( 'miDefaultOptions.maxReflectionRays', 10)
  cmds.setAttr( 'miDefaultOptions.maxRefractionRays', 10)
  cmds.setAttr( 'miDefaultOptions.maxRayDepth', 20)
  cmds.setAttr( 'miDefaultOptions.maxShadowRayDepth', 2)

  # Maya 2014, 2015+ AA settings
  # Check if we are running Maya 2014+ and enable MR Unified Sampling
  mayaVersion = getMayaVersionDome()

  if (mayaVersion >= 2014):
    #Enable Unified Sampling - The forced unified sampling mode is remmed out for Maya 2015 testing
    #cmds.setAttr( 'miDefaultOptions.miRenderUsing', 0)

    #Set the Unified Quality to 0.6
    cmds.setAttr( 'miDefaultOptions.miSamplesQualityR', 0.6)
    cmds.setAttr( 'miDefaultOptions.miSamplesMin', 1)
    cmds.setAttr( 'miDefaultOptions.miSamplesMax', 100)


"""
Domemaster3D SetRenderRes
----------------------
A python function to setup the basic mental ray 2K x 2K square render settings. 

"""
def setRenderRes():
  import maya.cmds as cmds
  import maya.mel as mel

  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()
  
  fulldomeRenderWidth = 2048
  fulldomeRenderHeight = 2048
  
  #---------------------------------------------------------------------
  # Setup the default render settings for a square domemaster image output
  # ---------------------------------------------------------------------
  cmds.setAttr( 'defaultResolution.width', fulldomeRenderWidth )
  cmds.setAttr( 'defaultResolution.height', fulldomeRenderHeight )
  cmds.setAttr( 'defaultResolution.deviceAspectRatio', 1)
  cmds.setAttr( 'defaultResolution.pixelAspect', 1)
  


"""
Domemaster3D changeRenderRes
----------------------
A python function to change the basic mental ray resolution square render settings. 

"""

def changeRenderRes( renderSizePx ):
  import maya.mel as mel
  import maya.cmds as cmds

  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()
  
  fulldomeRenderWidth = renderSizePx
  fulldomeRenderHeight = renderSizePx
  
  #---------------------------------------------------------------------
  # Setup the default render settings for a square domemaster image output
  # ---------------------------------------------------------------------
  cmds.setAttr( 'defaultResolution.width', fulldomeRenderWidth )
  cmds.setAttr( 'defaultResolution.height', fulldomeRenderHeight )
  cmds.setAttr( 'defaultResolution.deviceAspectRatio', 1)
  cmds.setAttr( 'defaultResolution.pixelAspect', 1)

  print ("Changed the render settings to output a " + str(renderSizePx) + "x" + str(renderSizePx) + " image.")

  
"""
Domemaster3D changeRenderResWH
----------------------
A python function to change the basic mental ray resolution render settings. 

"""

def changeRenderResWH( renderSizeW,  renderSizeH):
  import maya.mel as mel
  import maya.cmds as cmds

  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()
  
  domeRenderWidth = renderSizeW
  domeRenderHeight = renderSizeH
  domeDeviceAspectRatio=domeRenderWidth/domeRenderHeight
  
  #---------------------------------------------------------------------
  # Setup the default render settings for a square domemaster image output
  # ---------------------------------------------------------------------
  cmds.setAttr( 'defaultResolution.width', domeRenderWidth )
  cmds.setAttr( 'defaultResolution.height', domeRenderHeight )
  cmds.setAttr( 'defaultResolution.deviceAspectRatio', domeDeviceAspectRatio)
  cmds.setAttr( 'defaultResolution.pixelAspect', 1)

  print ("Changed the render settings to output a " + str(renderSizeW) + "x" + str(renderSizeW) + " image.")



"""
Domemaster3D Fulldome Stereo Rig
--------------------------------
A python function to create a fulldome stereo rig in Maya.
"""

def createFulldomeStereoRig():
  import maya.cmds as cmds
  import maya.mel as mel
  
  # ---------------------------------------------------------------------
  # Setup the default Maya / Mental Ray Settings
  # ---------------------------------------------------------------------
  cmds.loadPlugin( "stereoCamera", qt=True )
  
  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()

  # ---------------------------------------------------------------------
  # Create the stereo rig
  # ---------------------------------------------------------------------
  
  #import maya.app.stereo.stereoCameraMenus as stereoCameraMenus
  #stereoCameraMenus.buildCreateMenu()
  #import maya.app.stereo.stereoCameraRig
  #maya.app.stereo.stereoCameraRig.createStereoCameraRig()
  
  from maya.app.stereo import stereoCameraRig
  rig = stereoCameraRig.createStereoCameraRig('DomeStereoCamera')
  #[u'DomeStereoCamera', u'DomeStereoCameraLeft', u'DomeStereoCameraRight']
  
  #Get the stereo camera rig shape nodes for the center/right/left cameras
  rig_center_shape_name =  getObjectShapeNode(rig[0])
  #[u'stereoCameraCenterCamShape', u'stereoCameraFrustum'] #

  rig_left_shape_name =  getObjectShapeNode(rig[1])
  # Result: [u'stereoCameraLeftShape'] #

  rig_right_shape_name =  getObjectShapeNode(rig[2])
  # Result: [u'stereoCameraRightShape'] #
  
  """
  cmds.setAttr( rig[0]+'.rotateX', 90)
  cmds.setAttr( rig[0]+'.rotateY', 0)
  cmds.setAttr( rig[0]+'.rotateZ', 0)
  
  """
  
  # Changes the render settings to set the stereo camera to be a renderable camera
  cmds.setAttr( rig_left_shape_name[0]+'.renderable', 1) #stereoCameraLeftShape
  cmds.setAttr( rig_right_shape_name[0]+'.renderable', 1) #stereoCameraRightShape
  cmds.setAttr( 'topShape.renderable', 0)
  cmds.setAttr( 'sideShape.renderable', 0)
  cmds.setAttr( 'frontShape.renderable', 0)
  cmds.setAttr( 'perspShape.renderable', 0)

  #Set up the default mental ray AA sampling quality
  setDomeSamplingQuality()
  
  #import maya.cmds as cmds
  #rig_center_shape_name =  getObjectShapeNode(rig[0])
  #lensShaderName = cmds.listConnections( rig_center_shape_name[0]+'.miLensShader')

  #Debugging test line
  #lensShaderName = "center_domeAFL_FOV_Stereo";
  #print ("Lens shader name: " + str(lensShaderName))
  
  # Select the center camera's domeAFL_FOV_Stereo node
  #cmds.select(lensShaderName, replace=True)
  
  leftLensShader = cmds.listConnections(rig_left_shape_name[0]+'.miLensShader')
  rightLensShader = cmds.listConnections(rig_right_shape_name[0]+'.miLensShader')
  centerLensShader = cmds.listConnections(rig_center_shape_name[0]+'.miLensShader')
  
  #Select the camera's domeAFL_FOV_Stereo nodes in the attribute editor to add the Extra Attrs
  #mel.eval ( ' showEditorExact("' + centerLensShader[0] + '") ' )
  mel.eval ( ' showEditorExact("' + leftLensShader[0] + '") ' )
  mel.eval ( ' showEditorExact("' + rightLensShader[0] + '") ' )
  
  #Finish off by reselecting the center lens shader
  mel.eval ( ' showEditorExact("' + centerLensShader[0] + '") ' )
  
  #---------------------------------------------------------------------------
  # Enable Real-time 3D in the OpenGL viewport 
  # using a PreRender and PostRender MEL script
  #---------------------------------------------------------------------------
  #import maya.cmds as cmds

  #PreRender MEL:
  cmds.setAttr( 'defaultRenderGlobals.preMel', "source \"domeRender.mel\"; domemaster3DPreRenderMEL();", type='string')
  #PostRender MEL:
  cmds.setAttr( 'defaultRenderGlobals.postMel' , "source \"domeRender.mel\"; domemaster3DPostRenderMEL();", type='string')

  #enable realtime 3D
  mel.eval("source \"domeRender.mel\"; domemaster3DPostRenderMEL();");
  
  return rig
  

"""
Domemaster3D createDomeAFL_FOV_Camera
----------------------
A python function to create a domeAFL_FOV lens shader and attach it to a camera.
""" 
def createDomeAFL_FOV_Camera():
  import maya.cmds as cmds
  import maya.mel as mel  
  
  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()

  #Variables
  
  # ---------------------------------------------------------------------
  # Create the stereo rig
  # ---------------------------------------------------------------------
  
  # Create a camera and get the shape name.
  cameraName = cmds.camera(name='domeAFL_FOV_Camera')
  cameraShape = cameraName[1]
  
  # ---------------------------------------------------------------------
  # Create the domeAFL_FOV node
  # ---------------------------------------------------------------------
  domeAFL_lens_node = cmds.shadingNode( 'domeAFL_FOV', n='domeAFL_FOV', asUtility=True  ) 
  
  # Primary lens shader connection:
  # Connect to the .miLensShaderList[0] input on the camera
  #cmds.connectAttr( domeAFL_lens_node+'.message', cameraShape+'.miLensShaderList[0]' )
  
  # Alternate lens shader connection:
  # Connect directly to the first .miLensShader input on the camera
  # Note: This first lens shader connection is overwritten by the mental ray Sun & Sky system
  cmds.connectAttr( domeAFL_lens_node+'.message', cameraShape+'.miLensShader' )
  
  # Scale the stereo camera rig locator larger 
  #cmds.setAttr(cameraShape+'.locatorScale', 1) #Scale Camera icon
  
  # Link the new attribute 'Cam Locator Scale' to the dome camera's locator size control
  cmds.addAttr( cameraName[0], longName='Cam_Locator_Scale', niceName='Cam Locator Scale', attributeType='double', defaultValue=1.0, minValue=0.001)
  cmds.setAttr( cameraName[0]+'.Cam_Locator_Scale', keyable=False, channelBox=True)
  cmds.connectAttr ( cameraName[0]+'.Cam_Locator_Scale', cameraShape+'.locatorScale', force=True)
  
  cmds.setAttr( cameraName[0]+'.rotateX', 90)
  cmds.setAttr( cameraName[0]+'.rotateY', 0)
  cmds.setAttr( cameraName[0]+'.rotateZ', 0)
  
  # Changes the render settings to set the stereo camera to be a renderable camera
  cmds.setAttr( cameraShape+'.renderable', 1) #domeAFL_FOV_CameraShape
  cmds.setAttr( 'topShape.renderable', 0)
  cmds.setAttr( 'sideShape.renderable', 0)
  cmds.setAttr( 'frontShape.renderable', 0)
  cmds.setAttr( 'perspShape.renderable', 0)

  #Set up the default mental ray AA sampling quality
  setDomeSamplingQuality()
  
  # ---------------------------------------------------------------------
  # Setup the stereo rig camera attributes
  # ---------------------------------------------------------------------
  # 4 mm focal length = 160 degree FOV
  #cmds.setAttr( cameraShape+'.focalLength', 4 )

  # 18 mm focal length = 90 degree FOV
  cmds.setAttr( cameraShape+'.focalLength', 18 )
 
  #Select the center camera domeAFL_FOV_Stereo node in the attribute editor
  #This will add the extra attributes to the camera
  mel.eval ( ' showEditorExact("' + domeAFL_lens_node + '") ' )
  
  # ---------------------------------------------------------------------
  #Set the default camera separation based upon the scene size
  # ---------------------------------------------------------------------
  #defaultDomeRadius = 2

  #Set the dome radius
  #cmds.setAttr(domeAFL_lens_node+'.Dome_Radius', defaultDomeRadius)
  #print("Dome Radius: " + str(defaultDomeRadius))
  
  

"""
Domemaster3D createDomeAFL_WxH_Camera
----------------------
A python function to create a domeAFL_WxH lens shader and attach it to a camera.
"""
def createDomeAFL_WxH_Camera():
  import maya.cmds as cmds
  #import maya.mel as mel 

  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()

  #Variables

  # ---------------------------------------------------------------------
  # Create the stereo rig
  # ---------------------------------------------------------------------

  # Create a camera and get the shape name.
  cameraName = cmds.camera(name='domeAFL_WxH_Camera')
  cameraShape = cameraName[1]

  # ---------------------------------------------------------------------
  # Create the domeAFL_WxH node
  # ---------------------------------------------------------------------
  domeAFL_WxH_lens_node = cmds.shadingNode( 'domeAFL_WxH', n='domeAFL_WxH', asUtility=True  ) 

  # Primary lens shader connection:
  # Connect to the .miLensShaderList[0] input on the camera
  # cmds.connectAttr( domeAFL_WxH_lens_node+'.message', cameraShape+'.miLensShaderList[0]' )

  # Alternate lens shader connection:
  # Connect directly to the first .miLensShader input on the camera
  # Note: This first lens shader connection is overwritten by the mental ray Sun & Sky system
  cmds.connectAttr( domeAFL_WxH_lens_node+'.message', cameraShape+'.miLensShader' )

  # Scale the stereo camera rig locator larger 
  #cmds.setAttr(cameraShape+'.locatorScale', 1) #Scale Camera icon

  # Link the new attribute 'Cam Locator Scale' to the dome camera's locator size control
  cmds.addAttr( cameraName[0], longName='Cam_Locator_Scale', niceName='Cam Locator Scale', attributeType='double', defaultValue=1.0, minValue=0.001)
  cmds.setAttr( cameraName[0]+'.Cam_Locator_Scale', keyable=False, channelBox=True)
  cmds.connectAttr ( cameraName[0]+'.Cam_Locator_Scale', cameraShape+'.locatorScale', force=True)


  cmds.setAttr( cameraName[0]+'.rotateX', 90)
  cmds.setAttr( cameraName[0]+'.rotateY', 0)
  cmds.setAttr( cameraName[0]+'.rotateZ', 0)

  # Changes the render settings to set the stereo camera to be a renderable camera
  cmds.setAttr( cameraShape+'.renderable', 1) #domeAFL_WxH_CameraShape
  cmds.setAttr( 'topShape.renderable', 0)
  cmds.setAttr( 'sideShape.renderable', 0)
  cmds.setAttr( 'frontShape.renderable', 0)
  cmds.setAttr( 'perspShape.renderable', 0)

  #Set up the default mental ray AA sampling quality
  setDomeSamplingQuality()

  # ---------------------------------------------------------------------
  # Setup the stereo rig camera attributes
  # ---------------------------------------------------------------------
  # 4 mm focal length = 160 degree FOV
  #cmds.setAttr( cameraShape+'.focalLength', 4 )

  # 18 mm focal length = 90 degree FOV
  cmds.setAttr( cameraShape+'.focalLength', 18 )


"""
Domemaster3D createLatLong_Camera
----------------------
A python function to create a latitude longitude lens shader and attach it to a camera.
""" 

def createLatLong_Camera():
  import maya.cmds as cmds
  #import maya.mel as mel 

  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()

  #Variables

  # ---------------------------------------------------------------------
  # Create the stereo rig
  # ---------------------------------------------------------------------

  # Create a camera and get the shape name.
  cameraName = cmds.camera(name='latlong_Camera')
  cameraShape = cameraName[1]

  # ---------------------------------------------------------------------
  # Create the domeAFL_WxH node
  # ---------------------------------------------------------------------
  latlong_lens_node = cmds.shadingNode( 'latlong_lens', n='latlong_lens', asUtility=True  ) 

  # Primary lens shader connection:
  # Connect to the .miLensShaderList[0] input on the camera
  # cmds.connectAttr( latlong_lens_node+'.message', cameraShape+'.miLensShaderList[0]' )

  # Alternate lens shader connection:
  # Connect directly to the first .miLensShader input on the camera
  # Note: This first lens shader connection is overwritten by the mental ray Sun & Sky system
  cmds.connectAttr( latlong_lens_node+'.message', cameraShape+'.miLensShader' )

  # Scale the stereo camera rig locator larger 
  #cmds.setAttr(cameraShape+'.locatorScale', 1) #Scale Camera icon

  # Link the new attribute 'Cam Locator Scale' to the dome camera's locator size control
  cmds.addAttr( cameraName[0], longName='Cam_Locator_Scale', niceName='Cam Locator Scale', attributeType='double', defaultValue=1.0, minValue=0.001)
  cmds.setAttr( cameraName[0]+'.Cam_Locator_Scale', keyable=False, channelBox=True)
  cmds.connectAttr ( cameraName[0]+'.Cam_Locator_Scale', cameraShape+'.locatorScale', force=True)


  cmds.setAttr( cameraName[0]+'.rotateX', 0)
  cmds.setAttr( cameraName[0]+'.rotateY', 0)
  cmds.setAttr( cameraName[0]+'.rotateZ', 0)

  # Changes the render settings to set the stereo camera to be a renderable camera
  cmds.setAttr( cameraShape+'.renderable', 1) #latlong_CameraShape
  cmds.setAttr( 'topShape.renderable', 0)
  cmds.setAttr( 'sideShape.renderable', 0)
  cmds.setAttr( 'frontShape.renderable', 0)
  cmds.setAttr( 'perspShape.renderable', 0)

  #Set up the default mental ray AA sampling quality
  setDomeSamplingQuality()

  # ---------------------------------------------------------------------
  # Setup the stereo rig camera attributes
  # ---------------------------------------------------------------------
  # 4 mm focal length = 160 degree FOV
  #cmds.setAttr( cameraShape+'.focalLength', 4 )

  # 18 mm focal length = 90 degree FOV
  cmds.setAttr( cameraShape+'.focalLength', 18 )


"""
Domemaster3D Fulldome Stereo Rig
--------------------------------
A python function to create a fulldome stereo rig in Maya.
"""

def createLatLongStereoRig():
  import maya.cmds as cmds
  import maya.mel as mel
  
  # ---------------------------------------------------------------------
  # Setup the default Maya / Mental Ray Settings
  # ---------------------------------------------------------------------
  cmds.loadPlugin( "stereoCamera", qt=True )
  
  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()

  # ---------------------------------------------------------------------
  # Create the stereo rig
  # ---------------------------------------------------------------------
  
  #import maya.app.stereo.stereoCameraMenus as stereoCameraMenus
  #stereoCameraMenus.buildCreateMenu()
  #import maya.app.stereo.stereoCameraRig
  #maya.app.stereo.stereoCameraRig.createStereoCameraRig()
  
  from maya.app.stereo import stereoCameraRig
  rig = stereoCameraRig.createStereoCameraRig('LatLongStereoCamera')
  #[u'LatLongCamera', u'LatLongCameraLeft', u'LatLongCameraRight']
  
  #Get the stereo camera rig shape nodes for the center/right/left cameras
  rig_center_shape_name =  getObjectShapeNode(rig[0])
  #[u'stereoCameraCenterCamShape', u'stereoCameraFrustum'] #

  rig_left_shape_name =  getObjectShapeNode(rig[1])
  # Result: [u'stereoCameraLeftShape'] #

  rig_right_shape_name =  getObjectShapeNode(rig[2])
  # Result: [u'stereoCameraRightShape'] #
  
  """
  cmds.setAttr( rig[0]+'.rotateX', 90)
  cmds.setAttr( rig[0]+'.rotateY', 0)
  cmds.setAttr( rig[0]+'.rotateZ', 0)
  
  """
  
  # Changes the render settings to set the stereo camera to be a renderable camera
  cmds.setAttr( rig_left_shape_name[0]+'.renderable', 1) #stereoCameraLeftShape
  cmds.setAttr( rig_right_shape_name[0]+'.renderable', 1) #stereoCameraRightShape
  cmds.setAttr( 'topShape.renderable', 0)
  cmds.setAttr( 'sideShape.renderable', 0)
  cmds.setAttr( 'frontShape.renderable', 0)
  cmds.setAttr( 'perspShape.renderable', 0)

  #Set up the default mental ray AA sampling quality
  setDomeSamplingQuality()
  
  #import maya.cmds as cmds
  #rig_center_shape_name =  getObjectShapeNode(rig[0])
  #lensShaderName = cmds.listConnections( rig_center_shape_name[0]+'.miLensShader')

  #Debugging test line
  #lensShaderName = "center_domeAFL_FOV_Stereo";
  #print ("Lens shader name: " + str(lensShaderName))
  
  # Select the center camera's domeAFL_FOV_Stereo node
  #cmds.select(lensShaderName, replace=True)
  
  leftLensShader = cmds.listConnections(rig_left_shape_name[0]+'.miLensShader')
  rightLensShader = cmds.listConnections(rig_right_shape_name[0]+'.miLensShader')
  centerLensShader = cmds.listConnections(rig_center_shape_name[0]+'.miLensShader')
  
  #Select the camera's domeAFL_FOV_Stereo nodes in the attribute editor to add the Extra Attrs
  #mel.eval ( ' showEditorExact("' + centerLensShader[0] + '") ' )
  mel.eval ( ' showEditorExact("' + leftLensShader[0] + '") ' )
  mel.eval ( ' showEditorExact("' + rightLensShader[0] + '") ' )
  
  #Finish off by reselecting the center lens shader
  mel.eval ( ' showEditorExact("' + centerLensShader[0] + '") ' )
  
  #---------------------------------------------------------------------------
  # Enable Real-time 3D in the OpenGL viewport 
  # using a PreRender and PostRender MEL script
  #---------------------------------------------------------------------------
  #import maya.cmds as cmds

  #PreRender MEL:
  cmds.setAttr( 'defaultRenderGlobals.preMel', "source \"domeRender.mel\"; domemaster3DPreRenderMEL();", type='string')
  #PostRender MEL:
  cmds.setAttr( 'defaultRenderGlobals.postMel' , "source \"domeRender.mel\"; domemaster3DPostRenderMEL();", type='string')

  #enable realtime 3D
  mel.eval("source \"domeRender.mel\"; domemaster3DPostRenderMEL();");
  
  return rig



"""
Domemaster3D DomeGrid test background 
--------------------------------------
A python function to create a hemispherical yellow test grid in Maya. 

"""

#Suggested Maya Scene Grid Settings:
#length and width: 360 units
#Grid lines every: 180 units
#Subdivisions: 2

def createDomeGrid():
  import maya.cmds as cmds
  import maya.mel as mel
  
  #---------------------------------------------------------------------------
  # Variables
  #---------------------------------------------------------------------------
  
  #Reference Grid Meshes
  #domeGridSurface = 'domeGridSurface'
  domeGridSurface = 'domeGridSurface'
  domeGridlineSurface = 'domeGridlineSurface'
  
  #Set the diameter of the dome shape
  startingDomeDiameter = 360
  
  #---------------------------------------------------------------------------
  # Remove any existing domeGrid elements
  #---------------------------------------------------------------------------
  
  #---------------------------------------------------------------------------
  #Remove old geometry and paint effects nodes
  #---------------------------------------------------------------------------
  
  if cmds.objExists('domeGrid'): 
    print('Removing existing Domemaster3D object: domeGrid')
    cmds.select( 'domeGrid', replace=True)
    cmds.delete()

  if cmds.objExists('MeshGroup'): 
    print('Removing existing Domemaster3D object: MeshGroup')
    cmds.select( 'MeshGroup', replace=True)
    cmds.delete() 
  
  if cmds.objExists(domeGridSurface): 
    print('Removing existing Domemaster3D object: ' + domeGridSurface)
    cmds.select( domeGridSurface, replace=True)
    cmds.delete()
  
  if cmds.objExists('domeGridToon'): 
    print('Removing existing Domemaster3D object: domeGridToon')
    cmds.select( 'domeGridToon', replace=True)
    cmds.delete()
    
  if cmds.objExists('domeGrid_displayModeExpr'): 
    print('Removing existing Domemaster3D object: domeGrid_displayModeExpr')
    cmds.select( 'domeGrid_displayModeExpr', replace=True)
    cmds.delete()
  
  #--------------------------------------------------------------------------
  #Remove old dome Grid surface materials
  #---------------------------------------------------------------------------
  
  if cmds.objExists('domeGridLinesSurfaceShader'): 
    print('Removing existing Domemaster3D object: domeGridLinesSurfaceShader')
    cmds.select( 'domeGridLinesSurfaceShader', replace=True)
    cmds.delete()
  
  if cmds.objExists('domeGridLinesSurfaceShaderSG'): 
    print('Removing existing Domemaster3D object: domeGridLinesSurfaceShaderSG')
    cmds.select( 'domeGridLinesSurfaceShaderSG', replace=True)
    cmds.delete()
  
  if cmds.objExists('domeGridSurfaceShaderSG'): 
    print('Removing existing Domemaster3D object: domeGridSurfaceShaderSG')
    cmds.select( 'domeGridSurfaceShaderSG', replace=True)
    cmds.delete()
    
  if cmds.objExists('domeGridSurfaceShader'): 
    print('Removing existing Domemaster3D object: domeGridSurfaceShader')
    cmds.select( 'domeGridSurfaceShader', replace=True)
    cmds.delete()
  
  #--------------------------------------------------------------------------
  #Protect any existing surface shaders from the painf effects node
  #---------------------------------------------------------------------------
    
  if cmds.objExists('surfaceShader1SG'): 
    print('Renaming existing  object: surfaceShader1SG')
    cmds.rename( 'surfaceShader1SG', 'aSurfaceShader1SG' )
    
  if cmds.objExists('surfaceShader1'): 
    print('Renaming existing  object: surfaceShader1')
    cmds.rename( 'surfaceShader1', 'aSurfaceShader1' )
  
  #--------------------------------------------------------------------------
  # Make the dome mesh
  #--------------------------------------------------------------------------
  
  #-----------------------------------------------------------------------------
  #Create a hybrid NURBS/Polygon Paint effects Toon Surface
  #-----------------------------------------------------------------------------

  startingCurveRadius = 1.0
  
  #startingToonThickness = 0.1
    
  #Create the base curve with a 90 degree arc
  domeRadiusCurveName = cmds.circle(name='domeGridSurfaceCurve', c=(0, 0, 0), nr=(0, 0, 1), sw=90, r=startingCurveRadius, d=3, ut=0, tol=0.01, s=10, ch=1)

  #Get the curve's shape node name
  domeCurveShape = getObjectShapeNode(domeRadiusCurveName[0])

  #Setup the NURBS to Poly conversion prefs
  #nurbsToPolygonsPref -q -f;
  cmds.nurbsToPolygonsPref(format=3, uType=3, uNumber=1, vType=3, vNumber=1)

  """
  #MEL Code to debug NURBS to polygon conversion:
  int $f = `nurbsToPolygonsPref -q -f`;
  int $ut = `nurbsToPolygonsPref -q -ut`;
  int $un = `nurbsToPolygonsPref -q -un`;
  int $vt = `nurbsToPolygonsPref -q -vt`;
  int $vn = `nurbsToPolygonsPref -q -vn`;
  print ($f + " " + $ut + " " + $un+ " " + $vt+ " " + $vn);
  """

  #Revolve the base 90 degree arc curve into a NURBS dome shape
  domeRadiusSurfaceName = cmds.revolve(domeCurveShape, name='domeGridSurface', ch=1, po=0, rn=0, ssw=0, esw=360, ut=0, tol=0.01, degree=3, s=40, ulp=1, ax=(0, 1, 0), polygon=1)

  domeSurfaceShape = getObjectShapeNode(domeRadiusSurfaceName[0]);

  print "\nDome Preview elements:"
  print domeRadiusSurfaceName
  print "Dome Preview shape node:"
  print domeSurfaceShape
  print "\n"

  #Find out the preview curve's makeNurbCircle node name
  makeCurveShapeName = domeCurveShape
  makeCurveObject = cmds.listConnections( makeCurveShapeName[0]+'.create', type='makeNurbCircle')
  makeCurveNodeName = makeCurveObject[0]
  print("The NURBS circle creation node is: ")
  print(makeCurveNodeName)

  #-----------------------------------------------------------------------------
  #Make the NURBS Curve able to be moved without effecting the revolves
  #-----------------------------------------------------------------------------
      
  #Find out the name of the "makeNurbCircle" node that is used to create the domeGridPreviewCurve shape
  makeRevolveObjects= cmds.listConnections(  makeCurveShapeName[0]+'.worldSpace', type='revolve')
  makeRevolveNodeName = makeRevolveObjects[0];
  print("The circle creation node is: ")
  print(makeRevolveNodeName)

  #Reconnect the curve to the revolve node using local space
  #This replaces the curve's previous .worldSpace connection that inhibited the
  #ability to move the curve without effecting the revolve
  cmds.connectAttr( makeCurveShapeName[0]+".local", makeRevolveNodeName+".inputCurve",  f=True);

  #Put the domeSurface "PreviewShape" inside the domeGrid group
  #Have the revolved shape aligned relative to the domeGrid
  #cmds.parent(domeRadiusSurfaceName[0], domeRadiusTransform)

  #Parent the NURBS revolve curve to the domeGrid
  #cmds.parent(domeRadiusCurveName[0], domeRadiusTransform)
  
  #Create the base sphere with a 1 unit scale
  #domeGridName = cmds.polySphere( name=domeGridSurface, radius = 1, subdivisionsX=36, subdivisionsY=20, axis=(0, 1, 0),  createUVs=2, constructionHistory=True )
  
  #Chop the polysphere into a hemispherical dome
  #domeGridTransform = domeGridName[0]
  #domeGridShape = getObjectShapeNode( domeGridName[0] )
  #cmds.select( domeGridTransform+'.f[0:323]', domeGridTransform+'.f[648:683]', replace=True )
  #cmds.delete()
  
  domeGridTransform = domeRadiusSurfaceName[0];
  
  #Make the curve an intermediate shape
  cmds.setAttr(domeCurveShape[0]+'.intermediateObject', 1)

  #Tell the domeGridSurface to move with the domeGrid group node
  cmds.setAttr(domeGridTransform+'.inheritsTransform', 1)
  
 
  #---------------------------------------------------------------------------
  # Create the PaintFX Toon stroke outlines
  # --------------------------------------------------------------------------
  
  cmds.select( domeGridTransform, replace=True )
  
  #Assign the paint effects toon outlines
  mel.eval('assignNewPfxToon;')
  
  #rename the toon shader
  domeToonShader = 'domeGridToon'
  domeToonShaderShape = 'domeGridToonShape'
  cmds.rename( 'pfxToon1', domeToonShader )
  
  #Define the new toon shader controls
  cmds.setAttr( domeToonShaderShape+'.profileLines', 0 )
  cmds.setAttr( domeToonShaderShape+'.borderLines', 0 )
  cmds.setAttr( domeToonShaderShape+'.creaseLineWidth', 15 )
  cmds.setAttr( domeToonShaderShape+'.creaseColor', 1, 1, 0, type='double3' )
  cmds.setAttr( domeToonShaderShape+'.hardCreasesOnly', 0 )
  cmds.setAttr( domeToonShaderShape+'.creaseBreakAngle', 0 )
  cmds.setAttr( domeToonShaderShape+'.creaseAngleMin', 0 )
  cmds.setAttr( domeToonShaderShape+'.creaseAngleMax', 0 )
  cmds.setAttr( domeToonShaderShape+'.meshVertexColorMode', 1 )
  cmds.setAttr( domeToonShaderShape+'.meshQuadOutput', 1 )
  cmds.setAttr( domeToonShaderShape+'.meshHardEdges', 1 )
  
  #Create a polygon paint effects stroke output
  cmds.select( domeToonShader, replace=True );
  mel.eval('doPaintEffectsToPoly( 1,1,1,1,100000);')
  
  #Make a local space mesh connection to fix the grouped node double translation issue
  #connectAttr -f domeGridToonShape.outMainMesh MainShape.inMesh;
  #Result: Connected domeGridToonShape.outMainMesh to MainShape.inMesh. // 
  cmds.connectAttr( domeToonShaderShape+'.outMainMesh', 'MainShape.inMesh', force=True)
  
  if cmds.objExists('MeshGroup'): 
    print('Unlinking the Toon shader\'s inheritsTransform attribute')
    cmds.setAttr( 'MeshGroup.inheritsTransform', 0)
  
  # --------------------------------------------------------------------------
  #Adjust the grid lines shader
  #---------------------------------------------------------------------------
  
  #domeGridlineShadingGroup = cmds.sets( renderable=True, noSurfaceShader=True, empty=True, name='domeGridLinesSurfaceShaderSG' )
  domeGridlineMaterial = 'domeGridLinesSurfaceShader'
  domeGridlineShadingGroup  = 'domeGridLinesSurfaceShaderSG'
  
  #Rename the default gridlines shader
  cmds.rename( 'surfaceShader1', domeGridlineMaterial )
  cmds.rename( 'surfaceShader1SG', domeGridlineShadingGroup )
  
  #Standard Yellow Color
  #cmds.setAttr( 'surfaceShader1.outColor', 1, 1, 0, type='double3')
  
  #Super Bright Yellow Color for Physical Sky Compatibility
  cmds.setAttr(domeGridlineMaterial+'.outColor', 15, 15, 0, type='double3')
  
  #---------------------------------------------------------------------------
  #Adjust the grid surface shader
  #---------------------------------------------------------------------------
  
  #Create the dome Grid surface shader + shading group
  domeGridShadingGroup = cmds.sets( renderable=True, noSurfaceShader=True, empty=True, name='domeSurfaceShaderSG' )
  domeGridMaterial = cmds.shadingNode( 'surfaceShader', name='domeGridSurfaceShader', asShader=True) 
  
  #Make the surface shader black
  cmds.setAttr( domeGridMaterial+'.outColor', 0, 0, 0, type='double3')
  #Set the polygon surface to be transparent
  cmds.setAttr( domeGridMaterial+'.outTransparency', 1, 1, 1, type='double3')
  
  #Connect the surface shader to the shading group and the polygon surface
  cmds.connectAttr(domeGridMaterial+'.outColor', domeGridShadingGroup+'.surfaceShader')
  cmds.select(domeGridSurface)
  cmds.hyperShade(assign=domeGridShadingGroup)

  #---------------------------------------------------------------------------
  #Group the domeGrid surfaces under a node called "domeGrid"
  #---------------------------------------------------------------------------
  #cmds.group( 'domeGridSurface', 'domeGridToon', 'MeshGroup', name='domeGrid' )
  cmds.group( domeRadiusCurveName[0], domeRadiusSurfaceName[0], 'domeGridToon', 'MeshGroup', name='domeGrid' )
  #        
  #---------------------------------------------------------------------------
  # Add Extra Attrs to the domeGrid shape
  #---------------------------------------------------------------------------
  baseNodeName = 'domeGrid'
    
  #---------------------------------------------------------------------------  
  #Add a Field of View control to the domeGrid's transform node
  #---------------------------------------------------------------------------
  attrName = 'fieldOfView'

  #Check if the attribute exists on the domeGrid node
  #if(mel.attributeExists(attrName, baseNodeName) == 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="double", min=0.1, max=360, defaultValue=180 , keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  #---------------------------------------------------------------------------  
  #Add a Field of View expression
  #---------------------------------------------------------------------------
  
  #Connect the domeGrid dome radius control to the sphere's makeNurbCircle radius attribute
  expressionBuilderString = makeCurveNodeName + ".sweep = " + (baseNodeName+'.'+attrName) + "/2;"
  gridFOVRadiusExpressionName = 'domeGrid_FOVExpr'
  
  print "DomeGrid FOV Extra Attribute Expressions:"
  print expressionBuilderString

  cmds.expression( name=gridFOVRadiusExpressionName, string=expressionBuilderString, object=baseNodeName, alwaysEvaluate=True, unitConversion=all)
  
  #Connect the domeGrid dome radius control to the sphere's makeNurbCircle radius attribute:
  #cmds.connectAttr( (baseNodeName+'.'+attrName), makeCurveObject[0]+'.sweep', force=True)
    

  #---------------------------------------------------------------------------  
  #Add a dome Radius control to the domeGrid's transform node
  #---------------------------------------------------------------------------
  attrName = 'Dome_Radius'

  #Check if the attribute exists on the domeGrid node
  #if(mel.attributeExists(attrName, baseNodeName) == 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="double", min=0.1, max=1000000, hasSoftMaxValue=True, softMaxValue=360, defaultValue=startingDomeDiameter , keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  #Connect the domeGrid dome radius control to the sphere's makeNurbCircle radius attribute:
  cmds.connectAttr( (baseNodeName+'.'+attrName), makeCurveObject[0]+'.radius', force=True)

  #---------------------------------------------------------------------------  
  #Add a Dome Height Spans control to the domeGrid's transform node
  #---------------------------------------------------------------------------
  attrName = 'Dome_Spans'

  #Check if the attribute exists on the domeGrid node
  #if(mel.attributeExists(attrName, baseNodeName) == 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="double", min=4, max=120, hasSoftMaxValue=True, softMaxValue=40, defaultValue=12 , keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  #Connect the domeGrid dome radius control to the sphere's makeNurbCircle sections attribute:
  cmds.connectAttr( (baseNodeName+'.'+attrName), makeCurveObject[0]+'.sections', force=True)
    
  #---------------------------------------------------------------------------  
  #Add a Dome Width Sections control to the domeGrid's transform node
  #---------------------------------------------------------------------------
  attrName = 'Dome_Sections'

  #Check if the attribute exists on the domeGrid node
  #if(mel.attributeExists(attrName, baseNodeName) == 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="double", min=4, max=240, hasSoftMaxValue=True, softMaxValue=120, defaultValue=42 , keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  #Connect the domeGrid dome radius control to the sphere's revolve sections attribute:
  cmds.connectAttr( (baseNodeName+'.'+attrName), makeRevolveNodeName+'.sections', force=True)
  
  #---------------------------------------------------------------------------
  #Add a Display Mode control to the domeGrid's transform node
  #---------------------------------------------------------------------------
  attrName = 'displayMode'
  #if(mel.attributeExists(attrName, baseNodeName) == 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="enum", en="Off:Wireframe:Shaded:Wireframe on Shaded", defaultValue=2, keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  #---------------------------------------------------------------------------
  #Add a Double Sided Rendering control to the domeGrid's transform node
  #---------------------------------------------------------------------------
  attrName = 'doubleSidedShading'
  #if(mel.attributeExists(attrName, baseNodeName) == 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="enum", en="Double Sided:Show Frontfaces:Show Backfaces", defaultValue=2, min=0, keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  #---------------------------------------------------------------------------
  #Add a Grid Line Thickness control to the domeGrid's transform node
  #---------------------------------------------------------------------------
  attrName = 'gridLineThickness'

  #This is the default starting value for the grid line strokes
  initialGridLineThickness = 0.05
  #previous setting 0.035

  #Check if the attribute exists on the domeGrid node
  #if(mel.attributeExists(attrName, baseNodeName) == 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="double", min=0.001, max=50, hasSoftMaxValue=True, softMaxValue=2, defaultValue=initialGridLineThickness, keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  #Connect the domeGrid Grid Line Thickness to the toon shader line width attribute:
  cmds.connectAttr( (baseNodeName+'.'+attrName), domeToonShaderShape+'.lineWidth', force=True)

  #---------------------------------------------------------------------------
  #Add a Grid Line Color control to the domeGrid's transform node - Default color 1,1,0 = Yellow
  #---------------------------------------------------------------------------
  attrName = 'gridLineColor'
  attrRName = "gridLineColorR";
  attrGName = "gridLineColorG";
  attrBName = "gridLineColorB";
  #if(mel.attributeExists(attrName, baseNodeName) == 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="float3", usedAsColor=True, keyable=True)
  cmds.addAttr(baseNodeName, parent=attrName, longName=attrRName, attributeType="float", keyable=True, defaultValue=15)
  cmds.addAttr(baseNodeName, parent=attrName, longName=attrGName, attributeType="float", keyable=True, defaultValue=15)
  cmds.addAttr(baseNodeName, parent=attrName, longName=attrBName, attributeType="float", keyable=True, defaultValue=0)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  #Connect the Grid Line Color swatch to the surface shader
  cmds.connectAttr( (baseNodeName+'.'+attrName), domeGridlineMaterial+'.outColor', force=True)
  #---------------------------------------------------------------------------
  #Add a Grid Line Transparency control to the domeGrid's transform node - Default value 0.25
  #---------------------------------------------------------------------------
  attrName = 'gridLineTransparency'
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="double", keyable=True, defaultValue=0.0, min=0, max=1)
  
  #Connect the Grid Line transparency swatch to the surface shader
  cmds.connectAttr( (baseNodeName+'.'+attrName), domeGridlineMaterial+'.outTransparencyR', force=True)
  cmds.connectAttr( (baseNodeName+'.'+attrName), domeGridlineMaterial+'.outTransparencyG', force=True)
  cmds.connectAttr( (baseNodeName+'.'+attrName), domeGridlineMaterial+'.outTransparencyB', force=True)

  #---------------------------------------------------------------------------
  #Add a Grid Surface Color control to the domeGrid's transform node - Default color 0,0,0 = Black
  #---------------------------------------------------------------------------
  attrName = 'gridSurfaceColor'
  attrRName = "gridSurfaceColorR";
  attrGName = "gridSurfaceColorG";
  attrBName = "gridSurfaceColorB";
  #if(mel.attributeExists(attrName, baseNodeName) == 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="float3", usedAsColor=True, keyable=True)
  cmds.addAttr(baseNodeName, parent=attrName, longName=attrRName, attributeType="float", keyable=True, defaultValue=0)
  cmds.addAttr(baseNodeName, parent=attrName, longName=attrGName, attributeType="float", keyable=True, defaultValue=0)
  cmds.addAttr(baseNodeName, parent=attrName, longName=attrBName, attributeType="float", keyable=True, defaultValue=0)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  
  #Connect the Grid Surface Color swatch to the surface shader
  cmds.connectAttr( (baseNodeName+'.'+attrName), domeGridMaterial+'.outColor', force=True)
  #---------------------------------------------------------------------------
  #Add a Grid Surface Transparency control to the domeGrid's transform node - Default value 0.25
  #---------------------------------------------------------------------------
  attrName = 'gridSurfaceTransparency'
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="double", keyable=True, defaultValue=.5, min=0, max=1)
  
  #Connect the Grid Surface transparency swatch to the surface shader
  cmds.connectAttr( (baseNodeName+'.'+attrName), domeGridMaterial+'.outTransparencyR', force=True)
  cmds.connectAttr( (baseNodeName+'.'+attrName), domeGridMaterial+'.outTransparencyG', force=True)
  cmds.connectAttr( (baseNodeName+'.'+attrName), domeGridMaterial+'.outTransparencyB', force=True)


  #---------------------------------------------------------------------------  
  #Add a display mode expression to the domeGrid's transform node
  #---------------------------------------------------------------------------
  
  domeRadiusTransform =  "domeGrid"
  domeSurfaceShape = "domeGridSurface"
  domeSurfaceShapeNode = getObjectShapeNode(domeSurfaceShape)
  
  
  exprName = ""
  previewAttrName = "displayMode"
  #The expression name is domeGrid_displayModeExpr
  exprName = domeRadiusTransform + "_" + previewAttrName + "Expr"
 
  PreviewShapeExpr = ""

  PreviewShapeExpr += "// Custom " + previewAttrName + " Preview Shape Expressions\n\n"
  PreviewShapeExpr += "if (  " + domeRadiusTransform + "." + previewAttrName + " == 0){\n"
  PreviewShapeExpr += "  //Off Mode\n"
  PreviewShapeExpr += "  " + domeSurfaceShape + ".overrideDisplayType = 2;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideEnabled = 1;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideShading = 0;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".visibility = 0;\n"
  PreviewShapeExpr += "  MeshGroup.visibility = 0;\n"
  PreviewShapeExpr += "} else if (" + domeRadiusTransform + "." + previewAttrName + " == 1 ){\n"
  PreviewShapeExpr += "  //Wireframe Mode\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideEnabled = 1;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideShading = 0;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".visibility = 1;\n"
  PreviewShapeExpr += "  MeshGroup.visibility = 0;\n"
  PreviewShapeExpr += "} else if (" + domeRadiusTransform + "." + previewAttrName + " == 2 ){\n"
  PreviewShapeExpr += "  //Shaded Mode\n"
  PreviewShapeExpr += "  string $currentPanel = \"modelPanel4\";\n"
  PreviewShapeExpr += "  if ( `modelEditor -exists currentPanel` )\n"
  PreviewShapeExpr += "  modelEditor -edit -wireframeOnShaded 0 currentPanel;\n"
  PreviewShapeExpr += "  string $currentPanel = \"StereoPanel\";\n"
  PreviewShapeExpr += "  if ( `modelEditor -exists currentPanel` )\n"
  PreviewShapeExpr += "  modelEditor -edit -wireframeOnShaded 0 currentPanel;\n"
  PreviewShapeExpr += "  " + domeSurfaceShape + ".overrideDisplayType = 2;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideEnabled = 1;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideShading = 1;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".visibility = 1;\n"
  PreviewShapeExpr += "  MeshGroup.visibility = 1;\n"
  PreviewShapeExpr += "} else if (" + domeRadiusTransform + "." + previewAttrName + " == 3 ){\n"
  PreviewShapeExpr += "  //Wireframe on Shaded Mode\n"
  PreviewShapeExpr += "  string $currentPanel = \"modelPanel4\";\n"
  PreviewShapeExpr += "  if ( `modelEditor -exists currentPanel` )\n"
  PreviewShapeExpr += "  modelEditor -edit -wireframeOnShaded 1 currentPanel;\n"
  PreviewShapeExpr += "  string $currentPanel = \"StereoPanel\";\n"
  PreviewShapeExpr += "  if ( `modelEditor -exists currentPanel` )\n"
  PreviewShapeExpr += "  modelEditor -edit -wireframeOnShaded 1 currentPanel;\n"
  PreviewShapeExpr += "  " + domeSurfaceShape + ".overrideDisplayType = 2;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideEnabled = 1;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideShading = 1;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".visibility = 1;\n"
  PreviewShapeExpr += "  MeshGroup.visibility = 1;\n"
  PreviewShapeExpr += "}\n"
  PreviewShapeExpr += "\n"
  PreviewShapeExpr += "\n"

  #---------------------------------------------------------------------------  
  #Add a Double Sided Shading expression to the domeGrid's transform node
  #---------------------------------------------------------------------------

  previewAttrName = "doubleSidedShading";

  PreviewShapeExpr += "// Custom Double Sided Shading Expressions\n\n"
  PreviewShapeExpr += "if (" + previewAttrName + " == 0 ){\n"
  PreviewShapeExpr += "  print(\"Double Sided Shading Enabled\\n\");\n"
  PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".doubleSided\" 1; \n"
  PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".opposite\" 0; \n"
  PreviewShapeExpr += "} else if (" + previewAttrName + " == 1 ){\n"
  PreviewShapeExpr += "  print(\"Backface Shading Enabled\\n\");\n"
  PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".doubleSided\" 0; \n"
  PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".opposite\" 0; \n"
  PreviewShapeExpr += "} else if (" + previewAttrName + " == 2 ){\n"
  PreviewShapeExpr += "  print(\"Frontface Shading Enabled\\n\");\n"
  PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".doubleSided\" 0; \n"
  PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".opposite\" 1; \n"
  PreviewShapeExpr += "}\n"

  print "DomeGrid Extra Attribute Expressions:"
  print PreviewShapeExpr

  cmds.expression( name=exprName, string=PreviewShapeExpr, object='domeGrid', alwaysEvaluate=True, unitConversion=all)

  #Force a first value into the double sided shading attribute
  cmds.setAttr( (domeRadiusTransform+".doubleSidedShading"), 0)
  
  #---------------------------------------------------------------------------  
  # Select the domeGrid node in the Attribute Editor
  #---------------------------------------------------------------------------  
  mel.eval ( ' showEditorExact("' + domeRadiusTransform + '") ' )
  
  
"""
Domemaster3D createTestShapes
----------------------
A python function to create a test sphere and cube in Maya. 
"""

def  createTestShapes():
  import maya.cmds as cmds

  if cmds.objExists('domeTestLight'): 
    print('Removing existing Domemaster3D object: domeTestLight')
    cmds.select( 'domeTestLight', replace=True)
    cmds.delete()

  if cmds.objExists('polyTestSphere'): 
    print('Removing existing Domemaster3D object: polyTestSphere')
    cmds.select( 'polyTestSphere', replace=True)
    cmds.delete()

  if cmds.objExists('polyTestCube'): 
    print('Removing existing Domemaster3D object: polyTestCube')
    cmds.select( 'polyTestCube', replace=True)
    cmds.delete()

  test_sphere_name = cmds.polySphere( name='polyTestSphere', radius=24, subdivisionsX=20, subdivisionsY=20, axis=(0, 1, 0),  createUVs=2, constructionHistory=True)
  cmds.setAttr(test_sphere_name[0]+'.translateX', 80)
  cmds.setAttr(test_sphere_name[0]+'.translateY', 75)

  #Smooth the render time polygon sphere shape
  cmds.displaySmoothness( test_sphere_name, divisionsU=3, divisionsV=3, pointsWire=16, pointsShaded=4, polygonObject=3 )

  test_cube_name = cmds.polyCube( name='polyTestCube', width=40, height=40, depth=40, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=(0, 1, 0),  createUVs=4, constructionHistory=True)
  cmds.setAttr(test_cube_name[0]+'.translateX', 0)
  cmds.setAttr(test_cube_name[0]+'.translateY', 75)
  cmds.setAttr(test_cube_name[0]+'.translateZ', -80)
  cmds.setAttr(test_cube_name[0]+'.rotateX', 88)
  cmds.setAttr(test_cube_name[0]+'.rotateY', 0)
  cmds.setAttr(test_cube_name[0]+'.rotateZ', 0)

  dome_light_shape_name = cmds.directionalLight()
  dome_light_name = getObjectParentNode( dome_light_shape_name )
  dome_light_name = cmds.rename (dome_light_name, "domeTestLight")

  cmds.setAttr( (dome_light_name+'.translateX'), -32)
  cmds.setAttr( (dome_light_name+'.rotateX'), 38)
  cmds.setAttr( (dome_light_name+'.rotateY'), 47)
  cmds.setAttr( (dome_light_name+'.rotateZ'), -62)


"""
Domemaster3D createRobLookup
----------------------
A python function to create a mental ray screen space texture 
and connect it to a robLookupBackground lens shader. 
"""

def createRobLookup():
  import maya.cmds as cmds
  
  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()

  # ---------------------------------------------------------------------
  #Setup the base folder path for the Domemaster3D control maps
  # ---------------------------------------------------------------------
  
  #Variables
  separationMapFileTexture = getSourceImagesPath("separation_map.png")
  print "[Loading Separation Map]: " + separationMapFileTexture 

  # Create a camera and get the shape name.
  cameraName = cmds.camera(name='robLookupCamera')
  cameraShape = cameraName[1]
  
  # ---------------------------------------------------------------------
  # Create the robLookupBackground node
  # ---------------------------------------------------------------------
  rob_lens_node = cmds.shadingNode( 'rob_lookup_background', n='rob_lookup_background', asUtility=True  )
  cmds.connectAttr( rob_lens_node+'.message', cameraShape+'.miLensShader' )
  
  # ---------------------------------------------------------------------
  # Create the custom shading network connections
  # ---------------------------------------------------------------------
  
  # Create the nodes
  rob_map_tex_filter = cmds.shadingNode( 'mib_texture_filter_lookup', n='rob_map_mib_texture_filter_lookup1', asTexture=True)
  
  rob_tex_vector = cmds.shadingNode( 'mib_texture_vector', n='rob_mib_texture_vector1', asUtility=True )
  rob_tex_remap = cmds.shadingNode( 'mib_texture_remap', n='rob_mib_texture_remap1',  asUtility=True)
  
  rob_map_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='rob_map_mentalrayTexture1', asTexture=True)
  
  # Set the node to use mode (4) which is screen space
  cmds.setAttr( rob_tex_vector+'.selspace', 4)
  
  # Connect the nodes
  cmds.connectAttr( rob_map_tex_filter+'.outValueR', rob_lens_node+'.tex' )
  cmds.connectAttr( rob_map_mr_tex+'.message', rob_map_tex_filter+'.tex' )
  
  cmds.connectAttr( rob_tex_vector+'.outValue', rob_tex_remap+'.input' )
  cmds.connectAttr( rob_tex_remap+'.outValue', rob_map_tex_filter+'.coord' )
  
  cmds.setAttr( rob_map_mr_tex+'.fileTextureName', separationMapFileTexture , type="string")


"""
Domemaster3D createDomeRampTexture
----------------------
A python function to create a mental ray screen space ramp texture 
and connect it to a robLookupBackground lens shader.
"""
def createDomeRampTexture():
  import maya.cmds as cmds

  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()
  
  # Create a camera and get the shape name.
  cameraName = cmds.camera(name='robLookupCamera')
  cameraShape = cameraName[1]
  
  # ---------------------------------------------------------------------
  # Create the robLookupBackground node
  # ---------------------------------------------------------------------
  rob_lens_node = cmds.shadingNode( 'rob_lookup_background', n='rob_lookup_background', asUtility=True  )
  cmds.connectAttr( rob_lens_node+'.message', cameraShape+'.miLensShader' )
  
  # ---------------------------------------------------------------------
  # Create the custom shading network connections
  # ---------------------------------------------------------------------
  
  # Create the Ramp node
  # Create the Ramp node
  dome_ramp = cmds.shadingNode( 'ramp', n='domeRamp', asTexture=True) 
  cmds.setAttr( dome_ramp+'.colorEntryList', s=2 )
  cmds.setAttr(dome_ramp+'.colorEntryList[0].ep', 0.5)
  cmds.setAttr( dome_ramp+'.colorEntryList[0].ec', 1, 1, 1, type="float3")
  cmds.setAttr(dome_ramp+'.colorEntryList[2].ep', 0.44999998807907104)
  cmds.setAttr( dome_ramp+'.colorEntryList[2].ec',  0, 0, 0, type="float3")
  
  # Create the texture space conversion node
  rob_tex_vector = cmds.shadingNode( 'mib_texture_vector', n='rob_mib_texture_vector1', asUtility=True )
  
  # Set the node to use mode (4) which is screen space
  cmds.setAttr( rob_tex_vector+'.selspace', 4)
  
  #Connect the texture_vector node to the ramp node using the XY values for the UV coordinates.
  cmds.connectAttr( dome_ramp+'.outColor.outColorR', rob_lens_node+'.tex' )
  cmds.connectAttr( rob_tex_vector+'.outValue.outValueX', dome_ramp+'.uvCoord.uCoord' )
  cmds.connectAttr( rob_tex_vector+'.outValue.outValueY', dome_ramp+'.uvCoord.vCoord' )


"""
A python function to create a mental ray texture and connect it to an mental ray mentalrayIbl node. 

The this function will offset the texture coordinates so a 180 degree fisheye image would sit in the center of the mental ray IBL system's 360 degree angular fisheye input.

The input isMasked variable allows you to choose if you want an alpha channel to be applied to the fulldome image to crop off the outside frame labelling.
"""
def createFulldomeIBL():
  import maya.cmds as cmds
  import maya.mel as mel 
  
  isMasked = 1

  iblDialogString = 'Do you want to have a circular alpha mask applied to the imagery in your fulldome IBL shading network?\n'
  iblDialogString += '\n'
  iblDialogString += 'Note: This is useful for hiding comments written in the border zone of the domemaster frame and will stop them from showing up in the environment map background.'
  
  iblDialogButtonSelected = cmds.confirmDialog( title='FulldomeIBL Creation', message=iblDialogString, button=['Yes','No'], defaultButton='No', cancelButton='No', dismissString='No', icon='question' )

  if(iblDialogButtonSelected == 'Yes'):
    print 'Creating a circular masked FulldomeIBL Shading Network.\n'
    #Masked Domemaster Frame Boundary input = 1
    isMasked = 1
  else:
    print 'Creating a regular FulldomeIBL Shading Network.\n'
    #UnMasked Domemaster Frame Boundary input = 0
    isMasked = 0

  #Check if we are running Maya 2015+ and then enable the emit light mode
  mayaVersion = getMayaVersionDome()
  # ---------------------------------------------------------------------
  #Setup the base folder path for the Domemaster3D control maps
  # ---------------------------------------------------------------------

  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()

  #Remove old mental ray IBL Shape nodes
  if cmds.objExists('mentalrayIbl*'):
    cmds.delete('mentalrayIbl*')
    print("Removing the old mentalrayIbl shape.")

  #Add the mental ray miDefaultOptions settings to the scene before accessing MR indirect lighting features
  mel.eval("miCreateDefaultNodes();")

  # Show the render settings window
  #mel.eval("unifiedRenderGlobalsWindow;")

  #Variables
  #iblMapFileTexture = ""
  #iblMapFileTexture = getSourceImagesPath("fulldome_2K.jpg")
  iblMapFileTexture = getSourceImagesPath("fulldomeAlignmentGrid_4k.png")
  print "[Loading IBL Map]: " + iblMapFileTexture

  #Create the alpha domemaster frame mask
  if(isMasked):
    domeMaskMapFileTexture = getSourceImagesPath("domemaster_mask.png")
    print "[Loading Domemaster Circular Mask Map]: " + domeMaskMapFileTexture

  # ---------------------------------------------------------------------
  # Create the mentalrayIblShape node
  # ---------------------------------------------------------------------
  # miCreateIbl is found in: 
  # C:\Program Files\Autodesk\mentalrayForMaya2015\scripts\createMentalRayIndirectLightingTab.mel
  # C:/Users/<User Account>/Documents/maya/2015-x64/prefs/scripts/createMentalRayIndirectLightingTab.mel

  #import maya.mel as mel 
  mel.eval("source \"createMentalRayIndirectLightingTab.mel\";")
  mel.eval("miCreateIbl();")

  #Find the name of the new IBL shape  

  #Hardcoded IBL testing names
  #iblTransformName = 'mentalrayIbl1'
  #iblShapeName = 'mentalrayIblShape1'

  #Search the scene for Mental ray IBL shapes
  iblNodeList = cmds.ls( 'mentalrayIbl*' )
  #print iblNodeList
  #[u'mentalrayIbl1', u'mentalrayIblShape1']
  iblTransformName = iblNodeList[0]
  iblShapeName = iblNodeList[1]

  #Select the mentalrayIbl1 node in the attribute editor
  #This will add the extra attributes to the mentalrayIbl node
  mel.eval ( ' showEditorExact("' + iblShapeName + '") ' )
  
  # ---------------------------------------------------------------------
  # Create the custom shading network connections
  # ---------------------------------------------------------------------

  # Create the nodes
  #dome_map_tex_filter = cmds.shadingNode( 'mib_texture_filter_lookup', n='dome_map_mib_texture_filter_lookup1', asTexture=True)
  dome_map_tex_filter = cmds.shadingNode( 'mib_texture_lookup', n='dome_map_mib_texture_lookup1', asTexture=True)
  dome_tex_vector = cmds.shadingNode( 'mib_texture_vector', n='dome_mib_texture_vector1', asUtility=True )
  dome_tex_remap = cmds.shadingNode( 'mib_texture_remap', n='dome_mib_texture_remap1',  asUtility=True)
  dome_map_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='dome_map_mentalrayTexture1', asTexture=True)
  dome_remap_color = cmds.shadingNode( 'remapColor', n='dome_remapColor1', asTexture=True)

  #Create the alpha domemaster frame mask
  if(isMasked):
    dome_mask_map_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='dome_mask_mentalrayTexture1', asTexture=True)
    dome_mask_tex_filter = cmds.shadingNode( 'mib_texture_lookup', n='dome_mask_mib_texture_lookup1', asTexture=True)

    dome_mask_multiply = cmds.shadingNode( 'multiplyDivide', n='dome_mask_multiply', asUtility=True)

  # Connect the nodes
  #RGB Domemaster Texture Map
  cmds.setAttr( dome_map_mr_tex+'.fileTextureName', iblMapFileTexture , type="string")
  #cmds.setAttr( dome_map_mr_tex+'.fileTextureName', '' , type="string")

  #Create the alpha domemaster frame mask
  if(isMasked):
    #Circular Domemaster Mask Texture Map
    cmds.setAttr( dome_mask_map_mr_tex+'.fileTextureName', domeMaskMapFileTexture , type="string")
    #cmds.setAttr( dome_mask_tex_filter+'.fileTextureName', '' , type="string")


  #Set the IBL mapping to "angular"
  cmds.setAttr( iblShapeName+'.mapping', 1)

  #Set the IBL image type to "texture"
  cmds.setAttr( iblShapeName+'.type',  1)

  #Connect the rest of the MR texture shading network
  #RGB Domemaster Map
  cmds.connectAttr( dome_map_mr_tex+'.message', dome_map_tex_filter+'.tex' )
  cmds.connectAttr( dome_tex_vector+'.outValue', dome_tex_remap+'.input' )
  cmds.connectAttr( dome_tex_remap+'.outValue', dome_map_tex_filter+'.coord' )

  #Create the alpha domemaster frame mask
  if(isMasked):
    #Circular Domemaster Mask Map
    cmds.connectAttr( dome_mask_map_mr_tex+'.message', dome_mask_tex_filter+'.tex' )
    cmds.connectAttr( dome_tex_remap+'.outValue', dome_mask_tex_filter+'.coord' )

    #Create a multiply divide node to comp the alpha mask texture over the fulldome image.
    cmds.connectAttr( dome_mask_tex_filter+'.outValue', dome_mask_multiply+'.input1')
    cmds.connectAttr( dome_map_tex_filter+'.outValue', dome_mask_multiply+'.input2')

    #Create the alpha domemaster frame mask
    #Apply a composited fulldome mask over the domemaster RGB image
    cmds.connectAttr( dome_mask_multiply+'.output', dome_remap_color+'.color' )
  else:
    #Skip the domemaster mask and just apply the raw RGB image
    cmds.connectAttr( dome_map_tex_filter+'.outValue', dome_remap_color+'.color' )


  #Connect the mr material to the ibl texture input

  #Connect the remapColor node between the mib_texture_lookup and mentalrayIblShape1 nodes
  cmds.connectAttr( dome_remap_color+'.outColor', iblShapeName+'.color' )
  # or
  #Skip the remapColor node and connect mib_texture_lookup.OutValue > mentalrayIblShape1.color
  #cmds.connectAttr( dome_map_tex_filter+'.outValue', iblShapeName+'.color' )


  #Scale the texture to fit a 180 degree angular fisheye in the IBL nodes' 360 degree fisheye image space
  cmds.setAttr(dome_tex_remap+'.minX', -0.5)
  cmds.setAttr(dome_tex_remap+'.minY', -0.5)
  cmds.setAttr(dome_tex_remap+'.minZ', 0)
  cmds.setAttr(dome_tex_remap+'.maxX', 1.5)
  cmds.setAttr(dome_tex_remap+'.maxY', 1.5)
  cmds.setAttr(dome_tex_remap+'.maxZ', 1.0)

  #Set the matrix to use a -1 mirror effect on the transform matrix
  #cmds.setAttr(dome_tex_remap+'.transform',(-1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1),type='matrix')
  #Work around a Maya 2010 Tupple matrix setAttr issue with the above command
  melSetAttrMatrixString = 'setAttr "' + dome_tex_remap + '.transform" -type "matrix" -1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;'
  mel.eval(melSetAttrMatrixString)

  #melSetAttrMatrixString = 'setAttr \\"' + dome_tex_remap + '.transform\\" -type \\"matrix\\" -1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;'
  #melRunString = 'mel.eval("' + melSetAttrMatrixString + '")'
  #print("Mel  string: " + melRunString )
  #cmds.evalDeferred(melRunString)



  """
  if (mayaVersion >= 2015):
    #Run the ENV Light creator attr from:
    #/Applications/Autodesk/mentalrayForMaya2015/scripts/AETemplates/AEmentalrayIblShapeTemplate.mel
    mel.eval('miSetEnvironmentLightingQuality()')
    
    #Set the IBL light emission quality to 0.5
    envLightQuality = 0.5
    cmds.floatSliderGrp('miEnvironmentLightingQualityCtrl',  edit=True, value=envLightQuality )

    #Enable Light Emission
    cmds.setAttr(iblShapeName+'.enableEmitLight', 1)
  """

  #Position the IBL dome shape
  cmds.setAttr(iblTransformName+'.translateX', 0)
  cmds.setAttr(iblTransformName+'.translateY', 0)
  cmds.setAttr(iblTransformName+'.translateZ', 0)
  cmds.setAttr(iblTransformName+'.rotateZ', 0)

  #Right side up
  #cmds.setAttr(iblTransformName+'.rotateX', 90)
  #cmds.setAttr(iblTransformName+'.rotateY', 90)

  #Regular Dome Up Orientation
  cmds.setAttr(iblTransformName+'.rotateX', 90)
  cmds.setAttr(iblTransformName+'.rotateY', 0)

  #Flip the env upside down
  #cmds.setAttr(iblTransformName+'.rotateX', -90)
  #cmds.setAttr(iblTransformName+'.rotateY', 90)
  #Mirror the fulldome camera view with the FlipX command
  #cmds.setAttr(domeAFL_lens_node+'.Flip_Ray_X' ,1)

  """
  # Scale the IBL preview shape to 50 units in size
  cmds.setAttr(iblTransformName+'.scaleX', 50)
  cmds.setAttr(iblTransformName+'.scaleY', 50)
  cmds.setAttr(iblTransformName+'.scaleZ', 50)
  """
  
  # Scale the IBL preview shape to 100 units in size
  cmds.setAttr(iblTransformName+'.scaleX', 100)
  cmds.setAttr(iblTransformName+'.scaleY', 100)
  cmds.setAttr(iblTransformName+'.scaleZ', 100)
  
  #Create Mental Ray Texture Extra Attributes
  import domeMaterial as domeMaterial
  reload(domeMaterial)
  domeMaterial.createMentalrayTextureExtraAttrs(dome_map_mr_tex, iblMapFileTexture)

  #Select the mentalray texture node in the attribute editor
  melRunString = 'import maya.mel as mel \n'
  melRunString += 'mel.eval(\"showEditorExact(\\"' + dome_map_mr_tex + '\\")\")'
  #print("Deferred string: " + melRunString)
  cmds.evalDeferred(melRunString)
  #or
  #mel.eval('showEditorExact("'+ dome_map_mr_tex + '")')

"""
A python function to create a mental ray texture and connect it to an mental ray mentalrayIbl node. 

The this function will offset the texture coordinates so a hemirect/hemi-equirectangular (half height equirectangular image) would sit in at the top of the mental ray IBL system's 360x180 degree spherical input.
"""
def createHemirectIBL():
  import maya.cmds as cmds
  import maya.mel as mel 
  
  #Check if we are running Maya 2015+ and then enable the emit light mode
  mayaVersion = getMayaVersionDome()
  # ---------------------------------------------------------------------
  #Setup the base folder path for the Domemaster3D control maps
  # ---------------------------------------------------------------------

  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()

  #Remove old mental ray IBL Shape nodes
  if cmds.objExists('mentalrayIbl*'):
    cmds.delete('mentalrayIbl*')
    print("Removing the old mentalrayIbl shape.")

  #Add the mental ray miDefaultOptions settings to the scene before accessing MR indirect lighting features
  mel.eval("miCreateDefaultNodes();")

  # Show the render settings window
  #mel.eval("unifiedRenderGlobalsWindow;")

  #Variables
  #iblMapFileTexture = ""
  iblMapFileTexture = getSourceImagesPath("hemirectAlignmentGrid_4x2k.png")
  print "[Loading IBL Map]: " + iblMapFileTexture

  # ---------------------------------------------------------------------
  # Create the mentalrayIblShape node
  # ---------------------------------------------------------------------
  # miCreateIbl is found in: 
  # C:\Program Files\Autodesk\mentalrayForMaya2015\scripts\createMentalRayIndirectLightingTab.mel
  # C:/Users/<User Account>/Documents/maya/2015-x64/prefs/scripts/createMentalRayIndirectLightingTab.mel

  #import maya.mel as mel 
  mel.eval("source \"createMentalRayIndirectLightingTab.mel\";")
  mel.eval("miCreateIbl();")

  #Find the name of the new IBL shape  

  #Hardcoded IBL testing names
  #iblTransformName = 'mentalrayIbl1'
  #iblShapeName = 'mentalrayIblShape1'

  #Search the scene for Mental ray IBL shapes
  iblNodeList = cmds.ls( 'mentalrayIbl*' )
  #print iblNodeList
  #[u'mentalrayIbl1', u'mentalrayIblShape1']
  iblTransformName = iblNodeList[0]
  iblShapeName = iblNodeList[1]

  #Select the mentalrayIbl1 node in the attribute editor
  #This will add the extra attributes to the mentalrayIbl node
  mel.eval ( ' showEditorExact("' + iblShapeName + '") ' )
  
  # ---------------------------------------------------------------------
  # Create the custom shading network connections
  # ---------------------------------------------------------------------

  # Create the nodes
  #dome_map_tex_filter = cmds.shadingNode( 'mib_texture_filter_lookup', n='dome_map_mib_texture_filter_lookup1', asTexture=True)
  dome_map_tex_filter = cmds.shadingNode( 'mib_texture_lookup', n='hemi_map_mib_texture_lookup1', asTexture=True)
  dome_tex_vector = cmds.shadingNode( 'mib_texture_vector', n='hemi_mib_texture_vector1', asUtility=True )
  dome_tex_remap = cmds.shadingNode( 'mib_texture_remap', n='hemi_mib_texture_remap1',  asUtility=True)
  dome_map_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='hemi_map_mentalrayTexture1', asTexture=True)
  dome_remap_color = cmds.shadingNode( 'remapColor', n='hemi_remapColor1', asTexture=True)

  # Connect the nodes
  cmds.setAttr( dome_map_mr_tex+'.fileTextureName', iblMapFileTexture , type="string")
  #cmds.setAttr( dome_map_mr_tex+'.fileTextureName', '' , type="string")

  #Set the IBL mapping to "spherical"
  cmds.setAttr( iblShapeName+'.mapping', 0)

  #Set the IBL image type to "texture"
  cmds.setAttr( iblShapeName+'.type',  1)


  #Connect the image to the IBL

  #Connect the mr material to the IBL texture input

  #Skip the remapColor node and connect mib_texture_lookup.OutValue > mentalrayIblShape1.color
  #cmds.connectAttr( dome_map_tex_filter+'.outValue', iblShapeName+'.color' )

  #Connect the remapColor node between the mib_texture_lookup and mentalrayIblShape1 nodes
  cmds.connectAttr( dome_map_tex_filter+'.outValue', dome_remap_color+'.color' )
  cmds.connectAttr( dome_remap_color+'.outColor', iblShapeName+'.color' )

  #Connect the rest of the MR texture shading network
  cmds.connectAttr( dome_map_mr_tex+'.message', dome_map_tex_filter+'.tex' )
  cmds.connectAttr( dome_tex_vector+'.outValue', dome_tex_remap+'.input' )
  cmds.connectAttr( dome_tex_remap+'.outValue', dome_map_tex_filter+'.coord' )

  
  #Scale the texture to fit a half-height latlong image to the top of a spherical image space in the IBL nodes' 360x180 degree spherical image space
  cmds.setAttr(dome_tex_remap+'.minX', 0)
  cmds.setAttr(dome_tex_remap+'.minY', 0)
  cmds.setAttr(dome_tex_remap+'.minZ', 0)
  cmds.setAttr(dome_tex_remap+'.maxX', 1)
  cmds.setAttr(dome_tex_remap+'.maxY', 2)
  cmds.setAttr(dome_tex_remap+'.maxZ', 1)
  cmds.setAttr(dome_tex_remap+'.offsetX', 0)
  cmds.setAttr(dome_tex_remap+'.offsetY', -1)
  cmds.setAttr(dome_tex_remap+'.offsetZ', 0)


  #Set the matrix to use a -1 mirror effect on the transform matrix
  #cmds.setAttr(dome_tex_remap+'.transform',(-1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1),type='matrix')
  #Work around a Maya 2010 Tupple matrix setAttr issue with the above command
  melSetAttrMatrixString = 'setAttr "' + dome_tex_remap + '.transform" -type "matrix" -1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;'
  mel.eval(melSetAttrMatrixString)

  #melSetAttrMatrixString = 'setAttr \\"' + dome_tex_remap + '.transform\\" -type \\"matrix\\" -1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;'
  #melRunString = 'mel.eval("' + melSetAttrMatrixString + '")'
  #print("Mel  string: " + melRunString )
  #cmds.evalDeferred(melRunString)

  """
  if (mayaVersion >= 2015):
    #Run the ENV Light creator attr from:
    #/Applications/Autodesk/mentalrayForMaya2015/scripts/AETemplates/AEmentalrayIblShapeTemplate.mel
    mel.eval('miSetEnvironmentLightingQuality()')
    
    #Set the IBL light emission quality to 0.5
    envLightQuality = 0.5
    cmds.floatSliderGrp('miEnvironmentLightingQualityCtrl',  edit=True, value=envLightQuality )

    #Enable Light Emission
    cmds.setAttr(iblShapeName+'.enableEmitLight', 1)
  """

  #Position the IBL dome shape
  cmds.setAttr(iblTransformName+'.translateX', 0)
  cmds.setAttr(iblTransformName+'.translateY', 0)
  cmds.setAttr(iblTransformName+'.translateZ', 0)
  cmds.setAttr(iblTransformName+'.rotateZ', 0)

  #Regular Dome Up Orientation
  cmds.setAttr(iblTransformName+'.rotateX', 0)
  cmds.setAttr(iblTransformName+'.rotateY', 0)


  """
  # Scale the IBL preview shape to 50 units in size
  cmds.setAttr(iblTransformName+'.scaleX', 50)
  cmds.setAttr(iblTransformName+'.scaleY', 50)
  cmds.setAttr(iblTransformName+'.scaleZ', 50)
  """
  
  # Scale the IBL preview shape to 100 units in size
  cmds.setAttr(iblTransformName+'.scaleX', 100)
  cmds.setAttr(iblTransformName+'.scaleY', 100)
  cmds.setAttr(iblTransformName+'.scaleZ', 100)
  
  #Create Mental Ray Texture Extra Attributes
  import domeMaterial as domeMaterial
  reload(domeMaterial)
  domeMaterial.createMentalrayTextureExtraAttrs(dome_map_mr_tex, iblMapFileTexture)

  #Select the mentalray texture node in the attribute editor
  #dome_map_mr_tex = "hemi_map_mentalrayTexture1"
  #mel.eval('showEditorExact("'+ dome_map_mr_tex + '")')

  melRunString = 'import maya.mel as mel \n'
  melRunString += 'mel.eval(\"showEditorExact(\\"' + dome_map_mr_tex + '\\")\")'
  #print("Deferred string: " + melRunString)
  cmds.evalDeferred(melRunString)


"""
A python function to make sure mental ray is active 
and the MR shading nodes are read to be used.
"""
def forceMentalRayLoad():
  import maya.cmds as cmds
  import maya.mel as mel

  # Make sure the mental ray plugin was loaded
  if not (cmds.pluginInfo("Mayatomr",q=True,loaded=True)):
    cmds.loadPlugin("Mayatomr")
    print("The Mental Ray plugin was loaded.")
  #else:
  #  print("The Mental Ray plugin is already active.")

  #Set the active renderer to mental ray to avoid Hypershade red node errors 
  #mel.eval("setCurrentRenderer mentalRay")
  #or
  melRunString = 'import maya.mel as mel \n'
  melRunString += 'mel.eval(\"setCurrentRenderer mentalRay\")'
  #print("Deferred string: " + melRunString)
  cmds.evalDeferred(melRunString)
  

#Check what version of Maya is active
def getMayaVersionDome():
  import maya.cmds as cmds
  import maya.mel as mel

  #Check if we are running Maya 2011 or higher
  mayaVersion = mel.eval("getApplicationVersionAsFloat;")

  #Debug Test Mode
  #Test this GUI using the Maya 2010 - non-docked GUI mode
  #mayaVersion = 2010;

  #Write out the current Maya version number
  print("Maya " + str(mayaVersion) + " detected.\n")
  
  return mayaVersion


"""
A python function to get the current object's shape node

getObjectShapeNode("stereoCamera")
# Result: [u'stereoCameraCenterCamShape', u'stereoCameraFrustum'] # 

"""

def getObjectShapeNode ( object ) :
    import maya.cmds as cmds
    return cmds.listRelatives( object, children=True , shapes=True)


"""
A python function to get the current object's parent node

getObjectParentNode("nurbsSphereShape1")
# Result:  [u'nurbsSphere1'] #

"""

def getObjectParentNode ( object ) :
    import maya.cmds as cmds
    return cmds.listRelatives( object, parent=True)
