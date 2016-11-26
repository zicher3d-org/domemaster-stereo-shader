# Vray Domemaster3D Version History #

## <a name="credits"></a>Credits ##

- Roberto Ziche created the original `domeAFL_FOV_Stereo` and `LatLong_Stereo` shader for mental ray on 3DS Max, and finished the Vray for Max shader port.
- Andrew Hazelden ported the shaders to Maya and Softimage, and added support for Vray and Arnold.
- Daniel Ott created the original 2D `domeAFL_FOV` for mental ray.
- Thanks to Trygve Wastvedt for his help in getting the Vray for 3DS Max port started.
- Thanks to Toshiyuki Takahei for preparing the Japanese translations of the Domemaster3D Wiki pages.


## <a name="todo-list"></a>To Do List ##

### DomemasterStereo To Dos ###

- Correctly handle the black matting of the domemaster frame when "if (r < 1.0)" is false
- Implement the head tilt code

### Vray for Maya To Dos ###

- Implement screen space texture coordinates

### Vray for 3DS Max To Dos ###

- Done at the moment

### Vray for Softimage To Dos ###

- Finish figuring out how the VRay/SI Bridge SDK works. Get the DomemasterStereo and LatLongStereo lens shader translator working in Softimage.

### Shader Testing To Dos ###

- Generate a .vrscene file with screen space texture maps linked into the DomemasterStereo and LatLongStereo attributes. Verify the Maya/3DS Max/Softimage releases can all work with Vray Standalone.


## <a name="version-history"></a>Version History ##

### 2016-09-17 ###

- Added the DomeGrid function createDomeGrid() to create a spherical yellow reference grid in Maya.

- Updated the Vray Automagic tool's Autosetup() function to add the DomeGrid and test shapes.

- Edited the Dome Grid creation script so the catch command is used to handle the event that mental ray might not be installed and a doPaintEffectsToPoly function based Maya code dependency is going to try and change the .miFinalGatherCast attribute. Adjusted the line thickness on the Dome Grid.

- Updated the Vray Domemaster3D menu items and created an "Open Directories" section to better categorize the entries.

### 2015-08-10 ###

- Added Vray 3.1 for Maya support.

- Updated the wiki link in the Vray Domemaster3D Maya shelf tool.

### 2015-07-09 ###

**Vray for Max**

- Added a new Vray 3.2 for 3DS Max 2016 build of the DomemasterStereo and LatLongStereo shaders. 

### 2015-06-05 ###

**Vray for Maya**

- Updated the Linux Makefiles to better link against the lib files.

- Added a new Linux Vray 3.0 for Maya build of the Domemaster3D shaders. The shader .so files were compiled with CentOS 6.4 but they should work fine with any Redhat/CentOS/Fedora/etc... Linux version that supports Vray 3.0 for Maya.

- Updated the Domemaster3D Vray Maya shelf file to fix an icon file name capitalization issue that would occur on case sensitive file systems.

### 2015-06-01 ###

**Vray for Maya**

- Added new Linux makefiles for Vray 3.0 for Maya and Vray 2.5 for Maya. This allows users to compile their own Linux versions of the DomemasterStereo and LatLongStereo shaders.

### 2015-05-21 ###

**Vray for Maya**

- Added Vray 3.0 for Maya on macOS Support. This build works with macOS 10.9 Mavericks and 10.10 Yosemite only.

### 2015-05-08 ###

**Vray for Maya**

- Added a version info MEL script
- Added a Vray for Maya shelf toolbar labeled `VrayDomemaster3D`
- Created Maya Stereo Rig Manager scripts for the DomemasterStereo and LatLongStereo cameras.

- **Note:** If you want to use the Maya Render View's native stereo preview system, you have to turn off the **Use V-Ray VFB** checkbox in the Maya render settings window.

### 2015-04-02 ###

**Vray for Maya**

