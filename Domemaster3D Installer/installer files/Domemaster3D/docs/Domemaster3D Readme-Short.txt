Domemaster3D Stereo Lens Shader for Maya x64 and 3DS Max x64
Version 2.1.2 - September 15, 2016

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

Version 2.1.2
-------------
2016-09-15

Maya
  Updated Domemaster3D menu for compatibility with Maya 2017 + mental ray 3.14 beta 9
  
  Updated mental ray shader source code + makefiles for mental ray 3.14 ray differential texture sampling
  
  Improved the domeRadius.mel, domeCamera.py, domeMaterial.py, AEdomeAFL_FOV_StereoTemplate.mel, AEdomeAFL_FOVTemplate.mel, and domeHistogram.mel script's Maya 2017 compatibility by fixing the MEL "Redeclaration of variable" warnings
  
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

Version 1.9.3
-------------
2016-02-08

Maya
  Updated the DomeViewer tool to add Ricoh Theta S support along with a set of Ricoh Theta S panoramic viewing meshes "ricoh_theta_s_mesh.obj", and "ricoh_theta_s_mesh.ma" to the Domemaster3D sourceimages folder

  Updated the DomeViewer tool to add Facebook Cube Map 3x2 support along with a set of Facebook Cube Map 3x2 panoramic viewing meshes "facebookCube3x2_mesh.obj", and "facebookCube3x2_mesh.ma" to the Domemaster3D sourceimages folder

  Updated the Dome Diagnostics tool to add support for the mental ray env variable "MAYA_MRFM_SHOW_CUSTOM_SHADERS" that will expose the custom mental ray shaders in Maya.

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
