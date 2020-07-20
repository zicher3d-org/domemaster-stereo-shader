"""
 Domemain3D Fulldome Stereo Rig V2.4
 2018-08-21
 by Andrew Hazelden  andrew@andrewhazelden.com
 -----------------------------------------------------------------------

 This script makes it easy to start creating fulldome stereoscopic content in Autodesk Maya.
 
 Version 2.1
 -------------
 2016-08-02
 
 Added Maya 2017+ support for creating Maya file node based screen space texture maps with the help of a mib_texture_vector node and a place2Dtexture node. This replaces the previous mentalrayTexture node based approach that has been depreciated in Maya 2017.
 
 Version 1.9.1 
 -------------
 2015-10-15

 Added the ability to use a "DOMEMASTER3D_MAYA_REALTIME_FOV" environment variable through your operating system, the Maya.env file, or a Maya module file to set the realtime OpenGL "persp" viewport field of view FOV value for domeAFL_FOV, domeAFL_FOV_Stereo, latlong_lens, and LatLong_Stereo camera rigs. Typical values would be 4 (mm) for a wide angle 160 degree FOV in the OpenGL persp viewport, or 18 (mm) for a regular 90 degree view.

In a Maya.env file you would change this environment variable by adding a line like this. (4 in this example means a 4mm lens):

 DOMEMASTER3D_MAYA_REALTIME_FOV=4
 
 Version 1.8
 ------------
 2015-08-21

 Version 1.7
 ------------
 2015-03-07
 
 Version 1.6
 ------------
 Oct 3, 2014

 Updated the sourceimages path code to allow the installation of the Domemain3D shader to a folder other than the default path.
 
 New in Version 1.5
 ------------------
 Changed the openGL viewport default focal length from 4 mm (160 degree FOV) to 18 mm (90 degree FOV)

 Updated the tilt map settings

 Modified the stereo camera name to have a random uppercase letter addon so each camera rig name is unique:
 This turns: DomeStereoCamera into DomeStereoCameraX

The sepration, turn, and tilt source images are loaded using the DOMEMASTER3D_SOURCEIMAGES_DIR value defined in your maya.env file.

 Stereo Rig Script Notes
 --------------------------
 This rig is based upon the example file: stereoCameraDefaultRig.py

 The original file can be located at:
 C:\Program Files\Autodesk\Maya2014\Python\Lib\site-packages\maya\app\stereo\stereoCameraDefaultRig.py
 -----------------------------------------------------------------------
"""

# Check what Maya version is active
def getMayaVersionDome():
  import maya.mel as mel
  import maya.cmds as cmds

  # Check if we are running Maya 2011 or higher
  mayaVersion = mel.eval("getApplicationVersionAsFloat;")

  # Test this GUI using the Maya 2010 - non-docked GUI mode
  #mayaVersion = 2010;

  # Write out the current Maya version number
  print("Maya " + str(mayaVersion) + " detected.\n")
  
  return mayaVersion

#-----------------------------------------------------------------------------

# Setup the stereo rig libraries
import maya.cmds as cmds

# Check if we are running Maya 2011+ and then add the stereoCameraSets module
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
  import os
  import maya.cmds as cmds
  import maya.mel as mel
  # ---------------------------------------------------------------------
  # Set up the base folder path for the Domemain3D control maps
  # ---------------------------------------------------------------------

  # Check OS platform for Windows/Mac/Linux Paths
  import platform

  # This is the base path for the images folder
  baseImagesFolder = ""
  
  # Try and read the value from the current Maya.env file's environment variables
  baseImagesFolder = os.environ.get('DOMEMASTER3D_SOURCEIMAGES_DIR') + "/"
  # Typical Result: C:/Program Files/Domemain3D/sourceimages/ 
  
  # Use a fixed value if the env var is empty
  if baseImagesFolder == None:
    if platform.system()=='Windows':
      # Check if the program is running on Windows 
      baseImagesFolder = "C:/Program Files/Domemain3D/sourceimages/"
    elif platform.system()== 'win32':
      # Check if the program is running on Windows 32
      baseImagesFolder = "C:/Program Files (x86)/Domemain3D/sourceimages/"
    elif platform.system()== 'Darwin':
      # Check if the program is running on macOS
      baseImagesFolder = "/Applications/Domemain3D/sourceimages/"
    elif platform.system()== 'Linux':
      # Check if the program is running on Linux
      baseImagesFolder = "/opt/Domemain3D/sourceimages/"
    elif platform.system()== 'Linux2':
      # Check if the program is running on Linux
      baseImagesFolder = "/opt/Domemain3D/sourceimages/"
    else:
      # Create the empty variable as a fallback mode
      baseImagesFolder = ""

  combinedFileAndImagePath = baseImagesFolder + imageFileName

  print "[Domemain3D is running on a " + platform.system() + " System]"
  print "[Requesting the image file]: " + combinedFileAndImagePath

  return combinedFileAndImagePath

