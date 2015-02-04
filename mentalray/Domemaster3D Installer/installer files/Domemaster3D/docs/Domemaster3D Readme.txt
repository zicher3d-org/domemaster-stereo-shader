Domemaster3D Stereo Lens Shader for Maya x64 and 3DS Max x64
Version 1.6.1 - February 4, 2015

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
The Domemaster3D v1.6 release for Windows has been compiled with Visual Studio 2012. If your system doesn't have the Visual Studio 2012 (VC++ 11.0) x64 Redistributable Package installed you can download it here: 
http://www.microsoft.com/en-us/download/details.aspx?id=30679

Mac Notes
----------
The minimum Mac OS X version required to run the compiled versions of the Domemaster3D mental ray shaders is now Mac OS X 10.8 due to the version of Xcode used to compile the current .dylib library files. 

If you need support for older versions of Mac OS X, you can compile the shaders locally on a legacy Mac OS X system using the included Makefiles and the shaders will run on systems as old as Mac OS X 10.6.

Domemaster3D Media Folder
--------------------------------
The Domemaster3D control texture maps, models, and the DomeViewer panoramic meshes are stored in the following directories:
Windows:
C:\Program Files\Domemaster3D\sourceimages\

Mac OS X:
/Applications/Domemaster3D/sourceimages/

Linux:
/opt/Domemaster3D/maya/sourceimages/


Maya Manual Installation
-----------------------------
The base Maya files are all inside this folder:
C:\Program Files\Domemaster3D\maya

The Domemaster3D for Maya common icons, presets, and scripts that work across Maya 2010-2015 are stored in the following folder:
C:\Program Files\Domemaster3D\maya\common

The specific scripts that work with each Maya release are stored in a folder with the Maya version number in the name. For example, Maya 2015 specific files like the shelves, mental ray physical sky & sun override scripts, and Maya.env backup files are stored in:
C:\Program Files\Domemaster3D\maya\2015

The Maya.env files for each specific Maya version are named:
Maya.env.linux
Maya.env.osx
Maya.env.win

To use the appropriate Maya.env file you need to select the right one for your platform, rename it to "Maya.env", and copy it to your user account's "Maya version-x64" folder:
C:\Users\<Your User Account>\Documents\Maya\Maya2012-x64\Maya.env


Maya Tools
-------------------
The Maya version of the Domemaster3D shader comes with a custom shelf with 29 tools that help automate the fulldome production process, and features a matching Domemaster3D Menu system.

Domemaster3D Shelf Tools

Automagic Button
The AutoMagic tool creates a domeAFL_FOV_Stereo based fulldome stereo camera rig and adds a hemispherical reference grid to the scene.

Stereo Rig button
The Stereo Rig tool create a stereo fulldome camera rig with the domeAFL_FOV_Stereo lens shader applied.

Dome Texture Button
The Dome Texture tool creates a screen space file texture. This is useful for loading file textures as control maps for the domeAFL_FOV_Stereo and LatLong_Stereo shaders.

DomeRamp Button
The DomeRamp tool creates a screen space ramp texture. This is useful for creating editable gradients that can be used to drive the control maps on the domeAFL_FOV_Stereo and LatLong_Stereo shaders.

DomeAFL_FOV Button
The DomeAFL_FOV tool creates a standard 2D fulldome camera with the domeAFL_FOV lens shader applied.

DomeAFL_WxH Button
The DomeAFL_WxH tool creates a 2D fulldome camera with the domeAFL_WxH lens shader applied. This shader uses a diameter and height setting instead of a field of view control.

LatLong Button
The LatLong tool creates a latlong / equirectangular / spherical camera with the latlong_lens shader applied.

LatLong3D Button
The LatLong_Stereo tool creates a stereoscopic latlong / equirectangular / spherical camera with the LatLong_Stereo shader applied.

Color Material Button
The Color Material tool creates a mia_material_x_passes based mental ray shading network with support for color file textures.

Color + Bump Material button
The Color + Bump Material tool creates a mia_material_x_passes based mental ray shading network with support for color and bump file textures.

Color Image Sequence Material Button
The Color Image Sequence Material tool creates a mia_material_x_passes based mental ray shading network with support for color file textures. The mentalrayTexture node has extra attributes applied that allow you to create image sequences.
Note: The image sequence mode requires your batch rendering software to distribute the rendering job using 1 frame per packet / render slice so a new image is loaded for each frame of the sequence.

Starglobe Button
The Starglobe tool creates a mia_material_x_passes based starry background for your fulldome scenes.

FulldomeIBL Button
The FulldomeIBL tool creates a custom mentalrayTexture based shading network that lets you feed fulldome 180 degree images and image sequences into mentalray IBL's angular texture input.
Note: The FulldomeIBL image sequence mode requires your batch rendering software to distribute the rendering job using 1 frame per packet / render slice so a new image is loaded for each frame of the sequence. The FulldomeIBL tool works with Maya 2015's newly improved "emit light" IBL lighting system

