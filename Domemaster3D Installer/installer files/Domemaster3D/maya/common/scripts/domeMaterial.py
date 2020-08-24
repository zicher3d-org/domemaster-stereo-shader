"""
Dome Material Script V2.4
2018-08-21
Created by Andrew Hazelden  andrew@andrewhazelden.com

This script makes it easy to start creating fulldome content in Autodesk Maya.

This is a set of python functions for Maya that create domeAFL shader compatible surface materials.

The textures are loaded as mental ray textures and connected to a standard mia_material.

You can set the file textures to an empty path if you don't want a default texture applied to the mentalrayTexture nodes. On my system I get an error if I try and render a scene with an empty mentalrayTexture node. 

------------------------------------------------------------------------------

Version History
----------------

Version 2.2.2 - 2016-12-29
-------------------------------

mental ray 3.14 + Maya 2017 Starglobe tool update

Version 2.2.1 - 2016-12-25
-------------------------------
Code Reformatting

Facebook Vertical Strip Cube image projection

Fixed the LG360 camera preview icon loading issue
  
Added stereo 360 degree viewing support for Side by Side Stereo, and Over Under Stereo panoramic imagery.

Added an unlockAncestor() function.

Version 2.1 - 2016-09-15
-----------------------------

Improved the domeMaterial.mel script's Maya 2017 compatibility by fixing the MEL "Redeclaration of variable" warnings.

Version 2.0 - 2016-05-27
-----------------------------

Added DomeViewer image projection support for the Facebook 360 Pyramid, LG360 Camera, and the Samsung Gear 360 Camera image projections.
  
Version 1.9.3 - 2016-02-08
-----------------------------

Updated the DomeViewer tool to add Ricoh Theta S support along with a set of Ricoh Theta S panoramic viewing meshes "ricoh_theta_s_mesh.obj", and "ricoh_theta_s_mesh.ma" to the Domemain3D sourceimages folder

Updated the DomeViewer tool to add Facebook Cube Map 3x2 support along with a set of Facebook Cube Map 3x2 panoramic viewing meshes "facebookCube3x2_mesh.obj", and "facebookCube3x2_mesh.ma" to the Domemain3D sourceimages folder

Version 1.9.2 - 2016-01-03
-----------------------------

Updated the DomeViewer tool to addGearVR Mono Cube support, and included a set of Gear VR panoramic viewing meshes "gearVRCube_mesh.obj", and "gearVRCube_mesh.ma" in the Domemain3D sourceimages folder

Changed the DomeViewer "Show Focal Length in HUD" default state to off

Added a new DomeViewer "Connect Alpha Channel" checkbox to the Extra Controls section of the GUI. This checkbox tells the DomeViewer to connect the alpha channel from the DomeViewer loaded imagery to the surface material node. Th new "Connect Alpha Channel" checkbox is disabled by default so imagery with transparent mental ray rendered physical sky and sun and IBL based environment backdrops can be viewed in the viewport and you will still see the sky background.

Version 1.8 - 2015-08-17 
-----------------------------

Added a new Hybrid mentalrayTexture material that combines the render time improvements of a mental ray texture based surface material for reducing blurry streak artifacts when rendering with lens shaders, and a real-time high resolution preview benefit of a stock maya file texture node.

Version 1.7 - 2015-03-07 
-----------------------------


Version 1.6 Alpha 7 - 2014-11-16
-------------------------------------


Domemain3D attribute presets path detection code added:
  domeMaterial.getDomePresetsPath('remapColor/ldr_to_hdr_boost_10x.mel') 
  # C:/Program Files/Domemain3D/maya/common/presets/attrPresets/remapColor/ldr_to_hdr_boost_10x.mel


Version 1.6 - 2014-11-3
---------------------------

Updated the sourceimages path code

Version 1.5 - 2014-07-12
-------------------------------

Added a remapColor node to the Starglobe MR texture shading network so you can adjust the brightness of the stars

Updated the DomeViewer geometry with an all quads based fulldome mesh, updated the scale of the mirrorball mesh, and the quadsphere mesh

Updated DomeViewer view reset, and model scale setting

Added a mental ray forced plugin loading function to the domeMaterial commands that require mental ray to work. This will load the mental ray renderer when you use a command that requires it if mental ray wasn't set to to be an autostart plugin item in the plugin manager.

Added a mentalrayTexture image sequence function and shelf tool. This allows you to use image sequences with the mentalrayTexture node so you can avoid the blurry streak artifact that can occur with Maya's file texture node and mental ray lens shaders.

**Note**: You need to render animations that use the new mentalrayTexture image sequence tool using a single frame per render job packet/render slice size so the animated texture loading expression is updated on each frame in the sequence. 

If you are exporting your scene to a .mi file for Maya standalone rendering, you need to export one .mi file per frame so the image sequence texture is updated on every frame in the exported .mi output.


Version 1.4 Beta 10 - 2013-12-27
----------------------------------------

Added double sided shading code

Version 1.4 Beta 9 - 2013-12-07
------------------------------------

Updated Linux install path to:
/opt/Domemain3D

Added support for the Quadsphere (starglobe) mesh to the domeViewer

Added the "Flip the Panoramic Image" checkbox that causes a mirror effect on the panoramic image by flipping the panoramic texture so you are viewing the texture map as if it was an environmental reflection map viewed from the outside. This effect is done by scaling the domeViewer shape (scaleX * -1).


Version 1.4 Beta 6 Build 4 - 2013-10-27
--------------------------------------------

Added cylindrical panorama support
Added focal length HUD controls in the domeViewer window
Added Maya 2010 support to the starglobe GUI window


Version 1.4 Beta 4 - Build 4 - 2013-10-20
---------------------------------------------

Added the Dome Viewer feature for exploring rendered domemain formatted imagery


Version 1.3.5 Build 7 - 2013-08-20
--------------------------------------

Upgraded the Maya dome material shaders to use the mia_material_x_passes shader

Added a starglobe tool to the Maya shelf to create a night sky backdrop

The starglobe textures and meshes are stored in the Domemain3D/sourceimages folder.


Version 1.3.3 - 2013-05-29
------------------------------

Updated the default locator scale

Updated source image paths for Maya 2010 compatibility


Version 1.3.2 - Build 1 - 2013-04-16
----------------------------------------

Edited the default camera connections for the lens shaders to work with the modified versions of the maya createMentalRayIndirectLightingTab.mel & AEmia_physicalskyTemplate.mel scripts. This fixes the problem of the Physical Sky & Sum system overwriting the first .miLensShader input on cameras in the scene.

The location of the default domemain control map textures is now in the C:\Program Files\Domemain3D\sourceimages folder on Windows or the /Applications/Domemain3D/sourceimages folder on macOS. The Domemain3D shelf tools have been updated to link to the new sourceimages folder.

Version 1.3 - Build 27 - 2012-11-04
---------------------------------------

Edited default presets for bump map shading network, added WxH and FOV camera tools, changed the default lens shader connections to support the mental ray sky and sun system.

Version 1.0 - 2012-10-31
----------------------------

Created first python script to create a domeAFL mental ray shading network

------------------------------------------------------------------------------

Installation instructions

Step 1.
Source the python script in Maya using the python command:
import domeMaterial as domeMaterial

Step 2.
Test your current python script installation using the python command:
import domeMaterial as domeMaterial
reload(domeMaterial)
domeMaterial.createColorBumpMiaMaterial()

-------------------------------------------------------------------------------

Create a Color MIA material 
A python function to create a mia_material with a shading network for color + bump textures.

Run using the command:
import domeMaterial as domeMaterial
reload(domeMaterial)
domeMaterial.createColorMiaMaterial()

------------------------------------------------------------------------------

Create a Color and Bump MIA Material 
A python function to create a mia_material with a shading network for color + bump textures.

Run using the command:
import domeMaterial as domeMaterial
reload(domeMaterial)
domeMaterial.createColorBumpMiaMaterial()

------------------------------------------------------------------------------

Create a Color Image Sequence MIA Material
A python function to create a mia_material with a shading network for color + bump textures.

A python function to create a mia_material with a shading network for a mental ray native animated file texture using a mel expression to cycle the images used per frame.

This is designed so image sequences can be used as file texture on fulldome renders without having to worry about the blurry grey line artifact in MR.

Run using the command:
import domeMaterial as domeMaterial
reload(domeMaterial)
domeMaterial.createColorImageSequenceMiaMaterial()

------------------------------------------------------------------------------
Create a Hybrid MIA Material + Maya File Texture
A python function to create a hybrid shading network with a mia_material with a shading network for a mental ray native animated file texture using a mel expression to cycle the images used per frame, and a Maya file texture node shading network for high resolution previews in the real-time viewport window.

This is designed so image sequences can be used as file texture on fulldome renders without having to worry about the blurry grey line artifact in MR.

Run using the command:
import domeMaterial as domeMaterial
reload(domeMaterial)
domeMaterial.createHybridColorImageSequenceMiaMaterial()

------------------------------------------------------------------------------

Create Mental Ray Texture Extra Attributes
Add extra attributes for animation to a mentalrayTexture node

Run using the command:
import domeMaterial as domeMaterial
reload(domeMaterial)
domeMaterial.createMentalrayTextureExtraAttrs(color_mr_tex, fileTextureName)

------------------------------------------------------------------------------

Domemain3D Force Mental Ray to load
A python function to make sure mental ray is active and the MR shading nodes are read to be used.

Run using the command:
import domeMaterial
reload(domeMaterial)
domeMaterial.forceMentalRayLoad()

------------------------------------------------------------------------------

Create a Starglobe
A python function to create a 8K textured starglobe with a mental ray native mia_material_x_passes shading network.

The starglobe meshes are stored in the folder:
C:/Program Files/Domemain3D/sourceimages

Run using the command:
import domeMaterial as domeMaterial
reload(domeMaterial)
domeMaterial.createStarglobe()

------------------------------------------------------------------------------

Create a Dome Viewer
A python function to create a fulldome image viewer with an incandescent lambert based shading network.

The domeViewer mesh is stored in the folder:
C:/Program Files/Domemain3D/sourceimages

Run using the command:
import domeMaterial as domeMaterial
reload(domeMaterial)
domeMaterial.createDomeViewer()

------------------------------------------------------------------------------

Find out the path to the AttrPresets folder
A python function to check the operating system platform and the AttrPresets folder. 

import domeMaterial as domeMaterial
reload(domeMaterial)
domeMaterial.getDomePresetsPath('remapColor/ldr_to_hdr_boost_10x.mel')

------------------------------------------------------------------------------

Unlock Ancestor
A python function to lock/unlock an ancestor plug connection

import domeMaterial as domeMaterial
reload(domeMaterial)
domeMaterial.unlockAncestor('stereoCameraRight.rotate', True)

------------------------------------------------------------------------------

"""


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


"""
Find out the path to the models folder
----------------------
A python function to check the operating system platform and the models folder. 

"""
def getModelsPath(modelFileName):
  import os
  import maya.cmds as cmds
  import maya.mel as mel
  # ---------------------------------------------------------------------
  # Set up the base folder path for the Domemain3D models
  # ---------------------------------------------------------------------

  # Check OS platform for Windows/Mac/Linux Paths
  import platform

  # This is the base path for the images folder
  baseModelsFolder = ""
  
  # Try and read the value from the current Maya.env file's environment variables
  baseModelsFolder = os.environ.get('DOMEMASTER3D_SOURCEIMAGES_DIR') + "/"
  # Typical Result: C:/Program Files/Domemain3D/sourceimages/ 
  
  # Use a fixed value if the env var is empty
  if baseModelsFolder == None:
    if platform.system()=='Windows':
      # Check if the program is running on Windows 
      baseModelsFolder = "C:/Program Files/Domemain3D/sourceimages/"
    elif platform.system()== 'win32':
      # Check if the program is running on Windows 32
      baseModelsFolder = "C:/Program Files (x86)/Domemain3D/sourceimages/"
    elif platform.system()== 'Darwin':
      # Check if the program is running on macOS
      baseModelsFolder = "/Applications/Domemain3D/sourceimages/"
    elif platform.system()== 'Linux':
      # Check if the program is running on Linux
      baseModelsFolder = "/opt/Domemain3D/sourceimages/"
    elif platform.system()== 'Linux2':
      # Check if the program is running on Linux
      baseModelsFolder = "/opt/Domemain3D/sourceimages/"
    else:
      # Create the empty variable as a fallback mode
      baseModelsFolder = ""

  combinedFileAndModelPath = baseModelsFolder + modelFileName

  print "[Domemain3D is running on a " + platform.system() + " System]"
  print "[Requesting the model file]: " + combinedFileAndModelPath

  return combinedFileAndModelPath

  
"""
Find out the path to the AttrPresets folder
----------------------
A python function to check the operating system platform and the AttrPresets folder. 

"""
def getDomePresetsPath(PresetsFileName):
  import os
  import maya.cmds as cmds
  import maya.mel as mel
  
  # ---------------------------------------------------------------------
  # Setup the base folder path for the Domemain3D AttrPresets
  # ---------------------------------------------------------------------
  
  # Check OS platform for Windows/Mac/Linux Paths
  import platform

  # This is the base path for the images folder
  basePresetsFolder = ''
  
  # Try and read the value from the current Maya.env file's environment variables
  basePresetsFolder = os.environ.get('DOMEMASTER3D_MAYA_DIR') + '/common/presets/attrPresets/'
  # Typical Result: C:/Program Files/Domemain3D/maya/common/presets/attrPresets/
  
  # Use a fixed value if the env var is empty
  if basePresetsFolder == None:
    if platform.system()=='Windows':
      # Check if the program is running on Windows 
      basePresetsFolder = 'C:/Program Files/Domemain3D/maya/common/presets/attrPresets/'
    elif platform.system()== 'win32':
      # Check if the program is running on Windows 32
      basePresetsFolder = 'C:/Program Files (x86)/Domemain3D/maya/common/presets/attrPresets/'
    elif platform.system()== 'Darwin':
      # Check if the program is running on macOS
      basePresetsFolder = '/Applications/Domemain3D/maya/common/presets/attrPresets/'
    elif platform.system()== 'Linux':
      # Check if the program is running on Linux
      basePresetsFolder = '/opt/Domemain3D/maya/common/presets/attrPresets/'
    elif platform.system()== 'Linux2':
      # Check if the program is running on Linux
      basePresetsFolder = '/opt/Domemain3D/maya/common/presets/attrPresets/'
    else:
      # Create the empty variable as a fallback mode
      basePresetsFolder = ''

  combinedFileAndPresetsPath = basePresetsFolder + PresetsFileName

  print '[Domemain3D is running on a ' + platform.system() + ' System]'
  print '[Requesting the Presets file]: ' + combinedFileAndPresetsPath

  return combinedFileAndPresetsPath

  
