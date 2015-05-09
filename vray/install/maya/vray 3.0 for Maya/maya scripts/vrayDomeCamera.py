"""
Vray Domemaster3D Camera Setup Script V1.7.0
2015-05-08 10.08 pm
Created by Andrew Hazelden  andrew@andrewhazelden.com

This script makes it easy to start creating fulldome stereoscopic content in Autodesk Maya.
-------------------------------------------------------------------------------------------------------

Version History

Version 1.7
---------------
2015-05-08 

Initial version for Vray

------------------------------------------------------------------------------

Force Vray to Load

Run using the command:
import vrayDomeCamera as vrayDomeCamera
reload(vrayDomeCamera)
vrayDomeCamera.forceVrayLoad()

------------------------------------------------------------------------------

Domemaster3D Fulldome Stereo Rig
A python function to create a fulldome stereo rig in Maya.

Run using the command:
import vrayDomeCamera as vrayDomeCamera
reload(vrayDomeCamera)
vrayDomeCamera.createVrayFulldomeStereoRig()

------------------------------------------------------------------------------

Domemaster3D createVrayLatLongStereoRig
A python function to create a stereoscopic latitude longitude lens shader and attach it to a camera.

Run using the command:
import vrayDomeCamera as vrayDomeCamera
reload(vrayDomeCamera)
vrayDomeCamera.createVrayLatLongStereoRig()

------------------------------------------------------------------------------

Domemaster3D getMayaVersionDome

A python function to check what Maya version is active.

import vrayDomeCamera
reload(vrayDomeCamera)
vrayDomeCamera.getMayaVersionDome()

------------------------------------------------------------------------------

"""


"""
Show the Domemaster Wiki
--------------------------------
Loads the wiki page in your default web browser

Run using the command:
print("Open the Domemaster Wiki Page")
import vrayDomeCamera as vrayDomeCamera
vrayDomeCamera.openDomemasterWiki()

print("Open the Domemaster NING Group")
import vrayDomeCamera as vrayDomeCamera
vrayDomeCamera.openDomemasterNing()

print("Open the Domemaster Downloads Page")
import vrayDomeCamera as vrayDomeCamera
vrayDomeCamera.openDomemasterDownloads()

print("Open the Domemaster Bug Reporter")
import vrayDomeCamera as vrayDomeCamera
vrayDomeCamera.openDomemasterBugReport()


"""

def openDomemasterWiki():
  import webbrowser
  
  # Domemaster Stereo Shader - Wiki Page
  url = 'https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages'
  
  # Open URL in new window, raising the window if possible.
  webbrowser.open_new(url)
  
  
def openVrayDomemasterNing():
  import webbrowser
  
  # Domemaster NING Group
  url = 'http://fulldome.ning.com/forum/topics/stereoscopic-domemaster-images'
  
  # Open URL in new window, raising the window if possible.
  webbrowser.open_new(url)


def openVrayDomemasterDownloads():
  import webbrowser
  
  # Domemaster Stereo Shader - Download Page
  url = 'https://github.com/zicher3d-org/domemaster-stereo-shader/releases'

  # Open URL in new window, raising the window if possible.
  webbrowser.open_new(url)
  
def openVrayDomemasterBugReport():
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
def Autosetup():
  setRenderRes()
  setDomeSamplingQuality()
  createVrayFulldomeStereoRig()

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
  
  # Make sure the Vray plugin was loaded
  #forceVrayLoad()
  
  #mel.eval('unifiedRenderGlobalsWindow;')


  fulldomeRenderWidth = 2048
  fulldomeRenderHeight = 2048
  
  #---------------------------------------------------------------------
  # Setup the default render settings for a square domemaster image output
  # ---------------------------------------------------------------------
  cmds.setAttr( 'defaultResolution.width', fulldomeRenderWidth )
  cmds.setAttr( 'defaultResolution.height', fulldomeRenderHeight )
  cmds.setAttr( 'defaultResolution.deviceAspectRatio', 1)
  cmds.setAttr( 'defaultResolution.pixelAspect', 1)
  
  # Check if the vray settings element exists in the scene
  domeCreateVraySettingsNode()
    
  cmds.setAttr( 'vraySettings.width', fulldomeRenderWidth)
  cmds.setAttr( 'vraySettings.height', fulldomeRenderHeight)
  cmds.setAttr( 'vraySettings.aspectRatio', 1)

"""
Domemaster3D changeRenderRes
----------------------
A python function to change the basic resolution square render settings. 

"""

