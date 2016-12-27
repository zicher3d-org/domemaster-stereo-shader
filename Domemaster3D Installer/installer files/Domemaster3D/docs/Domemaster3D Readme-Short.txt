Domemaster3D Stereo Lens Shader for Maya x64 and 3DS Max x64
Version 2.2.1 - December 27, 2016

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

macOS:
/Applications/Domemaster3D/

Linux:
/opt/Domemaster3D/


Windows Notes
-------------------
The Domemaster3D v2.2 mental ray and Arnold release for Windows was compiled with Visual Studio 2012. If your system doesn't have the Visual Studio 2012 (VC++ 11.0) x64 Redistributable Package installed you can download it here: 
http://www.microsoft.com/en-us/download/details.aspx?id=30679

You can also find a copy of the Visual Studio 2012 (VC++ 11.0) x64 installer in the Domemaster3D "bin" folder at:
C:/Program Files/Domemaster3D/bin/vcredist_2012_vc11_x64.exe

The Domemaster3D v2.2 for Vray release for Windows was compiled using Visual Studio 2013. If your system doesn't have the Visual Studio 2013 Visual C++ Redistributable Package installed you can download it here:
https://www.microsoft.com/en-us/download/details.aspx?id=40784

You can also find a copy of the Visual Studio 2013 (VC++ 12.0) x64 installer in the Domemaster3D "bin" folder at:
C:/Program Files/Domemaster3D/bin/vcredist_2013_vc12_x64.exe

macOS Notes
----------
The minimum macOS version required to run the compiled versions of the Domemaster3D mental ray shaders is now macOS 10.9 due to the version of Xcode used to compile the current .dylib library files. 

If you need support for older versions of macOS, you can compile the shaders locally on a legacy macOS system using the included Makefiles and the shaders will run on systems as old as macOS 10.6.

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

Version 2.2.1
-----------------
2016-12-27

Installer

  Added new entries in the Domemaster3D installer for using the lens shaders with V-Ray for 3ds Max 2014-2017, Arnold for Cinema4D R16-R18, and mental ray 3.14 standalone for Maya 2016-2017.
  
Maya DomeViewer
  
  Updated the DomeViewer tool to add support for viewing stereoscopic 360° imagery. You can now set the Stereo Format control to "None - Mono 2D", "Side by Side Stereo", "Over Under Stereo", and "Stereo Image Pair". The Stereo Display control can be set to "Full Color Anaglyph", "Luminance Anaglyph", "Freeview (Parallel)", "Freeview (Crossed)", "Horizontal Interlace", "Checkerboard", "Center Eye", "Left Eye", and "Right Eye".
  
  Renamed the DomeViewer "Gear VR Mono Cube" Panoramic Format to "Gear VR Cube"
  
  Edited the DomeViewer tool to add support for the "Facebook Vertical Strip Cube" Panoramic Format 
  
  Fixed a DomeViewer "LG360" Panoramic Format preview icon loading issue
  
Arnold MaxtoA for 3ds Max Beta

  Started developing the Arnold MaxtoA for 3ds Max 2017 shaders by edited the metadata file to add a "max.category" entry for each of the shaders, and created custom Maxscript .ms based scripted controller files.

V-Ray for Max

  Compiled new V-Ray 3.4 for 3ds Max 3014, 2016, and 2017 lens shaders builds using Visual Studio 2013 Community Edition.

Version 2.2
-------------
2016-12-09

Installer

  Added new entries in the Domemaster3D installer for using the lens shaders V-Ray for Max, Arnold for Maya, and Arnold for Cinema4D.

Maya + Max

  A copy of the Windows based Visual Studio 2012 (vcredist_2012_vc11_x64.exe) and Visual Studio 2013 (vcredist_2013_vc12_x64.exe) Redistributable Package x64 installers are now included with Domemaster3D. These resources are accessible in the Domemaster3D "bin" folder: C:/Program Files/Domemaster3D/bin/
  
Maya

  Improved macOS Gatekeeper security by digitally signing the macOS .so lens shader files with:
  
    Apple Developer ID Application: Andrew Hazelden (7B24U9536W)
    
  Updated the Dome Text ImageMagick macOS support to include the homebrew provided program path of:
  
    /usr/local/bin/convert
  
  Updated the Dome Histogram ImageMagick macOS support to include the homebrew provided program path of:
  
    /usr/local/bin/convert

  Updated the wording of "Mac OS X" in the code and documentation to the newer "macOS" style.

mental ray for Maya

  The Domemaster3D lens shaders now officially work with the new mental ray 3.14 release.

Arnold for Maya

  Improved macOS Gatekeeper security by digitally signing the macOS .so lens shader files with:
  
    Apple Developer ID Application: Andrew Hazelden (7B24U9536W)