HemirectIBL Button
The HemirectIBL tool creates a custom mentalrayTexture based shading network that lets you feed in an image with the top half of an equirectangular panorama into mental ray IBL's spherical texture input. The word Hemirect is short for hemi-equirectangular which is a new panoramic format based upon using the top 90 degree field of view zone of an equirectangular image which gives a 360° horizontal by 90° vertical part of the "all sky" region that matches the coverage area of a regular fulldome image.
Note: The HemirectIBL image sequence mode requires your batch rendering software to distribute the rendering job using 1 frame per packet / render slice so a new image is loaded for each frame of the sequence. The HemirectIBL tool works with Maya 2015's newly improved "emit light" IBL lighting system.

DomeGrid Button
The DomeGrid tool creates a hemispherical yellow wireframe reference grid.

Galaxy Creator button
The Galaxy Creator tool creates dynamic particle based galaxies.

DomeText button
The DomeText button tool created raster titles and scrolling credits that can be used in a fulldome 2D or fulldome stereo production setting. This tool uses ImageMagick to render the title graphics using fonts installed in your system.

CrossBounce Button
Simulate the effect of "crossbounce" light pollution that happens when imagery is projected across a hemispherical fulldome theatre screen.

DomeViewer button
The DomeViewer tool provides an immersive fulldome and panoramic image / movie viewer.

Histogram Button
The Histogram tool uses ImageMagick to calculate a histogram analysis for the current image in the render view. Clicking the "Refresh the Histogram" button updates the plot.

Render Rez Buttons
The 0.5k button sets the render resolution to 512x512 pixels.
The 1k button sets the render resolution to 1024x1024 pixels.
The 2k button sets the render resolution to 2048x2048 pixels.
The 4k button sets the render resolution to 4096x4096 pixels.
The 8k button sets the render resolution to 8192x8192 pixels.
The 2x1k button sets the render resolution to 2048x1024 pixels.
The 4x2k button sets the render resolution to 4096x2048 pixels.
The 8x4k button sets the render resolution to 8192x4096 pixels.

Open Scenes Folder Button
The SCN button opens the scenes folder for the current project in a new window on your desktop. This is the same as if you manually browsed to the folder using Finder (Mac OS X), Windows Explorer, or Nautilus (Linux).

Open Images Folder Button
The IMG button opens the images folder for the current project in a new window on your desktop. This is the same as if you manually browsed to the folder using Finder (Mac OS X), Windows Explorer, or Nautilus (Linux).

Display Render Log Button
The rLog button opens the current MayaRenderLog.txt file to show the render statistics.

Diagnostics Button
The Diag button generates a Maya Diagnostics Report and saves it to your desktop. This is helpful for detecting issues with Maya and the Domemaster3D shader.
The diagnostics output is formatted in plain text format using the "markdown" syntax and can be opened in Markdown Pad / StackEdit / Notepad++ /TextWrangler / BBedit or any other plain text editor.

Task Viewer Button
This button will open the Mac OS X Activity Monitor, or the Windows Task Manager. This is useful to check the efficiency of the renderer by inspecting the memory usage and the processor utilization.

Upgrade Domemaster Node IDs button
The Upgr / "Upgrade Domemaster Node IDs" button will look in your Maya Binary scenes for any legacy latlong_lens, domeAFL_FOV, domeAFL_FOV_Stereo, or domeAFL_WxH nodes and replace them with newly created nodes using the current Node ID information from the current domeFL_FOV_Stereo.mi & latlong_lens.mi mental ray include files. The domeAFL node Extra Attributes settings will be refreshed too, along with the expressions linked dome preview shape.

Load Mental Ray Plugin Button
The Load MentalRay Plugin tool forces mental ray to reload. This can fix issues if Maya didn't startup correctly or the mental ray plugin isn't set to autoload.

Wiki Button
The Wiki Help tool loads the Domemaster Stereo Shader Wiki page in your web browser.

Version Button
The Version Info tool shows the current version number for the Domemaster Stereo Shader and provides links to the download page, and the NING group.


3DS Max Tools
-----------------
After installing the Domemaster3D shader for 3DS Max, you will find 5 new Lens shaders in the Material/Map Browser Window:
-The "Domemaster Stereo Shader" is used for fulldome stereo rendering. The center option in the domemaster stereo shader can also be used to 2D fulldome rendering.
-The "domeAFL_FOV" shader is used for 2D angular fisheye fulldome rendering.
-The "domeAFL_WxH"shader is used for 2D WxH fulldome rendering.
-The "rob_lookup_background" is used to preview screen space texture maps before attaching them to the Domemaster Stereo Shader. Screen space coordinates are required when preparing turn maps, separation maps, and tilt maps.
-The "LatLong Shader" is used to render latitude/longitude (equirectangular) images with a 360x180 degree view. These images are often rendered with a 2:1 aspect ratio.
-The "LatLong_Stereo Shader" is used to render stereoscopic 3D latitude/longitude (equirectangular) images with a 360x180 degree view. These images are often rendered with a 2:1 aspect ratio.

