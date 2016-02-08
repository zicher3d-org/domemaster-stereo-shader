# Vray for Max Domemaster3D #

## Table of Contents ##

*    [Overview](#overview)
*    [Known Issues](#known-issues)
*    [Vray for 3DS Max Lens Shaders](#vray-for-3ds-max-lens-shaders)
    *    [Domemaster Stereo Shader Controls](#domemaster-stereo)
    *    [LatLong Stereo Shader Controls](#latlong-stereo)
*    [Vray for 3DS Max Shader Installation](#vray-for-3ds-max-shader-installation)
*    [Vray RT for 3DS Max Shader Installation](#vray-rt-for-3ds-max-shader-installation)

## <a name="overview"></a>Overview ##

The Domemaster Stereo Shader is a set of fulldome stereo and latlong stereo production lens shaders for 3DS Max, Maya, Softimage, Houdini, Maxwell Studio, Mental Ray Standalone, Vray Standalone, and Arnold Standalone. The lens shaders are available for Mental Ray, Vray, and Arnold, and comes integrated in Maxwell Render version 3.2+.

This guide covers the Vray for 3DS Max version of the Domemaster3D Shaders.

## <a name="known-issues"></a>Known Issues ##

The current version of the Vray Domemaster3D shaders (as of 2016-02-05 ) is a development build.

There is a new version of the Vray Domemaster3D shaders that has been compiled for Vray 3.X and it has an updated GUI with new controls like pole correction options and support for parallel stereo rendering.

If you need access to the earlier version of the shaders builds for Vray 3.2 on 3DS Max 2015, Vray 3.0 on 3DS Max 2015 and 3DS Max 2014, and Vray 2.5 for 3DS Max 2015, and Vray 2.4 for 3DS Max 2013 you can find those shaders in the `C:\Program Files\Domemaster3D/vray/install/3dsmax/vray legacy builds\` folder.

More work needs to be done to apply a black overlay to the circular outside area of the domemaster frame. Right now the DomemasterStereo shader will fill the outside circular area in the frame with a solid color based upon the current data at the 0/0/0 X/Y/Z ray angle. Also the shader doesn't apply a circular alpha channel overlay yet.

## <a name="vray-for-3ds-max-lens-shaders"></a>Vray for 3DS Max Lens Shaders ##

### <a name="domemaster-stereo"></a>Domemaster Stereo Shader Controls ###

Here is a preview of the Domemaster Stereo shader's user interface:

![Vray for 3DS Max DomemasterStereo Shader](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_max_domemaster_stereo_v1.9.2.png)

#### Camera Controls ####

![Camera Controls](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_max_domemaster_stereo_camera.png)

**Type**: Select the stereo camera view to use for rendering. You can choose between the **Center**/**Left**/**Right** camera views in this options menu. The **Center** option skips 90% of the calculations and gives you a highly optimized standard fisheye image.

**Field of View Angle**: Controls the field of view for the rendered angular fisheye image. A "Domemaster" formatted image has a 180 degree field of view, and a "light probe" style angular fisheye image has a 360 degree field of view.

**Separation**: The initial separation of the left and right cameras.

**Vertical Mode**: Enables the vertical dome mode which automatically adjusts the head turn setting and adds a turn compensation for the upper and lower part of the dome. It's a simplified and optimized version of the Dome Tilt Compensation with a 90 degree tilt angle, but with a different automatic handling of the top and bottom pinch correction. It is faster and easier to use.

#### Separation/Turn/Tilt Controls ####

![Separation/Turn/Tilt Controls](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_max_domemaster_stereo_sep_turn_tilt_control_maps.png)

**Poles Correction**: This checkbox allows you to enable an automatic zenith and nadir zone stereo falloff effect. This gives another way to achieve the results you would typically need to use a separation map texture for.

**Start Angle**: This defines the beginning angle for the poles stereo falloff effect. The horizon is 0 degrees, and the poles are at +90 and -90. If you specify a value of 60, the fading effect for the poles will start at +60 and -60.

**End Angle**: This defines the end angle for the "nadir" pole stereo falloff effect. At this angle, the stereo effect will be off (Left and Right cameras will be coincident). We suggest to use a value smaller than 90 degrees or you won't be able to converge your eyes at all at the poles.

The default values will satisfy most cases. A narrow angle between Start and End results in a visible distortion of straight lines.

For a standard 180 degrees domemaster image the nadir will almost never be visible.

You can combine the effects of the separation map and the pole correction options if you need more control over the stereo effects in the image.

**Separation Multiplier**: A value between 0-1 that multiples the **Camera Separation**. It's used to control the amount of 3D effect, and eliminate it where desired.

**Turn Multiplier**: A value 0-1 that controls the amount of the head turn. Typical use, keep the head straight while looking at the top of the dome.

**Head Tilt**: A value 0-1 (with 0.5 being the "neutral" value) that tilts the cameras (or head) left/right. This attribute is meant to be used with a grayscale texture mapped using the screen space. 0 means 90 degrees to the left, 1 means 90 degrees to the right.

Note: The Head Tilt map is almost never used. All the other controls should generate images that are always pretty well aligned to the viewer eyes.

Important: Maps used for the various multipliers and tilt settings will have to be custom made for the proper dome tilt.

#### Parallax Controls ####

![Parallax Controls](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_max_parallax.png)

**Parallel Cameras**: This checkbox allow you to choose if you want the lens shader to operate in a converged or parallel stereo rendering mode. When the Parallel Cameras checkbox is disabled you get the typical converged stereo output that was present in previous Domemaster3D releases.

**Parallax Distance**: This is the zero parallax distance for the stereo rendering This is also known as the focus plane. This value is the distance at which the left and right camera's line of sight converges.
This value is ignored when Parallel Cameras is enabled.

#### Dome Controls ####

![Dome Controls](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_max_domemaster_stereo_dome_tilt.png)

**Forward Tilt**: This control allows you to adjust the Dome forward tilt angle in degrees. This will keep the fulldome camera rig and the viewer's head vertical while the simulated dome is rotated forward. Note that this value is not used unless you enable **Dome Tilt Compensation** checkbox.

**Dome Tilt Compensation**: This option will activate the Forward Tilt option that will shift all the lens shader calculations by the number of degrees specified in **Forward Tilt**.

#### Neck Controls ####

![Neck Controls](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_max_neck_controls.png)

**Forward Offset**: This control allows you to simulate the "neck offset" effect of a physical 360&deg; panoramic live action camera rig where the lens nodal points are shifted away from the camera origin. Make sure to keep the Forward Offset value lower than the nearest geometry in the scene or the forward offset will cause the camera to be pushed inside of it.

**Force Horizontal**: This control allows you to change how the neck offset simulation is calculated and lock the neck offset to a flat plane.

**Note**: The neck offset feature is primarily used with the LatLong Stereo lens shader. It is available in the Domemaster Stereo shader only for compatibility. Poles can get some odd distortions due to the different projection method.

![Neck Offset](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/neck-offset.png)

#### Image Controls ####

![Image Controls](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_max_image_controls.png)

**Flip X**: Flips the rendered view horizontally.

**Flip Y**: Flips the rendered view vertically.


### <a name="latlong-stereo"></a>LatLong Stereo Shader Controls ###

Here is a preview of the LatLong Stereo shader's user interface:

![Vray for 3DS Max LatLong Stereo Shader](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_max_latlong_stereo_v1.9.2.png)

#### Camera Controls ####

![Camera Controls](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_max_latlong_stereo_camera.png)

**Type**: Select the stereo camera view to use for rendering. You can choose between the **Center**/**Left**/**Right** camera views in this options menu. The **Center** option skips 90% of the calculations and gives you a highly optimized standard LatLong image.

**Separation**: The initial separation of the left and right cameras.

**Vertical Field of View**: Controls the vertical FOV angle (in degrees) of the rendered Latitude/Longitude image. The default value is 180&deg;.

**Hemirect**: The Hemirect (hemi-equirectangular) checkbox lets you render a partial LatLong image where the top edge of the rendering starts aligned to the zenith pole region. This is useful if you want to render a cropped 360&deg; x 90&deg; LatLong image that could then be converted in a compositing package into a 180&deg; domemaster (angular fisheye) image with no unused/over-rendered areas in the source image.

**Horizontal Field of View**: Controls the horizontal FOV angle (in degrees) of the rendered Latitude/Longitude image. The default value is 360&deg;.

**Zenith Mode**: This attribute allows you to adjust the `LatLong Stereo` lens shader to work with either a horizontal orientation (Zenith Mode OFF), or an upwards / vertical orientation (Zenith Mode ON) that lines up with the upright view orientation of the `DomeAFL FOV` / `Domemaster Stereo Shader` shaders.

#### Separation Controls ####

![Separation Controls](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_max_latlong_stereo_separation.png)

**Poles Correction**: This checkbox allows you to enable an automatic zenith and nadir zone stereo falloff effect. This gives another way to achieve the results you would typically need to use a separation map texture for.

**Start Angle**: This defines the beginning angle for the poles stereo falloff effect. The horizon is 0 degrees, and the poles are at +90 and -90. If you specify a value of 60, the fading effect for the poles will start at +60 and -60.

**End Angle**: This defines the end angle for the "nadir" pole stereo falloff effect. At this angle, the stereo effect will be off (Left and Right cameras will be coincident). We suggest to use a value smaller than 90 degrees or you won't be able to converge your eyes at all at the poles.

The default values will satisfy most cases. A narrow angle between Start and End results in a visible distortion of straight lines.

You can combine the effects of the separation map and the pole correction options if you need more control over the stereo effects in the image.

**Separation Multiplier**: A value between 0-1 that multiples the **Camera Separation**. This attribute is meant to be used with a grayscale texture mapped to the screen space. It's used to control the amount of 3D effect, and eliminate it where desired.

#### Parallax Controls ####

![Parallax Controls](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_max_parallax.png)

**Parallel Cameras**: This checkbox allow you to choose if you want the lens shader to operate in a converged or parallel stereo rendering mode. When the Parallel Cameras checkbox is disabled you get the typical converged stereo output that was present in previous Domemaster3D releases.

**Parallax Distance**: This is the zero parallax distance for the stereo rendering This is also known as the focus plane. This value is the distance at which the left and right camera's line of sight converges.
This value is ignored when Parallel Cameras is enabled.

#### Neck Controls ####

![](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_max_neck_controls.png)

**Forward Offset**: This control allows you to simulate the "neck offset" effect of a physical 360&deg; panoramic live action camera rig where the lens nodal points are shifted away from the camera origin. Make sure to keep the Forward Offset value lower than the nearest geometry in the scene or the forward offset will cause the camera to be pushed inside of it.

**Force Horizontal**: This control allows you to change how the neck offset simulation is calculated and lock the neck offset to a flat plane.

![Neck Offset](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/neck-offset.png)


#### Image Controls ####

![Image Controls](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_max_image_controls.png)

**Flip X**: Flips the rendered view horizontally.

**Flip Y**: Flips the rendered view vertically.


## <a name="screen-space-textures"></a>Screen Space Texture Maps ##

You can control the stereoscopic effect seen in the LatLong Stereo and Domemaster Stereo shaders with the help of control texture maps. The `LatLong Stereo` shader's **Separation Multiplier**, and the `Domemaster Stereo Shader` shader's **Separation Multiplier**, **Turn Multiplier**, **Head Tilt** attributes support control texture mapping. The images hare applied automatically using screen space coordinates.

To get you started there is a collection of pre-made control texture maps for the Domemaster3D shaders in the following folder:  

`C:\Program Files\Domemaster3D\sourceimages\`

You can also create your own control map images if you want to precisely control the stereoscopic effect across your scene and sculpt the stereo depth in your renderings.

Important: if you get jagged edges in your renderings where the maps have a gradient, make sure you have the proper map filtering or use 16-bit grayscale maps.

### Domemaster Stereo Control Maps ###

![Domemaster Stereo Control Maps](http://www.andrewhazelden.com/projects/domemaster3D/wiki/3dsmax/domemaster-control-maps.png)

`head_tilt_map.png`  
`separation_map.png`  
`turn_map.png`  

### LatLong Stereo Control Maps ###

![LatLong Stereo Control Maps](http://www.andrewhazelden.com/projects/domemaster3D/wiki/3dsmax/latlong-control-maps.png)

`latlong_separation_map.png`

Consider using the new automatic poles correction instead of a map to fix the distortions at the zenith and nadir. Use the map in combination with the automatic poles correction if you need to manually control the 3D effect in other parts of the image.

## <a name="vray-for-3ds-max-shader-installation"></a>Vray for 3DS Max Shader Installation ##

There are now Vray 2.4 for 3DS Max 2013, Vray 2.5 for 3DS Max 2015, Vray 3.0 for 3DS Max 2015 & Vray 3.0 for 3DS Max 2014, and Vray 3.2 on 3DS Max 2016 builds of the Domemaster3D shaders.

### Windows 64-bit ###

**Step 1.** Download the [Visual Studio 2013 (VC++ 12.0) Redistributable Package](http://www.microsoft.com/en-us/download/details.aspx?id=40784).

**Step 2.** Copy the .dlo files to the Vray for 3DS Max plugins directory.

`C:\Program Files\Autodesk\3ds Max <Max Version>\plugins\vrayplugins`

Note: Change `<Max Version>` to the release number of 3DS Max. Example: Write in 2015 for the `<Max Version>` if you are using 3DS Max 2015.

Vray Plugin Files:

    vraylatlongstereo2016.dlo
    vraydomemasterstereo2016.dlo

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
