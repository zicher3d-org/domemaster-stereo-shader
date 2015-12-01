# Automagic LatLong Stereo for Maxwell Studio
# --------------------------------------------
# 2015-11-30 9:15 am v0.3
# By Andrew Hazelden 
# Email: andrew@andrewhazelden.com
# Blog: http://www.andrewhazelden.com

# Description
# -----------
# The automagicLatLongStereo.py script is used to quickly prepare your Maxwell Studio mxs scenes for rendering immersive 360 degree LatLong Stereo VR content.


# Script Installation
# -------------------
# Copy the "stereo" folder to your Maxwell 3.2 scripts directory:

# Windows
# C:/Program Files/Next Limit/Maxwell 3/scripts/

# Linux
# /opt/maxwell/3/scripts/

# Mac
# /Applications/Maxwell 3/scripts/


# How do I use the script?
# ------------------------

# Step 1.
# Edit your Maxwell MXS scene file so there is an active camera. Set the focus distance on the camera to the exact location in the scene that you want to use as the stereo camera rig's zero parallax distance (which is the convergence point for the left and right eyes).

# Step 2.
# Launch PyMaxwell and open up the `automagicLatLongStereo.py` python script.

# Step 3.
# Edit the "mxsFilePath" variable in the main function near the bottom of this script and specify your Maxwell Studio based MXS scene file.
# Edit the separationTexturePath variable in the main function near the bottom of this script and specify your LatLong Stereo separation map texture image.
# Edit the the camera views to render section in the main function near the bottom of this script and specify if you want to render the left, right, or center camera views.

# Step 4. Select the Script > Run menu item in PyMaxwell.

# The script will start running. First the script will verify the mxs scene file exists.

# If the mxs file is located then the scene will be opened in maxwell and the camera parameters will be edited. A LatLong Stereo lens shader extension is applied to the camera.

# Camera's focus distance value will be used as the parallax distance for the lens shader and a suitable camera separation value is calculated based upon the current "stereoDepthStrength" value that is specified in the main function at the bottom of this script.

# Then the lens shader's camera view is adjusted so a set of center, left and right camera view based scene files are generated with the names `<scene>_C.mxs`, `<scene>_L.mxs` and `<scene>.R.mxs`. These new files are saved to the same folder as the original mxs scene file.

# -----------------------------------------

from pymaxwell import *
from math import *
import os
import sys


# Return the lens type name as a string
# Example: it = CmaxwellCameraIterator(); camera = it.first(scene); cameraLens = cameraParams.getLensType();  aml_lensTypeName(cameraLens)
def aml_lensTypeName(cameraLens):

  lensTypeName = ''
  if cameraLens[0] == TYPE_CYLINDRICAL_LENS:
    lensTypeName = 'Cylindrical'
  elif cameraLens[0] == TYPE_EXTENSION_LENS:
    lensTypeName = 'Extension Lens'
  elif cameraLens[0] == TYPE_FISHEYE_LENS:
    lensTypeName = 'Fisheye'
  elif cameraLens[0] == TYPE_ORTHO_LENS:
    lensTypeName = 'Ortho'
  elif cameraLens[0] == TYPE_PINHOLE_LENS:
    lensTypeName = 'Pinhole'
  elif cameraLens[0] == TYPE_SPHERICAL_LENS:
    lensTypeName = 'Spherical'
  elif cameraLens[0] == TYPE_THIN_LENS:
    lensTypeName = 'Thin'

  return lensTypeName


