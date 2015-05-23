# Vray for Max Domemaster3D #

## Table of Contents ##

*    [Overview](#overview)
*    [Known Issues](#known-issues)
*    [Vray for 3DS Max Shader Installation](#vray-for-3ds-max-shader-installation)
*    [Vray RT for 3DS Max Shader Installation](#vray-rt-for-3ds-max-shader-installation)
*    [Vray for 3DS Max Lens Shaders](#vray-for-3ds-max-lens-shaders)

## <a name="overview"></a>Overview ##

The Domemaster Stereo Shader is a set of fulldome stereo and latlong stereo production lens shaders for 3DS Max, Maya, Softimage, Houdini, Maxwell Studio, Mental Ray Standalone, Vray Standalone, and Arnold Standalone. The lens shaders are available for Mental Ray, Vray, and Arnold, and comes integrated in Maxwell Render version 3.1+.

This guide covers the Vray for 3DS Max version of the Domemaster3D Shaders.

## <a name="known-issues"></a>Known Issues ##

The current version of the Vray Domemaster3D shaders (as of 2015-05-23 ) is a development build.

More work needs to be done to apply a black overlay to the circular outside area of the domemaster frame. Right now the DomemasterStereo shader will fill the outside circular area in the frame with a solid color based upon the current data at the 0/0/0 X/Y/Z ray angle. Also the shader doesn't apply a circular alpha channel overlay yet.

The first working version of the 3DS Max source code has been added and there are development shader builds for Vray 3.0 on 3DS Max 2015 and 3DS Max 2014, and Vray 2.5 for 3DS Max 2015, and Vray 2.4 for 3DS Max 2013.

## <a name="vray-for-3ds-max-shader-installation"></a>Vray for 3DS Max Shader Installation ##

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
    vraydomemasterstereo2013.dlo


**Step 3.**
If you get an "Error Loading Plugin-DLL" error message in 3DS Max when when you try and load the shader it means you haven't installed the Microsoft Visual Studio 2013 x64 Redistributable library that was mentioned as a required stage in **Step 1**. Now is a good time to go back to step 1 and actually install the library file!

![Visual Studio 2013 Library Missing Error](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray-max-no-vs2013-libs.png)
    
## <a name="vray-rt-for-3ds-max-shader-installation"></a>Vray RT for 3DS Max Shader Installation ##

### Windows 64-bit ###

**Step 1.** Download the [Visual Studio 2013 (VC++ 12.0) Redistributable Package](http://www.microsoft.com/en-us/download/details.aspx?id=40784).

**Step 2.** Copy the .dll files to the Vray RT plugins directory.

`C:\Program Files\Chaos Group\V-Ray\RT for 3ds Max <Max Version> for x64\bin\plugins`

Note: Change `<Max Version>` to the release number of 3DS Max. Example: Write in 2015 for the <Max Version> if you are using 3DS Max 2015.

Vray Plugin Files:  

    vray_DomemasterStereo.dll (Not compiled yet)
    vray_LatLongStereo.dll
    
**Step 3.** Edit the Windows environment variables and add an entry for the  `VRAY_PLUGINS_x64` Vray RT plugins path location.

`C:\Program Files\Chaos Group\V-Ray\RT for 3ds Max <Max Version> for x64\bin\plugins`

Note: Change `<Max Version>` to the release number of 3DS Max. Example: Write in 2015 for the `<Max Version>` if you are using 3DS Max 2015.

**Step 4.** Edit the Windows ENV Path and add the VRay RT `Bin` folder to the list.

`;C:\Program Files\Chaos Group\V-Ray\RT for 3ds Max <Max Version> for x64\bin`

Note: Change `<Max Version>` to the release number of 3DS Max. Example: Write in 2015 for the `<Max Version>` if you are using 3DS Max 2015.

## <a name="vray-for-3ds-max-lens-shaders"></a>Vray for 3DS Max Lens Shaders ##

Here are two screenshots showing the Vray for 3DS Max beta versions of the Domemaster3D lens shaders.

![Vray for 3DS Max DomemasterStereo Shader](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_max_domemaster_stereo.png)

![Vray for 3DS Max LatLongStereo Shader](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_max_latlong_stereo.png)

There are two new controls added for the first time in the Vray for 3DS Max lens shaders: 

- A Neck Offset allows you to simulate the effect of a physical 360&deg; panoramic camera rig where the lens nodal points are shifted away from the camera origin.

![Neck Offset](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/neck-offset.png)

- The hemirect (hemi-equirectangular) checkbox in the LatLongStereo shader that lets you render a partial LatLong image where the top edge of the rendering starts aligned to the zenith pole region. This is useful if you want to render a cropped 360&deg; x 90&deg; latlong image that could then be converted in post into a 180&deg; domemaster (angular fisheye) image with no unused/over-rendered areas in the source image.

