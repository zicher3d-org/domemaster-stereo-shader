"""
Arnold Domemaster3D Camera Setup Script V2.1.2
2016-09-17 05.27 PM
Created by Andrew Hazelden  andrew@andrewhazelden.com

This script makes it easy to start creating fulldome stereoscopic content in Autodesk Maya.
-------------------------------------------------------------------------------------------------------

Version History

Version 2.1.2
------------
2016-09-17

Edited the Dome Grid creation script so the catch command is used to handle the event that mental ray might not be installed and a doPaintEffectsToPoly function based Maya code dependency is going to try and change the .miFinalGatherCast attribute. Adjusted the line thickness, default light brightness setting, and the shadow settings on the Dome Grid.

Code reformatting

Version 2.1
------------
2016-07-28

Updated Arnold camera shape names

Updated the DomemasterWxH function name


Version 1.7.4
------------
2015-06-12

Updated the Maya Wiki page link to use the new GitHub Wiki table of contents.
 

Version 1.7
---------------
2015-05-07 

Updated the dome grid defaults to create a 360x180 sphere.

The stereo rig manager defaultRig is value is now switched automatically when a LatLongStereo or DomeStereo camera is created.

Version 1.6
---------------
2014-11-05

Adapted the mental ray script to work with Arnold

------------------------------------------------------------------------------

Force Arnold to Load

Run using the command:
import arnoldDomeCamera as arnoldDomeCamera
reload(arnoldDomeCamera)
arnoldDomeCamera.forceArnoldLoad()

------------------------------------------------------------------------------

Domemaster3D Fulldome Stereo Rig
A python function to create a fulldome stereo rig in Maya.

Run using the command:
import arnoldDomeCamera as arnoldDomeCamera
reload(arnoldDomeCamera)
arnoldDomeCamera.createArnoldFulldomeStereoRig()

------------------------------------------------------------------------------
Domemaster3D Fulldome FOV Camera

A python function to create a fulldome 2D FOV style camera in Maya using a single Arnold DomemasterStereo based camera.

Run using the command:
import arnoldDomeCamera as arnoldDomeCamera
reload(arnoldDomeCamera)
arnoldDomeCamera.createArnoldDomemasterFOV_Camera()

------------------------------------------------------------------------------

Domemaster3D Fulldome WxH Camera

A python function to create a fulldome 2D camera in Maya.

Run using the command:
import arnoldDomeCamera as arnoldDomeCamera
reload(arnoldDomeCamera)
arnoldDomeCamera.createArnoldDomemasterWxH_Camera()

------------------------------------------------------------------------------

Domemaster3D createArnoldLatLong_Camera
A python function to create a 2D LatLong / Equirectangular / Spherical camera.  This option uses the LatLong Stereo shader applied in a 2D center camera viewing mode.

Run using the command:
import arnoldDomeCamera as arnoldDomeCamera
reload(arnoldDomeCamera)
arnoldDomeCamera.createArnoldLatLong_Camera()

------------------------------------------------------------------------------

Domemaster3D createArnoldLatLongStereoRig
A python function to create a stereoscopic latitude longitude lens shader and attach it to a camera.

Run using the command:
import arnoldDomeCamera as arnoldDomeCamera
reload(arnoldDomeCamera)
arnoldDomeCamera.createArnoldLatLongStereoRig()

------------------------------------------------------------------------------

Domemaster3D DomeGrid test background 
A python function to create a hemispherical yellow test grid in Maya. 

Run using the command:
import arnoldDomeCamera as arnoldDomeCamera
reload(arnoldDomeCamera)
arnoldDomeCamera.createDomeGrid()

------------------------------------------------------------------------------

Domemaster3D LatLongGrid test background 
A python function to create a spherical yellow test grid in Maya that is rotated 90 degrees on the RotateX. 

Run using the command:
import arnoldDomeCamera as arnoldDomeCamera
reload(arnoldDomeCamera)
arnoldDomeCamera.createLatLongGrid()
------------------------------------------------------------------------------

Domemaster3D createTestShapes
A python function to create a test sphere and cube in Maya. 

Run using the command:
import arnoldDomeCamera as arnoldDomeCamera
reload(arnoldDomeCamera)
arnoldDomeCamera.createTestShapes()

------------------------------------------------------------------------------

Domemaster3D getMayaVersionDome
A python function to check what Maya version is active.

import arnoldDomeCamera
reload(arnoldDomeCamera)
arnoldDomeCamera.getMayaVersionDome()

------------------------------------------------------------------------------

Show the Domemaster Wiki
--------------------------------
Loads the wiki page in your default web browser

Run using the command:
print("Open the Domemaster Wiki Page")
import arnoldDomeCamera as arnoldDomeCamera
arnoldDomeCamera.openDomemasterWiki()

print("Open the Domemaster NING Group")
import arnoldDomeCamera as arnoldDomeCamera
arnoldDomeCamera.openDomemasterNing()

print("Open the Domemaster Downloads Page")
import arnoldDomeCamera as arnoldDomeCamera
arnoldDomeCamera.openDomemasterDownloads()

print("Open the Domemaster Bug Reporter")
import arnoldDomeCamera as arnoldDomeCamera
arnoldDomeCamera.openDomemasterBugReport()

"""

def openDomemasterWiki():
  import webbrowser
  
  # Domemaster Stereo Shader - Wiki Page
  url = 'https://github.com/zicher3d-org/domemaster-stereo-shader/wiki'
  
  # Open URL in new window, raising the window if possible.
  webbrowser.open_new(url)
  
  
def openArnoldDomemasterNing():
  import webbrowser
  
  # Domemaster NING Group
  url = 'http://fulldome.ning.com/forum/topics/stereoscopic-domemaster-images'
  
  # Open URL in new window, raising the window if possible.
  webbrowser.open_new(url)


def openArnoldDomemasterDownloads():
  import webbrowser
  
  # Domemaster Stereo Shader - Download Page
  url = 'https://github.com/zicher3d-org/domemaster-stereo-shader/releases'

  # Open URL in new window, raising the window if possible.
  webbrowser.open_new(url)
  
def openArnoldDomemasterBugReport():
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
  # Set up the base folder path for the Domemaster3D control maps
  # ---------------------------------------------------------------------

  # Check OS platform for Windows/Mac/Linux Paths
  import platform

  # This is the base path for the images folder
  baseImagesFolder = ""
  
  # Try and read the value from the current Maya.env file's environment variables
  baseImagesFolder = os.environ.get('DOMEMASTER3D_SOURCEIMAGES_DIR')+ "/"
  # Typical Result: C:/Program Files/Domemaster3D/sourceimages/ 
  
  # Use a fixed value if the env var is empty
  if baseImagesFolder == None:
    if platform.system()=='Windows':
      # Check if the program is running on Windows 
      baseImagesFolder = "C:/Program Files/Domemaster3D/sourceimages/"
    elif platform.system()== 'win32':
      # Check if the program is running on Windows 32
      baseImagesFolder = "C:/Program Files(x86)/Domemaster3D/sourceimages/"
    elif platform.system()== 'Darwin':
      # Check if the program is running on Mac OS X
      baseImagesFolder = "/Applications/Domemaster3D/sourceimages/"
    elif platform.system()== 'Linux':
      # Check if the program is running on Linux
      baseImagesFolder = "/opt/Domemaster3D/sourceimages/"
    elif platform.system()== 'Linux2':
      # Check if the program is running on Linux
      baseImagesFolder = "/opt/Domemaster3D/sourceimages/"
    else:
      # Create the empty variable as a fallback mode
      baseImagesFolder = ""

  combinedFileAndImagePath = baseImagesFolder + imageFileName

  print "[Domemaster3D is running on a " + platform.system()+ " System]"
  print "[Requesting the image file]: " + combinedFileAndImagePath

  return combinedFileAndImagePath



