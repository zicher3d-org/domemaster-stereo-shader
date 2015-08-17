Domemaster3D Stereo Lens Shader for Maya x64 and 3DS Max x64
Version 1.8.2 - August 17, 2015

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
The Domemaster3D v1.7 release for Windows has been compiled with Visual Studio 2012. If your system doesn't have the Visual Studio 2012 (VC++ 11.0) x64 Redistributable Package installed you can download it here: 
http://www.microsoft.com/en-us/download/details.aspx?id=30679


Mac Notes
----------
The minimum Mac OS X version required to run the compiled versions of the Domemaster3D mental ray shaders is now Mac OS X 10.8 due to the version of Xcode used to compile the current .dylib library files. 

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
  Fixed an issue with the Domemaster3D menu where the LatLong Stereo menu item wasn't linked to the correct menu function.

Version 1.7.4
-------------
2015-06-12

3DS Max
  Updated the installer to remove the word "Beta" from the 3DS Max 2016 Support option
  
Maya
  Updated the installer to remove the word "Beta" from the Maya 2016 Support option

  Updated the Domemaster3D shelf directory buttons "SCN", "IMG", and "TMP" so they open and run a Nautilus file browser window as a non blocking task on Linux
  
  Updated the Domemaster3D for Maya Wiki page link to use the new GitHub Wiki table of contents
  
  Updated the Dome Diagnostics tool for improved renderer support

Version 1.7.3
-------------
2015-04-16

Maya
  Maya 2016 Compatibility Release - Updated the Maya 2016 install paths, the Maya 2016 Visor tab script (visorPanel.mel), the MR physical sky files (AEmia_physicalskyTemplate.mel & createMentalRayIndirectLightingTab.mel), and the mental ray for Maya 2016 mentalrayCustomNodeClass.mel script.
	
  Updated the dome diagnostics tool to support Vray for Maya on Mac OS X environment variables
  
  Updated the Domemaster3D module file entry line for the Maya version specific Python Path:
    PYTHONPATH+:=../2015/scripts

Version 1.7.2
----------------
April 12, 2015

Maya
  Updated the dome diagnostics tool to support RLM environment variables
  
  Updated the dome diagnostics tool PlayblastVR OptionVar reading code
  
  Updated the dome diagnostics tool Arnold MtoA environment variables
  
  Added an entry to the Domemaster3D menu to load the "shelf_Domemaster3D.mel" shelf file.

  Added a Maya Domemaster3D.mod module file for Maya 2013-2016. This makes it easier to install Domemaster3D in a multi-user environment. This module file was created with the help of Randall Rickert (USC School of Cinematic Arts). Note: If you want to use the new Domemaster3D.mod module file instead of using the standard Maya.env file, you need to clear out and remove the Domemaster3D entries that are placed in the Maya.env file by the Domemaster3D installer. You can find the Maya.env file in the folder: (C:\Users\<User Account>\Documents\maya\<Version Number>\Maya.env).
  
Version 1.7.1
-----------------
March 28, 2015

Maya
  Updated Maya Domemaster3D Menu and Visor scripts


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
