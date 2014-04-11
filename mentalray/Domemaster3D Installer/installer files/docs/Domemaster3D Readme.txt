Domemaster3D Stereo Lens Shader for Maya x64 and 3DS Max x64
Version 1.5 - March 15, 2014

About This Shader
---------------------
The Domemaster Stereo lens shader is a custom mental ray shader that creates a stereoscopic 3D fisheye image. The lens shader provides advanced controls to optimize the viewing experience for stereoscopic dome renderings. 

The shader collection also supports fulldome 2D rendering using either the DomeAFL_FOV shader, the DomeAFL_WxH shader, or the "Center" camera option in the DomeAFL_FOV_Stereo shader. Latitude Longitude rendering (also known as spherical or equirectangular output) is supported with the help of the latlong_lens shader.

The Maya Domemaster3D shelf has buttons for the following features:

-The "AutoMagic" tool creates a Domemaster3D fulldome stereo camera rig and a hemispherical yellow wireframe test scene
-The "Stereo Rig" tool creates a standard Domemaster3D stereo camera rig
-The "Dome Texture" tool creates a screen space file texture
-The "DomeRamp" tool creates a screen space ramp texture
-The "DomeAFL_FOV" tool creates a standard 2D domeAFL_FOV node + camera
-The "DomeAFL_WxH" tool creates a standard 2D domeAFL_WxH node + camera
-The "LatLong" tool creates a 2D latlong_lens node + camera
-The "Color Material" tool creates a mia_material based mental ray shading network with support for color file textures.
-The "Color + Bump Material" tool creates a mia_material based mental ray shading network with support for color and bump file textures.
-The "Starglobe" tool creates a mia_material_x_passes based starry background for your fulldome scenes.
-The "DomeGrid" tool creates a hemispherical yellow wireframe reference grid.
-The "Galaxy Creator" tool creates dynamic particle based galaxies.
-The "DomeText" tool created raster titles and scrolling credits using the Dome Text GUI and ImageMagick.
-The "Viewer" tool creates an immersive fulldome and panoramic image+movie viewer.
-The "Load MentalRay Plugin" tool forces mental ray to reload. This can fix issues if Maya didn't startup correctly.
-The "Wiki Help" tool loads the Domemaster Stereo Shader Wiki page in your web browser.
-The "Version Info" tool shows the current version number for the Domemaster Stereo Shader and provides links to the download page, and the NING group.
-The "0.5k" button sets the render resolution to 512x512 pixels.
-The "1k" button sets the render resolution to 1024x1024 pixels.
-The "2k" button sets the render resolution to 2048x2048 pixels.
-The "4k" button sets the render resolution to 4096x4096 pixels.
-The "8k" button sets the render resolution to 8192x8192 pixels.

3DS Max Tools
---------------
After installing the Domemaster3D shader for 3DS Max, you will find 4 new Lens shaders in the Material/Map Browser Window:
-The "Domemaster Stereo Shader" is used for fulldome stereo rendering. The center option in the domemaster stereo shader can also be used to 2D fulldome rendering.
-The "domeAFL_FOV" shader is used for 2D angular fisheye fulldome rendering.
-The "domeAFL_WxH"shader is used for 2D WxH fulldome rendering.
-The "rob_lookup_background" is used to preview screen space texture maps before attaching them to the Domemaster Stereo Shader. Screen space coordinates are required when preparing turn maps, separation maps, and tilt maps.


Softimage Notes
----------------
Softimage provides an easy to use shader package installer format called an .xsiaddon. If you want to use the Domemaster3D shader with Softimage you can download the latest installer from the Domemaster Stereo Shader Google Code page:
http://code.google.com/p/domemaster-stereo-shader/


Documentation and Resources
----------------------------

Domemaster Stereo Shader Wiki
http://code.google.com/p/domemaster-stereo-shader/w/list

Join the discussion on the Domemaster Stereo Shader NING Group
http://fulldome.ning.com/forum/topics/stereoscopic-domemaster-images

Source Code:
http://code.google.com/p/domemaster-stereo-shader/


Project Developers
-------------------

Domemaster Stereo Shader for 3DS Max Created by Roberto Ziche
http://www.robertoziche.com/

Domemaster3D shader for Maya and Softimage by Andrew Hazelden
andrew@andrewhazelden.com      
http://www.andrewhazelden.com/blog

Based upon Daniel Ott's DomeAFL Angular Fisheye Lens Shader
http://www.thedott.net/shaders/domeAFL/