def changeRenderRes( renderSizePx ):
  import maya.mel as mel
  import maya.cmds as cmds
  
  # Make sure the Vray plugin was loaded
  #forceVrayLoad()
  
  #mel.eval('unifiedRenderGlobalsWindow;')

  fulldomeRenderWidth = renderSizePx
  fulldomeRenderHeight = renderSizePx
  
  #---------------------------------------------------------------------
  # Setup the default render settings for a square domemaster image output
  # ---------------------------------------------------------------------
  cmds.setAttr( 'defaultResolution.width', fulldomeRenderWidth )
  cmds.setAttr( 'defaultResolution.height', fulldomeRenderHeight )
  cmds.setAttr( 'defaultResolution.deviceAspectRatio', 1)
  cmds.setAttr( 'defaultResolution.pixelAspect', 1)
  
  # Check if the vray settings element exists in the scene
  domeCreateVraySettingsNode()
    
  cmds.setAttr( 'vraySettings.width', fulldomeRenderWidth)
  cmds.setAttr( 'vraySettings.height', fulldomeRenderHeight)
  cmds.setAttr( 'vraySettings.aspectRatio', 1)

  print ("Changed the render settings to output a " + str(renderSizePx) + "x" + str(renderSizePx) + " image.")

  
"""
Domemaster3D changeRenderResWH
----------------------
A python function to change the basic resolution render settings. 

"""

def changeRenderResWH( renderSizeW,  renderSizeH):
  import maya.mel as mel
  import maya.cmds as cmds

  # Make sure the Vray plugin was loaded
  #forceVrayLoad()
  
  #mel.eval('unifiedRenderGlobalsWindow;')

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
  
  # Check if the vray settings element exists in the scene
  domeCreateVraySettingsNode()
  
  cmds.setAttr( 'vraySettings.width', domeRenderWidth)
  cmds.setAttr( 'vraySettings.height', domeRenderHeight)
  cmds.setAttr( 'vraySettings.aspectRatio', domeDeviceAspectRatio)

  print ("Changed the render settings to output a " + str(renderSizeW) + "x" + str(renderSizeW) + " image.")


  """
Domemaster3D Vray Settings Node Check
--------------------------------
A python function to create a VRaySettingsNode in Maya.
"""
def domeCreateVraySettingsNode():
  import maya.cmds as cmds

  # Check if the vray settings element exists in the scene
  if cmds.objExists('vraySettings'):
    print('A VRaySettingsNode exists in the scene.\n')
  else:
    cmds.createNode( 'VRaySettingsNode', name='vraySettings')
    print('Adding a VRaySettingsNode to the scene.\n')

  

"""
Domemaster3D Fulldome Stereo Rig
--------------------------------
A python function to create a fulldome stereo rig in Maya.
"""

def createVrayFulldomeStereoRig():
  import maya.cmds as cmds
  import maya.mel as mel
  
  # ---------------------------------------------------------------------
  # Setup the default Maya Settings
  # ---------------------------------------------------------------------
  cmds.loadPlugin( "stereoCamera", qt=True )
  
  # Make sure the Vray plugin was loaded
  forceVrayLoad()

  # Show the Render Settings Window so the Post Translator Action can be loaded
  mel.eval('unifiedRenderGlobalsWindow;')

  # Check if the vray settings element exists in the scene
  domeCreateVraySettingsNode()
  # ---------------------------------------------------------------------
  # Create the stereo rig
  # ---------------------------------------------------------------------
  
  #import maya.app.stereo.stereoCameraMenus as stereoCameraMenus
  #stereoCameraMenus.buildCreateMenu()
  #import maya.app.stereo.stereoCameraRig
  #maya.app.stereo.stereoCameraRig.createStereoCameraRig()
  
  from maya.app.stereo import stereoCameraRig
  
  # Set the default rig to an VrayDomemasterStereoCamera
  cmds.stereoRigManager(defaultRig='VrayDomemasterStereoCamera')
  
  # Add the camera rig to the scene
  rig = stereoCameraRig.createStereoCameraRig('VrayDomemasterStereoCamera')
  #[u'VrayDomeStereoCamera', u'VrayDomemasterStereoCameraLeft', u'VrayDomemasterStereoCameraRight']
  
  #Get the stereo camera rig shape nodes for the center/right/left cameras
  rig_center_shape_name = getObjectShapeNode(rig[0])
  #[u'stereoCameraCenterCamShape', u'stereoCameraFrustum'] #

  rig_left_shape_name = getObjectShapeNode(rig[1])
  # Result: [u'stereoCameraLeftShape'] #

  rig_right_shape_name = getObjectShapeNode(rig[2])
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

  #Set up the default AA sampling quality
  setDomeSamplingQuality()
  

  #---------------------------------------------------------------------------
  # Enable Real-time 3D in the OpenGL viewport 
  # using a PreRender and PostRender MEL script
  #---------------------------------------------------------------------------
  #import maya.cmds as cmds

  #PreRender MEL:
  #cmds.setAttr( 'defaultRenderGlobals.preMel', "source \"domeRender.mel\"; domemaster3DPreRenderMEL();", type='string')
  #PostRender MEL:
  #cmds.setAttr( 'defaultRenderGlobals.postMel' , "source \"domeRender.mel\"; domemaster3DPostRenderMEL();", type='string')

  #enable realtime 3D
  #mel.eval("source \"domeRender.mel\"; domemaster3DPostRenderMEL();");
  
  return rig
  

