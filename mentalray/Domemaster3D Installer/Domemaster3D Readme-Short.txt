Domemaster3D Stereo Lens Shader for Maya x64 and 3DS Max x64
Version 1.6 alpha 5.1 - October 27, 2014

About This Shader
---------------------
The Domemaster Stereo lens shader is a custom mental ray shader that creates a stereoscopic 3D fisheye image. The lens shader provides advanced controls to optimize the viewing experience for stereoscopic dome renderings. 

The shader collection also supports fulldome 2D rendering using either the DomeAFL_FOV shader, the DomeAFL_WxH shader, or the "Center" camera option in the DomeAFL_FOV_Stereo shader. Latitude Longitude rendering (also known as spherical or equirectangular output) is supported with the help of the latlong_lens shader, and the stereoscopic LatLong_Stereo shader.

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


Documentation and Resources
-----------------------------------

Join the discussion on the Domemaster Stereo Shader NING Group
http://fulldome.ning.com/forum/topics/stereoscopic-domemaster-images

Downloads Page
https://github.com/zicher3d-org/domemaster-stereo-shader/releases

Domemaster Stereo Shader Wiki
https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/_pages

Maya Domemaster3D Shelf Tools
https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/Maya-Domemaster3D-Shelf

Report an Issue
https://github.com/zicher3d-org/domemaster-stereo-shader/issues

Source Code:
https://github.com/zicher3d-org/domemaster-stereo-shader/

Changes in Version 1.6 Alpha 5
-------------------------------------
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


Project Developers
----------------------

Domemaster Stereo Shader & LatLong_Stereo shaders for 3DS Max Created by Roberto Ziche
http://www.robertoziche.com/

Domemaster3D & LatLong_Stereo shaders for Maya and Softimage, and the installer by Andrew Hazelden
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
