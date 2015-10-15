"""
Fulldome Cross Bounce Setup Script V1.9
for Domemaster3D and Maya on Windows
2015-08-21

This script will create a Maya scene that uses Mental Ray Final Gather to compute a fulldome crossbounce light simulation. The rendered image shows the light pollution that happens when a video image is projected on a hemispherical dome screen. You can preview the full result in Photoshop or After Effects by applying the rendered crossbounce simulation with an Add (Linear Dodge) transfer mode over the original fulldome image.

The default image used is the ocean fulldome test image that comes with the domemaster3D shader:
C:\Program Files\Domemaster3D\sourceimages\fulldome_2K.jpg

When the script runs, the fulldome_2K.jpg image is used as the source texture for the FulldomeIBL sim and it is also loaded as a "kept image" in the Maya render view window. Also, the fulldome domeAFL_FOV camera is snapshoted automatically as the current render camera so the first time you hit render in the render view you will be looking through the correct camera.

The Domemaster3D v1.6 or newer FulldomeIBL tool is used to set up the domemaster formatted image sequence loading and a remapColor low dynamic range to high dynamic range image conversion preset is used to enhance the IBL based light simulation.


How to use this Script
-------------------------

Step 1. You need to download a copy of the Domemaster3D shader (version 1.6 or higher) to use this script:
https://github.com/zicher3d-org/domemaster-stereo-shader/releases

Step 2. Place the python "domeCrossBounce.py" script in one of Maya's 'script' folders and restart Maya. Copy the icon file "domeCrossBounce.png" to your Maya icons folder.

Step 3. Then you can run the script in the Maya Script Editor window using the commands:
import domeCamera
reload(domeCamera)
domeCamera.forceMentalRayLoad()

import domeCrossBounce
reload(domeCrossBounce)
domeCrossBounce.createCrossBounce()

Step 4. When the script starts you will be asked if you want an circular alpha mask to be applied to the fulldome frame. This will matte out any writing or captions that might exist around a domemaster frame. Choosing "Yes" or "No" in the Fulldome IBL Creation dialog is fine if you are using the sample fulldome_2K.jpg test image.

Step 5. If you click "render" in the Render View you will see the simulated crossbounce light pollution. If you save the frame to your desktop you can try compositing it over the original image ( C:\Program Files\Domemaster3D\sourceimages\fulldome_2K.jpg ) in Photoshop using the Linear Dodge / Add transfer mode to compare the difference.
"""

