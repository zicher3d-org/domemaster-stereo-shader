Domemaster3D Stereo Lens Shader for Maya x64 and 3DS Max x64
Version 2.1 - September 6, 2016

About This Shader
---------------------
The Domemaster Stereo lens shader is a custom mental ray shader that creates a stereoscopic 3D fisheye image. The lens shader provides advanced controls to optimize the viewing experience for stereoscopic dome renderings. 

The shader collection also supports fulldome 2D rendering using either the DomeAFL_FOV shader, the DomeAFL_WxH shader, or the "Center" camera option in the DomeAFL_FOV_Stereo shader. 

Latitude Longitude rendering (also known as spherical or equirectangular output) is supported with the help of the latlong_lens shader, and the stereoscopic LatLong_Stereo shader.

Note: The previous Domemaster3D Shader v1.5 has updated the Maya Binary (.mb) Node ID codes used for the domeAFL and latlong_lens shaders. If you open a .mb file created in a previous Domemaster3D release, you should use the "upgrade" tool in the Domemaster3D shelf to modify the Node ID codes. Lens shader nodes that need to be updated will have their icons replaced in the Hypershade with the red text that reads "NodeID Upgrade Required."

Install Directory
-------------------
The Domemaster3D shader is installed to the following paths:

Windows:
C:\Program Files\Domemaster3D\

Mac OS X:
/Applications/Domemaster3D/

Linux:
/opt/Domemaster3D/


Windows Notes
-------------------
The Domemaster3D v2.1 mental ray release for Windows has been compiled with Visual Studio 2012. If your system doesn't have the Visual Studio 2012 (VC++ 11.0) x64 Redistributable Package installed you can download it here: 
http://www.microsoft.com/en-us/download/details.aspx?id=30679

The Domemaster3D v2.1 for Vray release for Windows was compiled using Visual Studio 2013. If your system doesn't have the Visual Studio 2013 Visual C++ Redistributable Package installed you can download it here:
https://www.microsoft.com/en-us/download/details.aspx?id=40784

Mac Notes
----------
The minimum Mac OS X version required to run the compiled versions of the Domemaster3D mental ray shaders is now Mac OS X 10.9 due to the version of Xcode used to compile the current .dylib library files. 

If you need support for older versions of Mac OS X, you can compile the shaders locally on a legacy Mac OS X system using the included Makefiles and the shaders will run on systems as old as Mac OS X 10.6.

https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/Maya-Domemaster3D-Shader-Compiling#compiling-a-mac-os-x-build

Documentation and Resources
-----------------------------------

Join the discussion on the Domemaster Stereo Shader NING Group
http://fulldome.ning.com/forum/topics/stereoscopic-domemaster-images

Downloads Page
https://github.com/zicher3d-org/domemaster-stereo-shader/releases

Domemaster Stereo Shader Wiki
https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/

Maya Domemaster3D Shelf Tools
https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/Maya-Domemaster3D-Shelf

Report an Issue
https://github.com/zicher3d-org/domemaster-stereo-shader/issues

Source Code:
https://github.com/zicher3d-org/domemaster-stereo-shader/

-----------------------------------------------------------------------

Version History
-----------------

Version 2.1
-------------
2016-09-06