# Syntax: createDomeViewerTexture('domeViewer', True, 1, 1)
def createDomeViewerTexture(meshName, isGrid, stereoMode, stereoView):
  import os
  import maya.cmds as cmds
  import maya.mel as mel
  
  # stereoMode 1=Mono2D, 2=Side by Side Stereo, 3=Over Under Stereo
  # stereoView 1=Center, 2=Left, 3=Right
  
  stereoViewPrefix = ''
  if stereoView == 1:
    # Center View
    stereoViewPrefix = 'center_'
  elif stereoView == 2:
    # Left View
    stereoViewPrefix = 'left_'
  elif stereoView == 3:
    # Right View
    stereoViewPrefix = 'right_'
  else:
    # The fallback option is to use the center view
    stereoViewPrefix = 'center_'
    
  # ---------------------------------------------------------------------
  # Set up the base folder path for the Domemain3D textures
  # ---------------------------------------------------------------------

  # Set the file texture variables to '' if you don't want a file to be specified
  domeViewerMapFileTexture = ''
 
  # Read the texture from the Domemain3D Folder
  #domeViewerMapFileTexture = getSourceImagesPath("fulldome_1K.jpg")

  materialNamePrefix = ''
  
  # Check if the stereo format is: "None - Mono 2D", "Side by Side Stereo", "Over Under Stereo"
  stereoMode = cmds.optionMenuGrp('menuDomeViewerStereoFormat', query=True, select=True)
  
  # Check if the image's alpha channel should be connected to the surface material
  connectAlphaEnabled = cmds.checkBoxGrp('checkGrpDomeViewerConnectAlpha', query=True, value1=True)
  
  # Check if this is a pano or an alignment grid
  if(isGrid == True):
    # Image is a alignment grid
    materialNamePrefix = stereoViewPrefix + 'domeViewerGrid_'
    # Load the Aaron Bradbury fulldome alignment grid
    domeViewerMapFileTexture = getSourceImagesPath('fulldomeAlignmentGrid_4k.png')
    
    domeViewer_maya_tex = cmds.shadingNode('file', n=materialNamePrefix+'FileTexture', asTexture=True) 
  else:
    # Image is a regular pano
    materialNamePrefix = stereoViewPrefix + 'domeViewer_'
    
    # Check if the Stereo Pair mode is active and then read in separate left and right texture maps
    if stereoMode == 4:
      # Read in the left or right image filename
      if stereoView == 1:
        # Center View
        # Read the texture from the Image Name field in the GUI
        domeViewerMapFileTexture = cmds.textFieldGrp('textDomeViewerImageOutputName', query=True, text=True)
      elif stereoView == 2:
        # Left View
        # Read the texture from the Image Name field in the GUI
        domeViewerMapFileTexture = cmds.textFieldGrp('textDomeViewerImageOutputName', query=True, text=True)
      elif stereoView == 3:
        # Right View
        # Read the texture from the Image Name field in the GUI
        domeViewerMapFileTexture = cmds.textFieldGrp('textDomeViewerImageOutputNameRight', query=True, text=True)
      else:
        # The fallback option is to use the center view
        # Read the texture from the Image Name field in the GUI
        domeViewerMapFileTexture = cmds.textFieldGrp('textDomeViewerImageOutputName', query=True, text=True)
    else:
      # For mono 2D images, Side by Side Stereo, and Over Under Stereo load an image from a single file
      # Read the texture from the Image Name field in the GUI
       domeViewerMapFileTexture = cmds.textFieldGrp('textDomeViewerImageOutputName', query=True, text=True)
    
    # Check if the media type is a movie or an image
    if cmds.optionMenuGrp('menuDomeViewerMediaType', query=True, select=True) == 3:
      # Create a Movie Node
      domeViewer_maya_tex = cmds.shadingNode('movie', n=materialNamePrefix+'MovieTexture', asTexture=True) 
    else:
      # File Texture Node
      domeViewer_maya_tex = cmds.shadingNode('file', n=materialNamePrefix+'FileTexture', asTexture=True) 

  # Create the shading group
  domeViewer_shader_group_name = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=materialNamePrefix+'materialSG')

  # Create the Lambert in-scene preview material
  domeViewer_preview_shader_name = cmds.shadingNode('lambert', n=materialNamePrefix+'preview_material', asShader=True) 
  
  domeViewer_maya_placement = cmds.shadingNode('place2dTexture', n=materialNamePrefix+'place2dTexture', asUtility=True) 

  # Connect the place2D texture to the Maya domeViewer file texture
  cmds.connectAttr(domeViewer_maya_placement+'.coverage', domeViewer_maya_tex+'.coverage', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.translateFrame', domeViewer_maya_tex+'.translateFrame', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.rotateFrame', domeViewer_maya_tex+'.rotateFrame', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.mirrorU', domeViewer_maya_tex+'.mirrorU', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.mirrorV', domeViewer_maya_tex+'.mirrorV', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.stagger', domeViewer_maya_tex+'.stagger', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.wrapU', domeViewer_maya_tex+'.wrapU', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.wrapV', domeViewer_maya_tex+'.wrapV', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.repeatUV', domeViewer_maya_tex+'.repeatUV', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.offset', domeViewer_maya_tex+'.offset', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.rotateUV', domeViewer_maya_tex+'.rotateUV', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.noiseUV', domeViewer_maya_tex+'.noiseUV', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.vertexUvOne', domeViewer_maya_tex+'.vertexUvOne', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.vertexUvTwo', domeViewer_maya_tex+'.vertexUvTwo', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.vertexUvThree', domeViewer_maya_tex+'.vertexUvThree', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.vertexCameraOne', domeViewer_maya_tex+'.vertexCameraOne', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.outUV', domeViewer_maya_tex+'.uvCoord', f=True)
  cmds.connectAttr(domeViewer_maya_placement+'.outUvFilterSize', domeViewer_maya_tex+'.uvFilterSize', f=True)
  
  # Connect the Lambert preview shader

  # Connect the Maya domeViewer file texture to the lambert preview material color and incandescent shader inputs
  cmds.connectAttr(domeViewer_maya_tex+'.outColor', domeViewer_preview_shader_name+'.color', f=True)
  cmds.connectAttr(domeViewer_maya_tex+'.outColor', domeViewer_preview_shader_name+'.incandescence', f=True)

  # Connect the alpha channel transparency from a still image, image sequence file texture, or a movie node:
  connectAlphaEnabled = cmds.checkBoxGrp('checkGrpDomeViewerConnectAlpha', query=True, value1=True)
  if(connectAlphaEnabled == True):
    cmds.connectAttr(domeViewer_maya_tex+'.outTransparency', domeViewer_preview_shader_name+'.transparency', f=True)

  # Connect the Lambert in-scene preview shader to the shading group
  cmds.connectAttr(domeViewer_preview_shader_name+'.outColor', domeViewer_shader_group_name+'.surfaceShader', f=True)
  
  # Set the image exposure settings
  imageExposure = cmds.floatSliderGrp('sliderDomeViewerImageExposure', query=True, value=True)
  cmds.setAttr( domeViewer_maya_tex+'.colorGain', imageExposure, imageExposure, imageExposure, type='double3')
  
  checkFileName = 'filetest -f "' + domeViewerMapFileTexture + '";'
  if mel.eval(checkFileName):
    # Set the filename for the maya file texture node
    cmds.setAttr(domeViewer_maya_tex+'.fileTextureName', domeViewerMapFileTexture , type="string")
    print('Loading the File texture: ' + domeViewerMapFileTexture)
  else:
    print('Texture Not Found: ' + domeViewerMapFileTexture)
  
  # Check if this is a panorama - then enable image sequence caching
  if(isGrid == False):
    # Check what Media Type was selected
    if cmds.optionMenuGrp('menuDomeViewerMediaType', query=True, select=True) == 1:
      print('Loading a still image.')
    elif cmds.optionMenuGrp('menuDomeViewerMediaType', query=True, select=True) == 2:
      print('Loading an image sequence.')
      # Enable Image Sequence Support
      cmds.setAttr(domeViewer_maya_tex+'.useFrameExtension',  1)
       
      if cmds.checkBoxGrp('checkGrpDomeViewerPreviewCache', query=True, value1=True) == True:
        # Enable RAM caching
        cmds.setAttr(domeViewer_maya_tex+'.useHardwareTextureCycling', 1)
      
      # Set start and end frames for RAM caching
      startFrame = cmds.intFieldGrp("intDomeViewerImageStartFrame", query=True, value1=True)
      endFrame = cmds.intFieldGrp("intDomeViewerImageEndFrame", query=True, value1=True)
      
      cmds.setAttr(domeViewer_maya_tex+'.startCycleExtension', startFrame)
      cmds.setAttr(domeViewer_maya_tex+'.endCycleExtension', endFrame)
    elif cmds.optionMenuGrp("menuDomeViewerMediaType", query=True, select=True) == 3:
      print('Loading a Movie File.')
      # Enable Image Sequence Support
      cmds.setAttr(domeViewer_maya_tex+'.useFrameExtension',  1)
      
      if cmds.checkBoxGrp('checkGrpDomeViewerPreviewCache', query=True, value1=True) == True:
        # Enable RAM caching
        cmds.setAttr(domeViewer_maya_tex+'.useHardwareTextureCycling', 1)
      
      # Set start and end frames for RAM caching
      startFrame = cmds.intFieldGrp('intDomeViewerImageStartFrame', query=True, value1=True)
      endFrame = cmds.intFieldGrp('intDomeViewerImageEndFrame', query=True, value1=True)
      
      cmds.setAttr(domeViewer_maya_tex+'.startCycleExtension', startFrame)
      cmds.setAttr(domeViewer_maya_tex+'.endCycleExtension', endFrame)
  
  if cmds.checkBoxGrp('checkGrpDomeViewerFocalLength', query=True, value1=True) == True:
    # Display the focal length in the heads up display
    mel.eval('setFocalLengthVisibility(1)')
  else:
    # Hide the focal length in the heads up display
    mel.eval('setFocalLengthVisibility(0)')

  # Rotate the Cylinder texture 90 degrees to an "Upright" orientation
  #if(meshName == 'cylinder'):
  #  cmds.setAttr(domeViewer_maya_placement+'.rotateFrame', 90)

  # Apply the shading group to the selected geometry
  #cmds.select("domeViewer")
  cmds.select(meshName)
  cmds.hyperShade(assign=domeViewer_shader_group_name)
    
  #---------------------------------------------------------------------------
  # Add Extra Attrs to the meshName shape
  #---------------------------------------------------------------------------
  baseNodeName = meshName

  #---------------------------------------------------------------------------
  # Add a Display Mode control to the domeGrid's transform node
  #---------------------------------------------------------------------------
  
  attrName = 'displayMode'
  #if(mel.attributeExists(attrName, baseNodeName) == 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType='enum', en='Off:Wireframe:Shaded:Wireframe on Shaded', defaultValue=2, keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)


  #---------------------------------------------------------------------------
  # Add a Double Sided Mode control to the domeGrid's transform node
  #---------------------------------------------------------------------------
  
  attrName = 'doubleSidedShading'
  #if(mel.attributeExists(attrName, baseNodeName) == 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType='enum', en='Double Sided:Show Frontfaces', defaultValue=0, keyable=True)
  #cmds.addAttr(baseNodeName, longName=attrName, attributeType="enum", en="Double Sided:Show Frontfaces:Show Backfaces", defaultValue=0, keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)


  #---------------------------------------------------------------------------
  # Add an Exposure control to the domeGrid's transform node - Default value 0.25
  #---------------------------------------------------------------------------
  # Have the code switch the input value based upon an isGrid check
  imageExposure = cmds.floatSliderGrp('sliderDomeViewerImageExposure', query=True, value=True)

  attrName = 'exposure';
  cmds.addAttr(baseNodeName, longName=attrName, attributeType='double', keyable=True, defaultValue=imageExposure, min=0, max=100, softMinValue=0.0001, softMaxValue=10)

  #---------------------------------------------------------------------------
  # Add a Color Tint control to the domeGrid's transform node - Default color 0,0,0 = Black
  #---------------------------------------------------------------------------

  # Have the code switch the input value based upon an isGrid check
  colorTintRGBcolor = cmds.colorSliderGrp('sliderDomeViewerColorTint', query=True, rgb=True)

  attrName = 'colorTint'
  attrRName = 'colorTintColorR'
  attrGName = 'colorTintColorG'
  attrBName = 'colorTintColorB'

  #if(mel.attributeExists(attrName, baseNodeName) == 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType='float3', usedAsColor=True, keyable=True)
  cmds.addAttr(baseNodeName, parent=attrName, longName=attrRName, attributeType='float', keyable=True, defaultValue=colorTintRGBcolor[0])
  cmds.addAttr(baseNodeName, parent=attrName, longName=attrGName, attributeType='float', keyable=True, defaultValue=colorTintRGBcolor[1])
  cmds.addAttr(baseNodeName, parent=attrName, longName=attrBName, attributeType='float', keyable=True, defaultValue=colorTintRGBcolor[2])
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  
  # Connect the Grid Surface Color swatch to the surface shader
  #cmds.connectAttr( (baseNodeName+'.'+attrName), domeViewer_maya_tex+'.colorGain', force=True)

  # Setup the domeViewer & domeViewerGrid transparency
  baseTransparency = 0

  if (isGrid == True):
    # The grid background is 75% transparent
    baseTransparency = 0.75
  else:
    # The viewer background is solid
    baseTransparency = 0

  #---------------------------------------------------------------------------
  # Add a Grid Surface Transparency control to the domeGrid's transform node - Default value 0.25
  #---------------------------------------------------------------------------
  attrName = 'transparency'
  cmds.addAttr(baseNodeName, longName=attrName, attributeType='double', keyable=True, defaultValue=baseTransparency, min=0, max=1)

  # Connect the Grid Surface transparency swatch to the surface shader
  cmds.connectAttr((baseNodeName+'.'+attrName), domeViewer_preview_shader_name+'.transparencyR', force=True)
  cmds.connectAttr((baseNodeName+'.'+attrName), domeViewer_preview_shader_name+'.transparencyG', force=True)
  cmds.connectAttr((baseNodeName+'.'+attrName), domeViewer_preview_shader_name+'.transparencyB', force=True)

  #---------------------------------------------------------------------------  
  # Add a display mode expression to the domeGrid's transform node
  #---------------------------------------------------------------------------

  domeRadiusTransform =  meshName
  domeSurfaceShape = meshName
  domeSurfaceShapeNode = getObjectShapeNode(domeSurfaceShape)

  exprName = ''
  previewAttrName = 'displayMode'
  # The expression name is domeGrid_displayModeExpr
  exprName = domeRadiusTransform + '_' + previewAttrName + 'Expr'

  PreviewShapeExpr = ''

  PreviewShapeExpr += '// Custom ' + previewAttrName + ' Preview Shape Expressions\n\n'

  # Color controls - colorGain is the result of multiplying the exposure by the color tint
  PreviewShapeExpr += domeViewer_maya_tex + ".colorGainR = " + domeRadiusTransform+ ".colorTintColorR" + " * " + domeRadiusTransform+ ".exposure;"+ "\n\n"
  PreviewShapeExpr += domeViewer_maya_tex + ".colorGainG = " + domeRadiusTransform+ ".colorTintColorG" + " * " + domeRadiusTransform+ ".exposure;"+ "\n\n"
  PreviewShapeExpr += domeViewer_maya_tex + ".colorGainB = " + domeRadiusTransform+ ".colorTintColorB" + " * " + domeRadiusTransform+ ".exposure;"+ "\n\n"

  # Visibility Controls
  PreviewShapeExpr += "string $currentPanel;\n"
  PreviewShapeExpr += "if(" + domeRadiusTransform + "." + previewAttrName + " == 0){\n"
  PreviewShapeExpr += "  // Off Mode\n"
  PreviewShapeExpr += "  " + domeSurfaceShape + ".overrideDisplayType = 2;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideEnabled = 1;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideShading = 0;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".visibility = 0;\n"
  PreviewShapeExpr += "}else if(" + domeRadiusTransform + "." + previewAttrName + " == 1){\n"
  PreviewShapeExpr += "  // Wireframe Mode\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideEnabled = 1;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideShading = 0;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".visibility = 1;\n"
  PreviewShapeExpr += "}else if(" + domeRadiusTransform + "." + previewAttrName + " == 2){\n"
  PreviewShapeExpr += "  // Shaded Mode\n"
  PreviewShapeExpr += "  $currentPanel = \"modelPanel4\";\n"
  PreviewShapeExpr += "  if(`modelEditor -exists currentPanel`)\n"
  PreviewShapeExpr += "  modelEditor -edit -wireframeOnShaded 0 currentPanel;\n"
  PreviewShapeExpr += "  $currentPanel = \"StereoPanel\";\n"
  PreviewShapeExpr += "  if (`modelEditor -exists currentPanel`)\n"
  PreviewShapeExpr += "  modelEditor -edit -wireframeOnShaded 0 currentPanel;\n"
  PreviewShapeExpr += "  " + domeSurfaceShape + ".overrideDisplayType = 2;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideEnabled = 1;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".overrideShading = 1;\n"
  PreviewShapeExpr += "  " + domeRadiusTransform + ".visibility = 1;\n"
  PreviewShapeExpr += "}else if(" + domeRadiusTransform + "." + previewAttrName + " == 3 ){\n"
  PreviewShapeExpr += "  // Wireframe on Shaded Mode\n"
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
  PreviewShapeExpr += "}\n"
  PreviewShapeExpr += "\n"
  PreviewShapeExpr += "\n"

  #----------------------------------------------------
  # Double Sided Preview Shape Rendering
  #----------------------------------------------------

  previewAttrName = 'doubleSidedShading'

  # Visibility Controls
  PreviewShapeExpr += "// Custom Double Sided Shading Expressions\n\n"
  PreviewShapeExpr += "if(" + previewAttrName + " == 0){\n"
  PreviewShapeExpr += "  print(\"Double Sided Shading Enabled\\n\");\n"
  PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".doubleSided\" 1; \n"
  PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".opposite\" 0; \n"
  PreviewShapeExpr += "}else if(" + previewAttrName + " == 1 ){\n"
  PreviewShapeExpr += "  print(\"Frontface Shading Enabled\\n\");\n"
  PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".doubleSided\" 0; \n"
  PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".opposite\" 0; \n"
  PreviewShapeExpr += "}\n"
  #PreviewShapeExpr += "}else if(" + previewAttrName + " == 2){\n"
  #PreviewShapeExpr += "  print(\"Backface Shading Enabled\\n\");\n"
  #PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".doubleSided\" 0; \n"
  #PreviewShapeExpr += "  setAttr \"" + domeSurfaceShape + ".opposite\" 1; \n"
  #PreviewShapeExpr += "}\n"
  

  print 'DomeGrid Extra Attribute Expressions:'
  print PreviewShapeExpr

  cmds.expression(name=exprName, string=PreviewShapeExpr, object=domeRadiusTransform, alwaysEvaluate=True, unitConversion=all)

  # ---------------------------------------------------
  # Set up the stereo place 2D texture map offsets
  # ---------------------------------------------------
  
  # Swap the right and left views if required
  if cmds.checkBoxGrp('checkGrpDomeViewerReverseEyeOrder', query=True, value1=True):
    if stereoView == 2:
      # Flip the left eye to the right eye view
      stereoView = 3
    elif stereoView == 3:
      # Flip the right eye to the left eye view
      stereoView = 2
  
  
  # Get the selected panoramic image format
  currentPanoFormat = cmds.optionMenuGrp('menuDomeViewerPanoramaFormat', query=True, select=True)
  # Deal with left and right flipped 360 degree projections
  if(currentPanoFormat == 17):
    # GearVR Mono Cube
    if stereoView == 2:
      # Flip the left eye to the right eye view
      stereoView = 3
    elif stereoView == 3:
      # Flip the right eye to the left eye view
      stereoView = 2
  
  # Figure out what place 2D node shifts are required
  if stereoMode == 2:
    # Side by Side Stereo
    # Stretch the horizontal texture area (coverage U) to twice its width
    cmds.setAttr(domeViewer_maya_placement+'.coverageU', 2)
    if stereoView == 2:
      # Left Eye View
      # Pan the image so the origin is placed at the left frame position 
      cmds.setAttr(domeViewer_maya_placement+'.translateFrameU', 0)
    if stereoView == 3:
      # Right Eye View
      # Pan the image so the origin is placed at the right frame position 
      cmds.setAttr(domeViewer_maya_placement+'.translateFrameU', 1)
  elif stereoMode == 3:
    # Over Under Stereo
    # Stretch the vertical texture area (coverage V) to twice its width
    cmds.setAttr(domeViewer_maya_placement+'.coverageV', 2)
    if stereoView == 2:
      # Left Eye View
      # Pan the image so the origin is placed at the left frame position 
      cmds.setAttr(domeViewer_maya_placement+'.translateFrameV', 1)
    if stereoView == 3:
      # Right Eye View
      # Pan the image so the origin is placed at the right frame position 
      cmds.setAttr(domeViewer_maya_placement+'.translateFrameV', 0)
  
  # Selecting the file texture node so the image sequence expressions are active
  selectNodeEvalString = 'print("[Selecting Node] " + \"' + domeViewer_maya_tex + '\" + "\\n");evalDeferred("showEditorExact(\\"' + domeViewer_maya_tex + '\\")");'
  print(selectNodeEvalString)
  mel.eval(selectNodeEvalString)
  
  # Output the name of the new fileTexture node
  return domeViewer_maya_tex
  