- Synced the Vray for Maya code to include the 3DS Max "Neck Offset" and "Hemi-equirectangular" features.

- The Visual Studio compiler version has been switched to Visual Studio 2013. This means you will need to install the [Visual Studio 2013 (VC++ 12.0) Redistributable Package](http://www.microsoft.com/en-us/download/details.aspx?id=40784) if you don't have it on your workstations and render nodes.

Note: The Domemaster3D Vray for Maya shader parameters have been updated and may break compatibility with the previous releases. This was done to syncronise the variable names in .vrscene exports with the 3DS Max version of the shaders.

**Vray for Softimage**

- Synced the Vray for Softimage SPDL code to include the 3DS Max "Neck Offset" and "Hemi-equirectangular" features.

### 2015-03-31 ###

**Vray Standalone macOS Support**

- Work has started on updating the macOS based makefiles for the Vray DomemasterStereo and LatLongStereo shaders. At this point the vray tool `plgparams.bin` on macOS correctly reports the shader parameters in the Vray 2.5 for macOS i386 build of the shaders. Unfortunately, there is still a lazy binding issue with the shaders when used with Vray Standalone.

![Plgparams Listing the Shader Parameters on the macOS 1](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_mac_plugin_params_latlongstereo.png)  

![Plgparams Listing the Shader Parameters on the macOS  2](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_mac_plugin_params_domemasterstereo.png) 

**Vray for Softimage Support**

- A basic set of Vray for Sofimage SPDL and DSPreset files have been created for the DomemasterStereo and LatLongStereo lens shaders. The lens shader GUIs show up in Softimage but I haven't figured out the Softimage to Vray translator features yet which are required to export the lens shader data to a .vrscene file or activate the shader in the Vray Frame Buffer window.

![Vray for Softimage Support](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray-for-softimage-domemaster3d-shaders.png)


### Version 0.5 - 2015-03-23 ###

**3DS Max Builds Added**

- There are now initial builds of the Vray for 3DS Max version of the Domemaster3D shaders. These are the first development versions of the shader so some things are expected to change before the final release.

- The LatLongStereo shader for Vray on 3DS Max has a new Domemaster3D feature of a neck offset to simulate a physical 360&deg; camera rig's distance between a camera's lens nodal point and the origin on the tripod.

- The LatLongStereo shader for Vray on 3DS Max has a new Domemaster3D feature of a hemirect checkbox. Hemirect stands for hemi-equirectangular which is a partial spherical rendering. The hemirect feature allows you to align partial latlong renderings so they start at the top zenith region of the latlong frame. This is useful if you want to render a latlong image with a 90&deg; vertical field of view and then warp it in post into a 180&deg; fulldome image.

### Version 0.4 - 2015-02-28 ###

**Maya Code Update:**

- Added a Vray for Maya `Post Translate Python Script` item that handles the export and rendering of the DomemasterStereo and LatLongStereo shaders. The `Post Translate Python Script` data is stored in the vraySettings node using the `.ptp` / `.postTranslatePython` attribute. 

- When a DomemasterStereo or LatLongStereo Vray Extra Attribute is added to a Maya camera shape node and turned ON with the checkbox, a `Post Translate Python Script` code snippet is added automatically to the Vray Render Settings window.

### Version 0.3 - 2014-12-24 ###

- Added Vray 3.0 support for Maya/Standalone/Vray RT
- Added a Vray 3.0 for Max version of the `DomemasterStereo` and `LatLongStereo` source code. The GUI elements still need to be fine tuned and the Visual Studio makefile needs a bit of work to fix a `LibDescription` compiling error.

### Version 0.2 - 2014-11-26 ###

- Updated the DomemasterStereo and LatLongStereo camera org code. Hopefully this fixed the stereo rendering issues
- Rotated the DomemasterStereo view by 90 degrees clockwise to match the mental ray domeAFL_FOV_Stereo shader.

### Version 0.1 - 2014-11-14 ###

- Initial Vray support.