Maya
  Added initial Maya 2017 Support

  Added a mental ray native texture based Maya example project file named "Domemaster3D_transparent_materials_project.zip" that shows how to map a color material with a separate alpha channel to an mia_material. It is stored in the folder:
  
    C:\Program Files\Domemaster3D\docs\Maya_Examples\
    /Applications/Domemaster3D/docs/Maya_Examples/
    /opt/Domemaster3D/docs/Maya_Examples/
  
  Updated the Dome Diagnostics script to use Maya workspace based file paths. Added a "domeOpenVrayRenderLogFile();" function for opening the Vray for Maya render log file.
  
  Started improving the Domemaster3D/Vray for Maya integration. Added a new "VrayDomemaster3D.mod" Maya module file, updated the shelf tool items, and added new "VRay Domemaster3D" menu in the Maya Rendering menu set. 
  
  Started improving the Domemaster3D/Arnold for Maya integration. Updated the "ArnoldDomemaster3D.mod" Maya module file, updated the shelf tool items, and added a new "Arnold Domemaster3D" menu in the Maya rendering menu set.
  
  Added support in Maya 2016/2017 for creating Maya file node based screen space texture maps in the LatLong_Stereo and domeAFL_FOV_Stereo shaders, and in the screen space texture map shelf tool with the help of a mib_texture_vector node and a place2Dtexture node. This replaces the previous mentalrayTexture node based approach that has been depreciated in the Maya 2017/mental ray 3.14 beta releases.
  
  Updated the mental ray shader source code to create a new mental ray 3.14 version of the code that will support the new ray differential texture sampling mode. This new rendering mode will hopefully eliminate the "blurry streak" lens shader artifact seen on Maya file node based textures in panoramic scenes and remove the need to use mental ray native textures as a work around. This ray differential based lens shader feature can't be enabled until the beta 9 release of mental ray for Maya 2017 is released.
  
Version 2.0
-------------
2016-06-22

3DS Max
  Added Max 2017 Support

Maya
  Added Maya 2016.5 Support
  
  Switched the Domemaster3D for Maya 2016.5-2013 installer options from using a Maya.env approach to a Domemaster3D.mod file.
  Updated the Domemaster3D Menus
  
  Added the "DOMEMASTER3D_MAYA_REALTIME_FOV" attribute to the Domemaster3D.mod Module file.
  
  Added DomeViewer image projection support for the Facebook 360 Pyramid, LG360 Camera, and the Samsung Gear 360 Camera image projections.
  
  Updated the Dome Diagnostics script

Version 1.9.3
-------------
2016-02-08

Maya
  Updated the DomeViewer tool to add Ricoh Theta S support along with a set of Ricoh Theta S panoramic viewing meshes "ricoh_theta_s_mesh.obj", and "ricoh_theta_s_mesh.ma" to the Domemaster3D sourceimages folder

  Updated the DomeViewer tool to add Facebook Cube Map 3x2 support along with a set of Facebook Cube Map 3x2 panoramic viewing meshes "facebookCube3x2_mesh.obj", and "facebookCube3x2_mesh.ma" to the Domemaster3D sourceimages folder

  Updated the Dome Diagnostics tool to add support for the mental ray env variable "MAYA_MRFM_SHOW_CUSTOM_SHADERS" that will expose the custom mental ray shaders in Maya.

Version 1.9.2
-------------
2016-01-11

Vray for 3DS Max
  Roberto Ziche updated the Vray Domemaster Stereo and LatLong Stereo shaders.
  
  Added a new automatic pole correction option for controlling the stereo effect that can be used in addition to the separation multiplier map. It uses a Start Angle and End Angle control to fade out the stereo.

  Added a parallel camera option that skips the need to use the parallax distance control.

  Improved Neck Offset for matching against live action rig camera nodal point offsets.

  Added a Hemirect control that lets you lock the top frame edge at the zenith for a cropped FOV in a LatLong frame rendering. This lets you render a vertically cropped 360x90 FOV LatLong image for example and then be able to convert it into a fulldome frame later as the top boundary of the "hemirect" is the zenith pole area.