# Move the domeViewer camera back to it's default starting angle
def resetDomeViewerCameraAngle():
  import maya.cmds as cmds

  viewerCameraName = 'ViewerCamera1'

  if cmds.objExists(viewerCameraName):
      # Reset the camera position
      cmds.setAttr(viewerCameraName+'.rx', 0)
      cmds.setAttr(viewerCameraName+'.ry', 0)
      cmds.setAttr(viewerCameraName+'.rz', 0)
      cmds.setAttr(viewerCameraName+'.tx', 0)
      cmds.setAttr(viewerCameraName+'.ty', 0)
      cmds.setAttr(viewerCameraName+'.tz', 0)
      
      viewerCameraShape = getObjectShapeNode(viewerCameraName)
      
      # Reset the DomeViewer camera's field of view to use an 18mm lens which means a 90 degree FOV
      cmds.setAttr(viewerCameraShape[0]+'.focalLength', 18)
      

# Syntax: createDomeViewerCamera('ViewerCamera', 'domeViewer', 'domeViewerGrid')
def createDomeViewerCamera(viewerCameraName, meshName, gridMeshName):
  import os
  import math
  import maya.cmds as cmds
  import maya.mel as mel
  
  currentPanoFormat = cmds.optionMenuGrp('menuDomeViewerPanoramaFormat', query=True, select=True)
  
  #viewerCameraName = 'viewerCamera'
  
  # Remove the old camera
  if cmds.objExists(viewerCameraName + '1'): 
    cmds.select(viewerCameraName + '1', replace=True)
    cmds.delete()
  
  # Calculate the focal length from the field of view
  domeViewerFOV = cmds.floatSliderGrp('sliderDomeViewerFOV', query=True, value=True)
  horizontalFilmAperture = 1.417
  focal = math.tan (0.00872665 * domeViewerFOV)
  focal = (0.5 * horizontalFilmAperture) / (focal * 0.03937)
  
  cameraName = cmds.camera(name=viewerCameraName, focalLength=focal, filmFit='Vertical', nearClipPlane=1, farClipPlane=1000, cameraScale=1)
  
  # Unselect the geometry in the scene
  cmds.select(clear=True)
  
  # Change the icon size
  cmds.setAttr(cameraName[0]+'.locatorScale', 15)
  
  # Reset the camera position
  cmds.setAttr(cameraName[0]+'.rx', 0)
  cmds.setAttr(cameraName[0]+'.ry', 0)
  cmds.setAttr(cameraName[0]+'.rz', 0)
  cmds.setAttr(cameraName[0]+'.tx', 0)
  cmds.setAttr(cameraName[0]+'.ty', 0)
  cmds.setAttr(cameraName[0]+'.tz', 0)
  
  # Setup the default perspective camera view
  regularSceneCamera = 'persp'
  
  # Tipped View
  cmds.setAttr(regularSceneCamera+'.rx', 20)
  cmds.setAttr(regularSceneCamera+'.ry', -80)
  
  # Level View
  # cmds.setAttr(regularSceneCamera+'.rx', 0)
  # cmds.setAttr(regularSceneCamera+'.ry', -60)
  cmds.setAttr(regularSceneCamera+'.rz', 0)
  cmds.setAttr(regularSceneCamera+'.tx', -800)
  cmds.setAttr(regularSceneCamera+'.ty', 79)
  cmds.setAttr(regularSceneCamera+'.tz', 450)
  
  cmds.viewFit(regularSceneCamera)
  
  # Turn off the grid
  cmds.modelEditor('modelPanel4', edit=True, grid=False)
  
  # Turn on hardware texturing and shading
  cmds.modelEditor('modelPanel1', edit=True, displayAppearance='smoothShaded', wireframeOnShaded=False, displayTextures=True, displayLights="none")
  cmds.modelEditor('modelPanel4', edit=True, displayAppearance='smoothShaded', wireframeOnShaded=False, displayTextures=True, displayLights="none")
  
  gridModeEnabled = cmds.checkBoxGrp('checkGrpDomeViewerGridlinesOverlay', query=True, value1=True)
  
  # Point constrain the mesh to the camera
  if cmds.checkBoxGrp('checkGrpDomeViewerPointConstrain', query=True, value1=True):
    cmds.pointConstraint(cameraName[0], meshName, weight=1)

    # Add the point constraint for the fulldome grid too
    if (currentPanoFormat == 1):
      if (gridModeEnabled == 1):
        cmds.pointConstraint(cameraName[0], gridMeshName, weight=1)
      
  # Switch the viewport to look through a new fulldome viewing camera
  cmds.lookThru(cameraName)


# Syntax: createDomeViewerStereoCamera('stereoCamera', 'domeViewer', 'domeViewerGrid', 800)
def createDomeViewerStereoCamera(viewerCameraName, meshName, gridMeshName, cameraSeparation):
  import os
  import math
  import maya.cmds as cmds
  import maya.mel as mel
  cmds.loadPlugin('stereoCamera', qt=True)
  import maya.app.stereo.stereoCameraRig as stereoCameraRig
  
  currentPanoFormat = cmds.optionMenuGrp('menuDomeViewerPanoramaFormat', query=True, select=True)
  
  # Manually define the name of the center camera object
  # viewerCameraName = "stereoCamera"
  cameraName =  viewerCameraName
  
  # Remove the old camera
  if cmds.objExists(viewerCameraName): 
    cmds.select(viewerCameraName, replace=True)
    cmds.delete()
    print('[Removing Old Camera Rig] ' + viewerCameraName)
   
  # Calculate the focal length from the field of view
  domeViewerFOV = cmds.floatSliderGrp('sliderDomeViewerFOV', query=True, value=True)
  horizontalFilmAperture = 1.417
  focal = math.tan (0.00872665 * domeViewerFOV)
  focal = (0.5 * horizontalFilmAperture) / (focal * 0.03937)

  # Add the stereo camera rig
  rig = stereoCameraRig.createStereoCameraRig('StereoCamera')
  # [u'stereoCamera', u'stereoCameraLeft', u'stereoCameraRight']
  
  # Get the stereo camera rig shape nodes for the center/right/left cameras
  rig_center_shape_name = getObjectShapeNode(rig[0])
  # Result: [u'stereoCameraCenterCamShape', u'stereoCameraFrustum'] #

  rig_left_shape_name = getObjectShapeNode(rig[1])
  # Result: [u'stereoCameraLeftShape'] #

  rig_right_shape_name = getObjectShapeNode(rig[2])
  # Result: [u'stereoCameraRightShape'] #
  
  # Changes the render settings to set the stereo camera to be a renderable camera
  cmds.setAttr(rig_left_shape_name[0]+'.renderable', 1) #stereoCameraLeftShape
  cmds.setAttr(rig_right_shape_name[0]+'.renderable', 1) #stereoCameraRightShape
  cmds.setAttr('topShape.renderable', 0)
  cmds.setAttr('sideShape.renderable', 0)
  cmds.setAttr('frontShape.renderable', 0)
  cmds.setAttr('perspShape.renderable', 0)
  
  # Adjust the focal length
  cmds.setAttr(rig_center_shape_name[0]+'.focalLength', focal)
  
  # Set the stereo mode to parallel
  cmds.setAttr(rig_center_shape_name[0]+'.stereo', 3)
  
  # Lock the stereo mode control
  cmds.setAttr(rig_center_shape_name[0]+'.stereo', lock=True)
  
  # Adjust the rig's interaxial separation to move the cameras apart
  cmds.setAttr(rig_center_shape_name[0]+'.interaxialSeparation', cameraSeparation)
  
  # Lock the interaxialSeparation control
  cmds.setAttr(rig_center_shape_name[0]+'.interaxialSeparation', lock=True)
  
  # This attribute isn't actually used i the DomeViewer since the stereo rig is set to a parallel stereo mode
  cmds.setAttr(rig_center_shape_name[0]+'.zeroParallax', cameraSeparation)
  
  # Break apart the left and right camera transform node's translation and rotation attributes
  cmds.setAttr(rig[1]+'.inheritsTransform', 0);
  cmds.setAttr(rig[2]+'.inheritsTransform', 0);
  
  # Unselect the geometry in the scene
  cmds.select(clear=True)
  
  # Change the icon size
  cmds.setAttr(rig_center_shape_name[0]+'.locatorScale', 15)
  cmds.setAttr(rig_left_shape_name[0]+'.locatorScale', 15)
  cmds.setAttr(rig_right_shape_name[0]+'.locatorScale', 15)
  
  # Lock the center camera rig transform
  cmds.setAttr(rig[0]+'.translate', lock=True)
  
  # Un-lock the left camera rig rotations
  unlockAncestor(rig[1]+'.rotate', False)
  
  # Un-lock the right camera rig rotations
  unlockAncestor(rig[2]+'.rotate', False)
  
  # Connect the left camera rotation to the base of the rig
  cmds.connectAttr(rig[0]+'.rotate', rig[1]+'.rotate', force=True)

  # Connect the right camera rotation to the base of the rig
  cmds.connectAttr(rig[0]+'.rotate', rig[2]+'.rotate', force=True)
  
  # Reset the camera position
  cmds.setAttr(rig[0]+'.rx', 0)
  cmds.setAttr(rig[0]+'.ry', 0)
  cmds.setAttr(rig[0]+'.rz', 0)
  
  # Setup the default perspective camera view
  regularSceneCamera = 'persp'
  
  # Tipped View
  cmds.setAttr(regularSceneCamera+'.rx', 20)
  cmds.setAttr(regularSceneCamera+'.ry', -80)
  
  # Level View
  # cmds.setAttr(regularSceneCamera+'.rx', 0)
  # cmds.setAttr(regularSceneCamera+'.ry', -60)
  cmds.setAttr(regularSceneCamera+'.rz', 0)
  cmds.setAttr(regularSceneCamera+'.tx', -800)
  cmds.setAttr(regularSceneCamera+'.ty', 79)
  cmds.setAttr(regularSceneCamera+'.tz', 450)
  
  cmds.viewFit(regularSceneCamera)

  # gridModeEnabled = cmds.checkBoxGrp('checkGrpDomeViewerGridlinesOverlay', query=True, value1=True)
  # 
  # Point constrain the mesh to the camera
  # if cmds.checkBoxGrp('checkGrpDomeViewerPointConstrain', query=True, value1=True):
  #   cmds.pointConstraint(cameraName[0], meshName, weight=1)

  #   # Add the point constraint for the fulldome grid too
  #   if (currentPanoFormat == 1):
  #     if (gridModeEnabled == 1):
  #       cmds.pointConstraint(cameraName[0], gridMeshName, weight=1)
   
  # Switch the viewport to look through a new stereo viewing camera
  cameraName = 'stereoCamera'
  #mel.eval('stereoCameraSwitchToCamera ' + cameraName + ' modelPanel1')
  #mel.eval('stereoCameraSwitchToCamera ' + cameraName + ' modelPanel4')
  from maya.app.stereo import stereoCameraCustomPanel
  stereoCameraCustomPanel.switchToCamera(cameraName, 'modelPanel4')
  #stereoCameraCustomPanel.switchToCamera(cameraName, 'StereoPanelEditor')

  # Turn off the grid
  cmds.modelEditor('modelPanel1', edit=True, grid=False)
  cmds.modelEditor('modelPanel4', edit=True, grid=False)
  cmds.modelEditor('StereoPanelEditor', edit=True, grid=False)
  
  # Turn on hardware texturing and shading
  cmds.modelEditor('modelPanel1', edit=True, displayAppearance='smoothShaded', activeOnly=False, wireframeOnShaded=False, displayTextures=True, displayLights="none")
  cmds.modelEditor('modelPanel4', edit=True, displayAppearance='smoothShaded', activeOnly=False, wireframeOnShaded=False, displayTextures=True, displayLights="none")
  cmds.modelEditor('StereoPanelEditor', edit=True, displayAppearance='smoothShaded', activeOnly=False, wireframeOnShaded=False, displayTextures=True, displayLights="none")
  
  
  # Read the current setting in the DomeViewer "Stereo Display" options menu
  stereoDisplayMode = cmds.optionMenuGrp('menuDomeViewerStereoDisplay', query=True, select=True)
  #stereoDisplayMode = 1
  
  # Stereo Display modes
  if stereoDisplayMode == 1:
    # Full Color Anaglyph
    stereoCameraCustomPanel.stereoCameraViewCallback("StereoPanelEditor", "{'displayMode': 'anaglyph'}")
  elif stereoDisplayMode == 2:
    # Luminanace Anaglyph
    stereoCameraCustomPanel.stereoCameraViewCallback("StereoPanelEditor", "{'displayMode': 'anaglyphLum'}")
  elif stereoDisplayMode == 3:
    # Freeview (Parallel)
    stereoCameraCustomPanel.stereoCameraViewCallback("StereoPanelEditor", "{'displayMode': 'freeview'}")
  elif stereoDisplayMode == 4:
    # Freeview (Crossed)
    stereoCameraCustomPanel.stereoCameraViewCallback("StereoPanelEditor", "{'displayMode': 'freeviewX'}")
  elif stereoDisplayMode == 5:
    # Horizontal Interlace
    stereoCameraCustomPanel.stereoCameraViewCallback("StereoPanelEditor", "{'displayMode': 'interlace'}")
  elif stereoDisplayMode == 6:
    # Checkerboard
    stereoCameraCustomPanel.stereoCameraViewCallback("StereoPanelEditor", "{'displayMode': 'checkerboard'}")
  elif stereoDisplayMode == 7:
    # Center Eye
    stereoCameraCustomPanel.stereoCameraViewCallback("StereoPanelEditor", "{'displayMode': 'centerEye'}")
  elif stereoDisplayMode == 8:
    # Left Eye
    stereoCameraCustomPanel.stereoCameraViewCallback("StereoPanelEditor", "{'displayMode': 'leftEye'}")
  elif stereoDisplayMode == 9:
    # Right Eye
    stereoCameraCustomPanel.stereoCameraViewCallback("StereoPanelEditor", "{'displayMode': 'rightEye'}")
  
  # return the rig array:
  # [u'stereoCamera', u'stereoCameraLeft', u'stereoCameraRight']
  return rig

