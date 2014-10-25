"""
 LatLong_Stereo Camera Rig V1.6
 Updated 2014-10-24 09.21 pm
 by Andrew Hazelden  andrew@andrewhazelden.com
 -----------------------------------------------------------------------

 This script makes it easy to start creating fulldome stereoscopic content in Autodesk Maya.
 
 New in Version 1.6
 ---------------------
 Initial LatLong_Stereo support

 Changed the openGL viewport default focal length from 4 mm (160 degree FOV) to 18 mm (90 degree FOV)

 Updated the tilt map settings

 Modified the stereo camera name to have a random uppercase letter addon so each camera rig name is unique:
 This turns: DomeStereoCamera into DomeStereoCameraX
 
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
def getSourceImagesPath(imageFileName):
  import maya.cmds as cmds
  import maya.mel as mel
  
  # ---------------------------------------------------------------------
  #Setup the base folder path for the Domemaster3D control maps
  # ---------------------------------------------------------------------

  #Check OS platform for Windows/Mac/Linux Paths
  import platform

  #This is the base path for the images folder
  baseImagesFolder = ""

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

def createLensShaders(centerCam, leftCam, rightCam):
  import maya.mel as mel
  import maya.cmds as cmds
  print"Center: " + centerCam + "Left: " + leftCam + "Right: " + rightCam
  # ---------------------------------------------------------------------
  #Set up the base folder path for the Domemaster3D control maps
  # ---------------------------------------------------------------------
  
  #Variables
  separationMapFileTexture = getSourceImagesPath("latlong_separation_map.png") 
  # turnMapFileTexture = getSourceImagesPath("latlong_turn_map.png")
  # tiltMapFileTexture = getSourceImagesPath("latlong_head_tilt_map.png")

  # ---------------------------------------------------------------------
  # Create the fulldome nodes for the rig
  # ---------------------------------------------------------------------
  centerCamLens = cmds.shadingNode( 'LatLong_Stereo', n='center_LatLong_Stereo', asUtility=True  )
  cmds.setAttr( centerCamLens+'.Camera', 0 ) #Set the view to center
  
  leftCamLens = cmds.shadingNode( 'LatLong_Stereo', n='left_LatLong_Stereo', asUtility=True )
  cmds.setAttr( leftCamLens+'.Camera', 1 ) #Set the view to left
  
  rightCamLens = cmds.shadingNode( 'LatLong_Stereo', n='right_LatLong_Stereo', asUtility=True )
  cmds.setAttr( rightCamLens+'.Camera', 2 ) #Set the view to right

  # ---------------------------------------------------------------------
  #Connect the lens shaders
  # ---------------------------------------------------------------------
  cmds.connectAttr( centerCamLens+'.message', centerCam+'.miLensShader', force=True)
  cmds.connectAttr( leftCamLens+'.message', leftCam+'.miLensShader', force=True ) 
  cmds.connectAttr( rightCamLens+'.message', rightCam+'.miLensShader', force=True )
  
  # ---------------------------------------------------------------------
  # Link the common left and right camera attributes to the center camera
  # ---------------------------------------------------------------------
  # Link the right camera attributes
  cmds.connectAttr( centerCamLens+'.FOV_Vert_Angle', rightCamLens+'.FOV_Vert_Angle', force=True )
  cmds.connectAttr( centerCamLens+'.FOV_Horiz_Angle', rightCamLens+'.FOV_Horiz_Angle', force=True )
  cmds.connectAttr( centerCamLens+'.Parallax_Distance', rightCamLens+'.Parallax_Distance', force=True )
  cmds.connectAttr( centerCamLens+'.Cameras_Separation', rightCamLens+'.Cameras_Separation', force=True )
  cmds.connectAttr( centerCamLens+'.Cameras_Separation_Map', rightCamLens+'.Cameras_Separation_Map', force=True )
  cmds.connectAttr( centerCamLens+'.Head_Tilt_Map', rightCamLens+'.Head_Tilt_Map', force=True )
  cmds.connectAttr( centerCamLens+'.Zenith_Mode', rightCamLens+'.Zenith_Mode', force=True )
  cmds.connectAttr( centerCamLens+'.Flip_Ray_X', rightCamLens+'.Flip_Ray_X', force=True )
  cmds.connectAttr( centerCamLens+'.Flip_Ray_Y', rightCamLens+'.Flip_Ray_Y', force=True )
  
  # Link the left camera attributes
  cmds.connectAttr( centerCamLens+'.FOV_Vert_Angle', leftCamLens+'.FOV_Vert_Angle', force=True )
  cmds.connectAttr( centerCamLens+'.FOV_Horiz_Angle', leftCamLens+'.FOV_Horiz_Angle', force=True )
  cmds.connectAttr( centerCamLens+'.Parallax_Distance', leftCamLens+'.Parallax_Distance', force=True )
  cmds.connectAttr( centerCamLens+'.Cameras_Separation', leftCamLens+'.Cameras_Separation', force=True )
  cmds.connectAttr( centerCamLens+'.Cameras_Separation_Map', leftCamLens+'.Cameras_Separation_Map', force=True )
  cmds.connectAttr( centerCamLens+'.Head_Tilt_Map', leftCamLens+'.Head_Tilt_Map', force=True )
  cmds.connectAttr( centerCamLens+'.Zenith_Mode', leftCamLens+'.Zenith_Mode', force=True )
  cmds.connectAttr( centerCamLens+'.Flip_Ray_X', leftCamLens+'.Flip_Ray_X', force=True )
  cmds.connectAttr( centerCamLens+'.Flip_Ray_Y', leftCamLens+'.Flip_Ray_Y', force=True )
  
  # ---------------------------------------------------------------------
  #Set the default camera separation based upon the scene size
  # ---------------------------------------------------------------------
  #centerCamLens = "center_LatLong_Stereo"

  # Check the current Maya scene units
  # Possible Values: [mm | millimeter | cm | centimeter | m | meter | km | kilometer | in | inch | ft | foot | yd | yard | mi | mile]
  sceneScale = cmds.currentUnit( query=True, linear=True )
  print("Scene scale in: " + sceneScale)
  
  baseSeparationValue = 6
  baseDomeRadiusInCm = 360 / baseSeparationValue
  
  if sceneScale == "cm":
    defaultSeparation = 6
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "centimeter":
    defaultSeparation = 6
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "m":
    defaultSeparation = .06
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "meter":
    defaultSeparation = .06
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "km":
    defaultSeparation = 0.00006
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "kilometer":
    defaultSeparation = 0.00006
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "in":
    defaultSeparation = 2.362204724409449
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "inch":
    defaultSeparation = 2.362204724409449
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "ft":
    defaultSeparation = 0.1968503937007874
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "foot":
    defaultSeparation = 0.1968503937007874
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "yd":
    defaultSeparation = 0.065616797900262
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "yard":
    defaultSeparation = 0.065616797900262
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "mi":
    defaultSeparation = 3.728227153424004e-5
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "mile":
    defaultSeparation = 3.728227153424004e-5
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  
  #Set the camera separation
  cmds.setAttr(centerCamLens+'.Cameras_Separation', defaultSeparation)
  print("Camera Separation: " + str(defaultSeparation))
  
  #Set the dome radius
  cmds.setAttr(centerCamLens+'.Parallax_Distance', defaultDomeRadius)
  print("Parallax_Distance: " + str(defaultDomeRadius))
  
  # ---------------------------------------------------------------------
  # Create the custom Domemaster3D shading networks
  # ---------------------------------------------------------------------
  
  # Create the nodes
  separation_map_tex_filter = cmds.shadingNode( 'mib_texture_filter_lookup', n='separation_map_mib_texture_filter_lookup1', asTexture=True) 
  # turn_map_tex_filter =cmds.shadingNode( 'mib_texture_filter_lookup', n='turn_map_mib_texture_filter_lookup1', asTexture=True )
  # tilt_map_tex_filter =cmds.shadingNode( 'mib_texture_filter_lookup', n='tilt_map_mib_texture_filter_lookup1', asTexture=True )
  
  latlong_tex_vector = cmds.shadingNode( 'mib_texture_vector', n='latlong_mib_texture_vector1', asUtility=True )
  latlong_tex_remap = cmds.shadingNode( 'mib_texture_remap', n='latlong_mib_texture_remap1',  asUtility=True)
  
  separation_map_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='separation_map_mentalrayTexture1', asTexture=True)
  # turn_map_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='turn_map_mentalrayTexture1', asTexture=True )
  # tilt_map_mr_tex = cmds.shadingNode( 'mentalrayTexture', n='tilt_map_mentalrayTexture1', asTexture=True )
  
  # Set the node to use mode (4) which is screen space
  cmds.setAttr( latlong_tex_vector+'.selspace', 4)
  
  # Connect the nodes
  cmds.connectAttr( separation_map_tex_filter+'.outValueR', centerCamLens+'.Cameras_Separation_Map', force=True )
  cmds.connectAttr( separation_map_mr_tex+'.message', separation_map_tex_filter+'.tex', force=True )
  
  # cmds.connectAttr( turn_map_tex_filter+'.outValueR', centerCamLens+'.Head_Turn_Map', force=True )
  # cmds.connectAttr( turn_map_mr_tex+'.message', turn_map_tex_filter+'.tex', force=True )
  
  # cmds.connectAttr( tilt_map_tex_filter+'.outValueR', centerCamLens+'.Head_Tilt_Map', force=True )
  # cmds.connectAttr( tilt_map_mr_tex+'.message', tilt_map_tex_filter+'.tex', force=True )

  cmds.connectAttr( latlong_tex_vector+'.outValue', latlong_tex_remap+'.input', force=True )

  cmds.connectAttr( latlong_tex_remap+'.outValue', separation_map_tex_filter+'.coord', force=True )
  # cmds.connectAttr( latlong_tex_remap+'.outValue', turn_map_tex_filter+'.coord', force=True )
  # cmds.connectAttr( latlong_tex_remap+'.outValue', tilt_map_tex_filter+'.coord', force=True )

  cmds.setAttr( separation_map_mr_tex+'.fileTextureName', separationMapFileTexture , type="string")
  # cmds.setAttr( turn_map_mr_tex+'.fileTextureName', turnMapFileTexture, type="string")
  # cmds.setAttr( tilt_map_mr_tex+'.fileTextureName', tiltMapFileTexture, type="string")

  # ---------------------------------------------------------------------
  #Set up the stereo camera rig's preview shape settings
  # ---------------------------------------------------------------------
  # import maya.mel as mel
  
  # Select the center camera LatLong_Stereo node
  # cmds.select(centerCamLens, replace=True)
  
  # Select the center camera LatLong_Stereo node in the attribute editor
  # centerCamLens = "center_LatLong_Stereo"
  # mel.eval ( ' showEditorExact(" ' + centerCamLens + ' ") ' )
  # mel.eval ( ' showEditorExact(" ' + leftCamLens + ' ") ' )
  # mel.eval ( ' showEditorExact(" ' + rightCamLens + ' ") ' )

  # mel.eval ( ' showEditorExact(" ' + centerCamLens + ' ") ' )
  
  # ---------------------------------------------------------------------
  # Link the center camera lens shader to the Maya camera rig stereo3d settings
  # This enables real-time 3D previews in the viewport
  # ---------------------------------------------------------------------
  cmds.connectAttr( centerCamLens+'.Parallax_Distance', centerCam+'.zeroParallax', force=True )
  cmds.connectAttr( centerCamLens+'.Cameras_Separation', centerCam+'.interaxialSeparation', force=True )

  #Turn on Stereo 3D support for the Domemaster3D Maya camera rig
  cmds.setAttr( centerCam+'.stereo',  1)
  
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
  cmds.setAttr( slave + '.renderable', 0 )
  
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
    cmds.setAttr(slaveAttr, keyable=False )
    
  # Hide some more attributes on the transform
  #
  for attr in [ 'scaleX', 'scaleY', 'scaleZ',
                'visibility',
                'centerOfInterest' ] :
    cmds.setAttr( slave + '.' + attr, keyable=False )

  return slave

def __createFrustumNode( mainCam, parent, baseName ):
  """
  Private method to this module.
  Create a display frustum node under the given parent.
  Make the default connections between the master camera and the frustum  
  Remove some of the channel box attributes that we do not want to show
  up in the channel box. 
  """

  frustum = cmds.createNode( 'stereoRigFrustum', name=baseName, parent=parent )
  for attr in [ 'localPositionX', 'localPositionY', 'localPositionZ',
                'localScaleX', 'localScaleY', 'localScaleZ' ] :
    cmds.setAttr( frustum + '.' + attr, channelBox=False )

  for attr in ['displayNearClip', 'displayFarClip', 'displayFrustum',
               'zeroParallaxPlane',
               'zeroParallaxTransparency',
               'zeroParallaxColor',
               'safeViewingVolume',
               'safeVolumeTransparency',
               'safeVolumeColor',
               'safeStereo',
               'zeroParallax' ] :
    cmds.connectAttr( mainCam+'.'+attr, frustum+'.'+attr )
    
  return frustum

def createRig(unusedBasename='LatLongStereoCamera'):
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
  #print ("The StereoCameraRig Random letter extension is: LatLongStereoCamera" + randomLetterPostfix)

  #Put a temp throwaway value of unusedBasename as the createRig input variable
  #Define basename here instead of the regular createRig() variable
  basename='LatLongStereoCamera' + randomLetterPostfix

  # Create the root of the rig
  # 
  root = cmds.createNode( 'stereoRigTransform', name=basename )

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
                              parent=root )
  for attr in ['stereo', 'interaxialSeparation',
               'zeroParallax', 'toeInAdjust',
               'filmOffsetRightCam', 'filmOffsetLeftCam'] :
    cmds.connectAttr( centerCam+'.'+attr, root+'.'+attr )
  cmds.connectAttr( centerCam + '.focalLength', root + '.focalLengthInput' )
  #cmds.setAttr( centerCam + '.stereo', 2 )
  cmds.setAttr( centerCam + '.renderable', 0 )

  # Create the Frustum node, connect it to the root.
  #
  frustum = __createFrustumNode(centerCam, root, rootName + 'Frustum')
  
  # Create the left & right eye cameras
  # 
  leftCam  = __createSlaveCamera(centerCam, rootName+'Left',  root)
  rightCam = __createSlaveCamera(centerCam, rootName+'Right', root)
  
  # Set up message attribute connections to define the role of each camera
  #
  cmds.connectAttr( leftCam   + '.message', frustum + '.leftCamera' )
  cmds.connectAttr( rightCam  + '.message', frustum + '.rightCamera' )
  cmds.connectAttr( centerCam + '.message', frustum + '.centerCamera')

  # Connect the specific left and right output attributes of the root
  # transform to the corresponding left and right camera attributes.
  #
  cmds.connectAttr( root + '.stereoLeftOffset',  leftCam  + '.translateX')
  cmds.connectAttr( root + '.stereoRightOffset', rightCam + '.translateX')
  cmds.connectAttr( root + '.stereoLeftAngle',  leftCam  + '.rotateY' )
  cmds.connectAttr( root + '.stereoRightAngle', rightCam + '.rotateY' )
  cmds.connectAttr( root + '.filmBackOutputLeft',  leftCam  + '.hfo' )
  cmds.connectAttr( root + '.filmBackOutputRight', rightCam + '.hfo' )

  # Lock the attributes that should not be manipulated by the artist.
  #
  for attr in [ 'translate', 'rotate' ] :
    cmds.setAttr( leftCam  + '.' + attr, lock=True )
    cmds.setAttr( rightCam + '.' + attr, lock=True )

  
  #---------------------------------------------------------------------------
  # Custom LatLong Setup code
  #---------------------------------------------------------------------------
  # 4 mm focal length = 160 degree FOV
  #cmds.setAttr( centerCam + '.focalLength', 4 )

  # 18 mm focal length = 90 degree FOV
  cmds.setAttr( centerCam + '.focalLength', 18 )
  
  #cmds.setAttr( centerCam + '.stereo', 0 )
  #cmds.setAttr( centerCam + '.zeroParallax', 0.1 )
  #cmds.setAttr( centerCam + '.interaxialSeparation', 0 )
  
  # Create the fulldome stereo lens shaders
  createLensShaders(centerCam, leftCam, rightCam)
  
  #Align the base camera to point upwards
  #cmds.setAttr( root+'.rotateX', 90)
  cmds.setAttr( root+'.rotateX', 0)
  cmds.setAttr( root+'.rotateY', 0)
  cmds.setAttr( root+'.rotateZ', 0)
  
   # Link the new attribute 'Cam Locator Scale' to the dome camera's locator size control
  cmds.addAttr( root, longName='Cam_Locator_Scale', niceName='Cam Locator Scale', attributeType='double', defaultValue=1.0, minValue=0.01)
  cmds.setAttr( root+'.Cam_Locator_Scale', keyable=False, channelBox=True)
  
  # Result: Connected DomeStereoCamera.Cam_Locator_Scale to DomeStereoCameraLeftShape.locatorScale. // 
  cmds.connectAttr ( root+'.Cam_Locator_Scale', centerCam+'.locatorScale', force=True)
  cmds.connectAttr ( root+'.Cam_Locator_Scale', leftCam+'.locatorScale', force=True)
  cmds.connectAttr ( root+'.Cam_Locator_Scale', rightCam+'.locatorScale', force=True)
  
  #---------------------------------------------------------------------------
  cmds.select(root)
  
  return [root, leftCam, rightCam]

def attachToCameraSet( *args, **keywords ):
  # The camera set creation will notify after all layers have been
  # created.  It will contain the keyword allDone.  We ignore those
  # calls for now.
  #
  if not keywords.has_key( 'allDone' ):
    stereoCameraSets.parentToLayer0Rig( *args, cameraSet=keywords['cameraSet'] )

rigTypeName = 'LatLongStereoCamera'

def registerThisRig():
  """
  Registers the rig in Maya's database
  """

  mayaVersion = getMayaVersionDome()
  if (mayaVersion >= 2011):
    global rigTypeName 
    cmds.stereoRigManager( add=[rigTypeName, 'Python', 'LatLongStereoRig.createRig'] )
    cmds.stereoRigManager( cameraSetFunc=[rigTypeName, 'LatLongStereoRig.attachToCameraSet'] )
  else:
    cmds.stereoRigManager(add=['StereoCamera', 'Python', 'maya.app.stereo.stereoCameraDefaultRig.createRig'])

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