Softimage Notes
-------------------
Softimage provides an easy to use shader package installer format called an .xsiaddon. If you want to use the Domemaster3D shader with Softimage you can download the latest installer from the Domemaster Stereo Shader GitHub page:
https://github.com/zicher3d-org/domemaster-stereo-shader/releases


Documentation and Resources
-----------------------------------

Join the discussion on the Domemaster Stereo Shader NING Group
http://fulldome.ning.com/forum/topics/stereoscopic-domemaster-images

Downloads Page
https://github.com/zicher3d-org/domemaster-stereo-shader/releases

Domemaster Stereo Shader Wiki
https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages

Report an Issue
https://github.com/zicher3d-org/domemaster-stereo-shader/issues

Source Code:
https://github.com/zicher3d-org/domemaster-stereo-shader/


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
I would like to thank the following people for their contributions:

Ralf Habel for the 2D latlong_lens shader
http://www.vi-motion.de/latlong_Tutorial/ (Link Broken)

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

-----------------------------------------------------------------------

Version History
-----------------

Version 1.6.1
-----------------
February 4, 2015

Updated the Installer splash screen.

Maya
  Added a new "TMP" Domemaster3D shelf tool and Domemaster3D menu item that opens the operating system's %TEMP% temporary files directory.
  Updated the userSetup.py script to improve the startup procedures
  
Version 1.6
---------------
January 1, 2015

3DS Max
  Added Autodesk 3DS Max 2016 shader install option

Maya
  Added Autodesk Maya 2016 shader install option
  
  
Version 1.6 alpha 9
--------------------
December 20, 2014

3DS Max
  Updated the domeAFL_FOV_Stereo and LatLong_Stereo mental ray include files to allow for a smaller minimum zero parallax distance of 0.001 to allow for smaller camera scales.

Maya
  Added a new ramp attrPreset for latlong_Stereo shader users. The "LatLongStereoSeparation" ramp preset is a vertical gradient that is a parametric version of the latlong separation map texture that is designed to be used in conjunction with the "screen space" DomeRamp shelf button.
  
  Updated the AE template file for the DomeAFL_FOV_Stereo and LatLong_Stereo shaders so the Camera Separation control is placed next to the Dome Radius / Zero Parallax Distance controls.
  
  Updated the domeAFL_FOV_Stereo and LatLong_Stereo mental ray include files and the Maya AE template files to allow for a smaller minimum Dome Radius / Zero Parallax Distance of 0.001 to allow for smaller camera scales.

Version 1.6 alpha 8
-----------------------
December 4, 2014

Maya
  Updated the DomeViewer tool's angular360_mesh.ma model to correct for a horizontal flipping
  Updated the DomeViewer tool's latlongSphere_mesh.ma model to correct for a Maya 2012 .fc attribute loading error.
  Updated the Crossbounce tool's "dome_mib_texture_remap1" node transform matrix attributes to correct for the Y-axis view flipping issue.

Version 1.6 Alpha 7
-----------------------
November 15, 2014

3DS Max/Maya
  Updated the LatLong_Stereo.mi file to have the default camera separation value of 6.5 cm.
  
  Updated the DomeAFL_FOV_Stereo source code to optimize rendering performance by reusing common cos/sin calculations when possible.
  
Maya
  Added a new fulldome crossbounce module that simulates the effect of "crossbounce" light pollution that happens when imagery is projected across a hemispherical fulldome theatre screen.
  
  Updated the LatLongStereoRig.py script to load the control map image using the DOMEMASTER3D_SOURCEIMAGES_DIR value defined in your maya.env file.

  Added a python function to get the Domemaster3D AttrPresets folder path:
    import domeMaterial as domeMaterial
    reload(domeMaterial)
    domeMaterial.getDomePresetsPath('remapColor/ldr_to_hdr_boost_10x.mel')
    

Version 1.6 Alpha 6
-----------------------
October 28, 2014

Rebuilt the DomeAFL_FOV_Stereo.dll shader.

Version 1.6 Alpha 5
---------------------
October 24, 2014

Updated LatLong_Stereo source code for a horizontal orientation
Updated domeAFL_FOV_Stereo code to fix a bug in the Flip X/Y code
Updated Makefiles for all platforms
Recompiled latlong_Stereo, domeAFL_FOV_Stereo, and latlong_lens shaders for Mac/Windows/Linux

3DS Max Changes
  Updated 3DS Max LatLong_Stereo .dll shader file and mental ray include file