Maya
  Updated the DomeViewer tool to add GearVR Mono Cube support, and included a set of Gear VR panoramic viewing meshes "gearVRCube_mesh.obj", and "gearVRCube_mesh.ma" in the Domemaster3D sourceimages folder
  
  Changed the DomeViewer "Show Focal Length in HUD" default state to off
  
  Added a new DomeViewer "Connect Alpha Channel" checkbox to the Extra Controls section of the GUI. This checkbox tells the DomeViewer to connect the alpha channel from the DomeViewer loaded imagery to the surface material node. Th new "Connect Alpha Channel" checkbox is disabled by default so imagery with transparent mental ray rendered physical sky and sun and IBL based environment backdrops can be viewed in the viewport and you will still see the sky background.

  Updated the Dome Diagnostics tool to add detection for the PlayblastVR Panoramic Format "Gear VR Mono Cube" option var
  
  Added Dome Diagnostics support for the following Maya environment variables:
    
    ALIAS_RENDER_LIB_PATH
    BIFROST_LOCATION
    ENABLE_DEFAULT_VIEWPORT_CAMERA_SETS
    IMF_PLUG_IN_PATH
    MAYA_ADSK_ASSET_LIBS
    MAYA_BATCH_RENDERING_STOPS_ON_ERROR
    MAYA_BG_DEPTH_IMAGE
    MAYA_BIFROST_COMPOUNDS
    MAYA_COLOR_MANAGEMENT_POLICY_FILE
    MAYA_COLOR_MANAGEMENT_POLICY_LOCK
    MAYA_CUSTOM_TEMPLATE_PATH
    MAYA_DISABLE_LOOKDEV_MATERIAL_VIEWER
    MAYA_DISABLE_LOOKDEV_PROPERTY_PANEL
    MAYA_DISABLE_VP2_WHEN_POSSIBLE
    MAYA_ENABLE_CLASSIC_HAIR
    MAYA_ENABLE_LEGACY_HYPERSHADE
    MAYA_ENABLE_LEGACY_PARTICLES
    MAYA_ENABLE_LEGACY_RIGID
    MAYA_ENABLE_VP2_SHAPE_INSTANCING
    MAYA_EXPOSE_FACADE_NODES
    MAYA_FBX_PLUGIN_LOCATION
    MAYA_HELP_URL
    MAYA_NO_INITIAL_AUTOLOAD_MT
    MAYA_OFFSCREEN_HRB
    MAYA_OGS_DEVICE_OVERRIDE
    MAYA_PLUG_IN_RESOURCE_PATH
    MAYA_PROJECT
    MAYA_PROJECTS_DIR
    MAYA_PSEUDOTRANS_MODE
    MAYA_REAL_WORLD_SIZE
    MAYA_REVERSE_FILEFORMAT_EXT
    MAYA_SCRIPT_BASE
    MAYA_SHADER_LIBRARY_PATH
    MAYA_TESTING_CLEANUP
    MAYA_TEXTURED_SCULPT
    MAYA_UI_LANGUAGE
    MAYA_VP2_DEVICE_OVERRIDE
    MAYA_VR_PER_SHAPE_ATTR
    NEX_DRINIT_PATH
    ONECLICK_KEEP_TEMP_FILES
    ONECLICK_SELECT_WHOLE_CHARACTER
    ONECLICK_TEMP_DIR
    PYMEL_SKIP_MEL_INIT
    QT_MAC_NO_NATIVE_MENUBAR
    SUBSTANCES_LOCATION
    WINEDITOR
    XPC_SERVICE_NAME

  Added Dome Diagnostics support for the following Vray environment variables:
    VRAY_ADVANCED_UI
    VRAY_FOR_MAYA_DRLISTS_PATH
    VRAY_FOR_MAYA_DRPORT
    VRAY_FOR_MAYA2012_SKIP_NODE_CATEGORIZATION
    VRAY_OSL_PATH_MAYA2016_PowerPC
    VRAY_OSL_PATH_MAYA2016_x64
    VRAY_PATH

Version 1.9.1
-------------
2015-10-15

Maya
  Added the ability to use a "DOMEMASTER3D_MAYA_REALTIME_FOV" environment variable through your operating system, the Maya.env file, or a Maya module file to set the realtime OpenGL "persp" viewport focal length value for domeAFL_FOV, domeAFL_FOV_Stereo, domeAFL_WxH, latlong_lens, and LatLong_Stereo camera rigs. Typical values would be 4 (mm) for a wide angle 160 degree FOV in the OpenGL persp viewport, or 18 (mm) for a regular 90 degree FOV view.

  In a Maya.env file you would change this environment variable by un-commenting/adding the line like this. (4 in this example means a 4mm lens in Maya):

  DOMEMASTER3D_MAYA_REALTIME_FOV=4


Version 1.9
-------------
2015-09-23 

Arnold
  Translated the Arnold C4DtoA Cinema4D shader UI to Japanese