# Load a new domeViewer polygon mesh into the scene
# Syntax: createDomeViewerMesh('pCube1', 'mentalRayCube1_mesh', '45', 300 , viewerFlipScale, stereoView)
def createDomeViewerMesh(meshName, meshFileName, domeTiltAngle, scale, viewerFlipScale, stereoView):
  import os  
  import maya.cmds as cmds
  import maya.mel as mel
  
  # stereoView 0= Don't rename 1=Center, 2=Left, 3=Right
  stereoViewPrefix = ''
  if stereoView == 0:
    # Keep the original name
    stereoViewPrefix = ''
  elif stereoView == 1:
    # Center View
    stereoViewPrefix = 'center_'
  elif stereoView == 2:
    # Left View
    stereoViewPrefix = 'left_'
  elif stereoView == 3:
    # Right View
    stereoViewPrefix = 'right_'
  else:
    # The fallback option is to use the center view
    stereoViewPrefix = 'center_'
  
  # Viewer Mesh Object Details
  meshFileExtension = '.ma'
  meshFileType = 'mayaAscii'
  
  # Get the selected geometry
  #object_selection = cmds.ls(sl=True)

  if cmds.objExists(meshName): 
    print('Removing existing Domemain3D object: ' + meshName)
    cmds.select(meshName, replace=True)
    cmds.delete()
  
  updatedMeshName = stereoViewPrefix+meshName
  if cmds.objExists(updatedMeshName): 
    print('Removing existing Domemain3D object: ' + updatedMeshName)
    cmds.select(updatedMeshName, replace=True)
    cmds.delete()
    
  #if cmds.objExists(meshFileName + '_sceneConfigurationScriptNode'): 
  #  cmds.select(meshFileName + '_sceneConfigurationScriptNode', replace=True)
  #  cmds.delete()
  
  #if cmds.objExists(meshFileName + '_uiConfigurationScriptNode'): 
  #  cmds.select(meshFileName + '_uiConfigurationScriptNode', replace=True)
  #  cmds.delete()
    
  # Load the viewer model from the Domemain3D source images directory
  domeViewerModelFile = getModelsPath(meshFileName + meshFileExtension)
  
  # Load the Maya .ma format viewer model into the scene
  domeViewer_mesh_file = cmds.file(domeViewerModelFile, i=True, type=meshFileType)
  
  # Set the default size (scale) of the viewer backdrop
  # Flip the scaleX attribute to mirror the texture direction left/right
  cmds.setAttr(meshName + '.scaleZ', scale)
  cmds.setAttr(meshName + '.scaleX', (scale * viewerFlipScale))
  cmds.setAttr(meshName + '.scaleY', scale)
  
  # Tilt the fulldome screen
  cmds.setAttr(meshName + '.rotateX', (-1*domeTiltAngle));

  # Rename the mesh
  if cmds.objExists(meshName): 
    print('[Renaming] ' + meshName + ' to: ' + updatedMeshName)
    cmds.rename(meshName, updatedMeshName)
    # Return the mesh name
    return updatedMeshName

  # Return the mesh name
  return meshName
  
"""
Create a DomeViewer mesh
---------------------------
A python function to create a fulldome image viewer with an incandescent lambert based shading network.
"""
def createDomeViewer():
  import os  
  import maya.cmds as cmds
  import maya.mel as mel
  
  # Setup the tilt angle on the fulldome screen
  domeTiltAngle = cmds.floatSliderGrp('sliderDomeViewerDomeTiltAngle', query=True, value=True)
  #domeTiltAngle = -35
  
  # Preview Camera Name
  viewerCameraName = 'ViewerCamera'
  
  #---------------------------------------------------------------------------
  # Find out what type of panorama to add
  #---------------------------------------------------------------------------
  
  # Get the selected panoramic image format
  currentPanoFormat = cmds.optionMenuGrp('menuDomeViewerPanoramaFormat', query=True, select=True)

  gridMeshName = ""
  gridMeshFileName = ""
  
  if(currentPanoFormat == 1):
    # 180 Degree Fulldome
    meshName = 'domeViewer'
    
    # Polygon sphere with triangle pinch point
    meshFileName = 'fulldome_mesh'

    # All quads polygon sphere - no pinch point
    #meshFileName = 'fulldome_quads_mesh'

    gridMeshName = 'domeViewerGrid'
    gridMeshFileName = 'fulldomeGrid_mesh'
  if(currentPanoFormat == 2):
    # 180 Degree Fulldome on 4:3 Ratio Background
    meshName = 'domeViewer'
    
    # Polygon sphere with triangle pinch point
    #meshFileName = 'fulldome_mesh'

    # All quads polygon sphere - no pinch point
    meshFileName = 'fulldome_quads_4_3_mesh'

    gridMeshName = 'domeViewerGrid'
    gridMeshFileName = 'fulldomeGrid_mesh'
  if(currentPanoFormat == 3):
    # 180 Degree Fulldome on 16:9 Ratio Background
    meshName = 'domeViewer'
    
    # Polygon sphere with triangle pinch point
    #meshFileName = 'fulldome_mesh'

    # All quads polygon sphere - no pinch point
    meshFileName = 'fulldome_quads_16_9_mesh'

    gridMeshName = 'domeViewerGrid'
    gridMeshFileName = 'fulldomeGrid_mesh'
  elif(currentPanoFormat == 4):
    # 360 Degree Angular Fisheye
    meshName = 'angular360'
    meshFileName = 'angular360_mesh'
  elif(currentPanoFormat == 5):
    # Mirror Ball
    meshName = 'mirrorball'
    meshFileName = 'mirrorball_mesh'
  elif(currentPanoFormat == 6):
    # Equirectangular (LatLong)
    meshName = 'latlong'
    meshFileName = 'latlongSphere_mesh'
  elif(currentPanoFormat == 7):
    # Cylindrical
    meshName = 'cylinder'
    meshFileName = 'cylinder_mesh'
  elif(currentPanoFormat == 8):
    # Cube Map 3x2
    meshName = 'cube3x2'
    meshFileName = 'cube3x2_mesh'
  elif(currentPanoFormat == 9):
    # Vertical Cross Cube
    meshName = 'verticalCross'
    meshFileName = 'verticalCrossCube_mesh'
  elif(currentPanoFormat == 10):
    # Horizontal Cross Cube
    meshName = 'horizontalCross'
    meshFileName = 'horizontalCrossCube_mesh'
  elif(currentPanoFormat == 11):
    # Vertical Tee Cube
    meshName = 'verticalTee'
    meshFileName = 'verticalTeeCube_mesh'
  elif(currentPanoFormat == 12):
    # Horizontal Tee Cube
    meshName = 'horizontalTee'
    meshFileName = 'horizontalTeeCube_mesh'
  elif(currentPanoFormat == 13):
    # Vertical Strip Cube
    meshName = 'verticalStrip'
    meshFileName = 'verticalStripCube_mesh'
  elif(currentPanoFormat == 14):
    # Horizontal Strip Cube
    meshName = 'horizontalStrip'
    meshFileName = 'horizontalStripCube_mesh'
  elif(currentPanoFormat == 15):
    # Mental Ray Horizontal Strip Cube
    meshName = 'pCube1'
    meshFileName = 'mentalRayCube1_mesh'
  elif(currentPanoFormat == 16):
    # Quadsphere
    meshName = 'polyStarglobe'
    meshFileName = 'starglobe_mesh'
  elif(currentPanoFormat == 17):
    # GearVR Mono Cube
    meshName = 'gearVRMono'
    meshFileName = 'gearVRCube_mesh'
  elif(currentPanoFormat == 18):
    # Ricoh Theta S
    meshName = 'thetaViewer'
    meshFileName = 'ricoh_theta_s_mesh'
  elif(currentPanoFormat == 19):
    # Facebook Cube Map 3x2
    meshName = 'facebookCube3x2'
    meshFileName = 'facebookCube3x2_mesh'
  elif(currentPanoFormat == 20):
    # Facebook Pyramid
    meshName = 'facebookPyramid'
    meshFileName = 'facebookPyramid_mesh'
  elif(currentPanoFormat == 21):
    # Facebook Vertical Strip Cube
    meshName = 'facebookVerticalStrip'
    meshFileName = 'facebookVerticalStripCube_mesh'
  elif(currentPanoFormat == 22):
    # LG360
    meshName = 'lg360Viewer'
    meshFileName = 'lg360_mesh'
  elif(currentPanoFormat == 23):
    # Samsung Gear 360 Camera
    meshName = 'SamsungGear360Viewer'
    meshFileName = 'samsungGear360_mesh'
   
  #---------------------------------------------------------------------------
  # Create the panoramic elements in Maya
  #---------------------------------------------------------------------------
  
  # Check if the viewer direction is flipped
  # This will flip the inside vs outside of the preview shape
  viewerMeshScale = 0
  viewerFlipEnabled = cmds.checkBoxGrp('checkGrpDomeViewerFlipScale', query=True, value1=True)
  
  # Checkbox enabled = flipped / checkbox disabled = not flipping
  if(viewerFlipEnabled):
    viewerFlipScale = -1
  else:
    viewerFlipScale = 1
  
  # Create the viewer mesh
  if(currentPanoFormat == 1):
    # fulldome mesh
    viewerMeshScale = 150
  elif(currentPanoFormat == 16):
    # The Quadsphere mesh is 12X larger than the other meshes by default
    viewerMeshScale = 25
  else:
    # All other meshes
    viewerMeshScale = 300

  # Check if the stereo format is: 1="None - Mono 2D", 2="Side by Side Stereo", 3="Over Under Stereo"
  stereoMode = cmds.optionMenuGrp('menuDomeViewerStereoFormat', query=True, select=True)
  
  if(stereoMode == 1):
    # Stereo: None - Mono 2D
    
    # Center Eye
    stereoView = 1
    # Add the mesh to the scene
    viewerMeshNodeCenter = createDomeViewerMesh(meshName, meshFileName, domeTiltAngle, viewerMeshScale, viewerFlipScale, stereoView)

    # Create the surface material
    viewerTextureNode = createDomeViewerTexture(viewerMeshNodeCenter, False, stereoMode, 1)
    
    # Create the fulldome alignment grid
    gridModeEnabled = cmds.checkBoxGrp('checkGrpDomeViewerGridlinesOverlay', query=True, value1=True)
    gridMeshNodeCenter = ''
    if(currentPanoFormat <= 3):
      if(gridModeEnabled == 1):
        print('Creating a Bradbury fulldome reference grid.')
        # Create the dome alignment grid mesh
        gridMeshNodeCenter = createDomeViewerMesh(gridMeshName, gridMeshFileName, domeTiltAngle, viewerMeshScale*0.98, 1, stereoView)
        # Create the dome alignment grid surface material
        viewerTextureNode = createDomeViewerTexture(gridMeshNodeCenter, True, stereoMode, stereoView)
        # Constrain the dome alignment grid mesh to the stereoCamera view
        cmds.pointConstraint(cameraRigArray[0], gridMeshNodeCenter, weight=1)
    
    # Add the camera to the scene
    createDomeViewerCamera(viewerCameraName, viewerMeshNodeCenter, gridMeshNodeCenter)
    
    # Select the File Texture node in the attribute editor so the image sequence loader will start working
    mel.eval('showEditorExact("' + viewerTextureNode + '")')
  elif(stereoMode == 2):
    # Stereo: Side by Side Stereo
    # Add the camera to the scene
    stereoCameraSeparation = viewerMeshScale*4
    cameraRigArray = createDomeViewerStereoCamera('stereoCamera', 'domeViewer', 'domeViewerGrid', stereoCameraSeparation)
    print('[Stereo Camera Rig]')
    print(cameraRigArray)
    
    # Center Eye
    stereoView = 1
    # Add the center mesh to the scene
    viewerMeshNodeCenter = createDomeViewerMesh(meshName, meshFileName, domeTiltAngle, viewerMeshScale, viewerFlipScale, stereoView)
    # Create the surface material - Center View
    viewerTextureNodeCenter = createDomeViewerTexture(viewerMeshNodeCenter, False, stereoMode, stereoView)
    # Constrain the center viewer mesh to the stereoCamera view
    cmds.pointConstraint(cameraRigArray[0], viewerMeshNodeCenter, weight=1)
    # Create the fulldome alignment grid
    gridModeEnabled = cmds.checkBoxGrp('checkGrpDomeViewerGridlinesOverlay', query=True, value1=True)
    gridMeshNodeCenter = ''
    if(currentPanoFormat <= 3):
      if(gridModeEnabled == 1):
        print('Creating a Bradbury fulldome reference grid.')
        # Create the dome alignment grid mesh
        gridMeshNodeCenter = createDomeViewerMesh(gridMeshName, gridMeshFileName, domeTiltAngle, viewerMeshScale*0.98, 1, stereoView)
        # Create the dome alignment grid surface material
        viewerTextureNode = createDomeViewerTexture(gridMeshNodeCenter, True, stereoMode, stereoView)
        # Constrain the dome alignment grid mesh to the stereoCamera view
        cmds.pointConstraint(cameraRigArray[0], gridMeshNodeCenter, weight=1)
    
    # Left Eye
    stereoView = 2
    # Add the left mesh to the scene
    viewerMeshNodeLeft = createDomeViewerMesh(meshName, meshFileName, domeTiltAngle, viewerMeshScale, viewerFlipScale, stereoView)
    # Create the surface material - Left View
    viewerTextureNodeLeft = createDomeViewerTexture(viewerMeshNodeLeft, False, stereoMode, stereoView)
    # Constrain the left viewer mesh to the stereoCameraLeft view
    cmds.pointConstraint(cameraRigArray[1], viewerMeshNodeLeft, weight=1)
    # Create the fulldome alignment grid
    gridModeEnabled = cmds.checkBoxGrp('checkGrpDomeViewerGridlinesOverlay', query=True, value1=True)
    gridMeshNodeLeft = ''
    if(currentPanoFormat <= 3):
      if(gridModeEnabled == 1):
        print('Creating a Bradbury fulldome reference grid.')
        # Create the dome alignment grid mesh
        gridMeshNodeLeft = createDomeViewerMesh(gridMeshName, gridMeshFileName, domeTiltAngle, viewerMeshScale*0.98, 1, stereoView)
        # Create the dome alignment grid surface material
        viewerTextureNodeLeft = createDomeViewerTexture(gridMeshNodeLeft, True, stereoMode, stereoView)
        # Constrain the dome alignment grid mesh to the stereoCameraLeft view
        cmds.pointConstraint(cameraRigArray[1], gridMeshNodeLeft, weight=1)
    
    # Right Eye
    stereoView = 3
    # Add the right mesh to the scene
    viewerMeshNodeRight = createDomeViewerMesh(meshName, meshFileName, domeTiltAngle, viewerMeshScale, viewerFlipScale, stereoView)
    # Create the surface material - Right View
    viewerTextureNodeRight = createDomeViewerTexture(viewerMeshNodeRight, False, stereoMode, stereoView)
    # Constrain the right viewer mesh to the stereoCameraRight view
    cmds.pointConstraint(cameraRigArray[2], viewerMeshNodeRight, weight=1)
    # Create the fulldome alignment grid
    gridModeEnabled = cmds.checkBoxGrp('checkGrpDomeViewerGridlinesOverlay', query=True, value1=True)
    gridMeshNodeRight = ''
    if(currentPanoFormat <= 3):
      if(gridModeEnabled == 1):
        print('Creating a Bradbury fulldome reference grid.')
        # Create the dome alignment grid mesh
        gridMeshNodeRight = createDomeViewerMesh(gridMeshName, gridMeshFileName, domeTiltAngle, viewerMeshScale*0.98, 1, stereoView)
        # Create the dome alignment grid surface material
        viewerTextureNodeLeft = createDomeViewerTexture(gridMeshNodeRight, True, stereoMode, stereoView)
        # Constrain the dome alignment grid mesh to the stereoCameraRight view
        cmds.pointConstraint(cameraRigArray[2], gridMeshNodeRight, weight=1)
  elif(stereoMode == 3):
    # Stereo: Over Under Stereo
    # Add the camera to the scene
    stereoCameraSeparation = viewerMeshScale*4
    cameraRigArray = createDomeViewerStereoCamera('stereoCamera', 'domeViewer', 'domeViewerGrid', stereoCameraSeparation)
    print('[Stereo Camera Rig]')
    print(cameraRigArray)
    
    # Center Eye
    stereoView = 1
    # Add the center mesh to the scene
    viewerMeshNodeCenter = createDomeViewerMesh(meshName, meshFileName, domeTiltAngle, viewerMeshScale, viewerFlipScale, stereoView)
    # Create the surface material - Center View
    viewerTextureNodeCenter = createDomeViewerTexture(viewerMeshNodeCenter, False, stereoMode, stereoView)
    # Constrain the center viewer mesh to the stereoCamera view
    cmds.pointConstraint(cameraRigArray[0], viewerMeshNodeCenter, weight=1)
    # Create the fulldome alignment grid
    gridModeEnabled = cmds.checkBoxGrp('checkGrpDomeViewerGridlinesOverlay', query=True, value1=True)
    gridMeshNodeCenter = ''
    if(currentPanoFormat <= 3):
      if(gridModeEnabled == 1):
        print('Creating a Bradbury fulldome reference grid.')
        # Create the dome alignment grid mesh
        gridMeshNodeCenter = createDomeViewerMesh(gridMeshName, gridMeshFileName, domeTiltAngle, viewerMeshScale*0.98, 1, stereoView)
        # Create the dome alignment grid surface material
        viewerTextureNode = createDomeViewerTexture(gridMeshNodeCenter, True, stereoMode, stereoView)
        # Constrain the dome alignment grid mesh to the stereoCamera view
        cmds.pointConstraint(cameraRigArray[0], gridMeshNodeCenter, weight=1)
    
    # Left Eye
    stereoView = 2
    # Add the left mesh to the scene
    viewerMeshNodeLeft = createDomeViewerMesh(meshName, meshFileName, domeTiltAngle, viewerMeshScale, viewerFlipScale, stereoView)
    # Create the surface material - Left View
    viewerTextureNodeLeft = createDomeViewerTexture(viewerMeshNodeLeft, False, stereoMode, stereoView)
    # Constrain the left viewer mesh to the stereoCameraLeft view
    cmds.pointConstraint(cameraRigArray[1], viewerMeshNodeLeft, weight=1)
    # Create the fulldome alignment grid
    gridModeEnabled = cmds.checkBoxGrp('checkGrpDomeViewerGridlinesOverlay', query=True, value1=True)
    gridMeshNodeLeft = ''
    if(currentPanoFormat <= 3):
      if(gridModeEnabled == 1):
        print('Creating a Bradbury fulldome reference grid.')
        # Create the dome alignment grid mesh
        gridMeshNodeLeft = createDomeViewerMesh(gridMeshName, gridMeshFileName, domeTiltAngle, viewerMeshScale*0.98, 1, stereoView)
        # Create the dome alignment grid surface material
        viewerTextureNodeLeft = createDomeViewerTexture(gridMeshNodeLeft, True, stereoMode, stereoView)
        # Constrain the dome alignment grid mesh to the stereoCameraLeft view
        cmds.pointConstraint(cameraRigArray[1], gridMeshNodeLeft, weight=1)
    
    # Right Eye
    stereoView = 3
    # Add the right mesh to the scene
    viewerMeshNodeRight = createDomeViewerMesh(meshName, meshFileName, domeTiltAngle, viewerMeshScale, viewerFlipScale, stereoView)
    # Create the surface material - Right View
    viewerTextureNodeRight = createDomeViewerTexture(viewerMeshNodeRight, False, stereoMode, stereoView)
    # Constrain the right viewer mesh to the stereoCameraRight view
    cmds.pointConstraint(cameraRigArray[2], viewerMeshNodeRight, weight=1)
    # Create the fulldome alignment grid
    gridModeEnabled = cmds.checkBoxGrp('checkGrpDomeViewerGridlinesOverlay', query=True, value1=True)
    gridMeshNodeRight = ''
    if(currentPanoFormat <= 3):
      if(gridModeEnabled == 1):
        print('Creating a Bradbury fulldome reference grid.')
        # Create the dome alignment grid mesh
        gridMeshNodeRight = createDomeViewerMesh(gridMeshName, gridMeshFileName, domeTiltAngle, viewerMeshScale*0.98, 1, stereoView)
        # Create the dome alignment grid surface material
        viewerTextureNodeLeft = createDomeViewerTexture(gridMeshNodeRight, True, stereoMode, stereoView)
        # Constrain the dome alignment grid mesh to the stereoCameraRight view
        cmds.pointConstraint(cameraRigArray[2], gridMeshNodeRight, weight=1)
  elif(stereoMode == 4):
    # Stereo: Stereo Image Pairs
    # Add the camera to the scene
    stereoCameraSeparation = viewerMeshScale*4
    cameraRigArray = createDomeViewerStereoCamera('stereoCamera', 'domeViewer', 'domeViewerGrid', stereoCameraSeparation)
    print('[Stereo Camera Rig]')
    print(cameraRigArray)
    
    # Center Eye
    stereoView = 1
    # Add the center mesh to the scene
    viewerMeshNodeCenter = createDomeViewerMesh(meshName, meshFileName, domeTiltAngle, viewerMeshScale, viewerFlipScale, stereoView)
    # Create the surface material - Center View
    viewerTextureNodeCenter = createDomeViewerTexture(viewerMeshNodeCenter, False, stereoMode, stereoView)
    # Constrain the center viewer mesh to the stereoCamera view
    cmds.pointConstraint(cameraRigArray[0], viewerMeshNodeCenter, weight=1)
    # Create the fulldome alignment grid
    gridModeEnabled = cmds.checkBoxGrp('checkGrpDomeViewerGridlinesOverlay', query=True, value1=True)
    gridMeshNodeCenter = ''
    if(currentPanoFormat <= 3):
      if(gridModeEnabled == 1):
        print('Creating a Bradbury fulldome reference grid.')
        # Create the dome alignment grid mesh
        gridMeshNodeCenter = createDomeViewerMesh(gridMeshName, gridMeshFileName, domeTiltAngle, viewerMeshScale*0.98, 1, stereoView)
        # Create the dome alignment grid surface material
        viewerTextureNode = createDomeViewerTexture(gridMeshNodeCenter, True, stereoMode, stereoView)
        # Constrain the dome alignment grid mesh to the stereoCamera view
        cmds.pointConstraint(cameraRigArray[0], gridMeshNodeCenter, weight=1)
    
    # Left Eye
    stereoView = 2
    # Add the left mesh to the scene
    viewerMeshNodeLeft = createDomeViewerMesh(meshName, meshFileName, domeTiltAngle, viewerMeshScale, viewerFlipScale, stereoView)
    # Create the surface material - Left View
    viewerTextureNodeLeft = createDomeViewerTexture(viewerMeshNodeLeft, False, stereoMode, stereoView)
    # Constrain the left viewer mesh to the stereoCameraLeft view
    cmds.pointConstraint(cameraRigArray[1], viewerMeshNodeLeft, weight=1)
    # Create the fulldome alignment grid
    gridModeEnabled = cmds.checkBoxGrp('checkGrpDomeViewerGridlinesOverlay', query=True, value1=True)
    gridMeshNodeLeft = ''
    if(currentPanoFormat <= 3):
      if(gridModeEnabled == 1):
        print('Creating a Bradbury fulldome reference grid.')
        # Create the dome alignment grid mesh
        gridMeshNodeLeft = createDomeViewerMesh(gridMeshName, gridMeshFileName, domeTiltAngle, viewerMeshScale*0.98, 1, stereoView)
        # Create the dome alignment grid surface material
        viewerTextureNodeLeft = createDomeViewerTexture(gridMeshNodeLeft, True, stereoMode, stereoView)
        # Constrain the dome alignment grid mesh to the stereoCameraLeft view
        cmds.pointConstraint(cameraRigArray[1], gridMeshNodeLeft, weight=1)
    
    # Right Eye
    stereoView = 3
    # Add the right mesh to the scene
    viewerMeshNodeRight = createDomeViewerMesh(meshName, meshFileName, domeTiltAngle, viewerMeshScale, viewerFlipScale, stereoView)
    # Create the surface material - Right View
    viewerTextureNodeRight = createDomeViewerTexture(viewerMeshNodeRight, False, stereoMode, stereoView)
    # Constrain the right viewer mesh to the stereoCameraRight view
    cmds.pointConstraint(cameraRigArray[2], viewerMeshNodeRight, weight=1)
    # Create the fulldome alignment grid
    gridModeEnabled = cmds.checkBoxGrp('checkGrpDomeViewerGridlinesOverlay', query=True, value1=True)
    gridMeshNodeRight = ''
    if(currentPanoFormat <= 3):
      if(gridModeEnabled == 1):
        print('Creating a Bradbury fulldome reference grid.')
        # Create the dome alignment grid mesh
        gridMeshNodeRight = createDomeViewerMesh(gridMeshName, gridMeshFileName, domeTiltAngle, viewerMeshScale*0.98, 1, stereoView)
        # Create the dome alignment grid surface material
        viewerTextureNodeLeft = createDomeViewerTexture(gridMeshNodeRight, True, stereoMode, stereoView)
        # Constrain the dome alignment grid mesh to the stereoCameraRight view
        cmds.pointConstraint(cameraRigArray[2], gridMeshNodeRight, weight=1)
        
   
  # Unselect the geometry in the scene
  cmds.select(clear=True)
  
  # return the name of the domeViewer mesh
  return viewerMeshNodeCenter