Maya Changes
  Updated the Maya.env file and MEL scripts so you can move the Domemaster3D shader for Maya to any folder location on your system including network volumes, or a non-administrative user's home folder.
  Updated Maya Domemaster3D shelf - Added a set of wide aspect ratio render resolution buttons
  Updated Maya AE Template/LatLongStereoRig.py file
  Updated DomeRender.mel script to improve PreRenderMEL & PostRenderMEL field of view scripting
  Updated the Maya Visor Example files and relinked the scene textures to use the sourceimages folder:
  C:\Program Files\Domemaster3D\sourceimages
  Added a new Maya rampShader attribute preset named "copperRampShader"


Version 1.6  Alpha 1
----------------------
September 17, 2014

Initial LatLong_Stereo support added
Updated Maya.env file to add a sourceimages path line
Updated Maya scripts so the Domemaster3D shader can be installed to any folder location by updating the Maya.env file

Version 1.5.0.2
------------------
Aug 19, 2014

Updated Task button for Linux Support.

Version 1.5.0.1
------------------
July 27, 2014

Maya Changes

  Added a "Task" shelf tool that allows you to quickly open the Mac OS X Activity Monitor, or the Windows Task Manager

  Updated the "diag" domeDiagnostics tool to profile more rendering engines, and improved the mr shader folder scanning


Version 1.5
--------------
July 12, 2014