Special Thanks
-----------------
I would like to thank the following people for their contributions:

Ralf Habel for the latlong_lens shader
http://www.vi-motion.de/latlong_Tutorial/

Aaron Bradbury for the installer imagery from his Vortex fulldome short film.
http://www.luniere.com/project/vortex/

Aaron Bradbury for the inclusion of the fulldome alignment grid:
http://www.luniere.com/2013/03/07/hi-res-fulldome-alignment-grid/

Jason Fletcher for creating a high quality equirectangular starglobe texture.
http://thefulldomeblog.com/2013/06/22/stars-to-surround-the-scene/

Martin Watt for writing the original galaxies.mel script.


-----------------------------------------------------------------------

Version History
-----------------

Version 1.5
--------------
March 15, 2014

Updated the DomeViewer mesh UV layouts
  Angular Fisheye 360 Degree
  Fulldome 180 Degree
  Latitude Longitude / Equirectangular

Changed the DomeViewer file selector filter to improve QuickTime and AVI move selection.

Updated the DomeGrid Attribute Editor Window UI
  Added domeGrid controls to change number of sections and spans on the dome shape.

Updated the Maya Domemaster3D Shelf's Version tool. The "Update" button URL now points to Google Drive.

Changed the openGL viewport default focal length from 4 mm (160 degree FOV) to 18 mm (90 degree FOV)

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


Installation Instructions
-------------------------

Maya on Windows
---------------

1. Unzip the domemaster3D.zip archive.

2. Copy the appropriate "domeAFL_FOV_Stereo.dll" file from either the "Windows 32-bit LIB" or "Windows 64-bit LIB" folder or to your mental ray LIB folder:
On Maya 2012:
C:\Program Files\Autodesk\Maya2012\mentalray\lib\

On Maya 2013:
C:\Program Files\Autodesk\Maya2013\mentalray\shaders\

If you are running a 32-bit version of Maya install the 32-bit DLL. If you are running a 64-bit version of Maya install the 64-bit DLL.


3. Copy the "domeAFL_FOV_Stereo.mi" mental ray include file to:
On Maya 2012:
C:\Program Files\Autodesk\Maya2012\mentalray\include\

On Maya 2013:
C:\Program Files\Autodesk\Maya2012\mentalray\shaders\include 

4. Copy the Maya AE Template file "AEdomeAFL_FOV_StereoTemplate.mel" to either the Maya AETemplates folder or to your user account's Maya script folder:

C:\Program Files\Autodesk\Maya2012\scripts\AETemplates\
or
My Documents\maya\2012\prefs\scripts


5. Copy the python and MEL scripts to your user account's Maya script folder:
My Documents\maya\2012\prefs\scripts

6. Copy the "shelf_Domemaster3D.mel" file from the "shelves" folder to your user account's Maya shelves folder:
My Documents\maya\2012\prefs\shelves

7. Copy the Hypershade icons from the "Icons" folder to your Maya icons directory or to your user account's Maya icons directory:
C:\Program Files\Autodesk\Maya2012\icons\
or
My Documents\maya\2012\prefs\icons\

8. Copy the textures from the "sourceimages" folder to your current project's sourceimage directory. 

The textures "checker.iff" and "bumpChecker.iff" are the default file textures applied when the Color Material or Color + bump material shelf icons are run. 

The head_tilt_map, separation_map, and turn_map textures are used to set up the DomeAFL_FOV_Stereo rig.

9. The next time you start Maya you will find the "domeAFL_FOV_Stereo", "domeAFL_FOV", "domeAFL_WxH", and "rob_lookup_background" lens shaders in the Hypershade. Look in the create bar under the mental ray > lenses section.



Maya on Mac OS X
---------------
This version of the domeAFL_FOV_Stereo shader mental ray shader was compiled for Maya 2011 and 2012 for Mac OS X 64-bit. Mac OS X 10.6 Snow Leopard is required.

1. Unzip the domemaster3D.zip archive.

2. Copy domeAFL_FOV_Stereo.dylib file from the "Mac OS X 64-bit LIB" folder to the mentalray lib directory:
On Maya 2012:
/Applications/Autodesk/maya2012/Maya.app/Contents/mentalray/lib/

If you want to go inside the Maya.app package, right click on Maya.app and select "Show Package Contents" from the contextual menu.

On Maya 2013:
/Applications/Autodesk/maya2013/mentalray/shaders/


3. Copy the "domeAFL_FOV_Stereo.mi" mental ray include file to:
On Maya 2012:
/Applications/Autodesk/maya2012/Maya.app/Contents/mentalray/include

