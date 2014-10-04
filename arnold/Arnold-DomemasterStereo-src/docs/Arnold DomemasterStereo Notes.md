# Arnold Domemaster Stereo Guide #
-------------------------
2014-10-04 08.36 am
![Maya DomemasterStereo for Arnold Screenshot](mtoa_domemasterstereo.png)

## Overview ##

The Domemaster Stereo Shader is a fulldome stereo production lens shader for 3DS Max, Maya, Softimage, Houdini, Maxwell Studio, Mental Ray Standalone, and Arnold Standalone. The lens shader is available for Mental Ray, and Arnold, and comes integrated in Maxwell Render version 3.1+.

This guide covers the Arnold version of the Domemaster Stereo Shader.

## Maya Shader Installation ##


### Windows 64-bit ###

**Step 1.**
Download the [Visual Studio 2012 (VC++ 11.0) Redistributable Package](http://www.microsoft.com/en-us/download/details.aspx?id=30679).


**Step 2.**
Copy the .dll and .mtd files to the Arnold shaders directory:
`C:\solidangle\mtoadeploy\<Version>\shaders\`

Maya Shader Files:

    DomemasterStereo.dll
    DomemasterStereo.mtd

**Step 3.**
Copy the Arnold AE Template File "DomeStereoTemplate.py" to the Arnold AE folder:

`C:\solidangle\mtoadeploy\<Version>\scripts\mtoa\ui\ae`

Note: The Maya AE Template path can be found using the following environment variable:
`%MTOA_TEMPLATES_PATH%` or `%MTOA_PATH%\scripts\mtoa\ui\ae\`

**Step 4.**
Edit your Windows Environment variables using the System Control Panel to include Arnold's env vars and path:

    PATH="C:\solidangle\mtoadeploy\2014\bin\"
    ARNOLD_PLUGIN_PATH="C:\solidangle\mtoadeploy\2014\shaders"
    MAYA_RENDER_DESC_PATH="C:\solidangle\mtoadeploy\2014\"


### Mac 64-bit ###

**Step 1.**
Copy the .dylib and .mtd files to the Arnold shaders directory:
`~/solidangle/mtoa/<Version>/shaders/`

Maya Shader Files:

    DomemasterStereo.dylib
    DomemasterStereo.mtd

**Step 2.**
Copy the Arnold AE Template File "DomeStereoTemplate.py" to the Arnold AE folder:
`~/solidangle/mtoa/<Version>/scripts/mtoa/ui/ae/`

Note: The Maya AE Template path can be found using the following environment variable:
`$(MTOA_TEMPLATES_PATH)` or `$(MTOA_PATH)/scripts/mtoa/ui/ae/`

**Step 3.**
Edit your `.bash_profile` to include Arnold's env vars and path:

    # Arnold Settings
    export PATH="$PATH:$HOME/solidangle/mtoa/2014/bin/"
    export ARNOLD_PLUGIN_PATH="$HOME/solidangle/mtoa/2014/shaders"
    export MAYA_RENDER_DESC_PATH="$HOME/solidangle/mtoa/2014/"

### Linux 64-bit ###

**Step 1.**
Copy the .so and .mtd files to the Arnold shaders directory:

`/opt/solidangle/mtoa/<Version>/shaders/`

Maya Shader Files:

    DomemasterStereo.so
    DomemasterStereo.mtd

**Step 2.**
Copy the Arnold AE Template File "DomeStereoTemplate.py" to the Arnold AE folder:

`/opt/solidangle/mtoa/<Version>/scripts/mtoa/ui/ae/`

Note: The Maya AE Template path can be found using the following environment variable:
`$(MTOA_TEMPLATES_PATH)` or `$(MTOA_PATH)/scripts/mtoa/ui/ae/`

**Step 3.**
Edit your .bash_profile to include Arnold's env vars and path:

    # Arnold Settings
    export PATH="$PATH:/opt/solidangle/mtoa/2014/bin/"
    export ARNOLD_PLUGIN_PATH="/opt/solidangle/mtoa/2014/shaders"
    export MAYA_RENDER_DESC_PATH="/opt/solidangle/mtoa/2014/"


## Verify the Shader Loaded in Arnold ##

### Listing the Nodes ###

You can list all of the active Arnold Shader nodes using:
#### Windows Node List ####

`C:\solidangle\mtoadeploy\<Version>\bin\kick.exe -nodes t`

#### Mac Node List ####

`~/solidangle/mtoa/<Version>/bin/kick -nodes t`

#### Linux Node List ####

`/opt/solidangle/mtoa/<Version>/bin/kick -nodes t`


### DomemasterStereo Node Parameters ###

A typical result would look like this:

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
      FLOAT         fov                               180
      FLOAT         separation                        6.5
      FLOAT         zero_parallax_sphere              360
      FLOAT         forward_tilt                      0
      FLOAT         separation_map                    1
      FLOAT         head_turn_map                     1
      FLOAT         head_roll_map                     0.5
      INT           flip_ray_x                        0
      INT           flip_ray_y                        0
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

Assuming Arnold's kick tool is in your system PATH variable, you can check if the shader is installed correctly and read the default parameters using:

#### Windows Parameters ####

![Rendering using Arnold Kick](arnold_kick_sample_mac_render.png)

`kick.exe -info DomemasterStereo`
or 
you can check if the shader is installed and define a custom library search path at the same time:

`kick -l C:\solidangle\mtoadeploy\<Version>\shaders\DomemasterStereo.dll -info DomemasterStereo`

#### Mac Parameters ####

`kick -info DomemasterStereo`
or 
you can check if the shader is installed and define a custom library search path at the same time:

`kick -l ~/solidangle/mtoa/<Version>/shaders/DomemasterStereo.dylib -info DomemasterStereo`

#### Linux Parameters ####

`kick -info DomemasterStereo`
or 
you can check if the shader is installed and define a custom library search path at the same time:

`kick -l /opt/solidangle/mtoa/<Version>/shaders/DomemasterStereo.so -info DomemasterStereo`


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
Compile the source code using "windows64_compile.bat" bat script in the same command prompt window used step 3:
`windows64_compile.bat`

### Mac OS X 64-bit ###

**Step 1.**
Install Xcode, Arnold, and MtoA.

**Step 2.**
Open a new terminal window and cd into the source code folder.

**Step 3.**
Edit the Makefile.osx file and change the "MAYA_VERSION" variable to match your current Maya release, and update the "MTOA_API_VERSION" variable to match your current Arnold release number. You might want to edit the "macosx_version_min" option if you are compiling the shader exclusively for systems running Mac OS X Mavericks 10.9 or newer.

**Step 4.**
Use the Mac OS X makefile to compile a new DomemasterStereo.dylib shader:
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
Edit the Makefile and change the "MAYA_VERSION" variable to match your current Maya release, and update the "MTOA_API_VERSION" variable to match your current Arnold release number.

**Step 4.**
Use the linux makefile to compile a new DomemasterStereo.so shader:
`Make -f Makefile`

## Credits ##

- Roberto Ziche created the original domeAFL_FOV_Stereo shader for 3DS Max.
- Luis Silva created the initial Arnold lens shader port for Softimage.
- Andrew Hazelden finished porting the DomemasterStereo lens shader for Arnold on Softimage/Maya/Houdini.
- Daniel Ott created the original 2D domeAFL_FOV lens shader for mental ray.

## Version History ##

### Version 0.1 - 2014-10-04 ###

Initial Arnold support for Softimage.

Created the DomemasterStereo.mtd and DomeStereoTemplate.py documents for Maya and Houdini users

Changed the attribute names to match the Domemaster Stereo Shader / Arnold conventions

`Dome_Radius` is now named `zero_parallax_sphere`, and `dome_tilt` is now `forward_tilt` based upon the fulldome ning discussion.

