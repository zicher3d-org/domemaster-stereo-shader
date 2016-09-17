![DomemasterStereo Shader in Cinema4D + Arnold](http://www.andrewhazelden.com/projects/domemaster3D/wiki/arnold/c4dtoa_domemaster_stereo.png)

## Overview ##

Domemaster3D is a set of fulldome stereo and latlong stereo production lens shaders for Maya/3DS Max/Softimage/Houdini (Arnold)/Cinema4D (Arnold)/Mental Ray/Vray/Arnold/Maxwell Render.

This guide covers the Cinema4D + [Arnold C4DtoA plugin renderer](https://www.solidangle.com/arnold/arnold-for-cinema-4d/) version of the Domemaster Stereo Shaders.

## Known Issues ##

The current version of the Arnold Domemaster3D shaders (as of 2016-09-17) are a development build. At this point in time there is no easy way to create stereoscopic production centric screen space texture maps using Arnold's C4DtoA render nodes. This means a solution has to be developed inside the Domemaster3D shaders that will remap an existing texture map into screen space coordinates.

The LatLongStereo shader generally works fine. The only thing to note is that there is no way to feather out the stereo effect in the zenith and nadir zones using the separation map attribute. 

The LatLongStereo shader should be rendered with a 2:1 aspect ratio to avoid vertically over-rendering the scene's FOV angle.

At this point, the DomemasterStereo shader will render a stereo fulldome image but you will notice something that looks like a small "swirly region" in the zenith part of the fulldome frame. This is due to a lack of a screen space turn map texture. 

## Shader Screenshot ##

![LatLong Stereo](http://www.andrewhazelden.com/projects/domemaster3D/wiki/arnold/c4dtoa_latlong_stereo.png)

## Cinema4D Shader Installation ##

### Windows 64-bit ###

**Step 1.** Download and install the [Visual Studio 2012 (VC++ 11.0) Redistributable Package](http://www.microsoft.com/en-us/download/details.aspx?id=30679).

**Step 2.** Download and install the file "Domemaster3D `<version>` for Maya + 3DS Max on Windows 64-bit" from the [Domemaster Project's GitHub Releases](https://github.com/zicher3d-org/domemaster-stereo-shader/releases) page or from [Andrew Hazelden's blog](http://www.andrewhazelden.com/blog/2012/04/domemaster3d-stereoscopic-shader-for-autodesk-maya/).

**Step 3.** Open up the new Domemaster3D folder:

`C:\Program Files\Domemaster3D\arnold\c4dtoa\shaders\`

Then copy the .dll and .mtd files from to the Domemaster3D C4DtoA **shaders** folder to the Arnold C4DtoA plugin's shaders directory:

`C:\Program Files\MAXON\CINEMA 4D <Version>\plugins\C4DtoA\shaders\`

Maya Shader Files:

    DomemasterStereo.dll
    DomemasterStereo.mtd
    DomemasterWxH.dll
    DomemasterWxH.mtd
    LatLongStereo.dll
    LatLongStereo.mtd

**Step 4.** Open up the Domemaster3D Resource folder :

`C:\Program Files\Domemaster3D\arnold\c4dtoa\res\`

Copy the Domemaster3D Cinema4D UI **res** resource files into the Arnold C4DtoA resource folder:

`C:\Program Files\MAXON\CINEMA 4D <Version>\plugins\C4DtoA\res\`

**Step 5.** Restart Cinema4D and check if the Arnold C4DtoA plugin was able to load the Domemaster3D shaders without any issues.

**Step 6.** The Domemaster3D for Cinema4D + C4DtoA example scene files are located at:

`C:\Program Files\Domemaster3D\arnold\scenes\C4DtoA Sample Project\`

### Mac OS X ###

**Step 1.** Download and install the file "Domemaster3D v1.9 for Maya + 3DS Max on Windows 64-bit" from the [Domemaster Project's GitHub Releases](https://github.com/zicher3d-org/domemaster-stereo-shader/releases) page or from [Andrew Hazelden's blog](http://www.andrewhazelden.com/blog/2012/04/domemaster3d-stereoscopic-shader-for-autodesk-maya/).

**Step 2.** Open up the new Domemaster3D shadersfolder:

`/Application/Domemaster3D/arnold/c4dtoa/shaders/`

Then copy the .dylib and .mtd files from to the Domemaster3D C4DtoA **shaders** folder to the Arnold C4DtoA plugin's shaders directory:

`/Applications/MAXON/CINEMA 4D <Version>/plugins/C4DtoA/shaders/`

Maya Shader Files:

    DomemasterStereo.dylib
    DomemasterStereo.mtd
    DomemasterWxH.dylib
    DomemasterWxH.mtd
    LatLongStereo.dylib
    LatLongStereo.mtd

**Step 3.** Open up the Domemaster3D Resource folder :

`/Application/Domemaster3D/arnold/c4dtoa/res/`

Copy the Domemaster3D Cinema4D UI **res** resource files into the Arnold C4DtoA resource folder:

`/Applications/MAXON/CINEMA 4D <Version>/plugins/C4DtoA/res/`

**Step 4.** Restart Cinema4D and check if the Arnold C4DtoA plugin was able to load the Domemaster3D shaders without any issues.

**Step 5.** The Domemaster3D for Cinema4D + C4DtoA example scene files are located at:

`/Application/Domemaster3D/arnold/scenes/C4DtoA Sample Project/`

## How are the Lens Shaders Applied in Cinema4D? ##

To use the Domemaster3D lens shaders in Cinema4D + C4DtoA you need to start by adding a new camera to the scene.

![Add a Camera](http://www.andrewhazelden.com/projects/domemaster3D/wiki/arnold/c4dtoa_add_a_camera.png)

Then you need to right click on the camera in the Cinema4D object view, and then add a C4DtoA Tag > Arnold Parameters entry from the popup contextual menu.

![Adding the Tags](http://www.andrewhazelden.com/projects/domemaster3D/wiki/arnold/c4dtoa_adding_the_tags.png)

When the new Arnold Parameters tag is selected in the Object view you can edit the Arnold Tag attributes.

To enable the custom lens shaders, select the camera tab in Arnold Tag window and enable the **Custom type** checkbox. The **Camera** options menu lets you choose the active lens shader that will be applied to the camera when a new Arnold C4DtoA rendering is done. 

When the Domemaster3D shaders are installed you will have the entries DomemasterStereo, DomemasterWxH, and LatLongStereo added to this list.

![](http://www.andrewhazelden.com/projects/domemaster3D/wiki/arnold/c4dtoa_arnold_parameters.png)

The Main tab in the Arnold Tag attributes section gives you access to all of the lens shaders custom attributes. 

### Developer Note on the Beta Shaders UI ###

At this point in time I am still working on customizing the appearance of the lens shaders controls inside of Cinema4D so things like the Camera setting which is still a number field will be turned into a popup menu with options like Center, Left, and Right.

With the current beta version of the DomemasterStereo and LatLong Stereo shaders, the **Camera** control number field settings are:

- Camera Center View = 0
- Camera Left View = 1
- Camera Right View = 2


In C4DtoA, the Arnold lens shader’s metadata (.mtd) file is used to set the default settings like the minimum and maximum values for each of the controls so it is possible for an end user to adjust the default values to meet their production needs.

Right now the Domemaster3D for C4DtoA shaders don’t have the stereo control texture maps enabled. I am still working out how to link them into the Cinema4D UI and still have to figure out the Arnold screen space texture mapping system.

This is the current Domemaster Stereo Shader UI in C4DtoA:

![Domemaster Stereo](http://www.andrewhazelden.com/projects/domemaster3D/wiki/arnold/c4dtoa_domemaster_stereo_shader.png)

This is the current LatLong Stereo Shader UI in C4DtoA:

![LatLong Stereo](http://www.andrewhazelden.com/projects/domemaster3D/wiki/arnold/c4dtoa_latlong_stereo_shader.png)

This is the current DomemasterWxH Shader UI in C4DtoA:

![Domemaster WxH](http://www.andrewhazelden.com/projects/domemaster3D/wiki/arnold/c4dtoa_domemaster_wxh_shader.png)