On Maya 2013:
/Applications/Autodesk/maya2013/mentalray/shaders/include

4. Copy the Maya AE Template file "AEdomeAFL_FOV_StereoTemplate.mel" to either the Maya AETemplates folder or to your user account's Maya script folder:
/Applications/Autodesk/maya2012/Maya.app/Contents/scripts/AETemplates/
or
~/Library/Preferences/Autodesk/maya/2012-x64/prefs/scripts

5. Copy the python and MEL scripts to your user account's Maya script folder:
~/Library/Preferences/Autodesk/maya/2012-x64/prefs/scripts

6. Copy the "shelf_Domemaster3D.mel" file from the "shelves" folder to your user account's Maya shelves folder:
~/Library/Preferences/Autodesk/maya/2012-x64/prefs/shelves

7. Copy the Hypershade icons from the "Icons" folder to your Maya icons directory or to your user account's Maya icons directory:
~/Library/Preferences/Autodesk/maya/2012-x64/prefs/icons

8. Copy the textures from the "sourceimages" folder to your current project's sourceimage directory. 

The textures "checker.iff" and "bumpChecker.iff" are the default file textures applied when the Color Material or Color + bump material shelf icons are run. 

The head_tilt_map, separation_map, and turn_map textures are used to set up the DomeAFL_FOV_Stereo rig.

9. The next time you start Maya you will find the "domeAFL_FOV_Stereo", "domeAFL_FOV", "domeAFL_WxH", and "rob_lookup_background" lens shaders in the Hypershade. Look in the create bar under the mental ray > lenses section.


Maya on Linux
---------------
This version of the domeAFL_FOV_Stereo shader mental ray shader was compiled for Maya 64-bit on RHEL 6.2.

1. Unzip the domemaster3D.zip archive.

2. Copy domeAFL_FOV_Stereo.so file from the "Linux X 64-bit LIB" folder to the mentalray lib directory:
On Maya 2012:
/usr/autodesk/maya2012-x64/mentalray/lib

On Maya 2013:
/usr/autodesk/maya2013-x64/mentalray/shaders/


3. Copy the "domeAFL_FOV_Stereo.mi" mental ray include file to:

On Maya 2012:
/usr/autodesk/maya2012-x64/mentalray/include

On Maya 2013:
/usr/autodesk/maya2013-x64/mentalray/shaders/include

4. Copy the Maya AE Template files to either the Maya AETemplates folder or to your user account's Maya script folder:
/usr/autodesk/maya2012-x64/scripts/AETemplates/
or
~/maya/2012-x64/prefs/scripts


5. Copy the python and MEL scripts to the Maya script folder:
/usr/autodesk/maya2012-x64/scripts
or
~/maya/2012-x64/prefs/scripts



6. Copy the "shelf_Domemaster3D.mel" file from the "shelves" folder to your user account's Maya shelves folder:
~/maya/2012-x64/prefs/shelves

7. Copy the Hypershade icons from the "Icons" folder to your Maya icons directory or to your user account's Maya icons directory:
/usr/autodesk/maya2012-x64/prefs/icons

8. Copy the textures from the "sourceimages" folder to your current project's sourceimage directory. 

The textures "checker.iff" and "bumpChecker.iff" are the default file textures applied when the Color Material or Color + bump material shelf icons are run. 

The head_tilt_map, separation_map, and turn_map textures are used to set up the DomeAFL_FOV_Stereo rig.

9. The next time you start Maya you will find the "domeAFL_FOV_Stereo", "domeAFL_FOV", "domeAFL_WxH", and "rob_lookup_background" lens shaders in the Hypershade. Look in the create bar under the mental ray > lenses section.



3D Studio Max
--------------

1. Unzip the domemaster3D.zip archive.

2. Copy the appropriate "domeAFL_FOV_Stereo.dll" file from either the "Windows 32-bit LIB" or "Windows 64-bit LIB" folder or to your mental ray shaders folder:
\mentalray\shaders_autoload\shaders

If you are running a 32-bit version of 3D Studio Max install the 32-bit DLL. If you are running a 64-bit version of 3D Studio Max install the 64-bit DLL.


3. Copy the "domeAFL_FOV_Stereo.mi" mental ray include file to:
\mentalray\shaders_autoload\include

When you start 3D Studio Max, you will have 4 new Lens shaders:
"Domemaster Stereo Shader"
"domeAFL_FOV"
"domeAFL_WxH"
"rob_lookup_background"