"""
Domemaster3D AutoSetup
----------------------
A python function to create a fulldome stereo rig and test grid in Maya. 

"""
def Autosetup():
  setRenderRes()
  setDomeSamplingQuality()
  createArnoldFulldomeStereoRig()
  createDomeGrid()
  createTestShapes()


"""
Domemaster3D setDomeSamplingQuality
----------------------
A python function to setup the AA sampling quality. 

"""
def setDomeSamplingQuality():
  import maya.cmds as cmds
  import maya.mel as mel
  #---------------------------------------------------------------------
  # Render AA Quality Settings
  # ---------------------------------------------------------------------



"""
Domemaster3D SetRenderRes
----------------------
A python function to setup the basic 2K x 2K square render settings. 

"""
def setRenderRes():
  import maya.cmds as cmds
  import maya.mel as mel
  
  # Make sure the Arnold plugin was loaded
  #forceArnoldLoad()
  
  #mel.eval('unifiedRenderGlobalsWindow;')


  fulldomeRenderWidth = 2048
  fulldomeRenderHeight = 2048
  
  #---------------------------------------------------------------------
  # Setup the default render settings for a square domemaster image output
  # ---------------------------------------------------------------------
  cmds.setAttr('defaultResolution.width', fulldomeRenderWidth)
  cmds.setAttr('defaultResolution.height', fulldomeRenderHeight)
  cmds.setAttr('defaultResolution.deviceAspectRatio', 1)
  cmds.setAttr('defaultResolution.pixelAspect', 1)
  


"""
Domemaster3D changeRenderRes
----------------------
A python function to change the basic resolution square render settings. 

"""

def changeRenderRes(renderSizePx):
  import maya.mel as mel
  import maya.cmds as cmds
  
  # Make sure the Arnold plugin was loaded
  #forceArnoldLoad()
  
  #mel.eval('unifiedRenderGlobalsWindow;')

  fulldomeRenderWidth = renderSizePx
  fulldomeRenderHeight = renderSizePx
  
  #---------------------------------------------------------------------
  # Setup the default render settings for a square domemaster image output
  # ---------------------------------------------------------------------
  cmds.setAttr('defaultResolution.width', fulldomeRenderWidth)
  cmds.setAttr('defaultResolution.height', fulldomeRenderHeight)
  cmds.setAttr('defaultResolution.deviceAspectRatio', 1)
  cmds.setAttr('defaultResolution.pixelAspect', 1)

  print("Changed the render settings to output a " + str(renderSizePx)+ "x" + str(renderSizePx)+ " image.")

  
"""
Domemaster3D changeRenderResWH
----------------------
A python function to change the basic resolution render settings. 

"""

def changeRenderResWH(renderSizeW,  renderSizeH):
  import maya.mel as mel
  import maya.cmds as cmds

  # Make sure the Arnold plugin was loaded
  #forceArnoldLoad()
  
  #mel.eval('unifiedRenderGlobalsWindow;')

  domeRenderWidth = renderSizeW
  domeRenderHeight = renderSizeH
  domeDeviceAspectRatio=domeRenderWidth/domeRenderHeight
  
  #---------------------------------------------------------------------
  # Setup the default render settings for a square domemaster image output
  # ---------------------------------------------------------------------
  cmds.setAttr('defaultResolution.width', domeRenderWidth)
  cmds.setAttr('defaultResolution.height', domeRenderHeight)
  cmds.setAttr('defaultResolution.deviceAspectRatio', domeDeviceAspectRatio)
  cmds.setAttr('defaultResolution.pixelAspect', 1)

  print("Changed the render settings to output a " + str(renderSizeW)+ "x" + str(renderSizeW)+ " image.")



"""
Domemaster3D Fulldome Stereo Rig
--------------------------------
A python function to create a fulldome stereo rig in Maya.
"""

def createArnoldFulldomeStereoRig():
  import maya.cmds as cmds
  import maya.mel as mel
  
  # ---------------------------------------------------------------------
  # Setup the default Maya Settings
  # ---------------------------------------------------------------------
  cmds.loadPlugin("stereoCamera", qt=True)
  
  # Make sure the Arnold plugin was loaded
  forceArnoldLoad()

  # ---------------------------------------------------------------------
  # Create the stereo rig
  # ---------------------------------------------------------------------
  
  #import maya.app.stereo.stereoCameraMenus as stereoCameraMenus
  #stereoCameraMenus.buildCreateMenu()
  #import maya.app.stereo.stereoCameraRig
  #maya.app.stereo.stereoCameraRig.createStereoCameraRig()
  
  from maya.app.stereo import stereoCameraRig
  
  # Set the default rig to an ArnoldDomeStereoCamera
  cmds.stereoRigManager(defaultRig='ArnoldDomeStereoCamera')
  
  # Add the camera rig to the scene
  rig = stereoCameraRig.createStereoCameraRig('ArnoldDomeStereoCamera')
  #[u'ArnoldDomeStereoCamera', u'ArnoldDomeStereoCameraLeft', u'ArnoldDomeStereoCameraRight']
  
  # Get the stereo camera rig shape nodes for the center/right/left cameras
  rig_center_shape_name = getObjectShapeNode(rig[0])
  #[u'stereoCameraCenterCamShape', u'stereoCameraFrustum'] #

  rig_left_shape_name = getObjectShapeNode(rig[1])
  # Result: [u'stereoCameraLeftShape'] #

  rig_right_shape_name = getObjectShapeNode(rig[2])
  # Result: [u'stereoCameraRightShape'] #
  
  """
  cmds.setAttr(rig[0]+'.rotateX', 90)
  cmds.setAttr(rig[0]+'.rotateY', 0)
  cmds.setAttr(rig[0]+'.rotateZ', 0)
  
  """
  
  # Changes the render settings to set the stereo camera to be a renderable camera
  cmds.setAttr(rig_left_shape_name[0]+'.renderable', 1)#stereoCameraLeftShape
  cmds.setAttr(rig_right_shape_name[0]+'.renderable', 1)#stereoCameraRightShape
  cmds.setAttr('topShape.renderable', 0)
  cmds.setAttr('sideShape.renderable', 0)
  cmds.setAttr('frontShape.renderable', 0)
  cmds.setAttr('perspShape.renderable', 0)

  # Set up the default AA sampling quality
  setDomeSamplingQuality()
  

  #---------------------------------------------------------------------------
  # Enable Real-time 3D in the OpenGL viewport 
  # using a PreRender and PostRender MEL script
  #---------------------------------------------------------------------------
  #import maya.cmds as cmds

  # PreRender MEL:
  #cmds.setAttr('defaultRenderGlobals.preMel', "source \"domeRender.mel\"; domemaster3DPreRenderMEL();", type='string')
  # PostRender MEL:
  #cmds.setAttr('defaultRenderGlobals.postMel' , "source \"domeRender.mel\"; domemaster3DPostRenderMEL();", type='string')

  # Enable realtime 3D
  #mel.eval("source \"domeRender.mel\"; domemaster3DPostRenderMEL();");
  
  return rig
  