"""
Create a starglobe
---------------------------
A python function to create a 8K textured starglobe with a mia_material_x_passes shading network.
"""
def createStarglobe():
  import os  
  import maya.cmds as cmds
  #import maya.mel as mel  

  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()

  # ---------------------------------------------------------------------
  # Set up the base folder path for the Domemain3D textures
  # ---------------------------------------------------------------------

  # Set the file texture variables to "" if you don't want a file to be specified
  #StarglobeMapFileTexture = ""

  StarglobeMapFileTexture = getSourceImagesPath('starglobe_quadsphere_8k.jpg')
  StarglobeMayaFileTexture = getSourceImagesPath('starglobe_quadsphere_2k.jpg')

  # Get the selected geometry
  object_selection = cmds.ls(sl=True)

  if cmds.objExists('polyStarglobe'): 
    print('Removing existing Domemain3D object: polyStarglobe')
    cmds.select( 'polyStarglobe', replace=True)
    cmds.delete()

  meshFileName= 'starglobe_mesh'

  if cmds.objExists(meshFileName + '_sceneConfigurationScriptNode'): 
   cmds.select( meshFileName + '_sceneConfigurationScriptNode', replace=True)
   cmds.delete()
  
  if cmds.objExists(meshFileName + '_uiConfigurationScriptNode'): 
   cmds.select( meshFileName + '_uiConfigurationScriptNode', replace=True)
   cmds.delete()

  # Load the quads based starglobe sphere model
  StarglobeModelFile = getModelsPath('starglobe_mesh.ma')

  # Load the Maya .ma format starglobe model into the scene
  starglobe_mesh_file = cmds.file (StarglobeModelFile, i=True, type='mayaAscii')

  # Create the shading group
  starglobe_mia_shader_group_name = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='starglobe_materialSG')
  
  starglobe_mia_shader_name = ''
  starglobe_tex_vector  = ''
  starglobe_tex_remap  = ''
  starglobe_tex_lookup  = ''
  starglobe_mr_tex  = ''
  starglobe_remap_color  = ''
  if cmds.checkBoxGrp('checkGrpCreateStarglobeMentalRayMaterials', query=True, value1=True) == True:
    # Create the mia_material + shading group
    starglobe_mia_shader_name = cmds.shadingNode('mia_material_x_passes', n='starglobe_material', asShader=True) 

    starglobe_tex_vector = cmds.shadingNode('mib_texture_vector', n='starglobe_mib_texture_vector1', asUtility=True ) 
    starglobe_tex_remap = cmds.shadingNode('mib_texture_remap', n='starglobe_mib_texture_remap1',  asUtility=True) 
    starglobe_tex_lookup= cmds.shadingNode('mib_texture_lookup', n='starglobe_mib_texture_lookup1',  asUtility=True) 
    starglobe_mr_tex = cmds.shadingNode('mentalrayTexture', n='starglobe_mentalrayTexture1', asTexture=True) 
    starglobe_remap_color = cmds.shadingNode('remapColor', n='starglobe_remapColor1', asTexture=True)

  # Create the Lambert in-scene preview material
  starglobe_preview_shader_name = cmds.shadingNode('lambert', n='starglobe_preview_material', asShader=True) 
  starglobe_maya_tex = cmds.shadingNode('file', n='starglobe_FileTexture', asTexture=True) 
  starglobe_maya_placement = cmds.shadingNode('place2dTexture', n='starglobe_place2dTexture', asUtility=True) 

  # Connect the place2D texture to the Maya starglobe file texture
  cmds.connectAttr(starglobe_maya_placement+'.coverage', starglobe_maya_tex+'.coverage', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.translateFrame', starglobe_maya_tex+'.translateFrame', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.rotateFrame', starglobe_maya_tex+'.rotateFrame', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.mirrorU', starglobe_maya_tex+'.mirrorU', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.mirrorV', starglobe_maya_tex+'.mirrorV', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.stagger', starglobe_maya_tex+'.stagger', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.wrapU', starglobe_maya_tex+'.wrapU', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.wrapV', starglobe_maya_tex+'.wrapV', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.repeatUV', starglobe_maya_tex+'.repeatUV', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.offset', starglobe_maya_tex+'.offset', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.rotateUV', starglobe_maya_tex+'.rotateUV', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.noiseUV', starglobe_maya_tex+'.noiseUV', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.vertexUvOne', starglobe_maya_tex+'.vertexUvOne', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.vertexUvTwo', starglobe_maya_tex+'.vertexUvTwo', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.vertexUvThree', starglobe_maya_tex+'.vertexUvThree', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.vertexCameraOne', starglobe_maya_tex+'.vertexCameraOne', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.outUV', starglobe_maya_tex+'.uvCoord', f=True)
  cmds.connectAttr(starglobe_maya_placement+'.outUvFilterSize', starglobe_maya_tex+'.uvFilterSize', f=True)

  if cmds.checkBoxGrp('checkGrpCreateStarglobeMentalRayMaterials', query=True, value1=True) == True:
    # Connect the color texture nodes
    cmds.connectAttr(starglobe_tex_vector+'.outValue', starglobe_tex_remap+'.input')
    #mib_texture_vector.outValue -> mib_texture_remap.input

    cmds.connectAttr(starglobe_tex_remap+'.outValue', starglobe_tex_lookup+'.coord')
    #mib_texture_remap.outValue -> mib_texture_lookup.coord

    cmds.connectAttr(starglobe_mr_tex+'.message', starglobe_tex_lookup+'.tex')
    #mentalrayTexture.message -> mib_texture_lookup.tex

    # Connect the starglobe texture to the diffuse color attribute
    #cmds.connectAttr(starglobe_tex_lookup+'.outValue', starglobe_mia_shader_name+'.diffuse')
    #mib_texture_lookup.outValue -> mia_material_x_passes.diffuse

    # Make the mia material shader act like an incandescent/surface shader material
    #cmds.connectAttr(starglobe_tex_lookup+'.outValue', starglobe_mia_shader_name+'.additional_color')
    #mib_texture_lookup.outValue -> mia_material_x_passes.additional_color

    # Make the mia material shader act like an incandescent/surface shader material
    # Add a remapColor node so it is possible to brighten the starglobe texture map
    cmds.connectAttr(starglobe_tex_lookup+'.outValue', starglobe_remap_color+'.color')
    cmds.connectAttr(starglobe_remap_color+'.outColor', starglobe_mia_shader_name+'.additional_color')
    #mib_texture_lookup.outValue -> remapColor.color
    #emapColor.outColor-> mia_material_x_passes.additional_color

    # Set values for the shading nodes

    # Set the mia_material to be a matte material
    #cmds.setAttr(starglobe_mia_shader_name+'.reflectivity', 0)

    # Set the mia_material to be a glossy material
    cmds.setAttr(starglobe_mia_shader_name+'.refl_color', 1, 1, 1, type='double3')
    cmds.setAttr(starglobe_mia_shader_name+'.reflectivity', 0)
    cmds.setAttr(starglobe_mia_shader_name+'.refl_gloss', 0.0)
    cmds.setAttr(starglobe_mia_shader_name+'.diffuse_roughness', 0)
    cmds.setAttr(starglobe_mia_shader_name+'.diffuse_weight', 1)

    # Set the material to a black diffuse color
    cmds.setAttr(starglobe_mia_shader_name+'.diffuse', 0, 0, 0, type='double3')

    # Note: the cutout opacity could be used to make the night sky alpha channel transparent or solid

    # Optional Light Linking

    # Set the mia_material_x_passes shader to ignore the illumination from the lights in the scene with "light linking"
    #starglobe_mia.mode 0 = Custom Linking
    #starglobe_mia.mode 1 = Inclusive Linking
    #starglobe_mia.mode 2 = Exclusive Linking
    #starglobe_mia.mode 4 = Maya Linking

    # Note: All scene lights are skipped by default with "Exclusive linking" mode 2
    cmds.setAttr(starglobe_mia_shader_name+'.mode', 2)

    # End of Optional Light Linking

  # Load the file texture maps
  if cmds.checkBoxGrp('checkGrpCreateStarglobeMentalRayMaterials', query=True, value1=True) == True:
    # Set the filename for the mental ray 8K texture nodes
    cmds.setAttr(starglobe_mr_tex+'.fileTextureName', StarglobeMapFileTexture , type="string")

    # Set the filename for the maya 2K file texture node
    cmds.setAttr(starglobe_maya_tex+'.fileTextureName', StarglobeMayaFileTexture , type="string")
  else:
    # Set the filename for the maya 8K file texture node
    cmds.setAttr(starglobe_maya_tex+'.fileTextureName', StarglobeMapFileTexture , type="string")
  
  # Connect the Lambert preview shader

  # Connect the Maya starglobe file texture to the lambert preview material color and incandescent shader inputs
  cmds.connectAttr(starglobe_maya_tex+'.outColor', starglobe_preview_shader_name+'.color', f=True)
  cmds.connectAttr(starglobe_maya_tex+'.outColor', starglobe_preview_shader_name+'.incandescence', f=True)
 
  # Connect the Lambert in-scene preview shader to the shading group
  cmds.connectAttr(starglobe_preview_shader_name+'.outColor', starglobe_mia_shader_group_name+'.surfaceShader', f=True)

  if cmds.checkBoxGrp('checkGrpCreateStarglobeMentalRayMaterials', query=True, value1=True) == True:
    # Connect the mia_material nodes

    # Connect the mia_material shader to the shading group
    cmds.connectAttr(starglobe_mia_shader_name+'.message', starglobe_mia_shader_group_name+'.miPhotonShader', f=True)
    cmds.connectAttr(starglobe_mia_shader_name+'.message', starglobe_mia_shader_group_name+'.miShadowShader', f=True)
    cmds.connectAttr(starglobe_mia_shader_name+'.message', starglobe_mia_shader_group_name+'.miMaterialShader', f=True)

  # Old mia_material to shading group connection - replaced by Lambert preview shader
  #cmds.connectAttr(starglobe_mia_shader_name+'.message', starglobe_mia_shader_group_name+'.surfaceShader', f=True)

  if cmds.checkBoxGrp('checkGrpCreateStarglobeMentalRayMaterials', query=True, value1=True) == True:
    # Enable the Hypershade shading group "Suppress all Maya Shaders" checkbox so only the mental ray nodes will be used.
    # This ensures the preview material will be skipped from rendering in older versions of Maya.
    cmds.setAttr(starglobe_mia_shader_group_name+'.miExportMrMaterial', 1)

  # Assign the starglobe surface material to the shape: polyStarglobe
  #polyStarglobe

  # Apply the shading group to the selected geometry
  cmds.select('polyStarglobe')
  cmds.hyperShade(assign=starglobe_mia_shader_group_name)

  # Set the default size (scale) of the starglobe backdrop
  cmds.setAttr('polyStarglobe.scaleZ', 25)
  cmds.setAttr('polyStarglobe.scaleX', 25)
  cmds.setAttr('polyStarglobe.scaleY', 25)

  # Select the surface material
  #cmds.select(starglobe_mia_shader_name, r=True)
  
  # Turn on hardware texturing and shading
  #import maya.cmds as cmds
  if cmds.modelEditor( 'modelPanel1', exists=True):
    cmds.modelEditor('modelPanel1', edit=True, displayAppearance='smoothShaded', wireframeOnShaded=False, displayTextures=True, displayLights="none")
  
  if cmds.modelEditor( 'modelPanel3', exists=True):
    cmds.modelEditor('modelPanel3', edit=True, displayAppearance='smoothShaded', wireframeOnShaded=False, displayTextures=True, displayLights="none")
  
  if cmds.modelEditor( 'modelPanel4', exists=True):
    cmds.modelEditor('modelPanel4', edit=True, displayAppearance='smoothShaded', wireframeOnShaded=False, displayTextures=True, displayLights="none")

  # Select the original objects
  if object_selection:
    cmds.select(object_selection)
    print('Selected: ')
    print(object_selection)

  # No objects were selected
  if not object_selection:
    #print "No objects selected"
    
    # Select the surface material
    if cmds.checkBoxGrp('checkGrpCreateStarglobeMentalRayMaterials', query=True, value1=True) == True:
      # mental ray native material
      cmds.select(starglobe_mia_shader_name, r=True)
    else:
      # Maya software renderer native material
      cmds.select(starglobe_preview_shader_name, r=True)
      
  # Return the name of the starglobe
  return 'polyStarglobe'