def createLensShaders(centerCam, leftCam, rightCam):
  import maya.mel as mel
  import maya.cmds as cmds
  print"Center: " + centerCam + "Left: " + leftCam + "Right: " + rightCam
  # ---------------------------------------------------------------------
  # Set up the base folder path for the Domemain3D control maps
  # ---------------------------------------------------------------------
  
  # Variables
  separationMapFileTexture = getSourceImagesPath("separation_map.png") 
  turnMapFileTexture = getSourceImagesPath("turn_map.png")
  tiltMapFileTexture = getSourceImagesPath("head_tilt_map.png")

  # ---------------------------------------------------------------------
  # Create the fulldome nodes for the rig
  # ---------------------------------------------------------------------
  centerCamLens = cmds.shadingNode('domeAFL_FOV_Stereo', n='center_domeAFL_FOV_Stereo', asUtility=True)
  cmds.setAttr(centerCamLens+'.Camera', 0) # Set the view to center
  
  leftCamLens = cmds.shadingNode('domeAFL_FOV_Stereo', n='left_domeAFL_FOV_Stereo', asUtility=True)
  cmds.setAttr(leftCamLens+'.Camera', 1) # Set the view to left
  
  rightCamLens = cmds.shadingNode('domeAFL_FOV_Stereo', n='right_domeAFL_FOV_Stereo', asUtility=True)
  cmds.setAttr(rightCamLens+'.Camera', 2) # Set the view to right

  # ---------------------------------------------------------------------
  # Connect the lens shaders
  # ---------------------------------------------------------------------
  cmds.connectAttr(centerCamLens+'.message', centerCam+'.miLensShader', force=True)
  cmds.connectAttr(leftCamLens+'.message', leftCam+'.miLensShader', force=True) 
  cmds.connectAttr(rightCamLens+'.message', rightCam+'.miLensShader', force=True)
  
  # ---------------------------------------------------------------------
  # Link the common left and right camera attributes to the center camera
  # ---------------------------------------------------------------------
  # Link the right camera attributes
  cmds.connectAttr(centerCamLens+'.FOV_Angle', rightCamLens+'.FOV_Angle', force=True)
  cmds.connectAttr(centerCamLens+'.Dome_Radius', rightCamLens+'.Dome_Radius', force=True)
  cmds.connectAttr(centerCamLens+'.Dome_Tilt', rightCamLens+'.Dome_Tilt', force=True)
  cmds.connectAttr(centerCamLens+'.Dome_Tilt_Compensation', rightCamLens+'.Dome_Tilt_Compensation', force=True)
  cmds.connectAttr(centerCamLens+'.Cameras_Separation', rightCamLens+'.Cameras_Separation', force=True)
  cmds.connectAttr(centerCamLens+'.Vertical_Mode',  rightCamLens+'.Vertical_Mode' , force=True)
  cmds.connectAttr(centerCamLens+'.Cameras_Separation_Map', rightCamLens+'.Cameras_Separation_Map', force=True)
  cmds.connectAttr(centerCamLens+'.Head_Turn_Map', rightCamLens+'.Head_Turn_Map' , force=True)
  cmds.connectAttr(centerCamLens+'.Head_Tilt_Map', rightCamLens+'.Head_Tilt_Map', force=True)
  cmds.connectAttr(centerCamLens+'.Flip_Ray_X', rightCamLens+'.Flip_Ray_X', force=True)
  cmds.connectAttr(centerCamLens+'.Flip_Ray_Y', rightCamLens+'.Flip_Ray_Y', force=True)
  
  # Link the left camera attributes
  cmds.connectAttr(centerCamLens+'.FOV_Angle', leftCamLens+'.FOV_Angle', force=True)
  cmds.connectAttr(centerCamLens+'.Dome_Radius', leftCamLens+'.Dome_Radius', force=True)
  cmds.connectAttr(centerCamLens+'.Dome_Tilt', leftCamLens+'.Dome_Tilt', force=True)
  cmds.connectAttr(centerCamLens+'.Dome_Tilt_Compensation', leftCamLens+'.Dome_Tilt_Compensation', force=True)
  cmds.connectAttr(centerCamLens+'.Cameras_Separation', leftCamLens+'.Cameras_Separation', force=True)
  cmds.connectAttr(centerCamLens+'.Vertical_Mode',  leftCamLens+'.Vertical_Mode', force=True)
  cmds.connectAttr(centerCamLens+'.Cameras_Separation_Map', leftCamLens+'.Cameras_Separation_Map', force=True)
  cmds.connectAttr(centerCamLens+'.Head_Turn_Map', leftCamLens+'.Head_Turn_Map', force=True)
  cmds.connectAttr(centerCamLens+'.Head_Tilt_Map', leftCamLens+'.Head_Tilt_Map', force=True)
  cmds.connectAttr(centerCamLens+'.Flip_Ray_X', leftCamLens+'.Flip_Ray_X', force=True)
  cmds.connectAttr(centerCamLens+'.Flip_Ray_Y', leftCamLens+'.Flip_Ray_Y', force=True)
  
  # ---------------------------------------------------------------------
  # Set the default camera separation based upon the scene size
  # ---------------------------------------------------------------------
  #centerCamLens = "center_domeAFL_FOV_Stereo"

  # Check the current Maya scene units
  # Possible Values: [mm | millimeter | cm | centimeter | m | meter | km | kilometer | in | inch | ft | foot | yd | yard | mi | mile]
  sceneScale = cmds.currentUnit(query=True, linear=True)
  print("Scene scale in: " + sceneScale)
  
  baseSeparationValue = 6.5
  baseDomeRadiusInCm = 360 / baseSeparationValue
  
  if sceneScale == "cm":
    defaultSeparation = 6.5
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "centimeter":
    defaultSeparation = 6.5
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "m":
    defaultSeparation = .065
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "meter":
    defaultSeparation = .065
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "km":
    defaultSeparation = 0.000065
    defaultDomeRadius = baseDomeRadiusInCm * defaultSeparation
  elif sceneScale == "kilometer":
    defaultSeparation = 0.000065
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
  
  # Set the camera separation
  cmds.setAttr(centerCamLens+'.Cameras_Separation', defaultSeparation)
  print("Camera Separation: " + str(defaultSeparation))
  
  # Set the dome radius
  cmds.setAttr(centerCamLens+'.Dome_Radius', defaultDomeRadius)
  print("Dome Radius: " + str(defaultDomeRadius))
  
  # ---------------------------------------------------------------------
  # Create the custom Domemain3D shading networks
  # ---------------------------------------------------------------------
  
  mayaVersion = getMayaVersionDome()
  if(mayaVersion <= 2015):
    # Temporary: Do the dev testing for Maya 2017 using Maya 2016
  #if (mayaVersion <= 2016):
    # Maya 2010-2016.5 uses a stock mentalrayTexture approach

    # Create the nodes
    separation_map_tex_filter = cmds.shadingNode('mib_texture_filter_lookup', n='separation_map_mib_texture_filter_lookup1', asTexture=True) 
    turn_map_tex_filter = cmds.shadingNode('mib_texture_filter_lookup', n='turn_map_mib_texture_filter_lookup1', asTexture=True)
    tilt_map_tex_filter = cmds.shadingNode('mib_texture_filter_lookup', n='tilt_map_mib_texture_filter_lookup1', asTexture=True)

    dome_tex_vector = cmds.shadingNode('mib_texture_vector', n='dome_mib_texture_vector1', asUtility=True)
    dome_tex_remap = cmds.shadingNode('mib_texture_remap', n='dome_mib_texture_remap1',  asUtility=True)

    separation_map_mr_tex = cmds.shadingNode('mentalrayTexture', n='separation_map_mentalrayTexture1', asTexture=True)
    turn_map_mr_tex = cmds.shadingNode('mentalrayTexture', n='turn_map_mentalrayTexture1', asTexture=True)
    tilt_map_mr_tex = cmds.shadingNode('mentalrayTexture', n='tilt_map_mentalrayTexture1', asTexture=True)

    # Set the node to use mode (4) which is screen space
    cmds.setAttr(dome_tex_vector+'.selspace', 4)

    # Connect the nodes
    cmds.connectAttr(separation_map_tex_filter+'.outValueR', centerCamLens+'.Cameras_Separation_Map', force=True)
    cmds.connectAttr(separation_map_mr_tex+'.message', separation_map_tex_filter+'.tex', force=True)

    cmds.connectAttr(turn_map_tex_filter+'.outValueR', centerCamLens+'.Head_Turn_Map', force=True)
    cmds.connectAttr(turn_map_mr_tex+'.message', turn_map_tex_filter+'.tex', force=True)

    cmds.connectAttr(tilt_map_tex_filter+'.outValueR', centerCamLens+'.Head_Tilt_Map', force=True)
    cmds.connectAttr(tilt_map_mr_tex+'.message', tilt_map_tex_filter+'.tex', force=True)

    cmds.connectAttr(dome_tex_vector+'.outValue', dome_tex_remap+'.input', force=True)

    cmds.connectAttr(dome_tex_remap+'.outValue', separation_map_tex_filter+'.coord', force=True)
    cmds.connectAttr(dome_tex_remap+'.outValue', turn_map_tex_filter+'.coord', force=True)
    cmds.connectAttr(dome_tex_remap+'.outValue', tilt_map_tex_filter+'.coord', force=True)

    cmds.setAttr(separation_map_mr_tex+'.fileTextureName', separationMapFileTexture , type="string")
    cmds.setAttr(turn_map_mr_tex+'.fileTextureName', turnMapFileTexture, type="string")
    cmds.setAttr(tilt_map_mr_tex+'.fileTextureName', tiltMapFileTexture, type="string")
  else:
    # Maya 2017+ uses a maya file node based screen space texture approach

    # Create the nodes
    dome_tex_vector = cmds.shadingNode('mib_texture_vector', n='dome_mib_texture_vector1', asUtility=True)

    # Set the node to use mode (4) which is screen space
    cmds.setAttr(dome_tex_vector+'.selspace', 4)

    dome_maya_placement = cmds.shadingNode('place2dTexture', n='dome_place2dTexture', asUtility=True) 

    separation_map_maya_tex = cmds.shadingNode('file', n='separation_map_FileTexture', asTexture=True)

    turn_map_maya_tex = cmds.shadingNode('file', n='turn_map_FileTexture', asTexture=True)

    tilt_map_maya_tex = cmds.shadingNode('file', n='tilt_map_FileTexture', asTexture=True)


    # Connect the place2D texture to the Maya file texture
    for tex in [separation_map_maya_tex, turn_map_maya_tex, tilt_map_maya_tex]:
      cmds.connectAttr(dome_maya_placement+'.coverage', tex+'.coverage', f=True)
      cmds.connectAttr(dome_maya_placement+'.translateFrame', tex+'.translateFrame', f=True)
      cmds.connectAttr(dome_maya_placement+'.rotateFrame', tex+'.rotateFrame', f=True)
      cmds.connectAttr(dome_maya_placement+'.mirrorU', tex+'.mirrorU', f=True)
      cmds.connectAttr(dome_maya_placement+'.mirrorV', tex+'.mirrorV', f=True)
      cmds.connectAttr(dome_maya_placement+'.stagger', tex+'.stagger', f=True)
      cmds.connectAttr(dome_maya_placement+'.wrapU', tex+'.wrapU', f=True)
      cmds.connectAttr(dome_maya_placement+'.wrapV', tex+'.wrapV', f=True)
      cmds.connectAttr(dome_maya_placement+'.repeatUV', tex+'.repeatUV', f=True)
      cmds.connectAttr(dome_maya_placement+'.offset', tex+'.offset', f=True)
      cmds.connectAttr(dome_maya_placement+'.rotateUV', tex+'.rotateUV', f=True)
      cmds.connectAttr(dome_maya_placement+'.noiseUV', tex+'.noiseUV', f=True)
      cmds.connectAttr(dome_maya_placement+'.vertexUvOne', tex+'.vertexUvOne', f=True)
      cmds.connectAttr(dome_maya_placement+'.vertexUvTwo', tex+'.vertexUvTwo', f=True)
      cmds.connectAttr(dome_maya_placement+'.vertexUvThree', tex+'.vertexUvThree', f=True)
      cmds.connectAttr(dome_maya_placement+'.vertexCameraOne', tex+'.vertexCameraOne', f=True)
      #cmds.connectAttr(dome_maya_placement+'.outUV', tex+'.uvCoord', f=True)
      cmds.connectAttr(dome_maya_placement+'.outUvFilterSize', tex+'.uvFilterSize', f=True)

      # Hook the mental ray texture vector node to the file node's UV coordinates inputs
      cmds.connectAttr(dome_tex_vector+'.outValueX', tex+'.uCoord', f=True)
      cmds.connectAttr(dome_tex_vector+'.outValueY', tex+'.vCoord', f=True)

      # End of the "for tex" loop section
    
    # Assign an initial texture maps to the file nodes
    cmds.setAttr(separation_map_maya_tex+'.fileTextureName', separationMapFileTexture, type="string")
    cmds.setAttr(turn_map_maya_tex+'.fileTextureName', turnMapFileTexture, type="string")
    cmds.setAttr(tilt_map_maya_tex+'.fileTextureName', tiltMapFileTexture, type="string")

    # Connect the nodes
    cmds.connectAttr(separation_map_maya_tex+'.outColorR', centerCamLens+'.Cameras_Separation_Map', force=True)

    cmds.connectAttr(turn_map_maya_tex+'.outColorR', centerCamLens+'.Head_Turn_Map', force=True)

    cmds.connectAttr(tilt_map_maya_tex+'.outColorR', centerCamLens+'.Head_Tilt_Map', force=True)


  # ---------------------------------------------------------------------
  # Set up the stereo camera rig's preview shape settings
  # ---------------------------------------------------------------------
  #import maya.mel as mel
  
  # Select the center camera domeAFL_FOV_Stereo node
  #cmds.select(centerCamLens, replace=True)
  
  # Select the center camera domeAFL_FOV_Stereo node in the attribute editor
  #centerCamLens = "center_domeAFL_FOV_Stereo"
  #mel.eval('showEditorExact(" ' + centerCamLens + ' ")')
  #mel.eval('showEditorExact(" ' + leftCamLens + ' ")')
  #mel.eval('showEditorExact(" ' + rightCamLens + ' ")')

  #mel.eval('showEditorExact(" ' + centerCamLens + ' ")')
  
  # ---------------------------------------------------------------------
  # Link the center camera lens shader to the Maya camera rig stereo3d settings
  # This enables real-time 3D previews in the viewport
  # ---------------------------------------------------------------------
  cmds.connectAttr(centerCamLens+'.Dome_Radius', centerCam+'.zeroParallax', force=True)
  cmds.connectAttr(centerCamLens+'.Cameras_Separation', centerCam+'.interaxialSeparation', force=True)

  # Turn on Stereo 3D support for the Domemain3D Maya camera rig
  cmds.setAttr(centerCam+'.stereo',  1)
  