# Automatically calibrate the current camera rig and prepare it for panoramic 360 degree stereo rendering:
# Example: automagicStereo('/Cube.mxs', 0.01)
def aml_automagicStereo(mxsFilePath, separationTexturePath, stereoDepthStrength):
  print('\n\n')
  print('Automagic LatLong Stereo for Maxwell Studio')
  print('By Andrew Hazelden <andrew@andrewhazelden.com>')
  print('-----------------------------------------------\n')
  # Find out the current scene file
  dirName = os.path.dirname(mxsFilePath)
  sceneName = os.path.basename(mxsFilePath)
  scenePathNoExt = os.path.splitext(mxsFilePath)[0]


  # Find out the current scene
  scene = Cmaxwell(mwcallback)
  scene.readMXS(mxsFilePath)
  it = CmaxwellCameraIterator()

  # Camera Details
  #camera = it.first(scene)
  camera = scene.getActiveCamera()
  cameraName = camera.getName()

  # Return the lens type name as a string
  cameraLens = camera.getLensType()
  lensTypeName = aml_lensTypeName(cameraLens)

  # Check if a lens shader is attached to the camera
  lensExt = camera.hasCameraLensExtension()

  # Camera Parameters
  position,focalPoint,up,focalLength,fStop,stepTime,ok = camera.getStep(0)

  # Get object position (camera target)
  #target,ok = object.getPosition()

  # Camera Resolution
  res = camera.getResolution()
  width = res[0]
  height = res[1]

  print('[Working Directory] ' + dirName)
  print('[Input Scene] ' + sceneName + ' [Camera] ' + str(cameraName) + ' [Lens] ' + str(lensTypeName) + ' (' + str(cameraLens[0]) + ')' + ' [Lens Shader Present] ' + str(lensExt) + ' [Resolution] ' + str(width) + 'x' + str(height))


  # -------------------------------------------------------
  # Write the Left and Right stereo camera scenes to disk
  # -------------------------------------------------------
  
  # Switch the camera to a LatLong Stereo lens
  latlong_stereo_lens_type = 6
  ok = camera.setLensType(latlong_stereo_lens_type)
  if ok == 0:
    print('There was an error changing the lens type')
    return 0

  # Update the lens shader settings
  if lensExt == 0:
    print('\nNote: There are no lens shaders attached to the "'  + cameraName + '" camera. You need to set the camera to use a LatLong Stereo lens in Maxwell Studio before running this script.')
    return 0
     
    # print('Assigning a new LatLong Stereo Lens to the "'  + cameraName + '" camera.')
    # Add the lens extension settings
    # -------------------------------------------------
    # Maxwell Python Lens Shader ParamList tips from: https://github.com/uhlik/blendmaxwell/blob/master/support/write_mxs.py
    # print('\nNote: No lens shader is attached. Creating the default lens shader extension params.')
    # params = MXparamList()
    # params.createUInt('Type', 1, 0, 2)
    # params.createFloat('FOV Vertical', 180.0, 180.0, 0.0)
    # params.createFloat('FOV Horizontal', 360.0, 360.0, 0.0)
    # params.createByte('Flip Ray X', 0, 0, 1)
    # params.createByte('Flip Ray Y', 0, 0, 1)
    # params.createFloat('Parallax Distance', 360.0, 0.0, 36000.0)
    # params.createByte('Zenith Mode', 0, 0, 1)
    # params.createFloat('Separation', 6.5, 0.0, 100000.0)
    
    # Set the lens shader's stereo separation texture map
    # if os.path.exists(separationTexturePath):
      # Note: setPath is from CtextureMap and createTextureMap is from MXparamList
      # tex = CtextureMap()
      # tex.setPath(separationTexturePath)
      # params.createTextureMap('Separation Map', tex)
      
    #camera.applyCameraLensExtension(params)
    
    
    # Alternate code to add the lens extension settings
    # -------------------------------------------------
    # param = MXparamList()
    # param.setUInt('Type', 1)
    # param.setFloat('FOV Vertical', 180.0)
    # param.setFloat('FOV Horizontal', 360.0)
    # param.setByte('Flip Ray X', 0)
    # param.setByte('Flip Ray Y', 0)
    # param.setFloat('Parallax Distance', 360.0)
    # param.setByte('Zenith Mode', 0)
    # param.setFloat('Separation', 6.5)
    
    # Set the lens shader's stereo separation texture map
    # if os.path.exists(separationTexturePath):
      # setPath is from CtextureMap and setTextureMap is from MXparamList
      # tex = CtextureMap()
      # tex.setPath(separationTexturePath)
      # param.setTextureMap('Separation Map', tex)
      # print('[Separation Map Texture]  '  + separationTexturePath )
    # else:
      # print('[The separation map image was not found] ' + separationTexturePath)
  
    #camera.applyCameraLensExtension(param)
  else:
    print('[LatLong Stereo Lens Shader Present on Camera]')


  # Return the lens type name as a string
  cameraLens = camera.getLensType()
  lensTypeName = aml_lensTypeName(cameraLens)

  # Set the camera resolution to a 2:1 aspect ratio
  outputWidth = height * 2
  outputHeight = height
  camera.setResolution(outputWidth, outputHeight)

  # Convert the focal point or target distance in meters to the lens shader's parallax distance in cm
  x = abs(position[0]-focalPoint[0])
  y = abs(position[1]-focalPoint[1])
  z = abs(position[1]-focalPoint[2])
  focalPointDistance = float(sqrt((x*x)+(y*y)+(z*z)))
  parallaxDistance = focalPointDistance * 100.0

  # Round parallaxDistance to 4 digits of floating point precision
  parallaxDistance = round(parallaxDistance , 4)

  # Use a strong stereo depth strength
  # cameraSeparation = parallaxDistance * (1.0/30.0)

  # Use a standard stereo depth strength
  # cameraSeparation = parallaxDistance * (1.0/55.0)

  # Use a gentle stereo depth strength
  # cameraSeparation = parallaxDistance * (1.0/120.0)
  
  # Pull the stereo depth multiplier from the script's main function
  cameraSeparation = parallaxDistance * stereoDepthStrength
  # Round cameraSeparation to 4 digits of floating point precision
  cameraSeparation = round(cameraSeparation, 4)
  # ToDo: Assign a gradient3 procedural with a vertical gradient effect / premade camera stereo control texture map
  
  # Find out the lens params
  # pymaxwell.MXparamList:
  # http://www.maxwellrender.com/api/3.2/doc-python/html/classpymaxwell_1_1_m_xparam_list.html
  lensParams, ok = camera.getCameraLensExtensionParams()
  if ok == 0:
    print('There was an error changing the lens type')
    return 0

  # Set the parallax distance
  lensParams.setFloat('Parallax Distance',  parallaxDistance)

  # Set the camera separation aka. interaxial pupil distance
  lensParams.setFloat('Separation', cameraSeparation)
  
  # Set the lens shader's stereo separation texture map
  if os.path.exists(separationTexturePath):
    # setTextureMap is from MXparamList
    # setPath is from CtextureMap
    tex = CtextureMap()
    tex.setPath(separationTexturePath)
    ok = lensParams.setTextureMap('Separation Map', tex)
    print('[Separation Map Texture]  '  + separationTexturePath )
  else:
    print('[Separation Map Image Not Found] ' + separationTexturePath)
  

  # Read the lens param items
  mx_type = lensParams.getByName('Type')
  mx_fovVertical = lensParams.getByName('FOV Vertical')
  mx_fovHorizontal = lensParams.getByName('FOV Horizontal')
  mx_flipRayX = lensParams.getByName('Flip Ray X')
  mx_flipRayY = lensParams.getByName('Flip Ray Y')
  mx_parallaxDistance = lensParams.getByName('Parallax Distance')
  mx_zenithMode = lensParams.getByName('Zenith Mode')
  mx_separation = lensParams.getByName('Separation')
  mx_separationMap = lensParams.getTextureMap('Separation Map')
  mx_separationMapFileTexture = mx_separationMap[0].getPath()

  print('\n--------------------------------------')
  print('LatLong Stereo Lens Shader Attributes')
  print('--------------------------------------')
  print('[Lens Type] ' + str(lensTypeName) + ' (' + str(cameraLens[0]) + ')' )

  print('[Lens Parameter Array Items] ' + str(lensParams.getNumItems()) )
  print('Type: ' + str(mx_type) )
  print('FOV Vertical: ' + str(mx_fovVertical) )
  print('FOV Horizontal: ' + str(mx_fovHorizontal) )
  print('Flip Ray X: ' + str(mx_flipRayX) )
  print('Flip Ray Y: ' + str(mx_flipRayY) )
  print('Parallax Distance: ' + str(mx_parallaxDistance) )
  print('Zenith Mode: ' + str(mx_zenithMode) )
  print('Separation: ' + str(mx_separation) )
  print('Separation Map: ' + str(mx_separationMap) )
  print('Separation Map Texture: ' + str(mx_separationMapFileTexture) )
  print('--------------------------------------\n')


  # Read the camera type UInt value
  activeCameraType = lensParams.getUInt('Type')[0]
  #print('[Camera View Type] ' + str(activeCameraType) )

  # Read the camera parallax distance Float value
  activeParallaxDistance = lensParams.getFloat('Parallax Distance')[0]
  #print('[Parallax Distance] ' + str(activeParallaxDistance) )

  # Read the camera separation Float value
  activeCameraSeparation= lensParams.getFloat('Separation')[0]
  #print('[Camera Separation] ' + str(activeCameraSeparation )

  # --------------------------------------------------------
  # Save the Center Camera

  # Switch the lens shader camera view to center
  cameraType = 0
  lensParams.setUInt('Type', cameraType)
  activeCameraType = lensParams.getUInt('Type')[0]

  centerFilename = scenePathNoExt + '_C.mxs'
  print('[Center MXS Scene] ' + os.path.basename(centerFilename) + ' [Lens] ' + 'LatLong Stereo' + ' [Camera View] ' + str(activeCameraType) + ' [Resolution 2:1 Ratio] ' + str(outputWidth) + 'x' + str(outputHeight) + ' [Parallax Distance CM] ' + str(activeParallaxDistance) + ' [Separation CM] ' + str(activeCameraSeparation))
  ok = scene.writeMXS(centerFilename)
  if ok == 0:
    print('There was an error saving: ' + centerFilename)
    return 0

  # --------------------------------------------------------
  # Save the Left Camera

  # Switch the lens shader camera view to left
  cameraType = 1
  lensParams.setUInt('Type', cameraType)
  activeCameraType = lensParams.getUInt('Type')[0]

  leftFilename = scenePathNoExt + '_L.mxs'
  print('[Left MXS Scene] ' + os.path.basename(leftFilename) + ' [Lens] ' + 'LatLong Stereo' + ' [Camera View] ' + str(activeCameraType) + ' [Resolution 2:1 Ratio] ' + str(outputWidth) + 'x' + str(outputHeight) + ' [Parallax Distance CM] ' + str(activeParallaxDistance) + ' [Separation CM] ' + str(activeCameraSeparation))
  ok = scene.writeMXS(leftFilename)
  if ok == 0:
    print('There was an error saving: ' + leftFilename)
    return 0

  # Todo:  Change the lens shader camera view to Right

  # --------------------------------------------------------
  # Save the Right Camera

  # Switch the lens shader camera view to right
  cameraType = 2
  lensParams.setUInt('Type', cameraType)
  activeCameraType = lensParams.getUInt('Type')[0]

  rightFilename = scenePathNoExt + '_R.mxs'
  print('[Right MXS Scene] ' + os.path.basename(rightFilename) + ' [Lens] ' + 'LatLong Stereo' + ' [Camera View] ' + str(activeCameraType) + ' [Resolution 2:1 Ratio] ' + str(outputWidth) + 'x' + str(outputHeight) + ' [Parallax Distance CM] ' + str(activeParallaxDistance) + ' [Separation CM] ' + str(activeCameraSeparation))
  ok = scene.writeMXS(rightFilename)
  if ok == 0:
    print('There was an error saving: ' + rightFilename)
    return 0

  print('\n--------------------------------------')
  print('Automagic Scene Setup Complete')
  return 1