def createCrossBounce():
  import maya.cmds as cmds
  import maya.mel as mel
  import domeCamera
  reload(domeCamera)
  import domeMaterial
  reload(domeMaterial)

  # ---------------------------------------------------------------------
  # Variables
  # ---------------------------------------------------------------------

  # The fulldome mesh should be 25 units in size
  fulldomeMeshScale = 25

  # Outliner name for the all quads fulldome mesh shape
  fulldomeMeshName = 'fulldomeMesh'

  # ---------------------------------------------------------------------
  # Scene Setup
  # ---------------------------------------------------------------------

  #Create a new Maya scene
  cmds.file( force=True, newFile=True)

  # Tell the mental ray plugin to load automatically
  domeCamera.forceMentalRayLoad()
  
  # Add a default mentalrayGlobals node
  mel.eval('createNode "mentalrayGlobals" -n "mentalrayGlobals";')

  # Add the initial rendering settings for the scene
  setupDomeRenderOptions()

  # ---------------------------------------------------------------------
  # FulldomeIBL Lighting Setup
  # ---------------------------------------------------------------------

  # Add a mental ray IBL shape to the scene
  domeCamera.createFulldomeIBL()

  # Adjust the IBL shape position
  cmds.setAttr('mentalrayIbl1.rotate', -90, 0, 0, type='float3')
  cmds.setAttr('mentalrayIbl1.scale', -200, 200, 200, type='float3')

  dome_tex_remap = 'dome_mib_texture_remap1'

  #Set the matrix to use a mirrored effect on the X and Y axis matrix cells
  melSetAttrMatrixString = 'setAttr "' + dome_tex_remap + '.transform" -type "matrix" -1 0 0 0 0 -1 0 0 0 0 1 0 0 0 0 1;'
  mel.eval(melSetAttrMatrixString)

  # Load the following LDR to HDR presets file:
  ldrToHdrPresetsFile = domeMaterial.getDomePresetsPath("remapColor/ldr_to_hdr_boost_10x.mel")

  # Apply the ldr_to_hdr_boost_10x preset to the FulldomeIBL shading network
  mel.eval('applyPresetToNode "dome_remapColor1" "" "" "' + ldrToHdrPresetsFile + '" 1')

  # Set the HDR light boosting ratio to 7.5X brighter on the highlights
  cmds.setAttr('dome_remapColor1.outputMax', 7.5)

  # 180 Degree Fulldome Camera
  domeCamera.createDomeAFL_FOV_Camera()

  # Turn off the domeAFL_FOV shader's preview shape
  cmds.setAttr('domeAFL_FOV.fovDisplayMode', 0)

  # ---------------------------------------------------------------------
  # Load the all quads based fulldome mesh
  # ---------------------------------------------------------------------

  # Add the fulldome_quads_mesh.ma mesh to the scene
  fulldomeBaseMesh = domeMaterial.getSourceImagesPath("fulldome_quads_mesh.ma")


  # Note: Maya 2014+ has the mergeNamespacesOnClash flag
  #mel.eval('file -import -type "mayaAscii" -ra true -mergeNamespacesOnClash false -rpr "fulldome_quads_mesh" -options "v=0;" "' + fulldomeBaseMesh + '"')

  # Note: Maya 2010 doesn't have the mergeNamespacesOnClash flag
  # Cross platform file path
  mel.eval('file -import -type "mayaAscii" -ra true -rpr "fulldome_quads_mesh" -options "v=0;" "' + fulldomeBaseMesh + '"')

  # Rename the fulldome mesh
  cmds.rename('fulldome_quads_mesh_domeViewer', fulldomeMeshName)      

  # Resize the fulldome mesh
  cmds.setAttr(fulldomeMeshName+'.scale', fulldomeMeshScale, fulldomeMeshScale, fulldomeMeshScale, type='float3')

  # ---------------------------------------------------------------------
  # Render Settings Setup
  # ---------------------------------------------------------------------

  #Add a surface material to the fulldome shape
  setupDomeMatteMaterial(fulldomeMeshName)

  # Frame the perspective view on the fulldome mesh shape
  cmds.setAttr('persp.rotate', 30, 45, 0, type='float3')
  cmds.select(fulldomeMeshName, replace=True)
  mel.eval('viewFit')

  # ---------------------------------------------------------------------
  # Load an image in the view
  # ---------------------------------------------------------------------

  referenceFulldomeImage = domeMaterial.getSourceImagesPath("fulldome_2K.jpg")

  # Load the ocean fulldome test image
  cmds.setAttr('dome_map_mentalrayTexture1.File_Name_Prefix', referenceFulldomeImage, type='string')

  # Set the mentalrayTexture's Frame Animation Ext value to name(Single Frame)
  cmds.setAttr('dome_map_mentalrayTexture1.Frame_Animation_Ext', 0)

  # Set the mentalrayTexture's Frame Animation Ext value to name.ext (Single Frame)
  #cmds.setAttr('dome_map_mentalrayTexture1.Frame_Animation_Ext', 1)
  
  #Enable the JPG image format
  cmds.setAttr('dome_map_mentalrayTexture1.Image_Format', 2)

  cmds.currentTime(2)
  cmds.currentTime(1)

  # Force the Frame_Animation_Ext mode to Native Image Name (Passthrough) once the referenceFulldomeImage name has been loaded once
  # Set the mentalrayTexture's Frame Animation Ext value to Native Image Name (Passthrough)
  cmds.setAttr('dome_map_mentalrayTexture1.Frame_Animation_Ext', 7)
  
  cmds.currentTime(2)
  cmds.currentTime(1)
  
  # ---------------------------------------------------------------------
  # Snapshot the fulldome camera in the render view
  # ---------------------------------------------------------------------

  # Grab the name of the current render view
  currentRenderView = cmds.getPanel( scriptType='renderWindowPanel' )
  theView = currentRenderView[0]
  #Result: theView = 'renderView'

  # Show the render view
  mel.eval('RenderViewWindow;')

  # Take a snapshot through the domeAFL_FOV camera
  mel.eval('renderWindowRenderCamera snapshot ' + theView + ' domeAFL_FOV_CameraShape2;')

  # Load the reference image in the view
  #referenceFulldomeImage = domeMaterial.getSourceImagesPath("fulldome_2K.jpg")
  print('Loading image ' + referenceFulldomeImage + ' in the render view\n')
  cmds.renderWindowEditor(theView, edit=True, autoResize=True, loadImage=referenceFulldomeImage)
  cmds.renderWindowEditor(theView, edit=True, realSize=True)

  # Snapshot the image in the view
  mel.eval('renderWindowMenuCommand keepImageInRenderView '+ theView)

  # ---------------------------------------------------------------------
  # Finish the last few steps
  # ---------------------------------------------------------------------

  #Show the mental ray texture in the Attribute Editor window
  mel.eval('evalDeferred( "showEditor dome_map_mentalrayTexture1");')

  #Turn on smooth shading with textures
  mel.eval('evalDeferred("DisplayShadedAndTextured")')