"""
Domemaster3D Fulldome Stereo Rig
--------------------------------
A python function to create a fulldome stereo rig in Maya.
"""

def createArnoldLatLongStereoRig():
  import maya.cmds as cmds
  import maya.mel as mel
  
  # ---------------------------------------------------------------------
  # Setup the default Maya Settings
  # ---------------------------------------------------------------------
  cmds.loadPlugin("stereoCamera", qt=True)
  
  # Make sure the Arnold plugin was loaded
  forceArnoldLoad()

  # ---------------------------------------------------------------------
  # Create the stereo rig
  # ---------------------------------------------------------------------
  
  #import maya.app.stereo.stereoCameraMenus as stereoCameraMenus
  #stereoCameraMenus.buildCreateMenu()
  #import maya.app.stereo.stereoCameraRig
  #maya.app.stereo.stereoCameraRig.createStereoCameraRig()
  
  from maya.app.stereo import stereoCameraRig
  
  # Set the default rig to an ArnoldLatLongStereoCamera
  cmds.stereoRigManager(defaultRig='ArnoldLatLongStereoCamera')
  
  # Add the camera rig to the scene
  rig = stereoCameraRig.createStereoCameraRig('ArnoldLatLongStereoCamera')
  #[u'ArnoldLatLongCamera', u'ArnoldLatLongCameraLeft', u'ArnoldLatLongCameraRight']
  
  #Get the stereo camera rig shape nodes for the center/right/left cameras
  rig_center_shape_name = getObjectShapeNode(rig[0])
  #[u'stereoCameraCenterCamShape', u'stereoCameraFrustum'] #

  rig_left_shape_name = getObjectShapeNode(rig[1])
  # Result: [u'stereoCameraLeftShape'] #

  rig_right_shape_name = getObjectShapeNode(rig[2])
  # Result: [u'stereoCameraRightShape'] #
  
  """
  cmds.setAttr(rig[0]+'.rotateX', 90)
  cmds.setAttr(rig[0]+'.rotateY', 0)
  cmds.setAttr(rig[0]+'.rotateZ', 0)
  
  """
  
  # Changes the render settings to set the stereo camera to be a renderable camera
  cmds.setAttr(rig_left_shape_name[0]+'.renderable', 1)#stereoCameraLeftShape
  cmds.setAttr(rig_right_shape_name[0]+'.renderable', 1)#stereoCameraRightShape
  cmds.setAttr('topShape.renderable', 0)
  cmds.setAttr('sideShape.renderable', 0)
  cmds.setAttr('frontShape.renderable', 0)
  cmds.setAttr('perspShape.renderable', 0)

  # Set up the default AA sampling quality
  setDomeSamplingQuality()
  
  #---------------------------------------------------------------------------
  # Enable Real-time 3D in the OpenGL viewport 
  # using a PreRender and PostRender MEL script
  #---------------------------------------------------------------------------
  #import maya.cmds as cmds

  # PreRender MEL:
  #cmds.setAttr('defaultRenderGlobals.preMel', "source \"domeRender.mel\"; domemaster3DPreRenderMEL();", type='string')
  # PostRender MEL:
  #cmds.setAttr('defaultRenderGlobals.postMel' , "source \"domeRender.mel\"; domemaster3DPostRenderMEL();", type='string')

  # Enable realtime 3D
  #mel.eval("source \"domeRender.mel\"; domemaster3DPostRenderMEL();");
  
  return rig


"""
Domemaster3D createDomemasterFOV_Camera
----------------------
A python function to create a fulldome 2D FOV style camera in Maya using a single Arnold DomemasterStereo based camera.
"""
def createArnoldDomemasterFOV_Camera():
  import maya.cmds as cmds
  #import maya.mel as mel 
  
  # Make sure the Arnold plugin was loaded
  forceArnoldLoad()

  # ---------------------------------------------------------------------
  # Variables
  # ---------------------------------------------------------------------
  
  # Arnold camera type
  cameraType = 'DomemasterStereo'
  
  # ---------------------------------------------------------------------
  # Create the stereo rig
  # ---------------------------------------------------------------------

  # Create a camera and get the shape name.
  cameraName = cmds.camera(name='ArnoldDomemasterFOV_Camera')
  cameraShape = cameraName[1]

  # ---------------------------------------------------------------------
  # Assign the Arnold DomemasterStereo camera type
  # ---------------------------------------------------------------------
  cmds.setAttr(cameraShape+'.ai_translator', cameraType, type='string')
  
  # Scale the stereo camera rig locator larger 
  #cmds.setAttr(cameraShape+'.locatorScale', 1)# Scale Camera icon

  # Link the new attribute 'Cam Locator Scale' to the dome camera's locator size control
  cmds.addAttr(cameraName[0], longName='Cam_Locator_Scale', niceName='Cam Locator Scale', attributeType='double', defaultValue=1.0, minValue=0.001)
  cmds.setAttr(cameraName[0]+'.Cam_Locator_Scale', keyable=False, channelBox=True)
  cmds.connectAttr(cameraName[0]+'.Cam_Locator_Scale', cameraShape+'.locatorScale', force=True)

  # Set the view to center
  cmds.setAttr(cameraShape+'.aiCamera', 0)
  
  # Adjust the stereo settings
  # cmds.setAttr(cameraShape+'.aiZeroParallaxSphere', 360)
  cmds.setAttr(cameraShape+'.aiSeparation', 0)
  
  # Align the base camera to point upwards
  cmds.setAttr(cameraName[0]+'.rotateX', 90)
  cmds.setAttr(cameraName[0]+'.rotateY', 0)
  cmds.setAttr(cameraName[0]+'.rotateZ', 0)

  # Changes the render settings to set the stereo camera to be a renderable camera
  cmds.setAttr(cameraShape+'.renderable', 1)# ArnoldDomemasterFOV_Camera
  cmds.setAttr('topShape.renderable', 0)
  cmds.setAttr('sideShape.renderable', 0)
  cmds.setAttr('frontShape.renderable', 0)
  cmds.setAttr('perspShape.renderable', 0)

  # Set up the default mental ray AA sampling quality
  #setDomeSamplingQuality()

  # ---------------------------------------------------------------------
  # Setup the stereo rig camera attributes
  # ---------------------------------------------------------------------
  # 4 mm focal length = 160 degree FOV
  #cmds.setAttr(cameraShape+'.focalLength', 4)

  # 18 mm focal length = 90 degree FOV
  cmds.setAttr(cameraShape+'.focalLength', 18)


