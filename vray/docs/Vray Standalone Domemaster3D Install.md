# Vray Standalone Domemaster3D Install #

## Table of Contents ##

*    [Overview](#overview)
*    [Known Issues](#known-issues)
*    [Vray Standalone](#vray-standalone)
    +    [DomemasterStereo in a VRSCENE File](#domemasterstereo-in-a-vrscene-file)
    +    [LatLongStereo in a VRSCENE File](#latlongstereo-in-a-vrscene-file)
*    [Vray Standalone Shader Installation](#vray-standalone-shader-installation)
*    [Verify the Shader is Loaded in Vray](#verify-the-shader-is-loaded-in-vray)
    +    [Vray Shader Parameters Screenshot](#vray-shader-parameters-screenshot)
    +    [Listing the Nodes](#listing-the-nodes)
        *    [Windows Node List](#windows-node-list)
        *    [macOS Node List](#mac-node-list)
        *    [Linux Node List](#linux-node-list)
    +    [Node Parameters](#node-parameters)
        *    [plgparams.exe DomemasterStereo](#plgparamsexe-domemasterstereo)
        *    [plgparams.exe LatLongStereo](#plgparamsexe-latlongstereo)
        *    [Windows Parameters](#windows-parameters)
        *    [macOS Parameters](#mac-parameters)
        *    [Linux Parameters](#linux-parameters)
*    [Rendering the Example Scenes](#rendering-the-example-scenes)

## <a name="overview"></a>Overview ##

The Domemaster Stereo Shader is a set of fulldome stereo and latlong stereo production lens shaders for 3DS Max, Maya, Softimage, Houdini, Maxwell Studio, Mental Ray Standalone, Vray Standalone, and Arnold Standalone. The lens shaders are available for Mental Ray, Vray, and Arnold, and comes integrated in Maxwell Render version 3.1+.

This guide covers the Vray Standalone version of the Domemaster3D Shaders.

## <a name="known-issues"></a>Known Issues ##

The current version of the Vray Domemaster3D shaders (as of 2015-05-23 ) is a development build.

The Vray Standalone version generally works without too many issues.

More work needs to be done to apply a black overlay to the circular outside area of the domemaster frame. Right now the DomemasterStereo shader will fill the outside circular area in the frame with a solid color based upon the current data at the 0/0/0 X/Y/Z ray angle. Also the shader doesn't apply a circular alpha channel overlay yet.

## <a name="vray-standalone"></a>Vray Standalone ##

Right now the DomemasterStereo and LatLongStereo shaders are accessible from Vray Standalone and Vray RT version 2.5 / 3.0 using the `vray.exe` command line program. Until the Maya and 3DS Max shader integrations are complete you will have to add the DomemasterStereo and LatLongStereo camera parameters to your .vrscene files manually. 

Andrew Hazelden's [Vray Syntax Highlighter](https://github.com/AndrewHazelden/Vray-Scene-Syntax-Highlighter) module for Notepad++, GEDIT, BBEdit, and TextWrangler is a good tool for simplifying the process of editing a .vrscene file.

### <a name="domemasterstereo-in-a-vrscene-file"></a>DomemasterStereo in a VRSCENE File ###

![DomemasterStereo Renderings](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_standalone_domemasterStereo_render.png)

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

### <a name="latlongstereo-in-a-vrscene-file"></a>LatLongStereo in a VRSCENE File ###

![LatLongStereo Renderings](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_standalone_LatLongStereo_render.png)

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

## <a name="vray-standalone-shader-installation"></a>Vray Standalone Shader Installation ##

### Windows 64-bit ###

**Step 1.** Download the [Visual Studio 2013 (VC++ 12.0) Redistributable Package](http://www.microsoft.com/en-us/download/details.aspx?id=40784).

**Step 2.** Copy the .dll files to the vray-plugins directory:  

`C:\Program Files\Chaos Group\V-Ray\Standalone for x64\bin\x64\vc101\plugins`

Vray Plugin Files:

    vray_DomemasterStereo.dll
    vray_LatLongStereo.dll

**Step 3.** Edit the Windows environment variables and add an entry for the  `VRAY_PLUGINS_x64` Vray standalone plugins path location.

![Adding an ENV Var](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/adding-a-new-env-var.png)

For Vray Standalone 2.5 the standard `VRAY_PLUGINS_x64` setting would be:   

`VRAY_PLUGINS_x64`  
`C:\Program Files\Chaos Group\V-Ray\Standalone for x64\bin\x64\vc101\plugins`


## <a name="verify-the-shader-is-loaded-in-vray"></a>Verify the Shader is Loaded in Vray ##

### <a name="vray-shader-parameters-screenshot"></a>Vray Shader Parameters Screenshot ###

![Plgparams Listing the Shader Parameters](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_plugin_parameters.png)  

![Plgparams Listing the Shader Parameters on the macOS 1](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_mac_plugin_params_latlongstereo.png)  

![Plgparams Listing the Shader Parameters on the macOS 2](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_mac_plugin_params_domemasterstereo.png)  

### <a name="listing-the-nodes"></a>Listing the Nodes ###

You can list all of the active Vray Shader nodes using the plugin parameters tool:

#### <a name="windows-node-list"></a>Windows Node List ####

`cd C:\Program Files\Chaos Group\V-Ray\Standalone for x64\bin\x64\vc101\`  
`plgparams.exe -list`

#### <a name="mac-node-list"></a>macOS Node List ####

`cd /Applications/ChaosGroup/V-Ray/Standalone_for_snow_leopard_x86/bin/snow_leopard_x86/gcc-4.2/`  
`./plgparams.bin -list`

#### <a name="linux-node-list"></a>Linux Node List ####

`./plgparams.bin -list`

### <a name="node-parameters"></a>Node Parameters ###

If you run the plgparams with the shader name listed you can see the individual node parameters. If you get a plgparams error asking for the -plugindir that means you are missing the vray plugins environment variable such as `VRAY_PLUGINS_x64` or `VRAY_PLUGINS_x86`.
	
#### <a name="plgparamsexe-domemasterstereo"></a>plgparams.exe DomemasterStereo ####

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

#### <a name="plgparamsexe-latlongstereo"></a>plgparams.exe LatLongStereo ####

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

#### <a name="windows-parameters"></a>Windows Parameters ####

`plgparams.exe DomemasterStereo`  
`plgparams.exe LatLongStereo`  

#### <a name="mac-parameters"></a>macOS Parameters ####

`./plgparams.bin DomemasterStereo`  
`./plgparams.bin LatLongStereo`  

#### <a name="linux-parameters"></a>Linux Parameters ####

`./plgparams.bin DomemasterStereo`  
`./plgparams.bin LatLongStereo`  


## <a name="rendering-the-example-scenes"></a>Rendering the Example Scenes ##

If you navigate to the Domemaster3D vray scenes folder you can try rendering the sample vray standalone vrscene files.

    vray.exe -sceneFile="vray 2 DomemasterStereo.vrscene"  
    vray.exe -sceneFile="vray 2 LatLongStereo.vrscene"  

    vray.exe -sceneFile="LatLongStereo_Boxworld_center.vrscene"  
    vray.exe -sceneFile="LatLongStereo_Boxworld_left.vrscene"  
    vray.exe -sceneFile="LatLongStereo_Boxworld_right.vrscene"  

    vray.exe -sceneFile="DomemasterStereo_Boxworld_center.vrscene"  
    vray.exe -sceneFile="DomemasterStereo_Boxworld_left.vrscene"  
    vray.exe -sceneFile="DomemasterStereo_Boxworld_right.vrscene"  