# Render the stereo project files
# Example: aml_renderStereo('C:/Program Files/Next Limit/Maxwell 3/scripts/stereo/CubeX.mxs', 0, 1, 1)
def aml_renderStereo(mxsFilePath, centerView, leftView, rightView, imageExtension):

  # Find out the current scene file
  dirName = os.path.dirname(mxsFilePath)
  sceneName = os.path.basename(mxsFilePath)
  scenePathNoExt = os.path.splitext(mxsFilePath)[0]

  # Generate the scene and image file names
  centerFilename = scenePathNoExt + '_C.mxs'
  centerImagename = scenePathNoExt  + '_C.' + imageExtension

  leftFilename = scenePathNoExt + '_L.mxs'
  leftImagename = scenePathNoExt  + '_L.' + imageExtension

  rightFilename = scenePathNoExt + '_R.mxs'
  rightImagename = scenePathNoExt  + '_R.' + imageExtension

  print('\n--------------------------------------')
  print('LatLong Stereo Rendering')

  if centerView == 1:
    if os.path.exists(centerFilename):
      print('Rendering the Center Camera View')
      parameters = []
      parameters.append('-mxs:' + centerFilename)
      parameters.append('-display')
      parameters.append('-o:' + centerImagename)
      parameters.append('-p:low')
      print('[Parameters] ' + str(parameters))
      runMaxwell(parameters)
    else:
      print('[Center View MXS file not found] ' + centerFilename)
    
  if leftView == 1:
    if os.path.exists(leftFilename):
      print('Rendering the Left Camera View')
      parameters = []
      parameters.append('-mxs:' + leftFilename)
      parameters.append('-display')
      parameters.append('-o:' + leftImagename)
      parameters.append('-p:low')
      print('[Parameters] ' + str(parameters))
      runMaxwell(parameters)
    else:
      print('[Left View MXS file not found] ' + centerFilename)
    
  if rightView == 1:
    if os.path.exists(rightFilename):
      print('Rendering the Right Camera View')
      parameters = []
      parameters.append('-mxs:' + rightFilename)
      parameters.append('-display')
      parameters.append('-o:' + rightImagename)
      parameters.append('-p:low')
      print('[Render Parameters] ' + str(parameters))
      runMaxwell(parameters)
    else:
      print('[Right View MXS file not found] ' + centerFilename)

  print('--------------------------------------')
  print('The Automagic rendering stage is complete!')
  