"""
Domemaster3D createDomemasterWxH_Camera
----------------------
A python function to set up an Arnold DomemasterWxH based camera.
"""
def createArnoldDomemasterWxH_Camera():
  import maya.cmds as cmds
  #import maya.mel as mel 
  
  # Make sure the Arnold plugin was loaded
  forceArnoldLoad()

  # ---------------------------------------------------------------------
  # Variables
  # ---------------------------------------------------------------------
  
  # Arnold camera type
  cameraType = 'DomemasterWxH'
  
  # ---------------------------------------------------------------------
  # Create the stereo rig
  # ---------------------------------------------------------------------

  # Create a camera and get the shape name.
  cameraName = cmds.camera(name='ArnoldDomemasterWxH_Camera')
  cameraShape = cameraName[1]

  # ---------------------------------------------------------------------
  # Assign the Arnold domemasterWxH camera type
  # ---------------------------------------------------------------------
  cmds.setAttr(cameraShape+'.ai_translator', cameraType, type='string')
  
  # Scale the stereo camera rig locator larger 
  #cmds.setAttr(cameraShape+'.locatorScale', 1)#Scale Camera icon

  # Link the new attribute 'Cam Locator Scale' to the dome camera's locator size control
  cmds.addAttr(cameraName[0], longName='Cam_Locator_Scale', niceName='Cam Locator Scale', attributeType='double', defaultValue=1.0, minValue=0.001)
  cmds.setAttr(cameraName[0]+'.Cam_Locator_Scale', keyable=False, channelBox=True)
  cmds.connectAttr(cameraName[0]+'.Cam_Locator_Scale', cameraShape+'.locatorScale', force=True)

  # Align the base camera to point upwards
  cmds.setAttr(cameraName[0]+'.rotateX', 90)
  cmds.setAttr(cameraName[0]+'.rotateY', 0)
  cmds.setAttr(cameraName[0]+'.rotateZ', 0)

  # Changes the render settings to set the stereo camera to be a renderable camera
  cmds.setAttr(cameraShape+'.renderable', 1)#domeAFL_WxH_CameraShape
  cmds.setAttr('topShape.renderable', 0)
  cmds.setAttr('sideShape.renderable', 0)
  cmds.setAttr('frontShape.renderable', 0)
  cmds.setAttr('perspShape.renderable', 0)

  # Set up the default mental ray AA sampling quality
  #setDomeSamplingQuality()

  # ---------------------------------------------------------------------
  # Setup the stereo rig camera attributes
  # ---------------------------------------------------------------------
  # 4 mm focal length = 160 degree FOV
  #cmds.setAttr(cameraShape+'.focalLength', 4)

  # 18 mm focal length = 90 degree FOV
  cmds.setAttr(cameraShape+'.focalLength', 18)


"""
Domemaster3D createArnoldLatLong_Camera
----------------------
A python function to create a 2D LatLong / Equirectangular / Spherical camera.  This option uses the LatLong Stereo shader applied in a 2D center camera viewing mode.
"""
def createArnoldLatLong_Camera():
  import maya.cmds as cmds
  #import maya.mel as mel 
  
  # Make sure the Arnold plugin was loaded
  forceArnoldLoad()

  # ---------------------------------------------------------------------
  # Variables
  # ---------------------------------------------------------------------
  
  # Arnold camera type
  cameraType = 'LatLongStereo'
  
  # ---------------------------------------------------------------------
  # Create the stereo rig
  # ---------------------------------------------------------------------

  # Create a camera and get the shape name.
  cameraName = cmds.camera(name='ArnoldLatLong_Camera')
  cameraShape = cameraName[1]

  # ---------------------------------------------------------------------
  # Assign the Arnold LatLongStereo camera type
  # ---------------------------------------------------------------------
  cmds.setAttr(cameraShape+'.ai_translator', cameraType, type='string')
  
  # Scale the stereo camera rig locator larger 
  #cmds.setAttr(cameraShape+'.locatorScale', 1)# Scale Camera icon

  # Link the new attribute 'Cam Locator Scale' to the dome camera's locator size control
  cmds.addAttr(cameraName[0], longName='Cam_Locator_Scale', niceName='Cam Locator Scale', attributeType='double', defaultValue=1.0, minValue=0.001)
  cmds.setAttr(cameraName[0]+'.Cam_Locator_Scale', keyable=False, channelBox=True)
  cmds.connectAttr(cameraName[0]+'.Cam_Locator_Scale', cameraShape+'.locatorScale', force=True)

  # Set the view to center
  cmds.setAttr(cameraShape+'.aiCamera', 0)
  
  # Adjust the stereo settings
  # cmds.setAttr(cameraShape+'.aiZeroParallaxSphere', 360)
  cmds.setAttr(cameraShape+'.aiSeparation', 0)
  
  # Set the Zenith Mode to ON
  cmds.setAttr(cameraShape+'.aiZenithMode', 1)
  
  # Align the base camera to point upwards
  cmds.setAttr(cameraName[0]+'.rotateX', 90)
  cmds.setAttr(cameraName[0]+'.rotateY', 0)
  cmds.setAttr(cameraName[0]+'.rotateZ', 0)

  # Changes the render settings to set the stereo camera to be a renderable camera
  cmds.setAttr(cameraShape+'.renderable', 1)# ArnoldLatLong_Camera
  cmds.setAttr('topShape.renderable', 0)
  cmds.setAttr('sideShape.renderable', 0)
  cmds.setAttr('frontShape.renderable', 0)
  cmds.setAttr('perspShape.renderable', 0)

  # Set up the default mental ray AA sampling quality
  #setDomeSamplingQuality()

  # ---------------------------------------------------------------------
  # Setup the stereo rig camera attributes
  # ---------------------------------------------------------------------
  # 4 mm focal length = 160 degree FOV
  #cmds.setAttr(cameraShape+'.focalLength', 4)

  # 18 mm focal length = 90 degree FOV
  cmds.setAttr(cameraShape+'.focalLength', 18)


"""
Domemaster3D LatLongGrid test background 
--------------------------------------
A python function to create a spherical yellow test grid in Maya that is rotated 90 degrees on the RotateX. 

"""
  
def createLatLongGrid():
  import maya.cmds as cmds
  import maya.mel as mel
  
  # Create a spherical yellow test grid in Maya. 
  createDomeGrid()
  
  # Align the grid on the horizontal axis
  #cmds.setAttr('domeGridSurface.rotateX', 90)
  
  # Set the grid to a full 360 degree FOV sphere
  cmds.setAttr('domeGrid.fieldOfView', 360)
  
  # Change the grid from 12 spans (fulldome) to 24 spans (sphere) to cover the full 360 degree FOV with more uniform square patches.
  cmds.setAttr('domeGrid.Dome_Spans', 24)


"""
Domemaster3D DomeGrid test background 
--------------------------------------
A python function to create a spherical yellow test grid in Maya. 

"""

# Suggested Maya Scene Grid Settings:
# Length and Width: 360 units
# Grid lines every: 180 units
# Subdivisions: 2