"""
This module defines a Stereo Camera rig.

    createRig() creates the rig itself
    registerThisRig() registers it into the system
"""

def __createSubordinateCamera(mainShape, name, parent):
  """
  Private method to this module.
  Create a subordinate camera
  Make the default connections between the main camera and the subordinate one.
  """

  # First create a camera under the right parent with the desired name
  #
  subordinate = cmds.camera()[0]
  subordinate = cmds.parent(subordinate, parent)[0]
  subordinate = cmds.rename(subordinate, name)
  subordinateShape = cmds.listRelatives(subordinate, path=True, shapes=True)[0]
  
  # Change some default attributes
  #
  cmds.setAttr(subordinate + '.renderable', 0)
  
  # Connect the camera attributes from the main, hide them
  #
  for attr in ['horizontalFilmAperture',
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
        'farClipPlane']:
    subordinateAttr = subordinateShape + '.' + attr
    cmds.connectAttr(mainShape + '.' + attr, subordinateAttr)
    cmds.setAttr(subordinateAttr, keyable=False)
    
  # Hide some more attributes on the transform
  #
  for attr in ['scaleX', 'scaleY', 'scaleZ',
        'visibility',
        'centerOfInterest']:
    cmds.setAttr(subordinate + '.' + attr, keyable=False)

  return subordinate