Maya Changes

  Updated the Domemaster3D installer for Maya to place the scripts, shelves, and icons in the C:\Program Files\Domemaster3D\maya folder.

  Menu Update
    The Domemaster3D Menu (that is located in the Rendering Menu Set) has been updated to include the new tools. If you want to add the Domemaster3D menu items to your own custom shelves, it is possible to use the "Control + Shift + Menu Item Click" technique. The selected menu item will then appear in the current shelf tab and have the unique icon preset for the specific tool. Maya 2015 users will notice the Domemaster3D Menu has implemented the new `menuItem -dividerLabel` grouping system to categorize the menu items for clarity.

  Upgrade DomeAFL Node IDs
    The new "Upgr" Upgrade Domemaster Node IDs button will look in your Maya scene for any legacy node types that are latlong_lens, domeAFL_FOV, domeAFL_FOV_Stereo, or domeAFL_WxH node types and replace them with newly created nodes using the information from the current "domeFL_FOV_Stereo.mi" mental ray include file for the shader's current Node ID type. The domeAFL Extra Attributes will be refreshed too, along with the linked in dome preview shape.

  Dome Viewer Updates
    Updated the DomeViewer geometry with a new all quads based fulldome mesh.

    Added a new "time" setting for adjusting the Maya scene's frame rate.

    Updated the DomeViewer mesh UV layouts
      Angular Fisheye 360 Degree
      Fulldome 180 Degree
      Fulldome 180 Degree on 4:3 Ratio Background
      Fulldome 180 Degree on 16:9 Ratio Background
      Latitude Longitude / Equirectangular

    Changed the DomeViewer file selector filter to improve QuickTime and AVI move selection.

    Added a DomeViewer View Navigation "Reset" button and improved the imported model's scale settings.

  Added a mental ray forced plugin loading function to the domeMaterial commands that require mental ray to work. This will load the mental ray renderer when you use a command that requires it if mental ray wasn't set to to be an autostart plugin item in the plugin manager.

  Updated the DomeGrid Attribute Editor Window UI
    Added domeGrid controls to change number of sections and spans on the dome shape.

  Updated the Automagic shelf button code to apply a render time smoothing to the sphere test shape.

  Adjusted the default AA anti-aliasing quality and render settings that mental ray uses when a domeAFL_FOV, domeAFL_FOV_Stereo, domeAFL_WxH, and latlong_lens camera is added to the scene.

  Updated the code that makes sure mental ray is loaded and active before adding Domemaster3D based mental ray lens shaders to the scene.

  Updated the starglobe tool to add a remapColor node to the Starglobe mentalrayTexture shading network so you can adjust the brightness of the stars. To brighten the starts you can select the "starglobe_remapColor1" node in the Hypershade, expand the remapColor "Input and Output Ranges" section and increase/decrease the "Output Max" value. This acts as a direct multiplier to the brightness of the starglobe texture and the results are visible at render time. An Output Max value of 1 means no change, a value of 4 will make the star texture map 4X brighter, and a value of 0.5 will make the star texture map half as bright.

  Updated the domeMenu.mel script to add the new tools to the Maya Rendering set's "Domemaster3D" menu.

  Updated the Maya Domemaster3D Shelf
    The Version tool & WIKI tool URLs point at the Domemaster Stereo shader page on GitHub

    New Color Image Sequence Material" tool added.

    New "FulldomeIBL" tool added

    New "HemirectIBL" tool added.

    New "rLog" button opens the current MayaRenderLog.txt file.

    New "Histogram" image analysis tool added.

    New "Diag" button generates a Maya Diagnostics Report and saves it to your desktop. 

  * * *

  Changed the openGL viewport default focal length from 4 mm (160 degree FOV) to 18 mm (90 degree FOV)

  * * *

  The following Maya attribute presets have been added:

  domeAFL_FOV_Stereo
    Large_Hyperstereo_Depth_65cm_Separation
    Normal_Depth_6.5cm_Separation
    Small_Macro_Scale_Depth_0.65cm_Separation

  gammaCorrect
    gamma_1_correction
    gamma_dot_4545_correction

  Note: This preset is helpful when using a gamma correct node to adjust a file texture, or color swatch for proper linear workflow (in Maya versions prior to Maya 2015). It applies a .4545 gamma correction to a color swatch or a non linear workflow gamma corrected texture like an 8-bit PNG, TIFF or JPEG image. You would connect the gamma correct node between the surface material and the texture map. For gamma corrected color swatches you would connect the gamma correct node to a surface material and the gamma nodes' color swatch would be used with the .4545 gamma value being applied at render time.

  mib_texture_remap
    angular_180_degree_remap
    angular_220_degree_remap
    angular_270_degree_remap
    angular_360_degree_remap
    hemirect_360x090_degree_remap
    hemirect_360x110_degree_remap
    hemirect_360x135_degree_remap
    hemirect_360x180_degree_remap
    regular_mapping

  Note: If you want to adjust the "FulldomeIBL" or "HemirectIBL" shelf tool to work with footage with different FOVs you can select the "mib_texture_remap" node in the Hypershade and apply one of the presets in the attribute editor window.

  When you apply the "mib_texture_remap" texture presets the IBL texture maps will appear flipped due to an inside vs outside view issue that is common in the Maya mental ray IBL shape node. You can correct the environment map direction by typing a "-1" value into the first field in the mib_texture_remap node's transform matrix cell grid.

  mib_texture_vector
    screen_space
    uv_texture_space

  pfxToon
    wireframeGridToon

  Note: wireframeGridToon is a simple preset that applies a wireframe style shader outline to a polygon mesh using the paintFX toon shader system. This can be used to render a fulldome compatible wireframe shape with the DomeAFL_FOV shader.

  remapColor
    regular_settings
    ldr_to_hdr_boost_05x
    ldr_to_hdr_boost_10x
    ldr_to_hdr_boost_15x
    ldr_to_hdr_boost_20x
    ldr_to_hdr_boost_25x
    ldr_to_hdr_boost_30x

  Note: If you have an 8-bit style PNG/JPEG/TGA/TIFF/IFF texture map or image sequence that you want to use as a final gather or light emission material you can use a remapColor node to boost the highlights.

  These presets will let you use the brightest areas in the low dynamic range image as the light sources. The ldr_to_hdr_boost presets will take the bright areas in the image that are at least 96% bright ( a 244+ value in a 0-255 color range, or a 0.96 value in a float range) and boost them dramatically. As far as the preset naming goes, the ldr_to_hdr_boost_15x preset will boost the maximum image value by 15 times which means a value of 1 in the float color range will be boosted to 15.0.

  If the ldr_to_hdr_boost preset doesn't make the scene bright enough for light emission you can change expand the remapColor nodes' Input and Output Ranges section and change the Output Max value higher. The Output Max control is a direct multiplier on the image brightness.

  To apply a remapColor node to an environment texture like the ones used in the FulldomeIBL and HemirectIBL tools you can place the remapColor node between the mib_texture_lookup.OutValue and the mentalrayIblShape1.color attributes.

  surfaceShader
    safe_viewing_zone_blue
    zero_parallax_orange

  viewColorManager
    linearWorkflow
    sRGB_workflow

  Note: You can apply the "viewColorManager" presets by opening the Render Window, then select the "Display > Color Management..." menu item. In the viewColorManager Attribute Editor window select the Presets button and choose the linearWorkflow or sRGB_workflow entries.

  The "linearWorkflow" preset sets the Render View's Color Management settings to "Linear" for the rendered image's color input profile and "sRGB" as the display profile. This will make it easier to view 16 bit half float EXR renders correctly in the Render View.

  The "sRGB_workflow" preset sets the Render View's Color Management settings to "sRGB" for the rendered image's color input profile and "sRGB" as the display profile. This will make it easier to view 8-bit style output PNG/JPEG/IFF renders correctly in the Render View.
  

  * * *

The Domemaster3D shader folder now has the following directory structure:

  The domeAFL mental ray shader files are stored in the following folders:
  C:\Program Files\Domemaster3D\maya\shaders
  C:\Program Files\Domemaster3D\maya\shaders\include

  The Maya files for the Domemaster3D shader are stored using the following hierarchy:

  The Maya and Max supporting images and meshes are stored in the folder:
  C:\Program Files\Domemaster3D\sourceimages

  The new "all quads" based fulldome mesh is located at:
  C:\Program Files\Domemaster3D\sourceimages\fulldome_quads_mesh.ma
  C:\Program Files\Domemaster3D\sourceimages\fulldome_quads_mesh.obj

  There is a version of the "all quads" fulldome mesh that has the UV space adjusted for fulldome video texture maps that have been composited over a 4:3 ratio and 16:9 ratio background. These were included for the DomeViewer tool so it would be possible to playback fulldome footage that was composited into a 1280x720 or 1920x1080 frame size.

  C:\Program Files\Domemaster3D\sourceimages\fulldome_quads_4_3_mesh.ma
  C:\Program Files\Domemaster3D\sourceimages\fulldome_quads_16_9_mesh.ma

  C:\Program Files\Domemaster3D\sourceimages\fulldome_quads_4_3_mesh.obj
  C:\Program Files\Domemaster3D\sourceimages\fulldome_quads_16_9_mesh.obj