def createDomeGrid():
  import maya.cmds as cmds
  import maya.mel as mel
  
  #---------------------------------------------------------------------------
  # Variables
  #---------------------------------------------------------------------------
  
  # Reference Grid Meshes
  #domeGridSurface = 'domeGridSurface'
  domeGridSurface = 'domeGridSurface'
  domeGridlineSurface = 'domeGridlineSurface'
  
  # Set the diameter of the dome shape
  startingDomeDiameter = 360
  
  #---------------------------------------------------------------------------
  # Remove any existing domeGrid elements
  #---------------------------------------------------------------------------
  
  #---------------------------------------------------------------------------
  # Remove old geometry and paint effects nodes
  #---------------------------------------------------------------------------
  
  if cmds.objExists('domeGrid'): 
    print('Removing existing Domemaster3D object: domeGrid')
    cmds.select('domeGrid', replace=True)
    cmds.delete()

  if cmds.objExists('MeshGroup'): 
    print('Removing existing Domemaster3D object: MeshGroup')
    cmds.select('MeshGroup', replace=True)
    cmds.delete()
  
  if cmds.objExists(domeGridSurface): 
    print('Removing existing Domemaster3D object: ' + domeGridSurface)
    cmds.select(domeGridSurface, replace=True)
    cmds.delete()
  
  if cmds.objExists('domeGridToon'): 
    print('Removing existing Domemaster3D object: domeGridToon')
    cmds.select('domeGridToon', replace=True)
    cmds.delete()
    
  if cmds.objExists('domeGrid_displayModeExpr'): 
    print('Removing existing Domemaster3D object: domeGrid_displayModeExpr')
    cmds.select('domeGrid_displayModeExpr', replace=True)
    cmds.delete()
  
  #--------------------------------------------------------------------------
  #Remove old dome Grid surface materials
  #---------------------------------------------------------------------------
  
  if cmds.objExists('domeGridLinesSurfaceShader'): 
    print('Removing existing Domemaster3D object: domeGridLinesSurfaceShader')
    cmds.select('domeGridLinesSurfaceShader', replace=True)
    cmds.delete()
  
  if cmds.objExists('domeGridLinesSurfaceShaderSG'): 
    print('Removing existing Domemaster3D object: domeGridLinesSurfaceShaderSG')
    cmds.select('domeGridLinesSurfaceShaderSG', replace=True)
    cmds.delete()
  
  if cmds.objExists('domeGridSurfaceShaderSG'): 
    print('Removing existing Domemaster3D object: domeGridSurfaceShaderSG')
    cmds.select('domeGridSurfaceShaderSG', replace=True)
    cmds.delete()
    
  if cmds.objExists('domeGridSurfaceShader'): 
    print('Removing existing Domemaster3D object: domeGridSurfaceShader')
    cmds.select('domeGridSurfaceShader', replace=True)
    cmds.delete()
  
  #--------------------------------------------------------------------------
  # Protect any existing surface shaders from the paint effects node
  #---------------------------------------------------------------------------
    
  if cmds.objExists('surfaceShader1SG'): 
    print('Renaming existing  object: surfaceShader1SG')
    cmds.rename('surfaceShader1SG', 'aSurfaceShader1SG')
    
  if cmds.objExists('surfaceShader1'): 
    print('Renaming existing  object: surfaceShader1')
    cmds.rename('surfaceShader1', 'aSurfaceShader1')
  
  #--------------------------------------------------------------------------
  # Make the dome mesh
  #--------------------------------------------------------------------------
  
  #-----------------------------------------------------------------------------
  # Create a hybrid NURBS/Polygon Paint effects Toon Surface
  #-----------------------------------------------------------------------------

  startingCurveRadius = 1.0
  
  #startingToonThickness = 0.1
    
  # Create the base curve with a 90 degree arc
  domeRadiusCurveName = cmds.circle(name='domeGridSurfaceCurve', c=(0, 0, 0), nr=(0, 0, 1), sw=90, r=startingCurveRadius, d=3, ut=0, tol=0.01, s=10, ch=1)

  # Get the curve's shape node name
  domeCurveShape = getObjectShapeNode(domeRadiusCurveName[0])

  # Setup the NURBS to Poly conversion prefs
  #nurbsToPolygonsPref -q -f;
  cmds.nurbsToPolygonsPref(format=3, uType=3, uNumber=1, vType=3, vNumber=1)

  """
  #MEL Code to debug NURBS to polygon conversion:
  int $f = `nurbsToPolygonsPref -q -f`;
  int $ut = `nurbsToPolygonsPref -q -ut`;
  int $un = `nurbsToPolygonsPref -q -un`;
  int $vt = `nurbsToPolygonsPref -q -vt`;
  int $vn = `nurbsToPolygonsPref -q -vn`;
  print($f + " " + $ut + " " + $un+ " " + $vt+ " " + $vn);
  """

  # Revolve the base 90 degree arc curve into a NURBS dome shape
  domeRadiusSurfaceName = cmds.revolve(domeCurveShape, name='domeGridSurface', ch=1, po=0, rn=0, ssw=0, esw=360, ut=0, tol=0.01, degree=3, s=40, ulp=1, ax=(0, 1, 0), polygon=1)

  domeSurfaceShape = getObjectShapeNode(domeRadiusSurfaceName[0]);

  print "\nDome Preview elements:"
  print domeRadiusSurfaceName
  print "Dome Preview shape node:"
  print domeSurfaceShape
  print "\n"

  # Find out the preview curve's makeNurbCircle node name
  makeCurveShapeName = domeCurveShape
  makeCurveObject = cmds.listConnections(makeCurveShapeName[0]+'.create', type='makeNurbCircle')
  makeCurveNodeName = makeCurveObject[0]
  print("The NURBS circle creation node is: ")
  print(makeCurveNodeName)

  #-----------------------------------------------------------------------------
  # Make the NURBS Curve able to be moved without effecting the revolves
  #-----------------------------------------------------------------------------
      
  # Find out the name of the "makeNurbCircle" node that is used to create the domeGridPreviewCurve shape
  makeRevolveObjects= cmds.listConnections( makeCurveShapeName[0]+'.worldSpace', type='revolve')
  makeRevolveNodeName = makeRevolveObjects[0];
  print("The circle creation node is: ")
  print(makeRevolveNodeName)

  # Reconnect the curve to the revolve node using local space
  # This replaces the curve's previous .worldSpace connection that inhibited the
  # ability to move the curve without effecting the revolve
  cmds.connectAttr(makeCurveShapeName[0]+".local", makeRevolveNodeName+".inputCurve",  f=True);

  # Put the domeSurface "PreviewShape" inside the domeGrid group
  # Have the revolved shape aligned relative to the domeGrid
  #cmds.parent(domeRadiusSurfaceName[0], domeRadiusTransform)

  # Parent the NURBS revolve curve to the domeGrid
  #cmds.parent(domeRadiusCurveName[0], domeRadiusTransform)
  
  # Create the base sphere with a 1 unit scale
  #domeGridName = cmds.polySphere(name=domeGridSurface, radius = 1, subdivisionsX=36, subdivisionsY=20, axis=(0, 1, 0),  createUVs=2, constructionHistory=True)
  
  # Chop the polysphere into a hemispherical dome
  #domeGridTransform = domeGridName[0]
  #domeGridShape = getObjectShapeNode(domeGridName[0])
  #cmds.select(domeGridTransform+'.f[0:323]', domeGridTransform+'.f[648:683]', replace=True)
  #cmds.delete()
  
  domeGridTransform = domeRadiusSurfaceName[0];
  
  # Make the curve an intermediate shape
  cmds.setAttr(domeCurveShape[0]+'.intermediateObject', 1)

  # Tell the domeGridSurface to move with the domeGrid group node
  cmds.setAttr(domeGridTransform+'.inheritsTransform', 1)
  
 
  # ---------------------------------------------------------------------------
  # Create the PaintFX Toon stroke outlines
  # --------------------------------------------------------------------------
  
  cmds.select(domeGridTransform, replace=True)
  
  # Assign the paint effects toon outlines
  mel.eval('assignNewPfxToon;')
  
  # Rename the toon shader
  domeToonShader = 'domeGridToon'
  domeToonShaderShape = 'domeGridToonShape'
  cmds.rename('pfxToon1', domeToonShader)
  
  # Define the new toon shader controls
  cmds.setAttr(domeToonShaderShape+'.profileLines', 0)
  cmds.setAttr(domeToonShaderShape+'.borderLines', 0)
  cmds.setAttr(domeToonShaderShape+'.creaseLineWidth', 15)
  cmds.setAttr(domeToonShaderShape+'.creaseColor', 1, 1, 0, type='double3')
  cmds.setAttr(domeToonShaderShape+'.hardCreasesOnly', 0)
  cmds.setAttr(domeToonShaderShape+'.creaseBreakAngle', 0)
  cmds.setAttr(domeToonShaderShape+'.creaseAngleMin', 0)
  cmds.setAttr(domeToonShaderShape+'.creaseAngleMax', 0)
  cmds.setAttr(domeToonShaderShape+'.meshVertexColorMode', 1)
  cmds.setAttr(domeToonShaderShape+'.meshQuadOutput', 1)
  cmds.setAttr(domeToonShaderShape+'.meshHardEdges', 1)
  
  # Create a polygon paint effects stroke output
  cmds.select(domeToonShader, replace=True)
  # The catchQuiet command is used to handle the event that mental ray might not be installed and a doPaintEffectsToPoly function based Maya code dependency is going to try and change the .miFinalGatherCast attribute...
  mel.eval('catch(doPaintEffectsToPoly(1,1,1,1,100000));')
  #mel.eval('catchQuiet(doPaintEffectsToPoly(1,1,1,1,100000));')
  
  
  # Make a local space mesh connection to fix the grouped node double translation issue
  #connectAttr -f domeGridToonShape.outMainMesh MainShape.inMesh;
  # Result: Connected domeGridToonShape.outMainMesh to MainShape.inMesh. // 
  cmds.connectAttr(domeToonShaderShape+'.outMainMesh', 'MainShape.inMesh', force=True)
  
  if cmds.objExists('MeshGroup'): 
    print('Unlinking the Toon shader\'s inheritsTransform attribute')
    cmds.setAttr('MeshGroup.inheritsTransform', 0)
  
  # --------------------------------------------------------------------------
  # Adjust the grid lines shader
  #---------------------------------------------------------------------------
  
  #domeGridlineShadingGroup = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='domeGridLinesSurfaceShaderSG')
  domeGridlineMaterial = 'domeGridLinesSurfaceShader'
  domeGridlineShadingGroup  = 'domeGridLinesSurfaceShaderSG'
  
  # Rename the default gridlines shader
  cmds.rename('surfaceShader1', domeGridlineMaterial)
  cmds.rename('surfaceShader1SG', domeGridlineShadingGroup)
  
  # Standard Yellow Color
  #cmds.setAttr('surfaceShader1.outColor', 1, 1, 0, type='double3')
  
  # Super Bright Yellow Color for Physical Sky Compatibility
  #cmds.setAttr(domeGridlineMaterial+'.outColor', 15, 15, 0, type='double3')
  cmds.setAttr(domeGridlineMaterial+'.outColor', 1, 1, 0, type='double3')
    
  #---------------------------------------------------------------------------
  # Adjust the grid surface shader
  #---------------------------------------------------------------------------
  
  # Create the dome Grid surface shader + shading group
  domeGridShadingGroup = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='domeSurfaceShaderSG')
  domeGridMaterial = cmds.shadingNode('surfaceShader', name='domeGridSurfaceShader', asShader=True)
  
  # Make the surface shader black
  cmds.setAttr(domeGridMaterial+'.outColor', 0, 0, 0, type='double3')
  #Set the polygon surface to be transparent
  cmds.setAttr(domeGridMaterial+'.outTransparency', 1, 1, 1, type='double3')
  
  # Connect the surface shader to the shading group and the polygon surface
  cmds.connectAttr(domeGridMaterial+'.outColor', domeGridShadingGroup+'.surfaceShader')
  cmds.select(domeGridSurface)
  cmds.hyperShade(assign=domeGridShadingGroup)

  #---------------------------------------------------------------------------
  # Group the domeGrid surfaces under a node called "domeGrid"
  #---------------------------------------------------------------------------
  #cmds.group('domeGridSurface', 'domeGridToon', 'MeshGroup', name='domeGrid')
  cmds.group(domeRadiusCurveName[0], domeRadiusSurfaceName[0], 'domeGridToon', 'MeshGroup', name='domeGrid')
       
  #---------------------------------------------------------------------------
  # Add Extra Attrs to the domeGrid shape
  #---------------------------------------------------------------------------
  baseNodeName = 'domeGrid'
    
  #---------------------------------------------------------------------------  
  # Add a Field of View control to the domeGrid's transform node
  #---------------------------------------------------------------------------
  attrName = 'fieldOfView'
  
  # Check if the attribute exists on the domeGrid node
  #if(mel.attributeExists(attrName, baseNodeName)== 0):
  
  # 180 degree default = 180
  # 360 degree default = 360
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="double", min=0.1, max=360, defaultValue=180 , keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  #---------------------------------------------------------------------------  
  # Add a Field of View expression
  #---------------------------------------------------------------------------
  
  # Connect the domeGrid dome radius control to the sphere's makeNurbCircle radius attribute
  expressionBuilderString = makeCurveNodeName + ".sweep = " +(baseNodeName+'.'+attrName)+ "/2;"
  gridFOVRadiusExpressionName = 'domeGrid_FOVExpr'
  
  print "DomeGrid FOV Extra Attribute Expressions:"
  print expressionBuilderString

  cmds.expression(name=gridFOVRadiusExpressionName, string=expressionBuilderString, object=baseNodeName, alwaysEvaluate=True, unitConversion=all)
  
  # Connect the domeGrid dome radius control to the sphere's makeNurbCircle radius attribute:
  #cmds.connectAttr((baseNodeName+'.'+attrName), makeCurveObject[0]+'.sweep', force=True)
    

  #---------------------------------------------------------------------------  
  # Add a dome Radius control to the domeGrid's transform node
  #---------------------------------------------------------------------------
  attrName = 'Dome_Radius'

  # Check if the attribute exists on the domeGrid node
  #if(mel.attributeExists(attrName, baseNodeName)== 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="double", min=0.1, max=1000000, hasSoftMaxValue=True, softMaxValue=360, defaultValue=startingDomeDiameter , keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  # Connect the domeGrid dome radius control to the sphere's makeNurbCircle radius attribute:
  cmds.connectAttr((baseNodeName+'.'+attrName), makeCurveObject[0]+'.radius', force=True)

  #---------------------------------------------------------------------------  
  # Add a Dome Height Spans control to the domeGrid's transform node
  #---------------------------------------------------------------------------
  attrName = 'Dome_Spans'

  # Check if the attribute exists on the domeGrid node
  #if(mel.attributeExists(attrName, baseNodeName)== 0):
  
  #  180 degree dome default value = 12
  #  360 degree dome default value = 24
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="double", min=4, max=120, hasSoftMaxValue=True, softMaxValue=40, defaultValue=12 , keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  # Connect the domeGrid dome radius control to the sphere's makeNurbCircle sections attribute:
  cmds.connectAttr((baseNodeName+'.'+attrName), makeCurveObject[0]+'.sections', force=True)
    
  #---------------------------------------------------------------------------  
  # Add a Dome Width Sections control to the domeGrid's transform node
  #---------------------------------------------------------------------------
  attrName = 'Dome_Sections'

  # Check if the attribute exists on the domeGrid node
  #if(mel.attributeExists(attrName, baseNodeName)== 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="double", min=4, max=240, hasSoftMaxValue=True, softMaxValue=120, defaultValue=42 , keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  # Connect the domeGrid dome radius control to the sphere's revolve sections attribute:
  cmds.connectAttr((baseNodeName+'.'+attrName), makeRevolveNodeName+'.sections', force=True)
  
  #---------------------------------------------------------------------------
  # Add a Display Mode control to the domeGrid's transform node
  #---------------------------------------------------------------------------
  attrName = 'displayMode'
  #if(mel.attributeExists(attrName, baseNodeName)== 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="enum", en="Off:Wireframe:Shaded:Wireframe on Shaded", defaultValue=2, keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  #---------------------------------------------------------------------------
  # Add a Double Sided Rendering control to the domeGrid's transform node
  #---------------------------------------------------------------------------
  attrName = 'doubleSidedShading'
  #if(mel.attributeExists(attrName, baseNodeName)== 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="enum", en="Double Sided:Show Frontfaces:Show Backfaces", defaultValue=2, min=0, keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  #---------------------------------------------------------------------------
  # Add a Grid Line Thickness control to the domeGrid's transform node
  #---------------------------------------------------------------------------
  attrName = 'gridLineThickness'

  # This is the default starting value for the grid line strokes
  #initialGridLineThickness = 0.05
  
  # PlayblastVR compatible thicker lines
  initialGridLineThickness = 0.200

  # Check if the attribute exists on the domeGrid node
  #if(mel.attributeExists(attrName, baseNodeName)== 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="double", min=0.001, max=50, hasSoftMaxValue=True, softMaxValue=2, defaultValue=initialGridLineThickness, keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  # Connect the domeGrid Grid Line Thickness to the toon shader line width attribute:
  cmds.connectAttr((baseNodeName+'.'+attrName), domeToonShaderShape+'.lineWidth', force=True)

  #---------------------------------------------------------------------------
  # Add a Grid Line Color control to the domeGrid's transform node - Default color 1,1,0 = Yellow
  #---------------------------------------------------------------------------
  attrName = 'gridLineColor'
  attrRName = "gridLineColorR";
  attrGName = "gridLineColorG";
  attrBName = "gridLineColorB";
  #if(mel.attributeExists(attrName, baseNodeName)== 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="float3", usedAsColor=True, keyable=True)
  
  # Super Bright Yellow Color
  # cmds.addAttr(baseNodeName, parent=attrName, longName=attrRName, attributeType="float", keyable=True, defaultValue=15)
  # cmds.addAttr(baseNodeName, parent=attrName, longName=attrGName, attributeType="float", keyable=True, defaultValue=15)
  # cmds.addAttr(baseNodeName, parent=attrName, longName=attrBName, attributeType="float", keyable=True, defaultValue=0)

  # Normal Yellow Color
  cmds.addAttr(baseNodeName, parent=attrName, longName=attrRName, attributeType="float", keyable=True, defaultValue=1)
  cmds.addAttr(baseNodeName, parent=attrName, longName=attrGName, attributeType="float", keyable=True, defaultValue=1)
  cmds.addAttr(baseNodeName, parent=attrName, longName=attrBName, attributeType="float", keyable=True, defaultValue=0)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  # Connect the Grid Line Color swatch to the surface shader
  cmds.connectAttr((baseNodeName+'.'+attrName), domeGridlineMaterial+'.outColor', force=True)
  #---------------------------------------------------------------------------
  # Add a Grid Line Transparency control to the domeGrid's transform node - Default value 0.25
  #---------------------------------------------------------------------------
  attrName = 'gridLineTransparency'
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="double", keyable=True, defaultValue=0.0, min=0, max=1)
  
  # Connect the Grid Line transparency swatch to the surface shader
  cmds.connectAttr((baseNodeName+'.'+attrName), domeGridlineMaterial+'.outTransparencyR', force=True)
  cmds.connectAttr((baseNodeName+'.'+attrName), domeGridlineMaterial+'.outTransparencyG', force=True)
  cmds.connectAttr((baseNodeName+'.'+attrName), domeGridlineMaterial+'.outTransparencyB', force=True)

  #---------------------------------------------------------------------------
  # Add a Grid Surface Color control to the domeGrid's transform node - Default color 0,0,0 = Black
  #---------------------------------------------------------------------------
  attrName = 'gridSurfaceColor'
  attrRName = "gridSurfaceColorR";
  attrGName = "gridSurfaceColorG";
  attrBName = "gridSurfaceColorB";
  #if(mel.attributeExists(attrName, baseNodeName)== 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="float3", usedAsColor=True, keyable=True)
  cmds.addAttr(baseNodeName, parent=attrName, longName=attrRName, attributeType="float", keyable=True, defaultValue=0)
  cmds.addAttr(baseNodeName, parent=attrName, longName=attrGName, attributeType="float", keyable=True, defaultValue=0)
  cmds.addAttr(baseNodeName, parent=attrName, longName=attrBName, attributeType="float", keyable=True, defaultValue=0)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  
  # Connect the Grid Surface Color swatch to the surface shader
  cmds.connectAttr((baseNodeName+'.'+attrName), domeGridMaterial+'.outColor', force=True)
  #---------------------------------------------------------------------------
  # Add a Grid Surface Transparency control to the domeGrid's transform node - Default value 0.25
  #---------------------------------------------------------------------------
  attrName = 'gridSurfaceTransparency'
  cmds.addAttr(baseNodeName, longName=attrName, attributeType="double", keyable=True, defaultValue=.5, min=0, max=1)
  
  # Connect the Grid Surface transparency swatch to the surface shader
  cmds.connectAttr((baseNodeName+'.'+attrName), domeGridMaterial+'.outTransparencyR', force=True)
  cmds.connectAttr((baseNodeName+'.'+attrName), domeGridMaterial+'.outTransparencyG', force=True)
  cmds.connectAttr((baseNodeName+'.'+attrName), domeGridMaterial+'.outTransparencyB', force=True)


  #---------------------------------------------------------------------------  
  # Add a display mode expression to the domeGrid's transform node
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
  PreviewShapeExpr += "string $currentPanel;\n"
  PreviewShapeExpr += "if( " + domeRadiusTransform + "." + previewAttrName + " == 0){\n"
  PreviewShapeExpr += "  //Off Mode\n"
  PreviewShapeExpr += "  " + domeSurfaceShape + ".overrideDisplayType = 2;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideEnabled = 1;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideShading = 0;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".visibility = 0;\n"
  PreviewShapeExpr += "  MeshGroup.visibility = 0;\n"
  PreviewShapeExpr += "} else if(" + domeRadiusTransform + "." + previewAttrName + " == 1){\n"
  PreviewShapeExpr += "  //Wireframe Mode\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideEnabled = 1;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideShading = 0;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".visibility = 1;\n"
  PreviewShapeExpr += "  MeshGroup.visibility = 0;\n"
  PreviewShapeExpr += "} else if(" + domeRadiusTransform + "." + previewAttrName + " == 2){\n"
  PreviewShapeExpr += "  //Shaded Mode\n"
  PreviewShapeExpr += "  $currentPanel = \"modelPanel4\";\n"
  PreviewShapeExpr += "  if(`modelEditor -exists currentPanel`)\n"
  PreviewShapeExpr += "  modelEditor -edit -wireframeOnShaded 0 currentPanel;\n"
  PreviewShapeExpr += "  $currentPanel = \"StereoPanel\";\n"
  PreviewShapeExpr += "  if(`modelEditor -exists currentPanel`)\n"
  PreviewShapeExpr += "  modelEditor -edit -wireframeOnShaded 0 currentPanel;\n"
  PreviewShapeExpr += "  " + domeSurfaceShape + ".overrideDisplayType = 2;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideEnabled = 1;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideShading = 1;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".visibility = 1;\n"
  PreviewShapeExpr += "  MeshGroup.visibility = 1;\n"
  PreviewShapeExpr += "} else if(" + domeRadiusTransform + "." + previewAttrName + " == 3){\n"
  PreviewShapeExpr += "  //Wireframe on Shaded Mode\n"
  PreviewShapeExpr += "  $currentPanel = \"modelPanel4\";\n"
  PreviewShapeExpr += "  if(`modelEditor -exists currentPanel`)\n"
  PreviewShapeExpr += "  modelEditor -edit -wireframeOnShaded 1 currentPanel;\n"
  PreviewShapeExpr += "  $currentPanel = \"StereoPanel\";\n"
  PreviewShapeExpr += "  if(`modelEditor -exists currentPanel`)\n"
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
  # Add a Double Sided Shading expression to the domeGrid's transform node
  #---------------------------------------------------------------------------

  previewAttrName = "doubleSidedShading";

  PreviewShapeExpr += "// Custom Double Sided Shading Expressions\n\n"
  PreviewShapeExpr += "if(" + previewAttrName + " == 0){\n"
  PreviewShapeExpr += "  print(\"Double Sided Shading Enabled\\n\");\n"
  PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".doubleSided\" 1; \n"
  PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".opposite\" 0; \n"
  PreviewShapeExpr += "} else if(" + previewAttrName + " == 1){\n"
  PreviewShapeExpr += "  print(\"Backface Shading Enabled\\n\");\n"
  PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".doubleSided\" 0; \n"
  PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".opposite\" 0; \n"
  PreviewShapeExpr += "} else if(" + previewAttrName + " == 2){\n"
  PreviewShapeExpr += "  print(\"Frontface Shading Enabled\\n\");\n"
  PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".doubleSided\" 0; \n"
  PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".opposite\" 1; \n"
  PreviewShapeExpr += "}\n"

  print "DomeGrid Extra Attribute Expressions:"
  print PreviewShapeExpr

  cmds.expression(name=exprName, string=PreviewShapeExpr, object='domeGrid', alwaysEvaluate=True, unitConversion=all)

  # Force a first value into the double sided shading attribute
  cmds.setAttr((domeRadiusTransform+".doubleSidedShading"), 0)
  
  #---------------------------------------------------------------------------  
  # Select the domeGrid node in the Attribute Editor
  #---------------------------------------------------------------------------  
  mel.eval(' showEditorExact("' + domeRadiusTransform + '")')
  
  