"""
Create a color and Bump MIA material 
------------------------------------
A python function to create a mia_material with a shading network for color + bump textures.
"""

# Create a color and Bump MIA material    
def createColorBumpMiaMaterial():
  import os  
  import maya.cmds as cmds
  #import maya.mel as mel

  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()

  # ---------------------------------------------------------------------
  # Set up the base folder path for the Domemain3D control maps
  # ---------------------------------------------------------------------

  # Set the file texture variables to "" if you don't want a file to be specified
  #ColorMapFileTexture = ""
  #BumpMapFileTexture = ""

  ColorMapFileTexture = getSourceImagesPath('checker.iff')
  BumpMapFileTexture = getSourceImagesPath('bumpChecker.iff')

  # Get the selected geometry
  object_selection = cmds.ls(sl=True)

  # Create the render nodes

  # Create the mia_material + shading group
  dome_mia_shader_group_name = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='dome_mia_materialSG')
 
  # Create a mia_material_x_passes shader
  dome_mia_shader_name = cmds.shadingNode('mia_material_x_passes', n='dome_mia_material', asShader=True) 

  # Create a mia_material shader
  #dome_mia_shader_name = cmds.shadingNode('mia_material', n='dome_mia_material', asShader=True)   

  # Apply the shading group to the selected geometry
  if object_selection:
    print('Applying the ' + dome_mia_shader_name + ' surface material to:')
    for obj in object_selection: 
      print obj
      
    for obj in object_selection: 
      cmds.select(obj)
      cmds.hyperShade(assign=dome_mia_shader_group_name)

  color_tex_vector = cmds.shadingNode('mib_texture_vector', n='color_mib_texture_vector1', asUtility=True ) 
  color_tex_remap = cmds.shadingNode('mib_texture_remap', n='color_mib_texture_remap1',  asUtility=True) 
  color_tex_lookup= cmds.shadingNode('mib_texture_lookup', n='color_mib_texture_lookup1',  asUtility=True) 
  color_mr_tex = cmds.shadingNode('mentalrayTexture', n='color_mentalrayTexture1', asTexture=True) 

  bump_mr_tex = cmds.shadingNode('mentalrayTexture', n='bump_mentalrayTexture1', asTexture=True) 

  bump_tex_vector = cmds.shadingNode('mib_texture_vector', n='bump_mib_texture_vector1', asUtility=True ) 
  bump_tex_remap = cmds.shadingNode('mib_texture_remap', n='bump_mib_texture_remap1',  asUtility=True) 
  bump_mib_bump_basis= cmds.shadingNode('mib_bump_basis', n='mib_bump_basis1',  asUtility=True) 
  bump_mib_passthrough_bump_map = cmds.shadingNode('mib_passthrough_bump_map', n='mib_passthrough_bump_map1', asUtility=True) 

  # Set the filename for the mental ray texture nodes
  cmds.setAttr(color_mr_tex+'.fileTextureName', ColorMapFileTexture , type="string")
  cmds.setAttr(bump_mr_tex+'.fileTextureName', BumpMapFileTexture, type="string")

  # Connect the color texture nodes
  cmds.connectAttr(color_tex_vector+'.outValue', color_tex_remap+'.input' )
  #mib_texture_vector.outValue -> mib_texture_remap.input

  cmds.connectAttr(color_tex_remap+'.outValue', color_tex_lookup+'.coord' )
  #mib_texture_remap.outValue -> mib_texture_lookup.coord

  cmds.connectAttr(color_mr_tex+'.message', color_tex_lookup+'.tex' )
  #mentalrayTexture.message -> mib_texture_lookup.tex

  cmds.connectAttr(color_tex_lookup+'.outValue', dome_mia_shader_name+'.diffuse' )
  #mib_texture_lookup.outValue -> mia_material.diffuse

  # Connect the bump map texture nodes
  cmds.connectAttr(bump_tex_vector+'.outValue', bump_tex_remap+'.input' )
  #mib_texture_vector.outValue -> mib_texture_remap.input

  cmds.connectAttr(bump_tex_remap+'.outValue', bump_mib_passthrough_bump_map+'.coord' )
  #mib_texture_remap.outValue -> mib_passthrough_bump_map.coord

  cmds.connectAttr(bump_mib_bump_basis+'.u', bump_mib_passthrough_bump_map+'.u' )
  cmds.connectAttr(bump_mib_bump_basis+'.v', bump_mib_passthrough_bump_map+'.v' )
  #mib_bump_basis2.u -> mib_passthrough_bump_map.u
  #mib_bump_basis2.v -> mib_passthrough_bump_map.v

  cmds.connectAttr(bump_mr_tex+'.message', bump_mib_passthrough_bump_map+'.tex' )
  #mentalrayTexture.message -> mib_passthrough_bump_map.tex

  cmds.connectAttr(bump_mib_passthrough_bump_map+'.outValue', dome_mia_shader_name+'.bump' )
  #mib_passthrough_bump_map.outvalue -> mia_material.bump

  # Set values for the shading nodes

  # Set the mia_material to be a glossy material
  cmds.setAttr(dome_mia_shader_name+'.refl_color', 1, 1, 1, type='double3')
  cmds.setAttr(dome_mia_shader_name+'.reflectivity', 1)
  cmds.setAttr(dome_mia_shader_name+'.refl_gloss', 0.3)
  cmds.setAttr(dome_mia_shader_name+'.diffuse_roughness', 0)
  cmds.setAttr(dome_mia_shader_name+'.diffuse_weight', 1)

  # Set the mia_material to be a matte material
  #cmds.setAttr(dome_mia_shader_name+'.reflectivity', 0)

  # Set the mia_material_x_passes shader to use bump mode to 0 so bump maps are displayed correctly
  cmds.setAttr(dome_mia_shader_name+'.bump_mode', 0)

  # Note mental ray bump directions are negative while the standard Maya bump2D depth value is positive
  # Set the bump step value to a default starting value of 0.0 to make the bump visible
  cmds.setAttr(bump_mib_passthrough_bump_map+'.stepX', 0.0)
  cmds.setAttr(bump_mib_passthrough_bump_map+'.stepY', 0.0)
  cmds.setAttr(bump_mib_passthrough_bump_map+'.stepZ', 0.0)

  # Set the bump factor default to 1 to make the bump map visible
  cmds.setAttr(bump_mib_passthrough_bump_map+'.factor', 1)

  # Connect the nodes
  # Connect the mia_material shader to the shading group
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.surfaceShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miPhotonShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miShadowShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miMaterialShader', f=True)

  # Select the surface material
  #cmds.select(dome_mia_shader_name, r=True)

  # Select the original objects
  if object_selection:
    cmds.select(object_selection)
    print('Selected: ')
    print(object_selection)

  # No objects were selected
  if not object_selection:
    #print "No objects selected"
    # Select the surface material
    cmds.select(dome_mia_shader_name, r=True)


"""
Create a color MIA material 
---------------------------
A python function to create a mia_material with a shading network for color + bump textures.
"""

# Create a color MIA material  
def createColorMiaMaterial():
  import maya.cmds as cmds
  #import maya.mel as mel  

  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()

  # Texture variables
  #Set the file texture variables to "" if you don't want a file to be specified
  #ColorMapFileTexture = ""

  ColorMapFileTexture = getSourceImagesPath('checker.iff')

  # Get the selected geometry
  object_selection = cmds.ls(sl=True)

  # Create the render nodes

  # Create the mia_material + shading group
  dome_mia_shader_group_name = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='dome_mia_materialSG')
  
  # Create a mia_material_x_passes shader
  dome_mia_shader_name = cmds.shadingNode('mia_material_x_passes', n='dome_mia_material', asShader=True) 

  # Create a mia_material shader
  #dome_mia_shader_name = cmds.shadingNode( 'mia_material', n='dome_mia_material', asShader=True)   

  # Apply the shading group to the selected geometry
  if object_selection:
    print('Applying the ' + dome_mia_shader_name + ' surface material to:')
    for obj in object_selection: 
      print obj
      
    for obj in object_selection: 
      cmds.select(obj)
      cmds.hyperShade(assign=dome_mia_shader_group_name)  

  # Create the nodes
  color_tex_vector = cmds.shadingNode('mib_texture_vector', n='color_mib_texture_vector1', asUtility=True) 
  color_tex_remap = cmds.shadingNode('mib_texture_remap', n='color_mib_texture_remap1',  asUtility=True) 
  color_tex_lookup= cmds.shadingNode('mib_texture_lookup', n='color_mib_texture_lookup1',  asUtility=True) 
  color_mr_tex = cmds.shadingNode('mentalrayTexture', n='color_mentalrayTexture1', asTexture=True) 

  # Set the filename for the mental ray texture nodes
  cmds.setAttr(color_mr_tex+'.fileTextureName', ColorMapFileTexture , type="string")

  # Connect the color texture nodes
  cmds.connectAttr(color_tex_vector+'.outValue', color_tex_remap+'.input')
  #mib_texture_vector.outValue -> mib_texture_remap.input

  cmds.connectAttr(color_tex_remap+'.outValue', color_tex_lookup+'.coord')
  #mib_texture_remap.outValue -> mib_texture_lookup.coord

  cmds.connectAttr(color_mr_tex+'.message', color_tex_lookup+'.tex')
  #mentalrayTexture.message -> mib_texture_lookup.tex

  cmds.connectAttr(color_tex_lookup+'.outValue', dome_mia_shader_name+'.diffuse')
  #mib_texture_lookup.outValue -> mia_material.diffuse

  # Set values for the shading nodes

  # Set the mia_material to be a glossy material
  cmds.setAttr(dome_mia_shader_name+".refl_color", 1, 1, 1, type="double3")
  cmds.setAttr(dome_mia_shader_name+".reflectivity", 1)
  cmds.setAttr(dome_mia_shader_name+".refl_gloss", 0.3)
  cmds.setAttr(dome_mia_shader_name+".diffuse_roughness", 0)
  cmds.setAttr(dome_mia_shader_name+".diffuse_weight", 1)

  # Set the mia_material to be a matte material
  #cmds.setAttr(dome_mia_shader_name+'.reflectivity', 0)

  # Connect the nodes

  # Connect the mia_material shader to the shading group
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.surfaceShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miPhotonShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miShadowShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miMaterialShader', f=True)

  # Select the original objects
  if object_selection:
    cmds.select(object_selection)
    print('Selected: ')
    print(object_selection)

  # No objects were selected
  if not object_selection:
    #print "No objects selected"
    # Select the surface material
    cmds.select(dome_mia_shader_name, r=True)
  