V-Ray for Maya

  Improved macOS Gatekeeper security by digitally signing the macOS .so lens shader files with:
  
    Apple Developer ID Application: Andrew Hazelden (7B24U9536W)
  
  Updated the Automagic DomemasterStereo and LatLongStereo shelf buttons to include a line of Python code to turn the Vray Frame Buffer off by default so the Maya Render View will show the stereo result.

  Updated the Domemaster3D for Vray installation instructions on the GitHub Wiki to include instructions on the new module based installation approach:
  
  https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/Vray-for-Maya-Domemaster3D

Version 2.1.4
-------------
2016-11-03

Maya + Max
  New Domemaster3D installer packaged.

Version 2.1.3
-------------
2016-10-04

Maya
	Recompiled the mental ray 3.14 for macOS versions of the lens shaders that are capable of working with Maya 2016/2016.5/2017. The newly compiled mental ray 3.14 lens shaders work with macOS 10.9+ Mavericks.
	
Version 2.1.2
-------------
2016-09-17

Arnold
  Updated the Maya based "Arnold Domemaster3D" menu and shelf to add 2D rendering style entries for creating Domemaster FOV 2D and LatLong 2D renderings using the center camera view in the existing stereo lens shaders.

  Added the DomeGrid function createDomeGrid() to create a spherical yellow reference grid in Maya.
  
  Edited the Dome Grid creation script so the catch command is used to handle the event that mental ray might not be installed and a doPaintEffectsToPoly function based Maya code dependency is going to try and change the .miFinalGatherCast attribute. Adjusted the line thickness, default light brightness setting, and the shadow settings on the Dome Grid.

  Updated the Arnold Domemaster3D menu items and created an "Open Directories" section to better categorize the entries.

Vray
  Added the DomeGrid function createDomeGrid() to create a spherical yellow reference grid in Maya.

  Updated the Vray Automagic tool's Autosetup() function to add the DomeGrid and test shapes.

  Edited the Dome Grid creation script so the catch command is used to handle the event that mental ray might not be installed and a doPaintEffectsToPoly function based Maya code dependency is going to try and change the .miFinalGatherCast attribute. Adjusted the line thickness on the Dome Grid.

  Updated the Vray Domemaster3D menu items and created an "Open Directories" section to better categorize the entries.

Maya
  Updated Domemaster3D menu for compatibility with Maya 2017 + mental ray 3.14 beta 9
  
  Added an Automagic LatLong 3D Scene shelf button to the mental ray Domemaster3D shelf that creates a LatLong_Stereo based test scene
  
  Updated mental ray shader source code + makefiles for mental ray 3.14 ray differential texture sampling
  
  Improved the domeRadius.mel, domeCamera.py, domeMaterial.py, AEdomeAFL_FOV_StereoTemplate.mel, AEdomeAFL_FOVTemplate.mel, and domeHistogram.mel script's Maya 2017 compatibility by fixing the MEL "Redeclaration of variable" warnings
  
  The domeMenu.mel script has been unified so Maya 2010-2017 all use the same MEL script file that is now stored in the Domemaster3D/maya/common/scripts folder
  
  Edited the Dome Grid creation script so the catch command is used to handle the event that mental ray might not be installed and a doPaintEffectsToPoly function based Maya code dependency is going to try and change the .miFinalGatherCast attribute. Adjusted the line thickness on the Dome Grid.
  
  Renamed the Domemaster3D shelf open project icon label text from "PRO" to "PROJ"
  
  Updated the Domemaster3D menu items and created an "Open Directories" section to better categorize the entries.
  
  Added new MEL functions to the domeRender.mel script to enable the mental ray 3.14 ray differential based elliptical filtering mode on Maya file node based texture maps:
  
  // List all of the Maya file nodes and examine the new mental ray elliptical filtering modes:

  // List the selected file nodes
  source "domeRender.mel";
  domeListMayaFileNodes(1);

  // List all file nodes in the scene
  source "domeRender.mel";
  domeListMayaFileNodes(0);

  // Update all of the Maya file nodes to use the new mental ray elliptical filtering modes:
  
  // Update the selected file nodes
  source "domeRender.mel";
  domeUpdateMayaFileNodes(1);
  
  // Update all file nodes in the scene
  source "domeRender.mel";
  domeUpdateMayaFileNodes(0);
  
Version 2.1.1
-------------
2016-09-11

Arnold
  Updated the LatLong Stereo shader defaults for the camera orientation and enabled the Zenith Mode checkbox

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
    
  Added a new Open Maya Project Folder "PRO" shelf button and Domemaster3D menu item. This button makes it easy to open the current Maya project folder in a new Finder/Explorer/Nautilus file browser window.
  
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