"""
Domemaster3D createTestShapes
----------------------
A python function to create a test sphere and cube in Maya. 
"""

def  createTestShapes():
  import maya.cmds as cmds

  if cmds.objExists('domeTestLight'): 
    print('Removing existing Domemaster3D object: domeTestLight')
    cmds.select('domeTestLight', replace=True)
    cmds.delete()

  if cmds.objExists('polyTestSphere'): 
    print('Removing existing Domemaster3D object: polyTestSphere')
    cmds.select('polyTestSphere', replace=True)
    cmds.delete()

  if cmds.objExists('polyTestCube'): 
    print('Removing existing Domemaster3D object: polyTestCube')
    cmds.select('polyTestCube', replace=True)
    cmds.delete()

  test_sphere_name = cmds.polySphere(name='polyTestSphere', radius=24, subdivisionsX=20, subdivisionsY=20, axis=(0, 1, 0),  createUVs=2, constructionHistory=True)
  cmds.setAttr(test_sphere_name[0]+'.translateX', 80)
  cmds.setAttr(test_sphere_name[0]+'.translateY', 75)

  # Smooth the render time polygon sphere shape
  cmds.displaySmoothness(test_sphere_name, divisionsU=3, divisionsV=3, pointsWire=16, pointsShaded=4, polygonObject=3)

  test_cube_name = cmds.polyCube(name='polyTestCube', width=40, height=40, depth=40, subdivisionsX=1, subdivisionsY=1, subdivisionsZ=1, axis=(0, 1, 0),  createUVs=4, constructionHistory=True)
  cmds.setAttr(test_cube_name[0]+'.translateX', 0)
  cmds.setAttr(test_cube_name[0]+'.translateY', 75)
  cmds.setAttr(test_cube_name[0]+'.translateZ', -80)
  cmds.setAttr(test_cube_name[0]+'.rotateX', 88)
  cmds.setAttr(test_cube_name[0]+'.rotateY', 0)
  cmds.setAttr(test_cube_name[0]+'.rotateZ', 0)

  dome_light_shape_name = cmds.directionalLight()
  dome_light_name = getObjectParentNode(dome_light_shape_name)
  
  # Turn off casting shadows on the dome grid shape
  cmds.setAttr((dome_light_shape_name+'.aiCastShadows'), 0)
  
  # Increase the light brightness to 4x the default intensity
  cmds.setAttr((dome_light_shape_name+'.intensity'), 4)
  
  dome_light_name = cmds.rename(dome_light_name, "domeTestLight")

  cmds.setAttr((dome_light_name+'.translateX'), -32)
  cmds.setAttr((dome_light_name+'.rotateX'), 38)
  cmds.setAttr((dome_light_name+'.rotateY'), 47)
  cmds.setAttr((dome_light_name+'.rotateZ'), -62)