Maya
  Added a new Domemaster3D menu item "LatLong Stereo Aim Camera" for making a camera rig that has an aim constraint applied for easier camera animation. Reminder: Maya has issues with using cameras that have aim constraints when you apply them to animation layers.
  A LatLong Stereo Aim Camera can be created using the following python code:
  
    import domeCamera as domeCamera
    reload(domeCamera)
    domeCamera.createLatLongStereoAimRig()

  Added a new Domemaster3D menu item "LatLong Stereo Zenith Camera" function for making a camera rig that has the "Zenith Mode" checkboxes enabled by default and a vertical orientation.
  A LatLong Stereo Zenith Camera can be created using the following python code:
  
    import domeCamera as domeCamera
    reload(domeCamera)
    domeCamera.createLatLongStereoZenithRig()

  Updated the dome Diagnostics tool with the following changes:
    
    Added detection for the Maya quicktime video encoding environment variable MAYA_QUICKTIME_ENCODING_GAMMA.
    
    Updated the PlayblastVR optionVar list for the batch sequence viewers
    
    Added detection for the MAYA_NO_CONSOLE_WINDOW environment variable. This environment variable lets you turn off the display of the Maya console window. It can effect the stability of batch renders that are launched with mayabatch if the console is disabled and anything is printed directly to the console window.

    Added the Environment variable detection for the following Maya 3rd party modules and plugins:
    
    Bifrost Env Vars:
      BIFROST_ECHO_GEOSHADER
      BIFROST_ENABLE_GRAPH_EDITING
    
    QT Support Env Vars:
      QT_HIGHDPI_AWARE
      MAYA_ALIEN_WIDGETS
    
    Mental Ray Env Vars:
      MI_MAYA_BATCH_OPTIONS
      MI_CUSTOM_SHADER_PATH
      MI_CUSTOM_SHADER_SUPPRESS - do not load suppressed files
      MAYATOMR   - used for a pipe to the renderer
    
    Arnold Env Vars:
      MTOA_SILENT_MODE 
      MTOA_COMMAND_PORT
      ARNOLD_LICENSE_ATTEMPTS
      ARNOLD_LICENSE_ATTEMPT_DELAY
      K_SEARCH_PATH
      
    XGEN Env Vars:
      XGEN_CONFIG_PATH
      XGEN_EXPORT_ARCHIVE_STANDALONE
      XGEN_LOCATION
      XGEN_ROOT
      HDF5_DISABLE_VERSION_CHECK
      
    SEEXPR Software Env Vars:  
      SE_EXPR_PLUGINS
    
    Mac & Linux Env Vars:
      LD_LIBRARY_PATH

Version 1.8.3
-------------
2015-08-27

Arnold
  Added the Maya AE python template resources to the MtoA shader release that is included with the Domemaster3D installer.

Maya
  Added a "Add Pre/Post Render Mel" and "Remove Pre/Post Render Mel" set of menu items to the Domemaster3D menu and shelf buttons labelled "ADD" and "REM". The "Add" shelf button adds the Domemaster3D pre-render mel scripts to the render settings window. This is used for the LatLongStereo and DomeAFL_FOV_Stereo shaders to switch the stereo camera rig between the realtime anaglyph stereo mode in the viewport and the mental ray lens shader controlled stereo mode at render time. The "Rem" button removes the Domemaster3D pre-render mel scripts from the render settings window and disables the realtime anaglyph viewport preview mode. This is used to prepare a scene that might be submitted to an online render farm service that doesn't allow pre/post render mel scripts to be included with a scene file.
  
  Added a "MAYA" shelf tool and the "Launch Another Maya Instance" Domemaster3D menu item will launch an additional copy of Maya that will run independently. This is handy if you want to work in two separate Maya sessions at the same time. The MEL command used by the shelf tool is: source "domeDiagnostics.mel"; domeLaunchMayaInstance();

  Updated the DomeAFL_FOV_Stereo and LatLong_Stereo python camera rig scripts to use a default camera separation of 6.5 cm.
  
  Added the `AddPrePostRenderScript()` and `RemovePrePostRenderScript()` functions to the domeCamera.py script to make it easier to set up the Domemaster3D pre render and post render mel scripts in the Maya render settings window.
  
  Added several new mia_material_x_passes material presets for rendering water simulation meshes:
  -  The `WaterBlueWideOceanDeep` preset is a refractive ocean water material with the color at max distance value set to 50 units. 
  -  The `WaterBlueWideOceanShallow` preset is a refractive ocean water material with the color at max distance value set to 2 units.
  -  The `WaterRustyIronLakeDeep` preset is a refractive lake water material with the color at max distance value set to 50 units.
  -  The `WaterRustyIronLakeShallow` preset is a refractive lake water material with the color at max distance value set to 2 units.

