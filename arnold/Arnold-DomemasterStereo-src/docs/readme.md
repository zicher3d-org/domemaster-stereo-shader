# Arnold Domemaster3D Guide #
-------------------------
2016-09-17

![Domemaster3D Shader Running on MtoA](http://www.andrewhazelden.com/projects/domemaster3D/wiki/arnold/mtoa_domemasterstereo.png)

## Overview ##

The Domemaster Stereo Shader is a set of fulldome stereo and latlong stereo production lens shaders for 3DS Max, Maya, Softimage, Houdini, Maxwell Studio, Mental Ray Standalone, and Arnold Standalone. The lens shaders are available for Mental Ray and Arnold, and comes integrated in Maxwell Render version 3.2+.

This guide covers the Arnold version of the Domemaster Stereo Shader.

**Tip:** After you use the Maya shelf tools to add a fulldome or latlong stereo camera rig to your scene, you need to adjust the left camera in the stereo rig to change the "linked" lens shader attributes for the **LatLongStereo** or **DomemasterStereo** rigs.

## Known Issues ##

The current version of the Arnold Domemaster3D shaders (as of 2016-09-17) are a development build. At this point in time there is no easy way to create stereoscopic production centric screen space texture maps using Arnold's MtoA and SItoA render nodes. This means a solution has to be developed inside the Domemaster3D shaders that will remap an existing texture map into screen space coordinates.

The LatLongStereo shader generally works fine. The only thing to note is that there is no way to feather out the stereo effect in the zenith and nadir zones using the separation map attribute. 

The LatLongStereo shader should be rendered with a 2:1 aspect ratio to avoid vertically over-rendering the scene's FOV angle.

At this point, the DomemasterStereo shader will render a stereo fulldome image but you will notice something that looks like a small "swirly region" in the zenith part of the fulldome frame. This is due to a lack of a screen space turn map texture. 


## Shader Screenshots ##

Here are a few screenshots of the Maya Shelf tools and the Arnold based **DomemasterStereo**, **DomemasterWxH**, and **LatLongStereo** shader GUIs for Maya.

### Maya Shelf ###
![Maya Shelf Icons](http://www.andrewhazelden.com/projects/domemaster3D/wiki/arnold/arnold-domemaster3d-shelf.png)


### DomemasterStereo Shader ###
![DomemasterStereo shader for Maya](http://www.andrewhazelden.com/projects/domemaster3D/wiki/arnold/domemasterstereo_attributes.png)

### DomemasterWxH Shader ###
![DomemasterWxH shader for Maya](http://www.andrewhazelden.com/projects/domemaster3D/wiki/arnold/domemasterwxh_attributes.png)

### LatLongStereo Shader ###
![LatLongStereo shader for Maya](http://www.andrewhazelden.com/projects/domemaster3D/wiki/arnold/latlongstereo_attributes.png)


## Maya Shader Installation ##

### Windows 64-bit ###

**Step 1.** Download and install the [Visual Studio 2012 (VC++ 11.0) Redistributable Package](http://www.microsoft.com/en-us/download/details.aspx?id=30679).

**Step 2.** Download and install the file "Domemaster3D for Maya + 3DS Max on Windows 64-bit" from the [Domemaster Project's GitHub Releases](https://github.com/zicher3d-org/domemaster-stereo-shader/releases) page or from [Andrew Hazelden's blog](http://www.andrewhazelden.com/blog/2012/04/domemaster3d-stereoscopic-shader-for-autodesk-maya/).

**Step 3.** Open up the new Domemaster3D folder:

`C:\Program Files\Domemaster3D\arnold\mtoa\modules`

Copy the Maya module file "ArnoldDomemaster3D.mod" from the Domemaster3D "modules" folder to:

(Single User Modules Install)

`C:\Users\<User Account>\Documents\maya\<Maya Version>\modules\`

If the modules folder doesn't exist in the destination folder path, then create the modules directory too.

or

(System Wide Modules Install)

`C:\Program Files\Common Files\Autodesk Shared\Modules\Maya\<Maya Version>\`

**Step 5.** Copy the Maya shelf file from the Domemaster3D MtoA "common\shelves" folder to your user account's Maya shelves folder.

`C:\Users\<User Account>\Documents\maya\<Maya Version>\prefs\shelves\`

**Step 6.**
Edit your Windows Environment variables using the System Control Panel to include Arnold's env vars and path:  

    PATH=C:\solidangle\mtoadeploy\2017\bin\
    ARNOLD_PLUGIN_PATH=C:\solidangle\mtoadeploy\2017\shaders;C:\Program Files\Domemaster3D\arnold\mtoa\shaders
    MAYA_RENDER_DESC_PATH=C:\solidangle\mtoadeploy\2017\
    solidangle_LICENSE=5053@<Write Your RLM Server Address Here>

**Step 6.** (Optional) Expand the Domemaster3D Maya / MtoA examples project that is located here:

`C:\Program Files\Domemaster3D\arnold\scenes\MtoA_LatLong_Sample_Project.zip `

and copy it to your Maya projects folder here:

`C:\Users\<User Account>\Documents\maya\projects\`

### macOS 64-bit ###

**Step 1.** Download and install the file "Domemaster3D for Maya on macOS" from the [Domemaster Project's GitHub Releases](https://github.com/zicher3d-org/domemaster-stereo-shader/releases) page or from [Andrew Hazelden's blog](http://www.andrewhazelden.com/blog/2012/04/domemaster3d-stereoscopic-shader-for-autodesk-maya/).

**Step 2.** Open up the new Domemaster3D folder:
`/Applications/Domemaster3D/arnold/mtoa/modules`

Copy the Maya module file "ArnoldDomemaster3D.mod" from the Domemaster3D mtoa "common/modules" folder to:

(Single User Modules Install)

`/Users/<User Account>/Library/Preferences/Autodesk/maya/<Maya Version>/modules/`

or

(System Wide Modules Install)

`/Users/Shared/Autodesk/modules/maya/<Maya Version>/`

If the modules folder doesn't exist in the destination folder path, then create the modules directory too.

**Step 4.** Copy the Maya shelf file from the Domemaster3D mtoa "common/shelves" folder to your user account's Maya shelves folder.

`/Users/<User Account>/Library/Preferences/Autodesk/maya/<Maya Version>/prefs/shelves/`

**Step 5.** (Optional) Edit your `.bash_profile` to include Arnold's env vars and path:

    # Arnold Settings
    export PATH="$PATH:/Applications/solidangle/mtoa/2017/bin/"
    export ARNOLD_PLUGIN_PATH="/Applications/solidangle/mtoa/2017/shaders:/Applications/Domemaster3D/arnold/mtoa/shaders"
    export MAYA_RENDER_DESC_PATH="/Applications/solidangle/mtoa/2017/"
    export solidangle_LICENSE=5053@<Write Your RLM Server Address Here>

**Step 6.** (Optional) Expand the Domemaster3D Maya / MtoA examples project that is located here:

`/Applications/Domemaster3D/arnold/scenes/MtoA_LatLong_Sample_Project.zip `

and copy it to your Maya projects folder here:

`~/Documents/maya/projects/`

### Linux 64-bit ###

**Step 1.** Download and install the file "Domemaster3D Manual Install for Maya + 3DS Max + Mental Ray Standalone 64-bit on Windows, macOS, Linux" from the [Domemaster Project's GitHub Releases](https://github.com/zicher3d-org/domemaster-stereo-shader/releases) page or from [Andrew Hazelden's blog](http://www.andrewhazelden.com/blog/2012/04/domemaster3d-stereoscopic-shader-for-autodesk-maya/).

**Step 2.** Open up the new Domemaster3D folder:

`/opt/Domemaster3D/arnold/mtoa/modules`

Copy the Maya module file "ArnoldDomemaster3D.mod" from the Domemaster3D "modules" folder to:

(Single User Modules Install)

`~/maya/<Maya Version>/modules/`

If the modules folder doesn't exist in the destination folder path, then create the modules directory too.

**Step 4.** Copy the Maya shelf file from the Domemaster3D MtoA "common\shelves" folder to your user account's Maya shelves folder.

`~/maya/<Maya Version>/prefs/shelves/`

**Step 6.** Edit your .bash_profile to include Arnold's env vars and path:

    # Arnold Settings
    export PATH="$PATH:/opt/solidangle/mtoa/2017/bin/"
    export ARNOLD_PLUGIN_PATH="/opt/solidangle/mtoa/2017/shaders:/opt/Domemaster3D/arnold/mtoa/shaders"
    export MAYA_RENDER_DESC_PATH="/opt/solidangle/mtoa/2017/"
    export solidangle_LICENSE="5053@<Write Your RLM Server Address Here>"

**Step 7.** (Optional) Expand the Domemaster3D Maya / MtoA examples project that is located here:

`/opt/Domemaster3D/arnold/scenes/MtoA_LatLong_Sample_Project.zip `

and copy it to your Maya projects folder here:

`~/maya/projects/`

## Verify the Shader Loaded in Arnold ##

### Listing the Nodes ###

You can list all of the active Arnold Shader nodes using:
#### Windows Node List ####

`C:\solidangle\mtoadeploy\<Version>\bin\kick.exe -nodes t`

#### macOS Node List ####

`~/solidangle/mtoa/<Version>/bin/kick -nodes t`

#### Linux Node List ####

`/opt/solidangle/mtoa/<Version>/bin/kick -nodes t`


### DomemasterStereo Node Parameters ###

If you run Arnold's Kick utility with the info flag you can see the DomemasterStereo shader's node parameters:

      WARNING |  node "DomemasterStereo" is already installed
      node:         DomemasterStereo
      type:         camera
      output:       (null)
      parameters:   27
      filename:     C:\solidangle\mtoadeploy\2014\shaders\DomemasterStereo.dll
      version:      4.2.0.6

      Type          Name                              Default
      ------------  --------------------------------  --------------------------------
      INT           camera                            0
      FLOAT         fov_angle                         180
      FLOAT         zero_parallax_sphere              360
      FLOAT         separation                        6.5
      FLOAT         forward_tilt                      0
      BOOL          tilt_compensation                 false
      BOOL          vertical_mode                     false
      FLOAT         separation_map                    1
      FLOAT         head_turn_map                     1
      FLOAT         head_tilt_map                     0.5
      INT           flip_ray_x                        false
      INT           flip_ray_y                        false
      POINT[]       position                          0, 0, 0
      POINT[]       look_at                           0, 0, -1
      VECTOR[]      up                                0, 1, 0
      MATRIX[]      matrix                            
      FLOAT         near_clip                         0.0001
      FLOAT         far_clip                          1e+30
      FLOAT         shutter_start                     0
      FLOAT         shutter_end                       0
      ENUM          shutter_type                      box
      POINT2[]      shutter_curve                     (empty)
      ENUM          rolling_shutter                   off
      FLOAT         rolling_shutter_duration          0
      NODE          filtermap                         (null)
      ENUM          handedness                        right
      FLOAT[]       time_samples                      (2 elements)
      POINT2        screen_window_min                 -1, -1
      POINT2        screen_window_max                 1, 1
      FLOAT         exposure                          0
      STRING        name   

![Rendering using Arnold Kick](http://www.andrewhazelden.com/projects/domemaster3D/wiki/arnold/arnold_kick_sample_mac_render.png)

Assuming Arnold's kick tool is in your system PATH variable, you can check if the shader is installed correctly and read the default parameters using the following parameters:

#### Windows Parameters ####

`kick.exe -info DomemasterStereo`
`kick.exe -info DomemasterWxH`
`kick.exe -info LatLongStereo`

or 

you can check if the shader is installed and define a custom library search path at the same time:

`kick -l C:\solidangle\mtoadeploy\<Version>\shaders\DomemasterStereo.dll -info DomemasterStereo`

`kick -l C:\solidangle\mtoadeploy\<Version>\shaders\DomemasterWxH.dll -info DomemasterWxH`

`kick -l C:\solidangle\mtoadeploy\<Version>\shaders\LatLongStereo.dll -info LatLongStereo`

#### macOS Parameters ####

`kick -info DomemasterStereo`
`kick -info DomemasterWxH`
`kick -info LatLongStereo`

or 

you can check if the shader is installed and define a custom library search path at the same time:

`kick -l ~/solidangle/mtoa/<Version>/shaders/DomemasterStereo.dylib -info DomemasterStereo`

`kick -l ~/solidangle/mtoa/<Version>/shaders/DomemasterWxH.dylib -info DomemasterWxH`

`kick -l ~/solidangle/mtoa/<Version>/shaders/LatLongStereo.dylib -info LatLongStereo`

#### Linux Parameters ####

`kick -info DomemasterStereo`
`kick -info DomemasterWxH`
`kick -info LatLongStereo`

or 

you can check if the shader is installed and define a custom library search path at the same time:

`kick -l /opt/solidangle/mtoa/<Version>/shaders/DomemasterStereo.so -info DomemasterStereo`

`kick -l /opt/solidangle/mtoa/<Version>/shaders/DomemasterWxH.so -info DomemasterWxH`

`kick -l /opt/solidangle/mtoa/<Version>/shaders/LatLongStereo.so -info LatLongStereo`


## Rendering the Example Scene ##

    kick -i DomemasterStereo_right.ass -r 512 512
    kick -i DomemasterStereo_left.ass -r 512 512

## Compiling Instructions ##

### Windows 64-bit ###

**Step 1.**
Install Visual Studio, Arnold, and MtoA. The current script has the paths for command line compiling with Visual Studio 2012 (11.0)

**Step 2.**
Open a new command prompt and cd into the source code folder.

**Step 3.**
Run the "windows64_setup.bat" script using a new command prompt window to setup the compiling environment variables:
`windows64_setup.bat`

**Step 4.**
Compile the source code using `windows64_compile.bat` bat script in the same command prompt window used step 3:
`windows64_compile.bat`

### macOS 64-bit ###

**Step 1.**
Install Xcode, Arnold, and MtoA.

**Step 2.**
Open a new terminal window and cd into the source code folder.

**Step 3.**
Edit the Makefile.osx file and change the `MAYA_VERSION` variable to match your current Maya release, and update the `MTOA_API_VERSION` variable to match your current Arnold release number. You might want to edit the `macosx_version_min` option if you are compiling the shader exclusively for systems running macOS Mavericks 10.9 or newer.

**Step 4.**
Use the macOS makefile to compile a new DomemasterStereo.dylib shader:
`Make -f Makefile.osx`

**Step 5.**
You can check your compiled dylib architecture with the following command:

    bash-3.2# lipo -info DomemasterStereo.dylib 
    Non-fat file: DomemasterStereo.dylib is architecture: x86_64

### Linux 64-bit ###

**Step 1.** 
Install G++, Arnold, and MtoA.

**Step 2.**
Open a new terminal window and cd into the source code folder.

**Step 3.**
Edit the Makefile and change the `MAYA_VERSION` variable to match your current Maya release, and update the `MTOA_API_VERSION` variable to match your current Arnold release number.

**Step 4.**
Use the linux makefile to compile a new DomemasterStereo.so shader:
`Make -f Makefile`

## Credits ##

- Roberto Ziche created the original `domeAFL_FOV_Stereo` shader for 3DS Max.
- Luis Silva created the initial Arnold lens shader port for Softimage.
- Andrew Hazelden is doing the ongoing port of the `DomemasterStereo` and `LatLongStereo` lens shader for Arnold on Maya/Softimage/Houdini.
- Daniel Ott created the original 2D `domeAFL_FOV`, and `domeAFL_WxH` lens shaders for mental ray.

## Version History ##

### Version 2.1.2 - 2016-09-17 ###

Updated the Maya based "Arnold Domemaster3D" menu and shelf to add 2D rendering style entries for creating Domemaster FOV 2D and LatLong 2D renderings using the center camera view in the existing stereo lens shaders.

Added the DomeGrid function createDomeGrid() to create a spherical yellow reference grid in Maya.

Edited the Dome Grid creation script so the catch command is used to handle the event that mental ray might not be installed and a doPaintEffectsToPoly function based Maya code dependency is going to try and change the .miFinalGatherCast attribute. Adjusted the line thickness, default light brightness setting, and the shadow settings on the Dome Grid.

Updated the Arnold Domemaster3D menu items and created an "Open Directories" section to better categorize the entries.

### Version 2.1 - 2016-09-06 ###

Improved the Domemaster3D/Arnold for Maya integration. Updated the "ArnoldDomemaster3D.mod" Maya module file, updated the shelf tool items, and added a new "Arnold Domemaster3D" menu in the Maya rendering menu set.

### Version 1.7 - 2015-05-07 ###

Updated the Maya shelf tools to add a new Automagic LatLong Stereo option

Updated the python script that creates the Arnold LatLongStereo and DomeStereo cameras. The stereo rig manager defaultRig value is now switched automatically when a LatLongStereo or DomeStereo camera is created. This fixes an alignment issue that happened when the wrong stereo camera defaultRig was active when creating a new camera in Arnold.

Updated the dome grid shape to use a full sphere as the default FOV value for the wireframe mesh geometry. This improves the rendering experience when a latlong shader is used.

### Version 1.6.2 - 2015-04-08 ###

Added the initial Cinema4D C4DtoA "res" support files for the lens shaders.

### Version 1.6.1 - 2015-02-23 ###

Updated the Windows builds to use Visual Studio 2013 for the Arnold .dll shader compiles.

Tweaked the LatLongStereo FOV code to improve the vertical FOV rendering issue. 

**Note:** The LatLongStereo shader currently expects a 2:1 aspect ratio render resolution for the output. The code to compensate for a non 2:1 rendered aspect ratio hasn't been finished yet so you will experience over-rendering of the vertical FOV if you render to an image with a 1:1 aspect ratio.

### Version 0.3 - 2015-01-31 ###

Updated the Maya userSetup.py script to avoid a condition where the code was run twice at startup.

Updated the metadata files to include the "is_perspective" attribute to fix the Arnold error message "node "%s" is not a perspective camera, cannot use view-dependent subdivision". This change was done in reference to the Arnold Ticket #1646: [https://trac.solidangle.com/mtoa/ticket/1646#comment:9](https://trac.solidangle.com/mtoa/ticket/1646#comment:9)

### Version 0.2 - 2014-12-20 ###

Updated the minimum `Zero Parallax Sphere` and  `Zero Parallax Distance` values in the DomemasterStereo and LatLongStereo shaders to 0.001 to support smaller camera scales.

### Version 0.1 - 2014-11-01 ###

Initial Arnold support for Maya/Softimage/Houdini.

Created `DomemasterStereo.mtd`, `DomemasterWxH`, and `LatLongStereo.mtd` documents for Maya and Houdini users.

Created Maya stereo rig scripts for the LatLongStereo and DomemasterStereo lens shaders.

Changed the attribute names to match the Domemaster Stereo Shader / Arnold conventions:

`Dome_Radius` is now named `zero_parallax_sphere`, and `dome_tilt` is now `forward_tilt` based upon the fulldome NING discussion.