def __createFrustumNode(mainCam, parent, baseName):
  """
  Private method to this module.
  Create a display frustum node under the given parent.
  Make the default connections between the main camera and the frustum  
  Remove some of the channel box attributes that we do not want to show
  up in the channel box. 
  """

  frustum = cmds.createNode('stereoRigFrustum', name=baseName, parent=parent)
  for attr in ['localPositionX', 'localPositionY', 'localPositionZ',
        'localScaleX', 'localScaleY', 'localScaleZ']:
    cmds.setAttr(frustum + '.' + attr, channelBox=False)

  for attr in ['displayNearClip', 'displayFarClip', 'displayFrustum',
           'zeroParallaxPlane',
           'zeroParallaxTransparency',
           'zeroParallaxColor',
           'safeViewingVolume',
           'safeVolumeTransparency',
           'safeVolumeColor',
           'safeStereo',
           'zeroParallax']:
    cmds.connectAttr(mainCam+'.'+attr, frustum+'.'+attr)
    
  return frustum

def createRig(unusedBasename='DomeStereoCamera'):
  """
  Creates a new stereo rig. Uses a series of Maya commands to build
  a stereo rig.
  
  The optional argument basename defines the base name for each DAG
  object that will be created.
  """

  # Create a random camera letter "extension" to fix the unique camera issue with the camera aim, and aim+up add-on bug
  import string
  import random
  randomLetterPostfix = random.choice(string.ascii_uppercase)
  #print ("The StereoCameraRig Random letter extension is: DomeStereoCamera" + randomLetterPostfix)

  # Put a temp throwaway value of unusedBasename as the createRig input variable
  # Define basename here instead of the regular createRig() variable
  basename = 'DomeStereoCamera' + randomLetterPostfix

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
           'filmOffsetRightCam', 'filmOffsetLeftCam']:
    cmds.connectAttr(centerCam+'.'+attr, root+'.'+attr)
  
  
  cmds.connectAttr(centerCam + '.focalLength', root + '.focalLengthInput')
  #cmds.setAttr(centerCam + '.stereo', 2)
  cmds.setAttr(centerCam + '.renderable', 0)

  # Create the Frustum node, connect it to the root.
  #
  frustum = __createFrustumNode(centerCam, root, rootName + 'Frustum')
  
  # Create the left & right eye cameras
  # 
  leftCam  = __createSubordinateCamera(centerCam, rootName+'Left',  root)
  rightCam = __createSubordinateCamera(centerCam, rootName+'Right', root)
  
  # Set up message attribute connections to define the role of each camera
  #
  cmds.connectAttr(leftCam   + '.message', frustum + '.leftCamera')
  cmds.connectAttr(rightCam  + '.message', frustum + '.rightCamera')
  cmds.connectAttr(centerCam + '.message', frustum + '.centerCamera')

  # Connect the specific left and right output attributes of the root
  # transform to the corresponding left and right camera attributes.
  #
  cmds.connectAttr(root + '.stereoLeftOffset',    leftCam  + '.translateX')
  cmds.connectAttr(root + '.stereoRightOffset',   rightCam + '.translateX')
  cmds.connectAttr(root + '.stereoLeftAngle',     leftCam  + '.rotateY')
  cmds.connectAttr(root + '.stereoRightAngle',    rightCam + '.rotateY')
  cmds.connectAttr(root + '.filmBackOutputLeft',  leftCam  + '.hfo')
  cmds.connectAttr(root + '.filmBackOutputRight', rightCam + '.hfo')

  # Lock the attributes that should not be manipulated by the artist.
  #
  for attr in ['translate', 'rotate']:
    cmds.setAttr(leftCam  + '.' + attr, lock=True)
    cmds.setAttr(rightCam + '.' + attr, lock=True)

  
  #---------------------------------------------------------------------------
  # Custom Domemain3D Setup code
  #---------------------------------------------------------------------------
  import os
  import sys
  
  # 18 mm focal length = 90 degree FOV
  defaultRealtimeFOV = 18
  # 4 mm focal length = 160 degree FOV
  #defaultRealtimeFOV = 4
  
  domeOverrideFOV = int(os.getenv('DOMEMASTER3D_MAYA_REALTIME_FOV', defaultRealtimeFOV))
    
  if((domeOverrideFOV >= 3) and (domeOverrideFOV <= 3500)):
    print ("Using a Domemain3D realtime viewport FOV value of " + str(domeOverrideFOV) + ".\n")
  else:
    print ("The \"DOMEMASTER3D_MAYA_REALTIME_FOV\" environment variable overridden FOV Value of " + str(domeOverrideFOV) + " is outside of the acceptable range of 3 mm to 3500mm that Maya accepts as a valid camera field of view value. The default value of " + str(defaultRealtimeFOV) + " will be used instead.\n")
    domeOverrideFOV = defaultRealtimeFOV
   
  # Use the default FOV value or pull the FOV value from the DOMEMASTER3D_MAYA_REALTIME_FOV env variable
  cmds.setAttr(centerCam+'.focalLength', domeOverrideFOV)
  
  # 4 mm focal length = 160 degree FOV
  #cmds.setAttr(centerCam + '.focalLength', 4)

  # 18 mm focal length = 90 degree FOV
  #cmds.setAttr(centerCam + '.focalLength', 18)
  
  #cmds.setAttr(centerCam + '.stereo', 0 )
  #cmds.setAttr(centerCam + '.zeroParallax', 0.1)
  #cmds.setAttr(centerCam + '.interaxialSeparation', 0)
  
  # Create the fulldome stereo lens shaders
  createLensShaders(centerCam, leftCam, rightCam)
  
  # Align the base camera to point upwards
  cmds.setAttr(root+'.rotateX', 90)
  cmds.setAttr(root+'.rotateY', 0)
  cmds.setAttr(root+'.rotateZ', 0)
  
   # Link the new attribute 'Cam Locator Scale' to the dome camera's locator size control
  cmds.addAttr(root, longName='Cam_Locator_Scale', niceName='Cam Locator Scale', attributeType='double', defaultValue=1.0, minValue=0.01)
  cmds.setAttr(root+'.Cam_Locator_Scale', keyable=False, channelBox=True)
  
  # Result: Connected DomeStereoCamera.Cam_Locator_Scale to DomeStereoCameraLeftShape.locatorScale. # 
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
    stereoCameraSets.parentToLayer0Rig(*args, cameraSet=keywords['cameraSet'])

