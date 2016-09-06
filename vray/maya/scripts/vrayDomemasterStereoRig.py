"""
 Vray DomemasterStereo Camera Rig V1.7
 2015-05-08 11.46 pm
 by Andrew Hazelden  andrew@andrewhazelden.com
 -----------------------------------------------------------------------

 This script makes it easy to start creating fulldome stereoscopic content in Autodesk Maya.
 
 Version 1.7
 ---------------
 2015-05-08

 Adapted the mental ray script to support Vray DomemasterStereo rendering


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
  
  # Check if Vray is loaded before linking the attributes
  if (cmds.pluginInfo("vrayformaya",q=True,loaded=True)):
    # -------------------------------------------------------------------------
    # Center Camera Lens Shader
    # -------------------------------------------------------------------------
    print( "[Center Camera] " + centerCam + "\n" )

    # Enable the Lens Shader's Vray Extra Attributes
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoOn', longName='vrayDomemasterStereoOn', attributeType='long', defaultValue=1)

    # Center Camera View
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoCamera', longName='vrayDomemasterStereoCamera', attributeType='long', defaultValue=0)

    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoFovAngle', longName='vrayDomemasterStereoFovAngle', attributeType='float', min=0.1, softMaxValue=360, defaultValue=180)
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoParallaxDistance', longName='vrayDomemasterStereoParallaxDistance', attributeType='float', min=0.001, softMaxValue=5000, defaultValue=720)
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoSeparation', longName='vrayDomemasterStereoSeparation', attributeType='float', min=0, softMaxValue=650, defaultValue=6.5)
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoForwardTilt', longName='vrayDomemasterStereoForwardTilt', attributeType='long', min=0, softMaxValue=360, defaultValue=0)
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoTiltCompensation', longName='vrayDomemasterStereoTiltCompensation', attributeType='long', defaultValue=0)
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoVerticalMode', longName='vrayDomemasterStereoVerticalMode', attributeType='long', defaultValue=0)

    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoSeparationMap', longName='vrayDomemasterStereoSeparationMap', attributeType='float3', usedAsColor=True , numberOfChildren=3)
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoSeparationMapr', longName='vrayDomemasterStereoSeparationMapr', attributeType='float', parent='vrayDomemasterStereoSeparationMap', defaultValue=1.0 )
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoSeparationMapg', longName='vrayDomemasterStereoSeparationMapg', attributeType='float', parent='vrayDomemasterStereoSeparationMap', defaultValue=1.0 )
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoSeparationMapb', longName='vrayDomemasterStereoSeparationMapb', attributeType='float', parent='vrayDomemasterStereoSeparationMap', defaultValue=1.0 )

    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoHeadTurnMap', longName='vrayDomemasterStereoHeadTurnMap', attributeType='float3', usedAsColor=True , numberOfChildren=3)
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoHeadTurnMapr', longName='vrayDomemasterStereoHeadTurnMapr', attributeType='float', parent='vrayDomemasterStereoHeadTurnMap', defaultValue=1.0 )
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoHeadTurnMapg', longName='vrayDomemasterStereoHeadTurnMapg', attributeType='float', parent='vrayDomemasterStereoHeadTurnMap', defaultValue=1.0 )
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoHeadTurnMapb', longName='vrayDomemasterStereoHeadTurnMapb', attributeType='float', parent='vrayDomemasterStereoHeadTurnMap', defaultValue=1.0 )

    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoHeadTiltMap', longName='vrayDomemasterStereoHeadTiltMap', attributeType='float3', usedAsColor=True , numberOfChildren=3)
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoHeadTiltMapr', longName='vrayDomemasterStereoHeadTiltMapr', attributeType='float', parent='vrayDomemasterStereoHeadTiltMap', defaultValue=0.5 )
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoHeadTiltMapg', longName='vrayDomemasterStereoHeadTiltMapg', attributeType='float', parent='vrayDomemasterStereoHeadTiltMap', defaultValue=0.5 )
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoHeadTiltMapb', longName='vrayDomemasterStereoHeadTiltMapb', attributeType='float', parent='vrayDomemasterStereoHeadTiltMap', defaultValue=0.5 )

    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoFlipX', longName='vrayDomemasterStereoFlipX', attributeType='long', defaultValue=0)
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoFlipY', longName='vrayDomemasterStereoFlipY', attributeType='long', defaultValue=0)
    cmds.addAttr( centerCam, shortName='vrayDomemasterStereoNeckOffset', longName='vrayDomemasterStereoNeckOffset', attributeType='float', min=-10000.0, softMaxValue=1000.0 , defaultValue=0.0 )

     
    # -------------------------------------------------------------------------
    # Left Camera Lens Shader
    # -------------------------------------------------------------------------
    leftCamShape = leftCam + 'Shape'
    # leftCamShape = leftCam
    # leftCamShape = getObjectShapeNode(leftCam)
    print( "[Left Camera Shape] " + leftCamShape + "\n" )

    # Enable the Lens Shader's Vray Extra Attributes
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoOn', longName='vrayDomemasterStereoOn', attributeType='long', defaultValue=1)

    # Left Camera View
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoCamera', longName='vrayDomemasterStereoCamera', attributeType='long', defaultValue=1)

    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoFovAngle', longName='vrayDomemasterStereoFovAngle', attributeType='float', min=0.1, softMaxValue=360, defaultValue=180)
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoParallaxDistance', longName='vrayDomemasterStereoParallaxDistance', attributeType='float', min=0.001, softMaxValue=5000, defaultValue=720)
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoSeparation', longName='vrayDomemasterStereoSeparation', attributeType='float', min=0, softMaxValue=650, defaultValue=6.5)
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoForwardTilt', longName='vrayDomemasterStereoForwardTilt', attributeType='long', min=0, softMaxValue=360, defaultValue=0)
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoTiltCompensation', longName='vrayDomemasterStereoTiltCompensation', attributeType='long', defaultValue=0)
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoVerticalMode', longName='vrayDomemasterStereoVerticalMode', attributeType='long', defaultValue=0)

    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoSeparationMap', longName='vrayDomemasterStereoSeparationMap', attributeType='float3', usedAsColor=True , numberOfChildren=3)
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoSeparationMapr', longName='vrayDomemasterStereoSeparationMapr', attributeType='float', parent='vrayDomemasterStereoSeparationMap', defaultValue=1.0 )
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoSeparationMapg', longName='vrayDomemasterStereoSeparationMapg', attributeType='float', parent='vrayDomemasterStereoSeparationMap', defaultValue=1.0 )
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoSeparationMapb', longName='vrayDomemasterStereoSeparationMapb', attributeType='float', parent='vrayDomemasterStereoSeparationMap', defaultValue=1.0 )

    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoHeadTurnMap', longName='vrayDomemasterStereoHeadTurnMap', attributeType='float3', usedAsColor=True , numberOfChildren=3)
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoHeadTurnMapr', longName='vrayDomemasterStereoHeadTurnMapr', attributeType='float', parent='vrayDomemasterStereoHeadTurnMap', defaultValue=1.0 )
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoHeadTurnMapg', longName='vrayDomemasterStereoHeadTurnMapg', attributeType='float', parent='vrayDomemasterStereoHeadTurnMap', defaultValue=1.0 )
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoHeadTurnMapb', longName='vrayDomemasterStereoHeadTurnMapb', attributeType='float', parent='vrayDomemasterStereoHeadTurnMap', defaultValue=1.0 )

    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoHeadTiltMap', longName='vrayDomemasterStereoHeadTiltMap', attributeType='float3', usedAsColor=True , numberOfChildren=3)
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoHeadTiltMapr', longName='vrayDomemasterStereoHeadTiltMapr', attributeType='float', parent='vrayDomemasterStereoHeadTiltMap', defaultValue=1.0 )
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoHeadTiltMapg', longName='vrayDomemasterStereoHeadTiltMapg', attributeType='float', parent='vrayDomemasterStereoHeadTiltMap', defaultValue=1.0 )
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoHeadTiltMapb', longName='vrayDomemasterStereoHeadTiltMapb', attributeType='float', parent='vrayDomemasterStereoHeadTiltMap', defaultValue=1.0 )

    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoFlipX', longName='vrayDomemasterStereoFlipX', attributeType='long', defaultValue=0)
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoFlipY', longName='vrayDomemasterStereoFlipY', attributeType='long', defaultValue=0)
    cmds.addAttr( leftCamShape, shortName='vrayDomemasterStereoNeckOffset', longName='vrayDomemasterStereoNeckOffset', attributeType='float', min=-10000.0, softMaxValue=1000.0 , defaultValue=0.0 )


    # -------------------------------------------------------------------------
    # Right Camera Lens Shader
    # -------------------------------------------------------------------------
    rightCamShape = rightCam + 'Shape'
    # rightCamShape = rightCam
    # rightCamShape = getObjectShapeNode(rightCam)
    print( "[Right Camera Shape] " + rightCamShape + "\n" )

    # Enable the Lens Shader's Vray Extra Attributes
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoOn', longName='vrayDomemasterStereoOn', attributeType='long', defaultValue=1)

    # Center Camera View
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoCamera', longName='vrayDomemasterStereoCamera', attributeType='long', defaultValue=2)

    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoFovAngle', longName='vrayDomemasterStereoFovAngle', attributeType='float', min=0.1, softMaxValue=360, defaultValue=180)
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoParallaxDistance', longName='vrayDomemasterStereoParallaxDistance', attributeType='float', min=0.001, softMaxValue=5000, defaultValue=720)
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoSeparation', longName='vrayDomemasterStereoSeparation', attributeType='float', min=0, softMaxValue=650, defaultValue=6.5)
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoForwardTilt', longName='vrayDomemasterStereoForwardTilt', attributeType='long', min=0, softMaxValue=360, defaultValue=0)
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoTiltCompensation', longName='vrayDomemasterStereoTiltCompensation', attributeType='long', defaultValue=0)
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoVerticalMode', longName='vrayDomemasterStereoVerticalMode', attributeType='long', defaultValue=0)

    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoSeparationMap', longName='vrayDomemasterStereoSeparationMap', attributeType='float3', usedAsColor=True , numberOfChildren=3)
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoSeparationMapr', longName='vrayDomemasterStereoSeparationMapr', attributeType='float', parent='vrayDomemasterStereoSeparationMap', defaultValue=1.0 )
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoSeparationMapg', longName='vrayDomemasterStereoSeparationMapg', attributeType='float', parent='vrayDomemasterStereoSeparationMap', defaultValue=1.0 )
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoSeparationMapb', longName='vrayDomemasterStereoSeparationMapb', attributeType='float', parent='vrayDomemasterStereoSeparationMap', defaultValue=1.0 )

    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoHeadTurnMap', longName='vrayDomemasterStereoHeadTurnMap', attributeType='float3', usedAsColor=True , numberOfChildren=3)
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoHeadTurnMapr', longName='vrayDomemasterStereoHeadTurnMapr', attributeType='float', parent='vrayDomemasterStereoHeadTurnMap', defaultValue=1.0 )
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoHeadTurnMapg', longName='vrayDomemasterStereoHeadTurnMapg', attributeType='float', parent='vrayDomemasterStereoHeadTurnMap', defaultValue=1.0 )
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoHeadTurnMapb', longName='vrayDomemasterStereoHeadTurnMapb', attributeType='float', parent='vrayDomemasterStereoHeadTurnMap', defaultValue=1.0 )

    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoHeadTiltMap', longName='vrayDomemasterStereoHeadTiltMap', attributeType='float3', usedAsColor=True , numberOfChildren=3)
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoHeadTiltMapr', longName='vrayDomemasterStereoHeadTiltMapr', attributeType='float', parent='vrayDomemasterStereoHeadTiltMap', defaultValue=1.0 )
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoHeadTiltMapg', longName='vrayDomemasterStereoHeadTiltMapg', attributeType='float', parent='vrayDomemasterStereoHeadTiltMap', defaultValue=1.0 )
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoHeadTiltMapb', longName='vrayDomemasterStereoHeadTiltMapb', attributeType='float', parent='vrayDomemasterStereoHeadTiltMap', defaultValue=1.0 )

    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoFlipX', longName='vrayDomemasterStereoFlipX', attributeType='long', defaultValue=0)
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoFlipY', longName='vrayDomemasterStereoFlipY', attributeType='long', defaultValue=0)
    cmds.addAttr( rightCamShape, shortName='vrayDomemasterStereoNeckOffset', longName='vrayDomemasterStereoNeckOffset', attributeType='float', min=-10000.0, softMaxValue=1000.0 , defaultValue=0.0 )

    # ---------------------------------------------------------------------
    # Link the common left and right camera attributes to the center camera
    # ---------------------------------------------------------------------

    # Link the left camera attributes
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoOn', leftCam+'.vrayDomemasterStereoOn', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoFovAngle', leftCam+'.vrayDomemasterStereoFovAngle', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoParallaxDistance', leftCam+'.vrayDomemasterStereoParallaxDistance', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoSeparation', leftCam+'.vrayDomemasterStereoSeparation', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoForwardTilt', leftCam+'.vrayDomemasterStereoForwardTilt', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoTiltCompensation', leftCam+'.vrayDomemasterStereoTiltCompensation', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoVerticalMode', leftCam+'.vrayDomemasterStereoVerticalMode', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoFlipX', leftCam+'.vrayDomemasterStereoFlipX', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoFlipY', leftCam+'.vrayDomemasterStereoFlipY', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoNeckOffset', leftCam+'.vrayDomemasterStereoNeckOffset', force=True )

    # Link the right camera attributes
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoOn', rightCam+'.vrayDomemasterStereoOn', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoFovAngle', rightCam+'.vrayDomemasterStereoFovAngle', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoParallaxDistance', rightCam+'.vrayDomemasterStereoParallaxDistance', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoSeparation', rightCam+'.vrayDomemasterStereoSeparation', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoForwardTilt', rightCam+'.vrayDomemasterStereoForwardTilt', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoTiltCompensation', rightCam+'.vrayDomemasterStereoTiltCompensation', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoVerticalMode', rightCam+'.vrayDomemasterStereoVerticalMode', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoFlipX', rightCam+'.vrayDomemasterStereoFlipX', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoFlipY', rightCam+'.vrayDomemasterStereoFlipY', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoNeckOffset', rightCam+'.vrayDomemasterStereoNeckOffset', force=True )

    # ---------------------------------------------------------------------
    # Create the custom Domemaster3D shading networks
    # ---------------------------------------------------------------------

    # Create the nodes

    # ---------------------------------------------------------------------
    # Link the center camera lens shader to the Maya camera rig stereo3d settings
    # This enables real-time 3D previews in the viewport
    # ---------------------------------------------------------------------
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoParallaxDistance', centerCam+'.zeroParallax', force=True )
    cmds.connectAttr( centerCam+'.vrayDomemasterStereoSeparation', centerCam+'.interaxialSeparation', force=True )

    #Turn off the Stereo 3D effect on the native Maya camera rig
    # This skips the need for a pre-render and post-render mel script.
    cmds.setAttr( centerCam+'.stereo',  0 )


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

def createRig(unusedBasename='VrayDomemasterStereoCamera'):
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
  #print ("The StereoCameraRig Random letter extension is: VrayDomemasterStereoCamera" + randomLetterPostfix)

  #Put a temp throwaway value of unusedBasename as the createRig input variable
  #Define basename here instead of the regular createRig() variable
  basename='VrayDomemasterStereoCamera' + randomLetterPostfix

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
  # Custom Dome Setup code
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
  
  # Result: Connected VrayDomemasterStereoCamera.Cam_Locator_Scale to VrayDomemasterStereoCameraLeftShape.locatorScale. // 
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

rigTypeName = 'VrayDomemasterStereoCamera'

def registerThisRig():
  """
  Registers the rig in Maya's database
  """
  
  mayaVersion = getMayaVersionDome()
  if (mayaVersion >= 2011):
    global rigTypeName 
    cmds.stereoRigManager( add=[rigTypeName, 'Python', 'vrayDomemasterStereoRig.createRig'] )
    cmds.stereoRigManager( cameraSetFunc=[rigTypeName, 'vrayDomemasterStereoRig.attachToCameraSet'] )
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