"""
A python function to make sure Arnold is active 
and the MR shading nodes are read to be used.
"""
def forceArnoldLoad():
  import maya.cmds as cmds
  import maya.mel as mel

  # Make sure the Arnold plugin was loaded
  if not(cmds.pluginInfo("mtoa",q=True,loaded=True)):
    cmds.loadPlugin("mtoa")
    print("The Arnold plugin was loaded.")
  #else:
  #  print("The Arnold plugin is already active.")

  # Set the active renderer to Arnold to avoid Hypershade red node errors 
  #mel.eval("setCurrentRenderer arnold")
  #or
  melRunString = 'import maya.mel as mel\n'
  melRunString += 'mel.eval(\"setCurrentRenderer arnold\")'
  #print("Deferred string: " + melRunString)
  cmds.evalDeferred(melRunString)
  

# Check what version of Maya is active
def getMayaVersionDome():
  import maya.cmds as cmds
  import maya.mel as mel

  # Check if we are running Maya 2011 or higher
  mayaVersion = mel.eval("getApplicationVersionAsFloat;")

  # Debug Test Mode
  # Test this GUI using the Maya 2010 - non-docked GUI mode
  #mayaVersion = 2010;

  # Write out the current Maya version number
  print("Maya " + str(mayaVersion)+ " detected.\n")
  
  return mayaVersion


"""
A python function to get the current object's shape node

getObjectShapeNode("stereoCamera")
# Result: [u'stereoCameraCenterCamShape', u'stereoCameraFrustum'] # 

"""

def getObjectShapeNode(object):
    import maya.cmds as cmds
    return cmds.listRelatives(object, children=True , shapes=True)


"""
A python function to get the current object's parent node

getObjectParentNode("nurbsSphereShape1")
# Result:  [u'nurbsSphere1'] #

"""

def getObjectParentNode(object):
    import maya.cmds as cmds
    return cmds.listRelatives(object, parent=True)