def setupDomeRenderOptions():
  import maya.cmds as cmds
  import maya.mel as mel
  import domeCamera
  reload(domeCamera)

  # Show the unified render settings window
  mel.eval('unifiedRenderGlobalsWindow')

  # Setup the mental ray render settings
  mel.eval('miCreateDefaultNodes()')

  # Enable the Final Gathering checkbox
  cmds.setAttr('miDefaultOptions.finalGather', 1)

  # Setup the Final Gather quality
  cmds.setAttr('miDefaultOptions.finalGatherRays', 500)
  cmds.setAttr('miDefaultOptions.finalGatherPresampleDensity', 1)
  cmds.setAttr('miDefaultOptions.finalGatherPoints', 100)

  # Enable 2 secondary light bounces
  cmds.setAttr('miDefaultOptions.finalGatherTraceDiffuse', 2)

  # Set the reflection trace depth to 2
  cmds.setAttr('miDefaultOptions.finalGatherTraceReflection', 2)

  # Disable the default light in the scene
  cmds.setAttr('defaultRenderGlobals.enableDefaultLight', 0)

  # Switch the render settings to 512px
  #domeCamera.changeRenderRes(512)

  # Switch the render settings to 1024px
  domeCamera.changeRenderRes(1024)

  # Set up a 1 second (30 frame) playback timeline range
  cmds.playbackOptions(  minTime='1', maxTime='30', loop='continuous' )
  cmds.setAttr('defaultRenderGlobals.startFrame', 1)
  cmds.setAttr('defaultRenderGlobals.endFrame', 30)

  # Enable the name.#.ext naming format for the rendered output with 4 digit frame padding
  cmds.setAttr('defaultRenderGlobals.outFormatControl', 0)
  cmds.setAttr('defaultRenderGlobals.animation', 1)
  cmds.setAttr('defaultRenderGlobals.putFrameBeforeExt', 1)
  cmds.setAttr('defaultRenderGlobals.extensionPadding', 4)
  cmds.setAttr('defaultRenderGlobals.periodInExt', 1)

  # Set the output image format to PNG ( PNG=32)
  renderImageFormat = 32
  cmds.setAttr('defaultRenderGlobals.imageFormat', renderImageFormat)

  # Set the Maya timeline frame rate to the NTSC 30fps format
  cmds.optionVar(stringValue=('workingUnitTimeDefault', 'ntsc'))
  cmds.optionVar(stringValue=('workingUnitTime', 'ntsc'))


# Set up the fulldome preview mesh as a grey matte mia_x_passes material
def setupDomeMatteMaterial(applyToMeshName):
  import maya.cmds as cmds
  import maya.mel as mel  

  #Get the selected geometry
  object_selection = applyToMeshName

  domeShaderName = 'dome_crossbounce_matte_material'

  #Create the mia_material + shading group
  dome_mia_shader_group_name = cmds.sets( renderable=True, noSurfaceShader=True, empty=True, name=domeShaderName+'SG' )
  
  #Create a mia_material_x_passes shader
  dome_mia_shader_name = cmds.shadingNode( 'mia_material_x_passes', n=domeShaderName, asShader=True) 

  #Apply the shading group to the selected geometry
  if object_selection:
    print("Applying the "+dome_mia_shader_name+" surface material to:")
    cmds.select(object_selection)
    cmds.hyperShade(assign=dome_mia_shader_group_name)  

  # Set the mia_material to be a matte material
  cmds.setAttr(dome_mia_shader_name+".diffuse", 0.5, 0.5, 0.5, type="double3")
  cmds.setAttr(dome_mia_shader_name+".diffuse_roughness", 0)
  cmds.setAttr(dome_mia_shader_name+".diffuse_weight", 1)
  cmds.setAttr(dome_mia_shader_name+".refl_color", 1, 1, 1, type="double3")
  cmds.setAttr(dome_mia_shader_name+".reflectivity", 0)

  # Connect the mia_material shader to the shading group
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.surfaceShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miPhotonShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miShadowShader', f=True)
  cmds.connectAttr(dome_mia_shader_name+'.message', dome_mia_shader_group_name+'.miMaterialShader', f=True)


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


#Run the code
#createCrossBounce()