Version 1.4 Beta 10 Changes
-------------------------------
Dec 27, 2013

Added the latlong_lens shader for rendering spherical/equirectangular imagery.

DomeViewer
  Added Double sided rendering controls

Version 1.4 Beta 9 Changes
------------------------------
Dec 9, 2013

3DS Max Changes
--------------------
Updated the 3DS Max Starglobe files to fix rendering issues. The new 3DS Max scenes are stored in the folder:
C:\Program Files\Domemaster3D\sourceimages

Added install option for 3DS Max 2015 (beta) support

Maya Changes
----------------
Added an install option for Maya 2015 (beta) support

Updated the Galaxy Creator, Starglobe, DomeText, and DomeViewer window's so the window settings are restored from the last setting. This allows the docked vs floating, and docked left/right window settings to be remembered.

Changed the default for the domeAFL_FOV and domeAFL_FOV_Stereo node's preview shape to the wireframe rendering mode.

Changed the default particle type setting for the Galaxy Creator GUI to MultiPoint particles.


Improved Linux Compatibility
The Domemaster3D shader files on Linux are installed to the folder: /opt/Domemaster3D/

Updated the mental ray lens shader's linux x64 makefile

Compiled a new linux x64 mental ray lens shader build of domeAFL_FOV_Stereo.so"

Updated the DomeText tool to scan the linux font folders at: /usr/share/fonts/


DomeViewer Update
Added support for previewing textures in the quadsphere (starglobe) mesh projection to the DomeViewer.

Added a "Flip the Panoramic Image" checkbox that causes a mirror effect on the panoramic image by flipping the panoramic texture so you are viewing the texture map as if it was an environmental reflection map viewed from the outside. This effect is done by scaling the domeViewer shape (scaleX * -1).

DomeText Update
Rewrote the Linux DomeText font scanning to scan through each of the font folders located in the linux font path: /usr/share/fonts/

Improved the Mac OS X DomeText font scanning. Fonts that are installed in the /Library/Fonts, /System/Library/Fonts, and ~/Library/Fonts folders are now added to the font menu list. The font folder path is added so it is possible to know which version of a font is selected.


Version 1.4 Beta 8 Changes
------------------------------
Nov 20, 2013

Maya Changes
----------------
Added a set of Maya shelf tools to change the render resolution.

Added a 16x8k equirectangular starglobe texture "starglobe_equirect_reversed_16x8k.jpg" to the sourceimages folder. This texture has been reversed for the view "inside" the night sky environment.

This release adds the DomeViewer tool, the DomeText tool, and a lot of other improvements to the Mac OS X release.

If you are interested in using the DomeText tool on Mac OS X, the ImageMagick library has to be downloaded separately. This ImageMagick library is available from:
http://www.imagemagick.org/script/binary-releases.php#macosx


Version 1.4 Beta 7 Changes
------------------------------
Nov 8, 2013

Maya Changes
----------------
Added Maya shelf tool to force the Mental Ray plugin to load. This is useful if Mental Ray didn't start-up automatically.

Improved the DomeViewer cylindrical, mirrorball, and angular360 degree meshes.

Maya + 3DS Max
-------------------
Updated the Starglobe texture maps. The previous version had the starglobe 2K and 8K quadsphere texture direction inverted.


Version 1.4 Beta 6 Changes
------------------------------
Oct 27, 2013

Maya Changes
----------------

DomeViewer
  Added cylindrical panorama support to the domeViewer
  Added a new 360 angular fisheye, and mirrorball mesh
  Improved transparency support on the grid overlay
  Added image exposure and color tint controls

DomeText
  Added wrapU and wrapV attributes to the GUI. (It is now easier to create scrolling credits by setting the auto scroll direction to "scroll up" and un-checking the WrapV checkbox.)
  Updated the text mirror controls

Updated the DomeGrid default settings.

Added code to detect if the Domemaster3D shader is running in GUI mode or batch mode. This will skip running the userSetup.py code for adding a custom menu when running in batch mode. 

Improved Maya 2010 support
  Updated the domeStereoRig.py camera rig file for Maya 2010 support.
  Improved the dome_AFL_FOV_Stereo GUI code for Maya 2010 support .
  Updated the Domemaster3D menu system for stereo rig support in Maya 2010.
  Updated the starglobe GUI window for Maya 2010 support.
  Updated the Maya Shelf files.