# This code is the "main" section that is run automatically when the python script is loaded in pyMaxwell:
if __name__ == "__main__":

  # Choose a Maxwell MXS scene file to process:
  #mxsFilePath = '/Applications/Maxwell 3/scripts/stereo/CubeX.mxs'
  mxsFilePath = 'C:/Program Files/Next Limit/Maxwell 3/scripts/stereo/CubeX.mxs'
  #mxsFilePath = '/opt/maxwell-3.2/scripts/stereo/CubeX.mxs'
  #mxsFilePath = '/home/andrew/maxwell-3.2/scripts/stereo/CubeX.mxs'

  # Choose a LatLong Stereo Separation Texture Map:
  #separationTexturePath = '/Applications/Maxwell 3/scripts/stereo/textures/separation_map.png'
  separationTexturePath = 'C:/Program Files/Next Limit/Maxwell 3/scripts/stereo/textures/separation_map.png'
  #separationTexturePath = '/opt/maxwell-3.2/scripts/stereo/textures/separation_map.png'
  #separationTexturePath = '/home/andrew/maxwell-3.2/scripts/stereo/textures/separation_map.png'


  # Choose a stereo depth ratio.
  # ----------------------------------------
  # This is a value like (1/100) or (1.0/55.0) which will be used to calculate a comfortable camera separation value. The camera's current focus distance is applied as the parallax distance value using the following math:
  # Example: camera separation (in cm) = parallax distance (in cm) * stereoDepthStrength
  # Example: 6.5 = 360 * (1/55)
  
  # Use a strong stereo depth ratio
  #stereoDepthStrength = (1.0/30.0)

  # Use a medium stereo depth ratio
  stereoDepthStrength = (1.0/55.0)
  
  # Use a standard stereo depth ratio
  #stereoDepthStrength = (1.0/100.0)
  
  # Use a gentle stereo depth ratio 
  #stereoDepthStrength = (1.0/120.0)
  
  
  # Camera Views to Render
  # ----------------------------------
  # Set each of the views to 1 to render, and 0 to skip rendering
  leftView = 1
  rightView = 1
  centerView = 0
 
 
  # Launch the automagic stereo camera set up command
  if os.path.exists(mxsFilePath):
    # Generate the stereo project files
  	ok = aml_automagicStereo(mxsFilePath, separationTexturePath, stereoDepthStrength)
  	if ok == 1:
  	  # Render the stereo project files
  	  aml_renderStereo(mxsFilePath, centerView, leftView, rightView, 'png')

  else:
    print('[MXS File Not Found] ' + mxsFilePath)

