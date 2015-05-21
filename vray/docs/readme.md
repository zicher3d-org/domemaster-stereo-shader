# Vray Domemaster3D Guide #
-------------------------
2015-05-21 
**
- Table of Contents
    *    [Overview](#overview)
    *    [Known Issues](#known-issues)
    *    [Vray Standalone](#vray-standalone)
        +    [DomemasterStereo in a VRSCENE File](#domemasterstereo-in-a-vrscene-file)
        +    [LatLongStereo in a VRSCENE File](#latlongstereo-in-a-vrscene-file)
    *    [Vray Standalone Shader Installation](#vray-standalone-shader-installation)
    *    [Vray for 3DS Max Shader Installation](#vray-for-3ds-max-shader-installation)
    *    [Vray RT for 3DS Max Shader Installation](#vray-rt-for-3ds-max-shader-installation)
        +    [Windows 64-bit](#windows-64-bit-1)
    *    [Verify the Shader is Loaded in Vray](#verify-the-shader-is-loaded-in-vray)
        +    [Vray Shader Parameters Screenshot](#vray-shader-parameters-screenshot)
        +    [Listing the Nodes](#listing-the-nodes)
            *    [Windows Node List](#windows-node-list)
            *    [Mac Node List](#mac-node-list)
            *    [Linux Node List](#linux-node-list)
        +    [Node Parameters](#node-parameters)
            *    [plgparams.exe DomemasterStereo](#plgparamsexe-domemasterstereo)
            *    [plgparams.exe LatLongStereo](#plgparamsexe-latlongstereo)
            *    [Windows Parameters](#windows-parameters)
            *    [Mac Parameters](#mac-parameters)
            *    [Linux Parameters](#linux-parameters)
    *    [Rendering the Example Scenes](#rendering-the-example-scenes)
    *    [Vray for 3DS Max Lens Shaders](#vray-for-3ds-max-lens-shaders)
    *    [Adding a Vray Lens Shader in Maya](#adding-a-vray-lens-shader-in-maya)
        +    [VRay DomemasterStereo Camera](#vray-domemasterstereo-camera)
        +    [VRay LatLongStereo Camera](#vray-latlongstereo-camera)
        +    [Removing a Lens Shader](#removing-a-lens-shader)
    *    [Maya Shader Installation](#maya-shader-installation)
        +    [Windows 64-bit](#windows-64-bit-2)
        +    [Mac 64-bit](#mac-64-bit)
        +    [Linux 64-bit](#linux-64-bit)
    *    [Compiling Instructions](#compiling-instructions)
        +    [Windows 64-bit](#windows-64-bit-3)
        +    [Mac OS X 64-bit](#mac-os-x-64-bit)
        +    [Linux 64-bit](#linux-64-bit-1)
    *    [Credits](#credits)
    *    [Version History](#version-history)
    *    [To Do List](#to-do-list)
        +    [DomemasterStereo To Dos](#domemasterstereo-to-dos)
        +    [Vray for Maya To Dos](#vray-for-maya-to-dos)
        +    [Vray for 3DS Max To Dos](#vray-for-3ds-max-to-dos)
        +    [Shader Testing To Dos](#shader-testing-to-dos)


## Overview ##

The Domemaster Stereo Shader is a set of fulldome stereo and latlong stereo production lens shaders for 3DS Max, Maya, Softimage, Houdini, Maxwell Studio, Mental Ray Standalone, Vray Standalone, and Arnold Standalone. The lens shaders are available for Mental Ray, Vray, and Arnold, and comes integrated in Maxwell Render version 3.1+.

This guide covers the Vray version of the Domemaster Stereo Shader.

## Known Issues ##

The current version of the Vray Domemaster3D shaders (as of 2015-05-09 ) is a development build.

The Vray Standalone version generally works without too many issues.

More work needs to be done to apply a black overlay to the circular outside area of the domemaster frame. Right now the DomemasterStereo shader will fill the outside circular area in the frame with a solid color based upon the current data at the 0/0/0 X/Y/Z ray angle. Also the shader doesn't apply a circular alpha channel overlay yet.

The Maya integration is still a work in progress. The Domemaster3D shaders are now active in the Maya render view and the custom Vray Extra Attributes are linked into the Vray for Maya .vrscene exporter when the lens shaders are added as Vray Extra Attributes on the camera shape node.

The first working version of the 3DS Max source code has been added and there are development shader builds for Vray 3.0 on 3DS Max 2015 and 3DS Max 2014, and Vray 2.5 for 3DS Max 2015, and Vray 2.4 for 3DS Max 2013.

## Vray Standalone ##

Right now the DomemasterStereo and LatLongStereo shaders are accessible from Vray Standalone and Vray RT version 2.5 / 3.0 using the `vray.exe` command line program. Until the Maya and 3DS Max shader integrations are complete you will have to add the DomemasterStereo and LatLongStereo camera parameters to your .vrscene files manually. 

Andrew Hazelden's [Vray Syntax Highlighter](https://github.com/AndrewHazelden/Vray-Scene-Syntax-Highlighter) module for Notepad++, GEDIT, BBEdit, and TextWrangler is a good tool for simplifying the process of editing a .vrscene file.

### DomemasterStereo in a VRSCENE File ###

![DomemasterStereo Renderings](images/vray_standalone_domemasterStereo_render.png)

You can upgrade a regular Vray camera (in this case named RenderCamShape) to a DomemasterStereo camera by finding the camera entry in your Vray .vrscene file and pasting the following text in its place:
	
	DomemasterStereo RenderCamShape {
	  camera=0;
	  fov_angle=360.0;
	  parallax_distance=355.0;
	  separation=6.5;
	  forward_tilt=0.0;
	  tilt_compensation=0;
	  vertical_mode=1;
	  separation_map=1.0;
	  head_turn_map=1.0;
	  head_tilt_map=0.5;
	  flip_x=0;
	  flip_y=0;
      neck_offset=0.0;
	}

Note: camera=0 means center view, camera=1 is left view, and camera=2 is right view.

You can test this code out using the included vray example scene "vray 2 DomemasterStereo.vrscene". To render the sample scene launch vray standalone from the command prompt with:
     
	vray.exe -sceneFile="vray 2 DomemasterStereo.vrscene"

### LatLongStereo in a VRSCENE File ###

![LatLongStereo Renderings](images/vray_standalone_LatLongStereo_render.png)

You can upgrade a regular Vray camera (in this case named RenderCamShape) to a LatLongStereo camera by finding the camera entry in your Vray .vrscene file and pasting the following text in its place:

	LatLongStereo RenderCamShape {
	  camera=0;
	  fov_vert_angle=180.0;
	  fov_horiz_angle=360.0;
	  parallax_distance=355.0;
	  separation=6.5;
	  zenith_mode=1;
	  separation_map=1;
      neck_offset=0.0;
      zenith_fov=0;
	}

Note: camera=0 means center view, camera=1 is left view, and camera=2 is right view.

You can test this code out using the included vray example scene "vray 2 LatLongStereo.vrscene". To render the sample scene launch vray standalone from the command prompt with:
      
    vray.exe -sceneFile="vray 2 LatLongStereo.vrscene" 

## Vray Standalone Shader Installation ##

### Windows 64-bit ###

**Step 1.** Download the [Visual Studio 2013 (VC++ 12.0) Redistributable Package](http://www.microsoft.com/en-us/download/details.aspx?id=40784).

**Step 2.** Copy the .dll files to the vray-plugins directory:  

`C:\Program Files\Chaos Group\V-Ray\Standalone for x64\bin\x64\vc101\plugins`

Vray Plugin Files:

    vray_DomemasterStereo.dll
    vray_LatLongStereo.dll

**Step 3.** Edit the Windows environment variables and add an entry for the  `VRAY_PLUGINS_x64` Vray standalone plugins path location.

![Adding an ENV Var](images/adding-a-new-env-var.png)

For Vray Standalone 2.5 the standard `VRAY_PLUGINS_x64` setting would be:   

`VRAY_PLUGINS_x64`  
`C:\Program Files\Chaos Group\V-Ray\Standalone for x64\bin\x64\vc101\plugins`

## Vray for 3DS Max Shader Installation ##

There are now Vray 2.4 for 3DS Max 2013, Vray 2.5 for 3DS Max 2015, Vray 3.0 for 3DS Max 2015, and Vray 3.0 for 3DS Max 2014 builds of the Domemaster3D shaders.

### Windows 64-bit ###

**Step 1.** Download the [Visual Studio 2013 (VC++ 12.0) Redistributable Package](http://www.microsoft.com/en-us/download/details.aspx?id=40784).

**Step 2.** Copy the .dlo files to the Vray for 3DS Max plugins directory.

`C:\Program Files\Autodesk\3ds Max <Max Version>\plugins\vrayplugins`

Note: Change `<Max Version>` to the release number of 3DS Max. Example: Write in 2015 for the `<Max Version>` if you are using 3DS Max 2015.

Vray Plugin Files:  

    vraylatlongstereo2015.dlo
    vraydomemasterstereo2015.dlo

    vraylatlongstereo2014.dlo
    vraydomemasterstereo2014.dlo

    vraylatlongstereo2013.dlo
    vraydomemasetrstereo2013.dlo

**Step 3.**
If you get an "Error Loading Plugin-DLL" error message in 3DS Max when when you try and load the shader it means you haven't installed the Microsoft Visual Studio 2013 x64 Redistributable library that was mentioned as a required stage in **Step 1**. Now is a good time to go back to step 1 and actually install the library file!

![Visual Studio 2013 Library Missing Error](images/vray-max-no-vs2013-libs.png)  
    
## Vray RT for 3DS Max Shader Installation ##

### Windows 64-bit ###

**Step 1.** Download the [Visual Studio 2013 (VC++ 12.0) Redistributable Package](http://www.microsoft.com/en-us/download/details.aspx?id=40784).

**Step 2.** Copy the .dll files to the Vray RT plugins directory.

`C:\Program Files\Chaos Group\V-Ray\RT for 3ds Max <Max Version> for x64\bin\plugins`

Note: Change <Max Version> to the release number of 3DS Max. Example: Write in 2015 for the <Max Version> if you are using 3DS Max 2015.

Vray Plugin Files:  

    vray_DomemasterStereo.dll (Not compiled yet)
    vray_LatLongStereo.dll
    
**Step 3.** Edit the Windows environment variables and add an entry for the  `VRAY_PLUGINS_x64` Vray RT plugins path location.

`C:\Program Files\Chaos Group\V-Ray\RT for 3ds Max <Max Version> for x64\bin\plugins`

Note: Change `<Max Version>` to the release number of 3DS Max. Example: Write in 2015 for the `<Max Version>` if you are using 3DS Max 2015.

**Step 4.** Edit the Windows ENV Path and add the VRay RT `Bin` folder to the list.

`;C:\Program Files\Chaos Group\V-Ray\RT for 3ds Max <Max Version> for x64\bin`

Note: Change `<Max Version>` to the release number of 3DS Max. Example: Write in 2015 for the `<Max Version>` if you are using 3DS Max 2015.

## Verify the Shader is Loaded in Vray ##

### Vray Shader Parameters Screenshot ###

![Plgparams Listing the Shader Parameters](images/vray_plugin_parameters.png)  

![Plgparams Listing the Shader Parameters on the Mac 1](images/vray_mac_plugin_params_latlongstereo.png)  

![Plgparams Listing the Shader Parameters on the Mac 2](images/vray_mac_plugin_params_domemasterstereo.png)  

### Listing the Nodes ###

You can list all of the active Vray Shader nodes using the plugin parameters tool:

#### Windows Node List ####

`cd C:\Program Files\Chaos Group\V-Ray\Standalone for x64\bin\x64\vc101\`  
`plgparams.exe -list`

#### Mac Node List ####

`cd /Applications/ChaosGroup/V-Ray/Standalone_for_snow_leopard_x86/bin/snow_leopard_x86/gcc-4.2/`  
`./plgparams.bin -list`

#### Linux Node List ####

`./plgparams.bin -list`


### Node Parameters ###

If you run the plgparams with the shader name listed you can see the individual node parameters. If you get a plgparams error asking for the -plugindir that means you are missing the vray plugins environment variable such as `VRAY_PLUGINS_x64` or `VRAY_PLUGINS_x86`.
	
#### plgparams.exe DomemasterStereo ####

	Parameters for plugin 'DomemasterStereo'
	  camera: integer = 0, Center, Left, Right Camera Views
	  fov_angle: float = 180, Field of View
	  parallax_distance: float = 360, Parallax Distance
	  separation: float = 6.5, Camera Separation Distance
	  forward_tilt: float = 0, Forward Tilt
	  tilt_compensation: bool = false, Tilt Compensation Mode
	  vertical_mode: bool = false, Vertical Mode
	  separation_map: float = 1, Separation Map
	  head_turn_map: float = 1, Head Turn Map
	  head_tilt_map: float = 0.5, Head Tilt map
	  flip_x: bool = false, Flip X
	  flip_y: bool = false, Flip Y
      neck_offset: float = 0, Neck Offset

#### plgparams.exe LatLongStereo ####

	Parameters for plugin 'LatLongStereo'
	  camera: integer = 0, Center, Left, Right Camera Views
	  fov_vert_angle: float = 180, Field of View Vertical
	  fov_horiz_angle: float = 360, Field of View Horizontal
	  parallax_distance: float = 360, Zero Parallax Distance
	  separation: float = 6.5, Camera Separation
	  zenith_mode: bool = false, Zenith Mode
	  separation_map: float = 1, Separation Map
	  head_tilt_map: float = 0.5, Head Tilt map
	  flip_x: bool = false, Flip X
	  flip_y: bool = false, Flip Y
      neck_offset: float = 0, Neck Offset
      zenith_fov: float = 0, Hemi-equirectangular

    
**Note:** If you receive the following error message it means you have tried to load a Vray 2.5 shader in Vray 3.0:  

    // Error: Error loading plugin library "C:\Program Files\Autodesk\Maya2015\vray\vrayplugins\vray_DomemasterStereo.dll" (127): The specified procedure could not be found. //   
    // Error: Error loading plugin library "C:\Program Files\Autodesk\Maya2015\vray\vrayplugins\vray_LatLongStereo.dll" (127): The specified procedure could not be found. //   

#### Windows Parameters ####

`plgparams.exe DomemasterStereo`  
`plgparams.exe LatLongStereo`  

#### Mac Parameters ####

`./plgparams.bin DomemasterStereo`  
`./plgparams.bin LatLongStereo`  

#### Linux Parameters ####

`./plgparams.bin DomemasterStereo`  
`./plgparams.bin LatLongStereo`  

## Rendering the Example Scenes ##

If you navigate to the Domemaster3D vray scenes folder you can try rendering the sample vray standalone vrscene files.

    vray.exe -sceneFile="vray 2 DomemasterStereo.vrscene"  
    vray.exe -sceneFile="vray 2 LatLongStereo.vrscene"  

    vray.exe -sceneFile="LatLongStereo_Boxworld_center.vrscene"  
    vray.exe -sceneFile="LatLongStereo_Boxworld_left.vrscene"  
    vray.exe -sceneFile="LatLongStereo_Boxworld_right.vrscene"  

    vray.exe -sceneFile="DomemasterStereo_Boxworld_center.vrscene"  
    vray.exe -sceneFile="DomemasterStereo_Boxworld_left.vrscene"  
    vray.exe -sceneFile="DomemasterStereo_Boxworld_right.vrscene"  

## Vray for 3DS Max Lens Shaders ##

Here are two screenshots showing the Vray for 3DS Max beta versions of the Domemaster3D lens shaders.

![Vray for 3DS Max DomemasterStereo Shader](images/vray_max_domemaster_stereo.png)

![Vray for 3DS Max LatLongStereo Shader](images/vray_max_latlong_stereo.png)

There are two new controls added for the first time in the Vray for 3DS Max lens shaders: 

- A Neck Offset allows you to simulate the effect of a physical 360&deg; panoramic camera rig where the lens nodal points are shifted away from the camera origin.

![Neck Offset](images/neck-offset.png)

- The hemirect (hemi-equirectangular) checkbox in the LatLongStereo shader that lets you render a partial LatLong image where the top edge of the rendering starts aligned to the zenith pole region. This is useful if you want to render a cropped 360&deg; x 90&deg; latlong image that could then be converted in post into a 180&deg; domemaster (angular fisheye) image with no unused/over-rendered areas in the source image.

## Adding a Vray Lens Shader in Maya #

![Domemaster3D Vray for Maya Shelf](images/domemaster3d-vray-for-maya-shelf.png)

There is now a custom VrayDomemaster3D shelf that makes it easier to use the Domemaster3D lens shaders. In addition to the shelf tools there is also a pair of LatLongStereo and DomemasterStereo camera rigs that work with Maya's native StereoRigManager system.

**Note:** If you want to use the Maya Render View's native stereo preview system, you have to turn off the **Use V-Ray VFB** checkbox in the Maya render settings window.

---

You can also add a custom Vray lens shader to a Maya camera using the **VRay Extra Attributes** feature. 

To turn a normal camera into a DomemasterStereo or LatLongStereo formatted camera, select the camera's shape node in the Attribute Editor window. Open the `Attributes > VRay` menu, and select either the `DomemasterStereo camera` or `LatLongStereo camera` items. 

At this point you can turn ON the lens shader by scrolling down to the bottom of the Attribute Editor window and expanding the `Extra VRay Attributes` section. Then enable the appropriate `Treat as a Vray DomemasterStereo` or `Treat as a Vray LatLongStereo Cam` checkbox.

### VRay Post Translate Python Script ###

When the `DomemasterStereo` or `LatLongStereo` Vray Extra Attribute section is enabled with the checkbox a new Vray Render Settings **Mel/Python Callbacks** `Post Translate Python Script` entry is added automatically that allows the `DomemasterStereo` and `LatLongStereo` lens shaders to work in the Maya Render View and the Vray Frame Buffer window.

![Post Translate Python Script](images/post-translate-python-script.png)

The `Post Translate Python Script` field is set to use the following python code:

    import domeVrayRender
    reload(domeVrayRender)
    domeVrayRender.domeVrayTranslator()

### VRay DomemasterStereo Camera ###

![VRay DomemasterStereo Camera](images/vray_DomemasterStereoCamera.png)

### VRay LatLongStereo Camera ###

![VRay LatLongStereo Camera](images/vray_LatLongStereoCamera.png)

### Removing a Lens Shader ###

You can remove a vray lens shader from a Maya camera by opening the `Attributes > VRay` menu and unchecking the specific lens shader. This will remove the lens shader's attributes that are listed in the `Extra VRay Attributes` section.

![Adding Extra Attributes](images/vray-extra-attributes.png)

You can also delete the python code in the **Mel/Python Callbacks** `Post Translate Python Script` field if you want to completly remove all references to the Domemaster3D shader elements from the Maya scene file.
![Clearing the Python Translator](images/clear-post-translate-python-script.png)

## Maya Shader Installation ##

### Windows 64-bit ###

**Step 1.** Download the [Visual Studio 2013 (VC++ 12.0) Redistributable Package](http://www.microsoft.com/en-us/download/details.aspx?id=40784).

**Step 2.**
Copy the .dll files to the vray-plugins directory:  

`C:\Program Files\Autodesk\Maya<Version>\vray\vrayplugins\`

Vray Plugin Files:

    vray_DomemasterStereo.dll
    vray_LatLongStereo.dll

**Step 3.**
Copy the Vray script files to the Vray scripts folder:  

`C:\Program Files\Autodesk\Maya<Version>\vray\scripts`

Vray Script Files:

    attributes.txt
    attributeNodes.txt
    attributeGroups.txt
    vrayAEFunctions.mel
    

**Note:** Several of the vray script files listed above already exist in the standard vray install. Those items need to be replaced with new ones that have the DomemasterStereo and LatLongStereo modules integrated in the settings. You should make a backup copy of the original files so you can restore them if required.

**Step 4.**
Copy the Maya script files to the scripts folder:  

`C:\Users\<User Account>\Documents\maya\<Version>\scripts`

Vray Script Files:

**Step 5.**
Copy the Maya shelf file `shelf_VrayDomemaster3D.mel` into your Shelves folder:

`C:\Users\<User Account>\Documents\maya\<Version>\prefs\shelves`

### Mac 64-bit ###

**Step 1.**
Copy the .so files to the vray-plugins directory:  

`/Applications/Autodesk/maya<Version>/vray/vrayplugins`

Vray Plugin Files:

    vray_DomemasterStereo.so
    vray_LatLongStereo.so

**Step 2.**
Copy the  Vray script files to the Vray scripts folder:  

`/Applications/Autodesk/maya<Version>/vray/scripts`

Vray Script Files:

    attributes.txt
    attributeNodes.txt
    attributeGroups.txt
    vrayAEFunctions.mel
    
**Note:** Several of the vray script files listed above already exist in the standard vray install. Those items need to be replaced with new ones that have the DomemasterStereo and LatLongStereo modules integrated in the settings. You should make a backup copy of the original files so you can restore them if required.

**Step 3.**
Copy the Maya script files to your scripts folder.

**Step 4.**
Copy the Maya shelf file `shelf_VrayDomemaster3D.mel` into your Shelves folder.

### Linux 64-bit ###

**Step 1.**
Copy the .so files to the vray-plugins directory:  

`/opt/Autodesk/Maya<Version>/vray/vrayplugins/`

Vray Plugin Files:

    vray_DomemasterStereo.so
    vray_LatLongStereo.so


**Step 3.**
Copy the Vray script files to the Vray scripts folder:  

`/opt/Autodesk/Maya<Version>/vray/scripts`

Vray Script Files:

    attributes.txt
    attributeNodes.txt
    attributeGroups.txt
    vrayAEFunctions.mel
    
**Note:** Several of the vray script files listed above already exist in the standard vray install. Those items need to be replaced with new ones that have the DomemasterStereo and LatLongStereo modules integrated in the settings. You should make a backup copy of the original files so you can restore them if required.

**Step 4.**
Copy the Maya script files to your scripts folder.

**Step 5.**
Copy the Maya shelf file `shelf_VrayDomemaster3D.mel` into your Shelves folder.

## Compiling Instructions ##

### Windows 64-bit ###

**Step 1.**
Install Visual Studio 2013 Community Edition and Vray Standalone (which includes a copy of the Vray plugin SDK).

**Step 2.**
Open a new command prompt and cd into the vray cameras source code folder:

`cd C:\Program Files\Chaos Group\V-Ray\Maya <Version> for x64\samples\vray_plugins\cameras`

**Step 3.**
Copy the Domemaster3D `vray_DomemasterStereo` and `vray_LatLongStereo` source code folders into the vray cameras source code folder. 

**Step 4.**
Set the compiling mode to "release" and compile the source code in Visual Studio 2013 with the following project files:

`vray_DomemasterStereo.vcxproj`  
`vray_LatLongStereo.vcxproj`  

If you are running an older version of Visual Studio you can use the legacy Microsoft Developer Studio project file:  

`vray_DomemasterStereo.dsp`  
`vray_LatLongStereo.dsp`  


### Mac OS X 64-bit ###

The first version of Vray for Mac OS X support has been added to the lens shaders. Mac OS X 10.9 Mavericks or 10.10 Yosemite is required to use the lens shaders.

**Step 1.**
Install Xcode and Vray Standalone (which includes a copy of the Vray plugin SDK).

**Step 2.**
Open a new terminal window and cd into the source code folder.

**Step 3.**
Copy the Vray Lib and Include files into the matching folders located next to the source code files.

**Step 4.**
Use the Mac OS X makefile to compile a new `vray_DomemasterStereo.so` and `vray_LatLongStereo` shader:  

`make -f MakefileMavericks.osx`

**Step 5.**
You can check your compiled .so architecture with the following commands:



	otool -L libvray_LatLongStereo.so  	
	lipo -info libvray_LatLongStereo.so   

	otool -L libvray_DomemasterStereo.so  
	lipo -info libvray_DomemasterStereo.so   

### Linux 64-bit ###

At this point a few of the required Vray on Linux shader compiling details are not known by the Domemaster3D developer. This means Linux support is currently a work-in-progress endeavour.

## Credits ##

- Roberto Ziche created the original `domeAFL_FOV_Stereo` and `LatLong_Stereo` shader for mental ray on 3DS Max.
- Andrew Hazelden ported the shader to Vray.
- Daniel Ott created the original 2D `domeAFL_FOV` for mental ray.
- Thanks to Trygve Wastvedt for his help in getting the Vray for 3DS Max port started.

## Version History ##

### 2015-05-21 ###

**Vray for Maya**

- Added Vray 3.0 for Maya on Mac OS X Support. This build works with Mac OS X 10.9 Mavericks and 10.10 Yosemite only.

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

**Vray Standalone Mac OS X Support**  

- Work has started on updating the Mac OS X based makefiles for the Vray DomemasterStereo and LatLongStereo shaders.

![Plgparams Listing the Shader Parameters on the Mac 1](images/vray_mac_plugin_params_latlongstereo.png)  

![Plgparams Listing the Shader Parameters on the Mac 2](images/vray_mac_plugin_params_domemasterstereo.png) 

**Vray for Softimage Support**

- A basic set of Vray for Sofimage SPDL and DSPreset files have been created for the DomemasterStereo and LatLongStereo lens shaders. The lens shader GUIs show up in Softimage but I haven't figured out the Softimage to Vray translator features yet which are required to export the lens shader data to a .vrscene file or activate the shader in the Vray Frame Buffer window.

![Vray for Softimage Support](images/vray-for-softimage-domemaster3d-shaders.png)

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
- Rotated the DomemasterStereo view by 90 degrees clockwise to match the mental ray `domeAFL_FOV_Stereo` shader.

### Version 0.1 - 2014-11-14 ###

- Initial Vray support.


## To Do List ##

### DomemasterStereo To Dos ###

- Correctly handle the black matting of the domemaster frame when "if (r < 1.0)" is false

### Vray for Maya To Dos ###

- Implement a screen space texture UV re-mapping mode in the lens shaders for the stereo control maps.

### Vray for 3DS Max To Dos ###

- Test the new Vray for 3DS Max shader builds.
- Figure out a way to reduce the noise in the screen space control map based renderings
- Improve the screen space texture map support

### Vray for Softimage To Dos ###

- Finish figuring out how the VRay/SI Bridge SDK works. Get the DomemasterStereo and LatLongStereo lens shader translator working in Softimage.

### Shader Testing To Dos ###

- Generate a .vrscene file with screen space texture maps linked into the DomemasterStereo and LatLongStereo attributes.