Version 1.4 Beta 5 Changes
------------------------------
Oct 24, 2013

Maya Changes
-----------------

Updated the domeAFL_FOV_Stereo camera preview code to fix a bug that stopped batch rendering from completing with the new domeRender.mel script.


Version 1.4 Beta 4 Changes
------------------------------

Oct 21, 2013

Maya Changes
-----------------

DomeAFL_FOV_Stereo 
  Now with a real-time OpenGL Stereo3D preview viewport using 4mm wide angle (non-fisheye) hardware rendering
  Added a custom preRender and postRender mel script called domeRender.mel
  The domeRender.mel script allows the Maya stereo camera rig + domeAFL_FOV_Stereo shader to display a realtime anaglyph 3D preview in the viewport. The openGL display mode shows a stereo3D version of the scene with the current camera separation, and dome radius (zero parallax values) and a 4 mm wide angle (non-fisheye) field of view.
  The domeRender.mel script also adjusts the domemaster3D camera rig's internal "shape node" focal length to solve the blurry line artifact with a toggle between 4mm FOV in the viewport and 500mm FOV at render time.
  
Dome Viewer
  Added a fulldome and panoramic image+movie viewer. The viewer supports all image and movie formats that can be opened using the Maya File Texture and Movie Nodes. You can display immersive images, image sequences, and movie files with accelerated RAM playback. Tilted fulldome theater screens can be simulated with the "Dome Tilt" attribute.
    
  A Bradbury alignment grid has been included for previewing calibrated fulldome scenes.

  The following panoramic viewing modes are supported:
    180 Degree Fulldome
    360 Degree Angular Fisheye*
    Mirror Ball*
    Equirectangular (LatLong)
    Cube Map 3x2
    Vertical Cross Cube
    Horizontal Cross Cube
    Vertical Tee Cube
    Horizontal Tee Cube
    Vertical Strip Cube
    Horizontal Strip Cube
    Mental Ray Horizontal Strip Cube

  Note: *The 360 Degree Angular Fisheye and Mirror Ball panorama modes still need some work.

Starglobe Updates
  Updated the Starglobe tool so the "Attach to Camera" menu uses the base camera name like 'persp' instead of the camera's shape node name like 'perspShape1'.

Dome Text Upgrades
  Added 93 international character encoding formats
  Added DomeText aim constraints
  Added Cylinder geometry support
  Added Lambert material support
  Added text animation features for automatic left/right/up/down scrolling text
  Changed the caption for the Copy Node Settings menu to "Copy Text Settings From"
  Added folder icon to Save Image As field
  Added Flip Text Direction control for horizontal text mirroring on a plane or cylinder surface
  Added controls for converting characters to:
    Upper Case
    Lower Case
    Hex Words
    Hex Single Column
    Binary Words
    Binary Single Column

Galaxy Creator
 Changed the caption for the Copy Node Settings menu to "Copy Particle Settings From"
 
Updated userSetup.py script for better compatibility with mentalCore. The code to auto-reload the mental ray plugin "Mayatomr" at startup has been commented out.

Version 1.4 Beta 2 Changes
---------------------------------
Oct 6, 2013

3DS Max Changes
---------------------

Starglobe Update
I've created a few different format starglobe models to make it easier for 3DS MAX users. The files are stored in the C:\Program Files\Domemaster3D\sourceimages folder.

There is a set of 2K and 8K texture resolution 3DS Max scene files: starglobe_mesh_2K.max, and starglobe_mesh_8K.max
There is a set of 2K and 8K texture resolution FBX scene files: starglobe_mesh_2K.fbx, and starglobe_mesh_8K.fbx (You may have to flip the surface normals on the mesh for proper Max based rendering)
There is a set of 2K and 8K texture resolution OBJ scene files: starglobe_mesh_2K.obj, and starglobe_mesh_8K.obj 

Maya Changes
-----------------

Updated Domemaster3D Shelf icons to a unified golden orange color palette

Added a Domemaster3D Menu to the rendering menu set

Added the DomeText GUI tool for creating fulldome titles in Maya. This tool is powered by the ImageMagick convert.exe utility which is stored in the Domemaster3D/bin folder. The tool uses the active fonts installed in the system's font folder. Note: When the "Transparent background" checkbox is enabled the rendered text has crisp anti-aliased edges in the alpha channel but the text color channels are rendered with hard edges to avoid black fringing due to alpha channel pre-multiplication.

The Galaxy Creator and DomeText user interfaces are dockable windows when used with Maya 2011 and higher.

Added a starglobe tool to the Maya shelf and Domemaster3D menu. The starglobe tool creates a night sky backdrop. The tool has a new GUI that lets you point constrain the starglobe mesh to any camera in your scene. The starglobe textures and the starglobe spherical model are stored in the Domemaster3D/sourceimages folder.

