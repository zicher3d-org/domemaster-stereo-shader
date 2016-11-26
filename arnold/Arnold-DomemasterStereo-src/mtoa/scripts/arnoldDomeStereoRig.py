"""
 Arnold Domemaster3D Fulldome Stereo Rig V2.1.2
 2016-09-17
 by Andrew Hazelden  andrew@andrewhazelden.com
 -----------------------------------------------------------------------

 This script makes it easy to start creating fulldome stereoscopic content in Autodesk Maya.
 
 Version 2.1.2
 ---------------
 2016-09-17
 
 Code reformatting
 
 Version 1.6
 ---------------
 2014-10-31
 
 Adapted the mental ray script to support Arnold fulldome rendering

 Stereo Rig Script Notes
 --------------------------
 This rig is based upon the example file: stereoCameraDefaultRig.py

 The original file can be located at:
 C:\Program Files\Autodesk\Maya2014\Python\Lib\site-packages\maya\app\stereo\stereoCameraDefaultRig.py
 -----------------------------------------------------------------------
"""

def getMayaVersionDome():
  import maya.mel as mel
  import maya.cmds as cmds

  #Check what Maya version is active

  #Check if we are running Maya 2011 or higher
  mayaVersion = mel.eval("getApplicationVersionAsFloat;")

  #Test this GUI using the Maya 2010 - non-docked GUI mode
  #mayaVersion = 2010;

  #Write out the current Maya version number
  print("Maya " + str(mayaVersion) + " detected.\n")
  
  return mayaVersion

#-----------------------------------------------------------------------------

#Setup the stereo rig libraries
import maya.cmds as cmds

#Check if we are running Maya 2011+ and then add the stereoCameraSets module
mayaVersion = getMayaVersionDome()
if (mayaVersion >= 2011):
  from maya.app.stereo import stereoCameraSets

#-----------------------------------------------------------------------------

"""
Find out the path to the sourceimages folder
----------------------
A python function to check the operating system platform and the source images folder. 

"""

"""
def getSourceImagesPath(imageFileName):
  import os
  import maya.cmds as cmds
  import maya.mel as mel
  
  # ---------------------------------------------------------------------
  #Setup the base folder path for the Domemaster3D control maps
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
      # Check if the program is running on Windows 
      baseImagesFolder = "C:/Program Files/Domemaster3D/sourceimages/"
    elif platform.system()== 'win32':
      # Check if the program is running on Windows 32
      baseImagesFolder = "C:/Program Files (x86)/Domemaster3D/sourceimages/"
    elif platform.system()== 'Darwin':
      # Check if the program is running on macOS
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

  print "[Domemaster3D is running on a " + platform.system() + " System]"
  print "[Requesting the image file]: " + combinedFileAndImagePath

  return combinedFileAndImagePath
  """