"""
Create a Color Image Sequence MIA Material
--------------------------------------------------
A python function to create a mia_material with a shading network for a mental ray native animated file texture using a mel expression to cycle the images used per frame.

This is designed so image sequences can be used as file texture on fulldome renders without having to worry about the blurry grey line artifact in MR.
"""
# Create a color image sequence MIA material    
def createColorImageSequenceMiaMaterial():
  import maya.cmds as cmds
  import maya.mel as mel  

  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()

  # Texture variables
  # Set the file texture variables to "" if you don't want a file to be specified
  #ColorMapFileTexture = ''

  ColorMapFileTexture = getSourceImagesPath('checker.iff')
  #ColorMapFileTexture = getSourceImagesPath('checker')

  # Get the selected geometry
  object_selection = cmds.ls(sl=True)

  # Create the render nodes

  # Create the mia_material + shading group
  dome_mia_shader_group_name = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='sequence_mia_material_x_passesSG')
  
  # Create a mia_material_x_passes shader
  dome_mia_shader_name = cmds.shadingNode('mia_material_x_passes', n='sequence_mia_material_x_passes', asShader=True)  

  # Create a mia_material shader
  #dome_mia_shader_name = cmds.shadingNode( 'mia_material', n='dome_mia_material', asShader=True)   

  # Apply the shading group to the selected geometry
  if object_selection:
    print('Applying the ' + dome_mia_shader_name + ' surface material to:')
    for obj in object_selection: 
      print obj
      
    for obj in object_selection: 
      cmds.select(obj)
      cmds.hyperShade(assign=dome_mia_shader_group_name)  

  # Create the nodes
  color_tex_vector = cmds.shadingNode('mib_texture_vector', n='sequence_mib_texture_vector1', asUtility=True) 
  color_tex_remap = cmds.shadingNode('mib_texture_remap', n='sequence_mib_texture_remap1',  asUtility=True) 
  color_tex_lookup= cmds.shadingNode('mib_texture_lookup', n='sequence_mib_texture_lookup1',  asUtility=True) 
  color_mr_tex = cmds.shadingNode('mentalrayTexture', n='sequence_mentalrayTexture1', asTexture=True) 

  # Set the filename for the mental ray texture nodes
  #cmds.setAttr( color_mr_tex+'.fileTextureName', ColorMapFileTexture , type="string")

  # Connect the color texture nodes
  cmds.connectAttr(color_tex_vector+'.outValue', color_tex_remap+'.input')
  #mib_texture_vector.outValue -> mib_texture_remap.input

  cmds.connectAttr(color_tex_remap+'.outValue', color_tex_lookup+'.coord')
  #mib_texture_remap.outValue -> mib_texture_lookup.coord

  cmds.connectAttr(color_mr_tex+'.message', color_tex_lookup+'.tex')
  #mentalrayTexture.message -> mib_texture_lookup.tex

  cmds.connectAttr(color_tex_lookup+'.outValue', dome_mia_shader_name+'.diffuse')
  #mib_texture_lookup.outValue -> mia_material.diffuse

  # Set values for the shading nodes

  # Set the mia_material to be a glossy material
  cmds.setAttr(dome_mia_shader_name+'.refl_color', 1, 1, 1, type='double3')
  #cmds.setAttr(dome_mia_shader_name+".reflectivity', 1)
  cmds.setAttr(dome_mia_shader_name+'.refl_gloss', 0.3)
  cmds.setAttr(dome_mia_shader_name+'.diffuse_roughness', 0)
  cmds.setAttr(dome_mia_shader_name+'.diffuse_weight', 1)

  # Set the mia_material to be a matte material
  cmds.setAttr(dome_mia_shader_name+'.reflectivity', 0)

  # Connect the nodes

  # Connect the mia_material shader to the shading group
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.surfaceShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miPhotonShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miShadowShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miMaterialShader', f=True)

  #-----------------------------------------------------------------------
  # Start the sequence animation code here
  #-----------------------------------------------------------------------

  #---------------------------------------------------------------------------
  # Add Extra Attrs to the node
  #---------------------------------------------------------------------------

  createMentalrayTextureExtraAttrs(color_mr_tex, ColorMapFileTexture)

  #-----------------------------------------------------------------------
  # Select the original objects
  #-----------------------------------------------------------------------
  """
  if object_selection:
    cmds.select(object_selection)
    print('Selected: ')
    print(object_selection)

  #No objects were selected
  if not object_selection:
    #print 'No objects selected'
    #Select the surface material
    cmds.select(color_mr_tex, r=True)
  """

  # Select the File Texture node in the attribute editor
  cmds.select(color_mr_tex, r=True)
  mel.eval ('showEditorExact("' + color_mr_tex + '")')

  #-----------------------------------------------------------------------
  # Output the name of the new fileTexture node
  return color_mr_tex


"""
Create a Hybrid MIA Material + Maya File Texture
--------------------------------------------------
A python function to create a hybrid shading network with a mia_material with a shading network for a mental ray native animated file texture using a mel expression to cycle the images used per frame, and a Maya file texture node shading network for high resolution previews in the real-time viewport window.

This is designed so image sequences can be used as file texture on fulldome renders without having to worry about the blurry grey line artifact in MR.
"""
# Create a Hybrid color image sequence MIA material    
def createHybridColorImageSequenceMiaMaterial():
  import maya.cmds as cmds
  import maya.mel as mel  

  # Make sure the mental ray plugin was loaded
  forceMentalRayLoad()

  # Texture variables
  # Set the file texture variables to "" if you don't want a file to be specified
  #ColorMapFileTexture = ""

  ColorMapFileTexture = getSourceImagesPath('checker.iff')
  #ColorMapFileTexture = getSourceImagesPath('checker')

  # Get the selected geometry
  object_selection = cmds.ls(sl=True)

  # Create the render nodes

  # Create the mia_material + shading group
  dome_mia_shader_group_name = cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='sequence_mia_material_x_passesSG')
  
  # Create a mia_material_x_passes shader
  dome_mia_shader_name = cmds.shadingNode('mia_material_x_passes', n='sequence_mia_material_x_passes', asShader=True)  

  # Create a mia_material shader
  #dome_mia_shader_name = cmds.shadingNode('mia_material', n='dome_mia_material', asShader=True)   

  # Apply the shading group to the selected geometry
  if object_selection:
    print('Applying the ' + dome_mia_shader_name + ' surface material to:')
    for obj in object_selection: 
      print obj
      
    for obj in object_selection: 
      cmds.select(obj)
      cmds.hyperShade(assign=dome_mia_shader_group_name)  

  # Create the MR nodes 
  color_tex_lookup = cmds.shadingNode('mib_texture_lookup', n='sequence_mib_texture_lookup1',  asUtility=True) 
  color_mr_tex = cmds.shadingNode('mentalrayTexture', n='sequence_mentalrayTexture1', asTexture=True) 

  # Create the Maya software nodes
  materialNamePrefix = 'sequence_'
  maya_tex = cmds.shadingNode('file', n=materialNamePrefix+'maya_file_texture', asTexture=True) 

  # Create the Lambert in-scene preview material
  preview_shader_name = cmds.shadingNode('lambert', n=materialNamePrefix+'preview_material', asShader=True) 
  maya_placement = cmds.shadingNode('place2dTexture', n=materialNamePrefix+'place2dTexture', asUtility=True)

  # Set the filename for the mental ray texture nodes
  #cmds.setAttr(color_mr_tex+'.fileTextureName', ColorMapFileTexture , type="string")

  # Connect the place2dTexture node to the mr shading network
  cmds.connectAttr(maya_placement+'.outU', color_tex_lookup+'.coordX')
  cmds.connectAttr(maya_placement+'.outV', color_tex_lookup+'.coordY')
  # place2dTexture.outU -> mib_texture_lookup.coordX
  # place2dTexture.outV -> mib_texture_lookup.coordY
  
  # Connect the color texture nodes
  cmds.connectAttr(color_mr_tex+'.message', color_tex_lookup+'.tex')
  #mentalrayTexture.message -> mib_texture_lookup.tex

  cmds.connectAttr(color_tex_lookup+'.outValue', dome_mia_shader_name+'.diffuse')
  #mib_texture_lookup.outValue -> mia_material.diffuse
  
  # Connect the mentalrayTexture filename to the Maya file texture node filename
  cmds.connectAttr(color_mr_tex+'.fileTextureName', maya_tex+'.fileTextureName')
  #mentalrayTexture.fileTextureName -> file.fileTextureName
  
  # Connect the place2D texture to the Maya file texture
  # Disabled WrapU and WrapV since the Mental ray network connections don't support it
  cmds.connectAttr(maya_placement+'.coverage', maya_tex+'.coverage', f=True)
  cmds.connectAttr(maya_placement+'.translateFrame', maya_tex+'.translateFrame', f=True)
  cmds.connectAttr(maya_placement+'.rotateFrame', maya_tex+'.rotateFrame', f=True)
  cmds.connectAttr(maya_placement+'.mirrorU', maya_tex+'.mirrorU', f=True)
  cmds.connectAttr(maya_placement+'.mirrorV', maya_tex+'.mirrorV', f=True)
  cmds.connectAttr(maya_placement+'.stagger', maya_tex+'.stagger', f=True)
  #cmds.connectAttr(maya_placement+'.wrapU', maya_tex+'.wrapU', f=True)
  #cmds.connectAttr(maya_placement+'.wrapV', maya_tex+'.wrapV', f=True)
  cmds.connectAttr(maya_placement+'.repeatUV', maya_tex+'.repeatUV', f=True)
  cmds.connectAttr(maya_placement+'.offset', maya_tex+'.offset', f=True)
  cmds.connectAttr(maya_placement+'.rotateUV', maya_tex+'.rotateUV', f=True)
  cmds.connectAttr(maya_placement+'.noiseUV', maya_tex+'.noiseUV', f=True)
  cmds.connectAttr(maya_placement+'.vertexUvOne', maya_tex+'.vertexUvOne', f=True)
  cmds.connectAttr(maya_placement+'.vertexUvTwo', maya_tex+'.vertexUvTwo', f=True)
  cmds.connectAttr(maya_placement+'.vertexUvThree', maya_tex+'.vertexUvThree', f=True)
  cmds.connectAttr(maya_placement+'.vertexCameraOne', maya_tex+'.vertexCameraOne', f=True)
  cmds.connectAttr(maya_placement+'.outUV', maya_tex+'.uvCoord', f=True)
  cmds.connectAttr(maya_placement+'.outUvFilterSize', maya_tex+'.uvFilterSize', f=True)
  
  # Connect the Lambert preview shader

  # Connect the Maya domeViewer file texture to the lambert preview material color shader inputs
  cmds.connectAttr(maya_tex+'.outColor', preview_shader_name+'.color', f=True)

  # Connect the Lambert in-scene preview shader to the shading group
  cmds.connectAttr(preview_shader_name+'.outColor', dome_mia_shader_group_name+'.surfaceShader', f=True)

  # Turn on the shading group "Suppress all Maya Shaders" checkbox
  cmds.setAttr(dome_mia_shader_group_name+'.miExportMrMaterial', 1)

  # Set values for the shading nodes

  # Set the mia_material to be a glossy material
  cmds.setAttr(dome_mia_shader_name+'.refl_color', 1, 1, 1, type='double3')
  #cmds.setAttr(dome_mia_shader_name+'.reflectivity', 1)
  cmds.setAttr(dome_mia_shader_name+'.refl_gloss', 0.3)
  cmds.setAttr(dome_mia_shader_name+'.diffuse_roughness', 0)
  cmds.setAttr(dome_mia_shader_name+'.diffuse_weight', 1)

  # Set the mia_material to be a matte material
  cmds.setAttr(dome_mia_shader_name+'.reflectivity', 0)
  
  # Disable the wrapU and WrapV settings so the mental ray shading network and maya file texture base network have the same image tiling settings when the image is transformed so the background is shown outside the image area.
  cmds.setAttr(maya_placement+'.wrapU', 0)
  cmds.setAttr(maya_placement+'.wrapV', 0)
  
  # Connect the nodes
  
  # Connect the mia_material shader to the shading group
  # cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.surfaceShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miPhotonShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miShadowShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miMaterialShader', f=True)

  #-----------------------------------------------------------------------
  # Start the sequence animation code here
  #-----------------------------------------------------------------------

  #---------------------------------------------------------------------------
  # Add Extra Attrs to the node
  #---------------------------------------------------------------------------

  createMentalrayTextureExtraAttrs(color_mr_tex, ColorMapFileTexture)

  #-----------------------------------------------------------------------
  # Select the original objects
  #-----------------------------------------------------------------------
  """
  if object_selection:
    cmds.select(object_selection)
    print('Selected: ')
    print(object_selection)

  # No objects were selected
  if not object_selection:
    #print 'No objects selected'
    #Select the surface material
    cmds.select(color_mr_tex, r=True)
  """

  # Select the File Texture node in the attribute editor
  cmds.select(color_mr_tex, r=True)
  mel.eval('showEditorExact("' + color_mr_tex + '")')


  # Enable Viewport Textures
  cmds.modelEditor('modelPanel4', edit=True, displayAppearance='smoothShaded', displayTextures=True)
  
  #-----------------------------------------------------------------------
  # Output the name of the new fileTexture node
  return color_mr_tex