Added an in-scene DomeAFL and DomeAFL_FOV_Stereo preview geometry shape. The preview shape displays the camera's field of view and can be displayed as a wireframe, shaded, or wireframe on shaded surface. In the DomeAFL_FOV_Stereo shader the shape's size is linked to the Dome Radius control to preview the stereoscopic zero parallax zone setting. The double sided shading controls let you choose how the surface is displayed with either both sides shaded, or only the inside or outside visible.

Added scene scale detection for setting the default domeAFL_FOV_Stereo dome radius and camera separation values based upon your current Maya scene scale [cm / meter / km / inch / foot / mile].

Added a custom fulldome stereo rig preset to the Maya StereoRigEditor. This allows a new fulldome 3D rig to be created by going to the Menu Create  > Cameras > Stereo Camera (DomeStereoCamera)

Added a userSetup.py script to handle the installation of the Domemaster3D menu and the addition of the camera rig to the StereoRigEditor list.

The default stereo rig can now be changed between the normal Maya stereo rig and the Domemaster3D rig by switching to the Rendering Menu set. From the Domemaster3D menu, select Dome Cameras > Choose a Default Stereo Rig > ... 

Renamed several of the MEL and python scripts for improved clarity

Updated the Galaxy Creator GUI
  Added elliptical galaxy support with radial and transverse orbits
  Added Galaxy Rotation attribute
  Added MultiPoint and MultiStreak particle rendering controls
  Added popup help captions for each of the attributes.
  Added a copy node settings option to reuse existing galaxy creation settings
  Added a "Open the Hardware Render Buffer window" button and hardware rendering presets

Added customized AE Template files for the domeAFL_FOV, domeAFL_WxH, and rob_lookup_background shaders.
  
Added the panotools based mpremap.exe application to the Domemaster3D/bin folder so textures could be remapped to different panoramic formats.

Version 1.3.5 Changes
---------------------------

Included an .obj mesh and a starglobe texture map for 3DS Max users.

Added a starglobe tool to the Maya shelf to create a night sky backdrop. The starglobe textures are stored in the Domemaster3D/sourceimages folder and the starglobe spherical model is stored in the Domemaster3D/models folder.

Upgraded the Maya dome shaders to use the mia_material_x_passes shader

Added Glow Intensity attributes to the Galaxy Creator GUI 

Version 1.3.4
---------------------------
Released June 27, 2013

Updated the the Automagic tool's dome grid color to a brighter yellow value. This makes the grid more visible in a Physical Sun & Sky scene.

Added a new HELP icon to the Maya Shelf toolset. This shelf item loads the domemaster stereo shader wiki page.


Version 1.3.3
---------------------------
Released May 30, 2013

Created the new Galaxies Creator user interface for Martin Watt's classic galaxies.mel script.

Updated the DomeRamp tool so the default ramp style is applied if the tool is run multiple times

Updated sourceimages path variables for Maya 2010 compatibility

Added a Maya Camera Locator Scale attribute to the dome cameras created using the shelf tools.

Updated the Domemaster3D Installer to support custom path selection for the 3DS Max mental ray shader and include folders.

Version 1.3.2
---------------------------
Released  April 16, 2013
Updated domemaster mental ray include file for improved 3DS Max GUI layout.

Added Maya 2014 support

The Maya camera connections for the lens shaders have been updated

The location of the default domemaster control map textures is now in the C:\Program Files\Domemaster3D\sourceimages folder on Windows or the /Applications/Domemaster3D/sourceimages folder on Mac OS X. The Domemaster3D shelf tools have been updated to automatically link to the new sourceimages folder.

There is a fix for the issue where the mental ray physical sky & sun system will overwrite existing connections to the .miLensShader port. The physical sky & sun system will now use the miLensShaderList[0] connection on a camera.


Version 1.3
---------------------------
Released Nov 4, 2012
Changed the DomeAFL_FOV and DomeADL_WxH source code to match the view orientation of the camera and the domemaster stereo lens shader. Recompiled the Domemaster3D Mac / Windows mental ray shaders.

Added a python script for creating a domeAFL compatible mia_material shading network. This should solve the typical "blurry grey line" texture sampling artifact that happens near the spring line.

Changed the default lens shader connections in the python scripts to support the mental ray sky and sun system.


Version 1.2.1
---------------------------
Released Aug 14, 2012
Added a Maya 2010 shelf and improved the python script. Created XPM formatted icons for the Domemaster3D shelf, create bar, and Hypershade nodes for Maya 2010 backwards compatibility.


Version 1.2
---------------------------
Released Aug 8, 2012
Added a Domemaster3D shelf, enabled domeAFL_FOV_Stereo FlipX/FlipY options, created a python stereo rig setup script, added an automatic screen space file texture and ramp texture script


Version 1.1
---------------------------
Released July 28, 2012
Added Maya stereo camera rig example, Linux Build + Makefile, new shader icons


Version 1.0
---------------------------
Released April 18, 2012

Initial version of the Domemaster3D shader for Maya