def createLensShaders(centerCam, leftCam, rightCam):
  import maya.mel as mel
  import maya.cmds as cmds
  print "[Center] " + centerCam + " [Left] " + leftCam + " [Right] " + rightCam
  # ---------------------------------------------------------------------
  #Set up the base folder path for the Domemaster3D control maps
  # ---------------------------------------------------------------------
  
  #Variables
  # separationMapFileTexture = getSourceImagesPath("separation_map.png") 
  # turnMapFileTexture = getSourceImagesPath("turn_map.png")
  # tiltMapFileTexture = getSourceImagesPath("head_tilt_map.png")

  # Arnold camera type
  cameraType = 'DomemasterStereo'
  
  # Check if Arnold is loaded before linking the attributes
  if (cmds.pluginInfo("mtoa",q=True,loaded=True)):
    # Switch the active camera type
    #cmds.setAttr(centerCam+'.ai_translator', cameraType, type='string')
    cmds.setAttr(leftCam+'.ai_translator', cameraType, type='string')
    cmds.setAttr(rightCam+'.ai_translator', cameraType, type='string')
    
    # ---------------------------------------------------------------------
    # Create the fulldome nodes for the rig
    # ---------------------------------------------------------------------
    #cmds.setAttr(centerCam+'.aiCamera', 0 ) #Set the view to center
    
    cmds.setAttr(leftCam+'.aiCamera', 1 ) #Set the view to left
    cmds.setAttr(rightCam+'.aiCamera', 2 ) #Set the view to right

    # ---------------------------------------------------------------------
    # Link the common left and right camera attributes to the center camera
    # ---------------------------------------------------------------------
    # Link the right camera attributes
    cmds.connectAttr(leftCam+'.aiFovAngle', rightCam+'.aiFovAngle', force=True)
    cmds.connectAttr(leftCam+'.aiZeroParallaxSphere', rightCam+'.aiZeroParallaxSphere', force=True)
    cmds.connectAttr(leftCam+'.aiSeparation', rightCam+'.aiSeparation', force=True)
    cmds.connectAttr(leftCam+'.aiForwardTilt', rightCam+'.aiForwardTilt', force=True)
    cmds.connectAttr(leftCam+'.aiTiltCompensation', rightCam+'.aiTiltCompensation', force=True)
    cmds.connectAttr(leftCam+'.aiVerticalMode',  rightCam+'.aiVerticalMode' , force=True)
    
    cmds.connectAttr(leftCam+'.aiSeparationMap', rightCam+'.aiSeparationMap', force=True)
    cmds.connectAttr(leftCam+'.aiHeadTurnMap', rightCam+'.aiHeadTurnMap' , force=True)
    cmds.connectAttr(leftCam+'.aiHeadTiltMap', rightCam+'.aiHeadTiltMap', force=True)
    
    cmds.connectAttr(leftCam+'.aiFlipRayX', rightCam+'.aiFlipRayX', force=True)
    cmds.connectAttr(leftCam+'.aiFlipRayY', rightCam+'.aiFlipRayY', force=True)
    
    # ---------------------------------------------------------------------
    # Create the custom Domemaster3D shading networks
    # ---------------------------------------------------------------------
    
    # Create the nodes

    # ---------------------------------------------------------------------
    # Link the center camera lens shader to the Maya camera rig stereo3d settings
    # This enables real-time 3D previews in the viewport
    # ---------------------------------------------------------------------
    cmds.connectAttr(leftCam+'.aiZeroParallaxSphere', centerCam+'.zeroParallax', force=True)
    cmds.connectAttr(leftCam+'.aiSeparation', centerCam+'.interaxialSeparation', force=True)
    
    # Turn off the Stereo 3D effect on the native Maya camera rig
    # This skips the need for a pre-render and post-render mel script.
    cmds.setAttr(centerCam+'.stereo',  0)
  
"""
This module defines a Stereo Camera rig.

    createRig() creates the rig itself
    registerThisRig() registers it into the system
"""

def __createSlaveCamera(masterShape, name, parent):
  """
  Private method to this module.
  Create a slave camera
  Make the default connections between the master camera and the slave one.
  """

  # First create a camera under the right parent with the desired name
  #
  slave = cmds.camera()[0]
  slave = cmds.parent(slave, parent)[0]
  slave = cmds.rename(slave, name)
  slaveShape = cmds.listRelatives(slave, path=True, shapes=True)[0]
  
  # Change some default attributes
  #
  cmds.setAttr(slave + '.renderable', 0)
  
  # Connect the camera attributes from the master, hide them
  #
  for attr in [ 'horizontalFilmAperture',
                'verticalFilmAperture',
                'focalLength',
                'lensSqueezeRatio',
                'fStop',
                'focusDistance',
                'shutterAngle',
                'cameraPrecompTemplate',
                'filmFit',
                'displayFilmGate',
                'displayResolution',
                'nearClipPlane',
                'farClipPlane' ] :
    slaveAttr = slaveShape + '.' + attr
    cmds.connectAttr(masterShape + '.' + attr, slaveAttr)
    cmds.setAttr(slaveAttr, keyable=False)
    
  # Hide some more attributes on the transform
  #
  for attr in [ 'scaleX', 'scaleY', 'scaleZ',
                'visibility',
                'centerOfInterest' ] :
    cmds.setAttr(slave + '.' + attr, keyable=False)

  return slave