rigTypeName = 'DomeStereoCamera'

def registerThisRig():
  """
  Registers the rig in Maya's database
  """
  mayaVersion = getMayaVersionDome()
  if(mayaVersion >= 2011):
    global rigTypeName 
    cmds.stereoRigManager(add=[rigTypeName, 'Python', 'domeStereoRig.createRig'])
    cmds.stereoRigManager(cameraSetFunc=[rigTypeName, 'domeStereoRig.attachToCameraSet'])
  else:
    cmds.stereoRigManager(add=['StereoCamera', 'Python', 'maya.app.stereo.stereoCameraDefaultRig.createRig'])


"""
A python function to get the current object's shape node

getObjectShapeNode("stereoCamera")
# Result: [u'stereoCameraCenterCamShape', u'stereoCameraFrustum'] # 
"""

def getObjectShapeNode(object):
  shape = cmds.listRelatives(object, children=True, shapes=True)
  print('Shape: ')
  print(shape)

  return shape

"""
A python function to get the current object's parent node

getObjectParentNode("nurbsSphereShape1")
# Result:  [u'nurbsSphere1'] #
"""

def getObjectParentNode(object):
  import maya.cmds as cmds
  parent = cmds.listRelatives(object, parent=True)

  print('Parent: ')
  print(parent)

  return parent