Version 1.8.2
-------------
2015-08-17

Vray
  Added the Vray 3.1 for Maya Domemaster3D shader beta files to the folder:
  C:\Program Files\Domemaster3D\vray
  
Arnold
  Added the first working version of the Cinema4D C4DtoA Domemaster3D shader beta files to the folder:
  C:\Program Files\Domemaster3D\arnold\c4dtoa
  
Maya
  Updated the Dome Diagnostics tool to include a check for the Maya "MAYA_DISABLE_IDLE_LICENSE" env variable detection
  
  Added a domeOpenSourceImagesDirectory() function to open the sourceimages directory. This is used by the Domemaster3D Maya shelf tool "SRC".
  
  Added a Maya Domemaster3D Hybrid MR + Maya Color Material. The new Hybrid mentalrayTexture material shading network combines the render time improvements of a mental ray texture based surface material for reducing blurry streak artifacts when rendering with lens shaders, and a real-time high resolution preview benefit of a stock maya file texture node. The shading group uses the "Suppress all Maya Shaders" setting to make sure the mentalrayTexture is used at render time in a similar fashion to how the Starglobe surface material works.
  
  Added two new mia_material_x_passes material presets "Gold" and "AmberCrystalGlass". They do a really good job of demonstrating the new Maya 2016 Hypershade material preview viewport window's mental ray rendering mode.

Version 1.8.1
-------------
2015-07-27 

Vray
  Added the Vray 3.2 Domemaster3D shader beta files to the folder:
  C:\Program Files\Domemaster3D\vray

Maya
  Fixed an issue that would occur with the domeAFL_FOV and DomeAFL_FOV_Stereo shader's preview hemisphere mesh alignment when linking the lens shader to an existing camera that is tipped away from the upright initial position.

Version 1.8
-------------
2015-07-08

Arnold
  Added the Arnold Domemaster3D shader beta files to the folder:
  C:\Program Files\Domemaster3D\arnold
  
Vray
  Added the Vray Domemaster3D shader beta files to the folder:
  C:\Program Files\Domemaster3D\vray

Maya
  Fixed an issue with the Domemaster3D Menu where the LatLong stereo menu item wasn't linked to the correct menu function.


Project Developers
----------------------

Domemaster Stereo Shader & LatLong_Stereo shaders created by Roberto Ziche
http://www.robertoziche.com/

Domemaster3D & LatLong_Stereo shaders for Maya and Softimage, the custom Domemaster3D shelves, the Wiki documentation, and the installer by Andrew Hazelden
andrew@andrewhazelden.com
http://www.andrewhazelden.com/blog

Domemaster Stereo Shader is Based upon Daniel Ott's DomeAFL Angular Fisheye Lens Shader
http://www.thedott.net/shaders/domeAFL/

Special Thanks
-----------------
Thanks to the following people for their contributions:

Ralf Habel for the 2D latlong_lens shader
http://www.vi-motion.de/latlong_Tutorial/

Aaron Bradbury for the installer imagery from his Vortex fulldome short film.
http://www.luniere.com/project/vortex/

Aaron Bradbury for the inclusion of the fulldome alignment grid:
http://www.luniere.com/2013/03/07/hi-res-fulldome-alignment-grid/

Jason Fletcher for creating a high quality equirectangular starglobe texture, and the starfield, sun, and nebula example scenes:
http://thefulldomeblog.com/2013/06/22/stars-to-surround-the-scene/
http://thefulldomeblog.com/2013/07/30/customizing-a-close-up-sun/
http://thefulldomeblog.com/2013/07/03/creating-a-star-field/
http://thefulldomeblog.com/2013/08/20/the-nebula-challenge/

Martin Watt for writing the original galaxies.mel script.