def __createFrustumNode(mainCam, parent, baseName):
  """
  Private method to this module.
  Create a display frustum node under the given parent.
  Make the default connections between the master camera and the frustum  
  Remove some of the channel box attributes that we do not want to show
  up in the channel box. 
  """

  frustum = cmds.createNode('stereoRigFrustum', name=baseName, parent=parent)
  for attr in [ 'localPositionX', 'localPositionY', 'localPositionZ',
                'localScaleX', 'localScaleY', 'localScaleZ' ] :
    cmds.setAttr(frustum + '.' + attr, channelBox=False)

  for attr in ['displayNearClip', 'displayFarClip', 'displayFrustum',
               'zeroParallaxPlane',
               'zeroParallaxTransparency',
               'zeroParallaxColor',
               'safeViewingVolume',
               'safeVolumeTransparency',
               'safeVolumeColor',
               'safeStereo',
               'zeroParallax' ] :
    cmds.connectAttr(mainCam+'.'+attr, frustum+'.'+attr)
    
  return frustum

def createRig(unusedBasename='ArnoldDomeStereoCamera'):
  """
  Creates a new stereo rig. Uses a series of Maya commands to build
  a stereo rig.
  
  The optional argument basename defines the base name for each DAG
  object that will be created.
  """

  #Create a random camera letter "extension" to fix the unique camera issue with the camera aim, and aim+up add-on bug
  import string
  import random
  randomLetterPostfix = random.choice(string.ascii_uppercase)
  #print ("The StereoCameraRig Random letter extension is: ArnoldDomeStereoCamera" + randomLetterPostfix)

  #Put a temp throwaway value of unusedBasename as the createRig input variable
  #Define basename here instead of the regular createRig() variable
  basename='ArnoldDomeStereoCamera' + randomLetterPostfix

  # Create the root of the rig
  # 
  root = cmds.createNode('stereoRigTransform', name=basename)

  # The actual basename use is the name of the top transform. If a
  # second rig is created, the default base name may be incremented
  # (e.g. stereoRig1). We want to use the same name for the whole
  # hierarchy.
  # If such a name already exists, root will be a partial path. Keep
  # only the last part for the name.
  #
  rootName = root.split('|')[-1]

  # Create the center (main) camera
  # Connect the center camera attributes to the root
  # Change any default parameters.
  #
  centerCam = cmds.createNode('stereoRigCamera',
                              name=rootName + 'CenterCamShape',
                              parent=root)
  for attr in ['stereo', 'interaxialSeparation',
               'zeroParallax', 'toeInAdjust',
               'filmOffsetRightCam', 'filmOffsetLeftCam'] :
    cmds.connectAttr(centerCam+'.'+attr, root+'.'+attr )
  cmds.connectAttr(centerCam + '.focalLength', root + '.focalLengthInput' )
  #cmds.setAttr(centerCam + '.stereo', 2 )
  cmds.setAttr(centerCam + '.renderable', 0 )

  # Create the Frustum node, connect it to the root.
  #
  frustum = __createFrustumNode(centerCam, root, rootName + 'Frustum')
  
  # Create the left & right eye cameras
  # 
  leftCam  = __createSlaveCamera(centerCam, rootName+'Left',  root)
  rightCam = __createSlaveCamera(centerCam, rootName+'Right', root)
  
  # Set up message attribute connections to define the role of each camera
  #
  cmds.connectAttr(leftCam + '.message', frustum + '.leftCamera')
  cmds.connectAttr(rightCam + '.message', frustum + '.rightCamera')
  cmds.connectAttr(centerCam + '.message', frustum + '.centerCamera')

  # Connect the specific left and right output attributes of the root
  # transform to the corresponding left and right camera attributes.
  #
  cmds.connectAttr(root + '.stereoLeftOffset',  leftCam  + '.translateX')
  cmds.connectAttr(root + '.stereoRightOffset', rightCam + '.translateX')
  cmds.connectAttr(root + '.stereoLeftAngle',  leftCam  + '.rotateY')
  cmds.connectAttr(root + '.stereoRightAngle', rightCam + '.rotateY')
  cmds.connectAttr(root + '.filmBackOutputLeft',  leftCam  + '.hfo')
  cmds.connectAttr(root + '.filmBackOutputRight', rightCam + '.hfo')

  # Lock the attributes that should not be manipulated by the artist.
  #
  for attr in [ 'translate', 'rotate' ] :
    cmds.setAttr(leftCam  + '.' + attr, lock=True)
    cmds.setAttr(rightCam + '.' + attr, lock=True)

  
  #---------------------------------------------------------------------------
  # Custom Domemaster3D Setup code
  #---------------------------------------------------------------------------
  # 4 mm focal length = 160 degree FOV
  #cmds.setAttr(centerCam + '.focalLength', 4 )

  # 18 mm focal length = 90 degree FOV
  cmds.setAttr(centerCam + '.focalLength', 18)
  
  #cmds.setAttr(centerCam + '.stereo', 0)
  #cmds.setAttr(centerCam + '.zeroParallax', 0.1)
  #cmds.setAttr(centerCam + '.interaxialSeparation', 0)
  
  # Create the fulldome stereo lens shaders
  createLensShaders(centerCam, leftCam, rightCam)
  
  # Align the base camera to point upwards
  cmds.setAttr(root+'.rotateX', 90)
  cmds.setAttr(root+'.rotateY', 0)
  cmds.setAttr(root+'.rotateZ', 0)
  
   # Link the new attribute 'Cam Locator Scale' to the dome camera's locator size control
  cmds.addAttr( root, longName='Cam_Locator_Scale', niceName='Cam Locator Scale', attributeType='double', defaultValue=1.0, minValue=0.01)
  cmds.setAttr(root+'.Cam_Locator_Scale', keyable=False, channelBox=True)
  
  # Result: Connected DomeStereoCamera.Cam_Locator_Scale to DomeStereoCameraLeftShape.locatorScale. // 
  cmds.connectAttr(root+'.Cam_Locator_Scale', centerCam+'.locatorScale', force=True)
  cmds.connectAttr(root+'.Cam_Locator_Scale', leftCam+'.locatorScale', force=True)
  cmds.connectAttr(root+'.Cam_Locator_Scale', rightCam+'.locatorScale', force=True)
  
  #---------------------------------------------------------------------------
  cmds.select(root)
  
  return [root, leftCam, rightCam]

def attachToCameraSet(*args, **keywords):
  # The camera set creation will notify after all layers have been
  # created.  It will contain the keyword allDone.  We ignore those
  # calls for now.
  #
  if not keywords.has_key('allDone'):
    stereoCameraSets.parentToLayer0Rig( *args, cameraSet=keywords['cameraSet'] )

rigTypeName = 'ArnoldDomeStereoCamera'

def registerThisRig():
  """
  Registers the rig in Maya's database
  """
  
  mayaVersion = getMayaVersionDome()
  if (mayaVersion >= 2011):
    global rigTypeName 
    cmds.stereoRigManager(add=[rigTypeName, 'Python', 'arnoldDomeStereoRig.createRig'] )
    cmds.stereoRigManager(cameraSetFunc=[rigTypeName, 'arnoldDomeStereoRig.attachToCameraSet'])
  else:
    cmds.stereoRigManager(add=['StereoCamera', 'Python', 'maya.app.stereo.stereoCameraDefaultRig.createRig'])

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
    return cmds.listRelatives( object, parent=True)