"""
Domemaster3D Fulldome Stereo Rig
--------------------------------
A python function to create a fulldome stereo rig in Maya.
"""

def createVrayLatLongStereoRig():
  import maya.cmds as cmds
  import maya.mel as mel
  
  # ---------------------------------------------------------------------
  # Setup the default Maya Settings
  # ---------------------------------------------------------------------
  cmds.loadPlugin( "stereoCamera", qt=True )
  
  # Make sure the Vray plugin was loaded
  forceVrayLoad()

  # Show the Render Settings Window so the Post Translator Action can be loaded
  mel.eval('unifiedRenderGlobalsWindow;')
  
  # Check if the vray settings element exists in the scene
  domeCreateVraySettingsNode()
  
  # ---------------------------------------------------------------------
  # Create the stereo rig
  # ---------------------------------------------------------------------
  
  #import maya.app.stereo.stereoCameraMenus as stereoCameraMenus
  #stereoCameraMenus.buildCreateMenu()
  #import maya.app.stereo.stereoCameraRig
  #maya.app.stereo.stereoCameraRig.createStereoCameraRig()
  
  from maya.app.stereo import stereoCameraRig
  
  # Set the default rig to an VrayLatLongStereoCamera
  cmds.stereoRigManager(defaultRig='VrayLatLongStereoCamera')
  
  # Add the camera rig to the scene
  rig = stereoCameraRig.createStereoCameraRig('VrayLatLongStereoCamera')
  #[u'VrayLatLongCamera', u'VrayLatLongCameraLeft', u'VrayLatLongCameraRight']
  
  #Get the stereo camera rig shape nodes for the center/right/left cameras
  rig_center_shape_name = getObjectShapeNode(rig[0])
  #[u'stereoCameraCenterCamShape', u'stereoCameraFrustum'] #

  rig_left_shape_name = getObjectShapeNode(rig[1])
  # Result: [u'stereoCameraLeftShape'] #

  rig_right_shape_name = getObjectShapeNode(rig[2])
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

  #Set up the default AA sampling quality
  setDomeSamplingQuality()
  
  #---------------------------------------------------------------------------
  # Enable Real-time 3D in the OpenGL viewport 
  # using a PreRender and PostRender MEL script
  #---------------------------------------------------------------------------
  #import maya.cmds as cmds

  #PreRender MEL:
  #cmds.setAttr( 'defaultRenderGlobals.preMel', "source \"domeRender.mel\"; domemaster3DPreRenderMEL();", type='string')
  #PostRender MEL:
  #cmds.setAttr( 'defaultRenderGlobals.postMel' , "source \"domeRender.mel\"; domemaster3DPostRenderMEL();", type='string')

  #enable realtime 3D
  #mel.eval("source \"domeRender.mel\"; domemaster3DPostRenderMEL();");
  
  return rig


"""
A python function to make sure Vray is active 
and the MR shading nodes are read to be used.
"""
def forceVrayLoad():
  import maya.cmds as cmds
  import maya.mel as mel

  # Make sure the Vray plugin was loaded
  if not (cmds.pluginInfo("vrayformaya",q=True,loaded=True)):
    cmds.loadPlugin("vrayformaya")
    print("The Vray plugin was loaded.")
  #else:
  #  print("The Vray plugin is already active.")

  #Set the active renderer to Vray to avoid Hypershade red node errors 
  #mel.eval("setCurrentRenderer vray")
  #or
  melRunString = 'import maya.mel as mel\n'
  melRunString += 'mel.eval(\"setCurrentRenderer vray\")'
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