# Add extra attributes for animation to a mentalrayTexture node
# Usage: createMentalrayTextureExtraAttrs("color_mentalrayTexture1", "fileTextureName")
def createMentalrayTextureExtraAttrs(color_mr_tex, fileTextureName):
  import maya.cmds as cmds
  import maya.mel as mel

  # Texture variables
  # Set the file texture variables to "" if you don't want a file to be specified
  #ColorMapFileTexture = ''
  
  #ColorMapFileTexture = getSourceImagesPath('NightSky_Domemain.exr')
  #ColorMapFileTexture = getSourceImagesPath('checker.iff')
  ColorMapFileTexture = fileTextureName

  #---------------------------------------------------------------------------
  # Add Extra Attrs to the node
  #---------------------------------------------------------------------------
  baseNodeName = color_mr_tex

  #---------------------------------------------------------------------------
  # Add a folder picker using the -usedAsFilename flag
  #---------------------------------------------------------------------------
  # Check if we are running Maya 2013+ and then enable the usedAsFilename mode
  mayaVersion = getMayaVersionDome()  

  if(mayaVersion >= 2013):
    attrName = 'File_Name_Prefix';
    cmds.addAttr(baseNodeName, longName=attrName, dataType='string', usedAsFilename=True, keyable=True)
    cmds.setAttr(baseNodeName + '.' + attrName, ColorMapFileTexture , type='string')
    print('Adding custom Attributes ' + baseNodeName + '.' + attrName)
  else:
    attrName = 'File_Name_Prefix';
    cmds.addAttr(baseNodeName, longName=attrName, dataType='string', keyable=True)
    cmds.setAttr(baseNodeName + '.' + attrName, ColorMapFileTexture , type='string')
    print('Adding custom Attributes ' + baseNodeName + '.' + attrName)

  #---------------------------------------------------------------------------
  # Add an Image Format options menu with a list of mentalrayTexture compatible image types
  #---------------------------------------------------------------------------
  
  attrName = 'Image_Format'
  #if(mel.attributeExists(attrName, baseNodeName) == 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType='enum', en='Maya IFF (iff):TIFF (tif):JPEG (jpg):Targa (tga):Windows Bitmap (bmp):HDR (hdr):PSD (psd):PNG (png):OpenEXR (exr):Softimage (pic):Portable Pixmap (ppm):', defaultValue=8, keyable=True)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)

  #defaultValue of 0 = iff
  #defaultValue of 7 = png
  #defaultValue of 8 = exr

  #---------------------------------------------------------------------------
  # Add a frame/animation extension options menu
  #---------------------------------------------------------------------------
  
  attrName = 'Frame_Animation_Ext'
  #if(mel.attributeExists(attrName, baseNodeName) == 0):
  cmds.addAttr(baseNodeName, longName=attrName, attributeType='enum', en='name (Single Frame):name.ext (Single Frame):name.#.ext:name.ext.#:name.#:name#.ext:name_#.ext:Native Image Name (Passthrough):', defaultValue=7, keyable=True)
  # defaultValue=0 means name (Single Frame)
  # defaultValue=7 means Native Image Name (Passthrough)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)

  #---------------------------------------------------------------------------
  # Add a frame padding attribute to choose how many leading zeros are on the filename's frame number section.
  #---------------------------------------------------------------------------
  
  attrName = 'Frame_Padding';
  cmds.addAttr(baseNodeName, longName=attrName, attributeType='long', keyable=True, defaultValue=0, min=0, max=10)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)

  #---------------------------------------------------------------------------
  # Add a frame offset attribute to allow to the animated image's frame number to be offset ahead or behind the timeline's current frame value.
  #---------------------------------------------------------------------------
  
  attrName = 'Frame_Offset';
  cmds.addAttr(baseNodeName, longName=attrName, attributeType='long', keyable=True, defaultValue=0, min=-100000, max=100000, softMinValue=-2000, softMaxValue=2000)
  print('Adding custom Attributes ' + baseNodeName + '.' + attrName)

  #---------------------------------------------------------------------------  
  # Add a textureAnimation mode expression to the mentalrayTexture node
  #---------------------------------------------------------------------------

  exprName = ''
  animationAttrName = 'Animation'
  # The expression name is domeGrid_displayModeExpr
  exprName = color_mr_tex + '_' + animationAttrName + 'Expr'

  animationNameExpr  = ''

  animationNameExpr += "//------------------------------------------------------------------------------------\n"
  animationNameExpr += "// This code goes in the MEL expression\n"
  animationNameExpr += "//------------------------------------------------------------------------------------\n\n"

  animationNameExpr += "// Run the Mental Ray Texture Animation code\n"
  animationNameExpr += "mta_get_sequence_frame_name();\n"
  animationNameExpr += "\n"
  animationNameExpr += "//----------------------------------------------------\n"
  animationNameExpr += "// Add the first part of the file name\n"
  animationNameExpr += "//----------------------------------------------------\n"
  animationNameExpr += "proc string mta_get_filename_prefix(){\n"
  animationNameExpr += "  return `getAttr " + color_mr_tex + ".File_Name_Prefix`;\n"
  animationNameExpr += "}\n"
  animationNameExpr += "\n"


  animationNameExpr += "//----------------------------------------------------\n"
  animationNameExpr += "// Calculate the current frame\n"
  animationNameExpr += "//----------------------------------------------------\n"
  animationNameExpr += "proc int mta_get_current_frame(){\n"
  animationNameExpr += "  int $currentFrame = `currentTime -query`;\n"
  animationNameExpr += "  int $frameOffset = `getAttr " + color_mr_tex + ".Frame_Offset`;\n"
  animationNameExpr += "  // Add the real frame from the timeline and the frame offset value from the Extra Attributes\n"
  animationNameExpr += "  int $combinedFrameCount = $currentFrame + $frameOffset;\n"
  animationNameExpr += "  return $combinedFrameCount;\n"
  animationNameExpr += "}\n"
  animationNameExpr += "\n"


  animationNameExpr += "//----------------------------------------------------\n"
  animationNameExpr += "// Add frame padding to the current frame string\n"
  animationNameExpr += "//----------------------------------------------------\n"
  animationNameExpr += "proc string mta_get_current_frame_str(){\n"
  animationNameExpr += "  int $combinedFrameCount = mta_get_current_frame();\n"
  animationNameExpr += "  int $framePadding = `getAttr " + color_mr_tex + ".Frame_Padding`;\n"
  animationNameExpr += "  return `python (\"'%0\"+$framePadding+\"d' % \"+$combinedFrameCount)`;\n"
  animationNameExpr += "}\n"
  animationNameExpr += "\n"
  animationNameExpr += "\n"


  animationNameExpr += "//----------------------------------------------------\n"
  animationNameExpr += "// Get the image format for the file type extension\n"
  animationNameExpr += "//----------------------------------------------------\n"
  animationNameExpr += "proc string mta_get_frame_ext(){\n"
  animationNameExpr += "  // " + color_mr_tex + ".Image_Format\n"
  animationNameExpr += "  // enum list item values\n"
  animationNameExpr += "  // 0 = Maya IFF (iff)\n"
  animationNameExpr += "  // 1 = TIFF (tif)\n"
  animationNameExpr += "  // 2 = JPEG (jpg)\n"
  animationNameExpr += "  // 3 = Targa (tga)\n"
  animationNameExpr += "  // 4 = Windows Bitmap (bmp)\n"
  animationNameExpr += "  // 5 = HDR (hdr)\n"
  animationNameExpr += "  // 6 = PSD (psd)\n"
  animationNameExpr += "  // 7 = PNG (png)\n"
  animationNameExpr += "  // 8 = OpenEXR (exr)\n"
  animationNameExpr += "  // 9 = Softimage (pic)\n"
  animationNameExpr += "  // 10 = Portable Pixmap (ppm)\n"
  animationNameExpr += "\n"
  animationNameExpr += "  int $mta_frame_ext = `getAttr " + color_mr_tex + ".Image_Format`;\n"
  animationNameExpr += "  string $mta_frame_ext_str;\n"
  animationNameExpr += "\n"
  animationNameExpr += "  switch($mta_frame_ext) {\n"
  animationNameExpr += "  case 0:\n"
  animationNameExpr += "    $mta_frame_ext_str = \"iff\"; \n"
  animationNameExpr += "    break;\n"
  animationNameExpr += "  case 1:\n"
  animationNameExpr += "    $mta_frame_ext_str = \"tif\"; \n"
  animationNameExpr += "    break;\n"
  animationNameExpr += "  case 2:\n"
  animationNameExpr += "    $mta_frame_ext_str = \"jpg\"; \n"
  animationNameExpr += "    break;\n"
  animationNameExpr += "  case 3:\n"
  animationNameExpr += "    $mta_frame_ext_str = \"tga\"; \n"
  animationNameExpr += "    break;\n"
  animationNameExpr += "  case 4:\n"
  animationNameExpr += "    $mta_frame_ext_str = \"bmp\"; \n"
  animationNameExpr += "    break;\n"
  animationNameExpr += "  case 5:\n"
  animationNameExpr += "    $mta_frame_ext_str = \"hdr\"; \n"
  animationNameExpr += "    break;\n"
  animationNameExpr += "  case 6:\n"
  animationNameExpr += "    $mta_frame_ext_str = \"psd\"; \n"
  animationNameExpr += "    break;\n"
  animationNameExpr += "  case 7:\n"
  animationNameExpr += "    $mta_frame_ext_str = \"png\"; \n"
  animationNameExpr += "    break;\n"
  animationNameExpr += "  case 8:\n"
  animationNameExpr += "    $mta_frame_ext_str = \"exr\"; \n"
  animationNameExpr += "    break;\n"
  animationNameExpr += "  case 9:\n"
  animationNameExpr += "    $mta_frame_ext_str = \"pic\"; \n"
  animationNameExpr += "    break;\n"
  animationNameExpr += "  case 10:\n"
  animationNameExpr += "    $mta_frame_ext_str = \"ppm\"; \n"
  animationNameExpr += "    break;\n"
  animationNameExpr += "  default:\n"
  animationNameExpr += "    $mta_frame_ext_str = \"exr\"; \n"
  animationNameExpr += "  }\n"
  animationNameExpr += "\n"
  animationNameExpr += "  return $mta_frame_ext_str;\n"
  animationNameExpr += "}\n"
  animationNameExpr += "\n"


  animationNameExpr += "//----------------------------------------------------\n"
  animationNameExpr += "// Build the Image Name string\n"
  animationNameExpr += "//----------------------------------------------------\n"
  animationNameExpr += "proc string mta_get_sequence_frame_name(){\n"
  animationNameExpr += "  string $finalFrameName = \"\";\n"
  animationNameExpr += "\n"
  animationNameExpr += "  //----------------------------------------------------\n"
  animationNameExpr += "  // Get the frame/animation extension format\n"
  animationNameExpr += "  //----------------------------------------------------\n"
  animationNameExpr += "  // " + color_mr_tex + ".Frame_Animation_Ext\n"
  animationNameExpr += "  // enum list item values\n"
  animationNameExpr += "  // 0 = name (Single Frame)\n"
  animationNameExpr += "  // 1 = name.ext (Single Frame)\n"
  animationNameExpr += "  // 2 = name.#.ext\n"
  animationNameExpr += "  // 3 = name.ext.#\n"
  animationNameExpr += "  // 4 = name.#\n"
  animationNameExpr += "  // 5 = name#.ext\n"
  animationNameExpr += "  // 6 = name_#.ext\n"
  animationNameExpr += "  // 7 = Native Image Name (Passthrough)\n"

  animationNameExpr += "\n"
  animationNameExpr += "  int $mta_animation_ext = `getAttr " + color_mr_tex + ".Frame_Animation_Ext`;\n\n"
  animationNameExpr += "  switch($mta_animation_ext) {\n"
  animationNameExpr += "    case 0:\n"
  animationNameExpr += "      // name (Single Frame)) \n"
  animationNameExpr += "      $finalFrameName += mta_get_filename_prefix();\n"
  animationNameExpr += "      break;\n"
  animationNameExpr += "    case 1:\n"
  animationNameExpr += "      // name.ext\n"
  animationNameExpr += "      $finalFrameName += mta_get_filename_prefix();\n"
  animationNameExpr += "      $finalFrameName += \".\";\n"
  animationNameExpr += "      $finalFrameName += mta_get_frame_ext();\n"
  animationNameExpr += "      break;\n"
  animationNameExpr += "    case 2:\n"
  animationNameExpr += "      // name.#.ext\n"
  animationNameExpr += "      $finalFrameName += mta_get_filename_prefix();\n"
  animationNameExpr += "      $finalFrameName += \".\";\n"
  animationNameExpr += "      $finalFrameName += mta_get_current_frame_str();\n"
  animationNameExpr += "      $finalFrameName += \".\";\n"
  animationNameExpr += "      $finalFrameName += mta_get_frame_ext();\n"
  animationNameExpr += "      break;\n"
  animationNameExpr += "    case 3:\n"
  animationNameExpr += "      // name.ext.#\n"
  animationNameExpr += "      $finalFrameName += mta_get_filename_prefix();\n"
  animationNameExpr += "      $finalFrameName += \".\";\n"
  animationNameExpr += "      $finalFrameName += mta_get_frame_ext();\n"
  animationNameExpr += "      $finalFrameName += \".\";\n"
  animationNameExpr += "      $finalFrameName += mta_get_current_frame_str();\n"
  animationNameExpr += "      break;\n"
  animationNameExpr += "    case 4:\n"
  animationNameExpr += "      // name.#\n"
  animationNameExpr += "      $finalFrameName += mta_get_filename_prefix();\n"
  animationNameExpr += "      $finalFrameName += \".\";\n"
  animationNameExpr += "      $finalFrameName += mta_get_current_frame_str();\n"
  animationNameExpr += "      break;\n"
  animationNameExpr += "    case 5:\n"
  animationNameExpr += "      // name#.ext\n"
  animationNameExpr += "      $finalFrameName += mta_get_filename_prefix();\n"
  animationNameExpr += "      $finalFrameName += mta_get_current_frame_str();\n"
  animationNameExpr += "      $finalFrameName += \".\";\n"
  animationNameExpr += "      $finalFrameName += mta_get_frame_ext();\n"
  animationNameExpr += "      break;\n"
  animationNameExpr += "    case 6:\n"
  animationNameExpr += "      // name_#.ext\n"
  animationNameExpr += "      $finalFrameName += mta_get_filename_prefix();\n"
  animationNameExpr += "      $finalFrameName += \"_\";\n"
  animationNameExpr += "      $finalFrameName += mta_get_current_frame_str();\n"
  animationNameExpr += "      $finalFrameName += \".\";\n"
  animationNameExpr += "      $finalFrameName += mta_get_frame_ext();\n"
  animationNameExpr += "      break;\n"
  animationNameExpr += "    case 7:\n"
  animationNameExpr += "      // Native Image Name (Passthrough)\n"
  animationNameExpr += "      $finalFrameName = `getAttr " + color_mr_tex + ".fileTextureName`;\n\n"
  animationNameExpr += "      break;\n"
  animationNameExpr += "  }\n"
  animationNameExpr += "\n"

  animationNameExpr += "  //----------------------------------------------------\n"
  animationNameExpr += "  // Set the final value\n"
  animationNameExpr += "  //----------------------------------------------------\n"
  animationNameExpr += "  setAttr -type \"string\" " + color_mr_tex + ".fileTextureName $finalFrameName;\n"
  animationNameExpr += "  // print (\"Image: \" + $finalFrameName +  \"\\n\");\n"
  animationNameExpr += "  return $finalFrameName;\n"
  animationNameExpr += "}"

  # Debug print the expression script output
  print (color_mr_tex + ' Extra Attribute Expressions:\n')
  print animationNameExpr

  # Create the final assembled expression and attach it to the mentalrayTexture node object
  cmds.expression(name=exprName, string=animationNameExpr, object=color_mr_tex, alwaysEvaluate=True, unitConversion=all)

  # Set the Image Name value for the first time in case the Frame_Animation_Ext option is set to #7 Native Image Name (Passthrough)
  cmds.setAttr(color_mr_tex + '.fileTextureName',  fileTextureName, type='string')

  # Force the new expression to evaluate once to update the mentalrayTexture filename field:
  cmds.getAttr(exprName+'.evaluateNow')

  #---------------------------------------------------------------------------
  # Add a note attribute
  #---------------------------------------------------------------------------

  noteMessage = "The mentalrayTexture based Extra Attribute image sequence feature requires this scene to be rendered with a single frame job distribution mode in your render farm / render queue software. This means the sequence should be rendered with 1 frame per render slice so Maya's Render.exe program will load a new texture for each frame of the animation."

  # Write to the attribute editor note field
  noteCommandString = 'setNotesAttribute(\"' + color_mr_tex + '\", "notes", "nts", "string", `scrollField -edit -text \"' + noteMessage + '\" AENotesScrollField`)'

  # Write to the attribute editor note field
  mel.eval(noteCommandString) 
  #print(noteCommandString)



"""
A python function to make sure mental ray is active 
and the MR shading nodes are read to be used.
"""
def forceMentalRayLoad():
  import maya.cmds as cmds
  import maya.mel as mel

  # Make sure the mental ray plugin was loaded
  if not (cmds.pluginInfo('Mayatomr',q=True,loaded=True)):
    cmds.loadPlugin('Mayatomr')
    print('The Mental Ray plugin was loaded.')
  #else:
  #  print("The Mental Ray plugin is already active.")

  # Set the active renderer to mental ray to avoid Hypershade red node errors 
  #mel.eval("setCurrentRenderer mentalRay")
  #or
  melRunString = 'import maya.mel as mel \n'
  melRunString += 'mel.eval(\"setCurrentRenderer mentalRay\")'
  #print("Deferred string: " + melRunString)
  cmds.evalDeferred(melRunString)
  

# Check what version of Maya is active
def getMayaVersionDome():
  import maya.cmds as cmds
  import maya.mel as mel

  # Check if we are running Maya 2011 or higher
  mayaVersion = mel.eval('getApplicationVersionAsFloat;')

  #Debug Test Mode
  # Test this GUI using the Maya 2010 - non-docked GUI mode
  #mayaVersion = 2010;

  # Write out the current Maya version number
  print('Maya ' + str(mayaVersion) + ' detected.\n')
  
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
    parent = cmds.listRelatives(object, parent=True)
    
    print('Parent: ')
    print(parent)
    
    return parent

    
"""
A python function to lock/unlock an ancestor plug connection

unlockAncestor('stereoCameraRight.rotate', True)
# Result:  [u'stereoCameraRight.rotate'] #
"""

def unlockAncestor(connectionName, lockState):
    import maya.cmds as cmds
    if cmds.connectionInfo( connectionName, getLockedAncestor=True):
    	cmds.setAttr(connectionName, lock=lockState)
    	print('[Locked Ancestor State] ' + connectionName + ' ' + str(lockState))
    	return connectionName
