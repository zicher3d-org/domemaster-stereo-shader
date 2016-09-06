# Vray for Maya Domemaster3D #

## Table of Contents ##

*    [Overview](#overview)
*    [Known Issues](#known-issues)
*    [Adding a Vray Lens Shader in Maya](#adding-a-vray-lens-shader-in-maya)
    +    [VRay DomemasterStereo Camera](#vray-domemasterstereo-camera)
    +    [VRay LatLongStereo Camera](#vray-latlongstereo-camera)
    +    [Removing a Lens Shader](#removing-a-lens-shader)
*    [Maya Shader Installation](#maya-shader-installation)
    +    [Windows 64-bit](#windows-64-bit)
    +    [Mac OS 64-bit](#mac-64-bit)
    +    [Linux 64-bit](#linux-64-bit)
*    [Compiling Instructions](#compiling-instructions)
    +    [Windows 64-bit](#windows-64-bit-compile)
    +    [Mac OS 64-bit](#mac-os-64-bit-compile)
    +    [Linux 64-bit](#linux-64-bit-compile)

## <a name="overview"></a>Overview ##

The Domemaster Stereo Shader is a set of fulldome stereo and latlong stereo production lens shaders for 3DS Max, Maya, Softimage, Houdini, Maxwell Studio, Mental Ray Standalone, Vray Standalone, and Arnold Standalone. The lens shaders are available for Mental Ray, Vray, and Arnold, and comes integrated in Maxwell Render version 3.1+.

This guide covers the Vray for Maya version of the Domemaster3D Shaders.

## <a name="known-issues"></a>Known Issues ##

The current version of the Vray Domemaster3D shaders (as of 2015-08-10) is a development build.

More work needs to be done to apply a black overlay to the circular outside area of the domemaster frame. Right now the DomemasterStereo shader will fill the outside circular area in the frame with a solid color based upon the current data at the 0/0/0 X/Y/Z ray angle. Also the shader doesn't apply a circular alpha channel overlay yet.

The Maya integration is still a work in progress. The Domemaster3D shaders are now active in the Maya render view and the custom Vray Extra Attributes are linked into the Vray for Maya .vrscene exporter when the lens shaders are added as Vray Extra Attributes on the camera shape node.

## <a name="adding-a-vray-lens-shader-in-maya"></a>Adding a Vray Lens Shader in Maya #

![Domemaster3D Vray for Maya Shelf](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/domemaster3d-vray-for-maya-shelf.png)

There is now a custom VrayDomemaster3D shelf that makes it easier to use the Domemaster3D lens shaders. In addition to the shelf tools there is also a pair of LatLongStereo and DomemasterStereo camera rigs that work with Maya's native StereoRigManager system.

**Note:** If you want to use the Maya Render View's native stereo preview system, you have to turn off the **Use V-Ray VFB** checkbox in the Maya render settings window.

---

You can add a custom Vray lens shader to a Maya camera using the **VRay Extra Attributes** feature. 

To turn a normal camera into a DomemasterStereo or LatLongStereo formatted camera, select the camera's shape node in the Attribute Editor window. Open the `Attributes > VRay` menu, and select either the `DomemasterStereo camera` or `LatLongStereo camera` items. 

At this point you can turn ON the lens shader by scrolling down to the bottom of the Attribute Editor window and expanding the `Extra VRay Attributes` section. Then enable the appropriate `Treat as a Vray DomemasterStereo` or `Treat as a Vray LatLongStereo Cam` checkbox.

### VRay Post Translate Python Script ###

When the `DomemasterStereo` or `LatLongStereo` Vray Extra Attribute section is enabled with the checkbox a new Vray Render Settings **Mel/Python Callbacks** `Post Translate Python Script` entry is added automatically that allows the `DomemasterStereo` and `LatLongStereo` lens shaders to work in the Maya Render View and the Vray Frame Buffer window.

![Post Translate Python Script](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/post-translate-python-script.png)

The `Post Translate Python Script` field is set to use the following python code:

    import domeVrayRender
    reload(domeVrayRender)
    domeVrayRender.domeVrayTranslator()

### <a name="vray-domemasterstereo-camera"></a>VRay DomemasterStereo Camera ###

![VRay DomemasterStereo Camera](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_DomemasterStereoCamera.png)

### <a name="vray-latlongstereo-camera"></a>VRay LatLongStereo Camera ###

![VRay LatLongStereo Camera](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray_LatLongStereoCamera.png)


### <a name="removing-a-lens-shader"></a>Removing a Lens Shader ###

You can remove a vray lens shader from a Maya camera by opening the `Attributes > VRay` menu and unchecking the specific lens shader. This will remove the lens shader's attributes that are listed in the `Extra VRay Attributes` section.

![Adding Extra Attributes](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/vray-extra-attributes.png)

You can also delete the python code in the **Mel/Python Callbacks** `Post Translate Python Script` field if you want to completly remove all references to the Domemaster3D shader elements from the Maya scene file.

![Clearing the Python Translator](http://www.andrewhazelden.com/projects/domemaster3D/wiki/vray/clear-post-translate-python-script.png)

## <a name="maya-shader-installation"></a>Maya Shader Installation ##

### <a name="windows-64-bit"></a>Windows 64-bit ###

**Step 1.** Download the [Visual Studio 2013 (VC++ 12.0) Redistributable Package](http://www.microsoft.com/en-us/download/details.aspx?id=40784).

**Step 2.** Copy the .dll files to the vray-plugins directory:  

`C:\Program Files\Autodesk\Maya<Version>\vray\vrayplugins\`

Vray Plugin Files:

    vray_DomemasterStereo.dll
    vray_LatLongStereo.dll

**Step 3.** Copy the Vray script files to the Vray scripts folder:  

`C:\Program Files\Autodesk\Maya<Version>\vray\scripts`

Vray Script Files:

    attributes.txt
    attributeNodes.txt
    attributeGroups.txt
    vrayAEFunctions.mel
    domeVrayRender.py
    

**Note:** Several of the vray script files listed above already exist in the standard vray install. Those items need to be replaced with new ones that have the DomemasterStereo and LatLongStereo modules integrated in the settings. You should make a backup copy of the original files so you can restore them if required.

**Step 3.**
Copy the icon files to your user account's Maya icon folder:

`C:\Users\<User Account>\Documents\maya\<Version>\prefs\icons`

**Step 4.**
Copy the Maya script files to your user account's Maya scripts folder, or a shared Maya scripts folder:

`C:\Users\<User Account>\Documents\maya\<Version>\scripts`

**Step 5.**
Copy the Maya shelf files to your user account's Maya shelf folder:

`C:\Users\<User Account>\Documents\maya\<Version>\prefs\shelves`


### <a name="mac-64-bit"></a>Mac 64-bit ###

**Step 1.**
Copy the .so files to the vray-plugins directory:  

`/Applications/Autodesk/maya<Version>/vray/vrayplugins`

Vray Plugin Files:

    vray_DomemasterStereo.so
    vray_LatLongStereo.so

**Step 2.**
Copy the Vray script files to the Vray scripts folder:  

`/Applications/Autodesk/maya<Version>/vray/scripts`

Vray Script Files:

    attributes.txt
    attributeNodes.txt
    attributeGroups.txt
    vrayAEFunctions.mel
    domeVrayRender.py
    

**Note:** Several of the vray script files listed above already exist in the standard vray install. Those items need to be replaced with new ones that have the DomemasterStereo and LatLongStereo modules integrated in the settings. You should make a backup copy of the original files so you can restore them if required.

**Step 3.**
Copy the icon files to your user account's Maya icon folder:

`~/Library/Preferences/Autodesk/maya/<Version>/prefs/icons`

**Step 4.**
Copy the Maya script files to your user account's Maya scripts folder, or a shared Maya scripts folder:

`~/Library/Preferences/Autodesk/maya/<Version>/scripts`

**Step 5.**
Copy the Maya shelf files to your user account's Maya shelf folder:

`~/Library/Preferences/Autodesk/maya/<Version>/prefs/shelves`



### <a name="linux-64-bit"></a>Linux 64-bit ###

**Step 1.**
Copy the .so files to the vray-plugins directory:  

`/usr/Autodesk/Maya<Version>/vray/vrayplugins/`

Vray Plugin Files:

    vray_DomemasterStereo.so
    vray_LatLongStereo.so

**Step 2.**
Copy the Vray script files to the Vray scripts folder:  

`/usr/Autodesk/Maya<Version>/vray/scripts`

Vray Script Files:

    attributes.txt
    attributeNodes.txt
    attributeGroups.txt
    vrayAEFunctions.mel
    domeVrayRender.py
    
**Note:** Several of the vray script files listed above already exist in the standard vray install. Those items need to be replaced with new ones that have the DomemasterStereo and LatLongStereo modules integrated in the settings. You should make a backup copy of the original files so you can restore them if required.

**Step 3.**
Copy the icon files to your user account's Maya icon folder:

`~/maya/<Version>/prefs/icons`

**Step 4.**
Copy the Maya script files to your user account's Maya scripts folder, or a shared Maya scripts folder:

`~/maya/<Version>/scripts`

**Step 5.**
Copy the Maya shelf files to your user account's Maya shelf folder:

`~/maya/<Version>/prefs/shelves`

## <a name="compiling-instructions"></a>Compiling Instructions ##

### Windows 64-bit Compile ###

**Step 1.** Install Visual Studio 2013 Community Edition and Vray Standalone (which includes a copy of the Vray plugin SDK).

**Step 2.** Open a new command prompt and cd into the vray cameras source code folder:

`cd C:\Program Files\Chaos Group\V-Ray\Maya <Version> for x64\samples\vray_plugins\cameras`

**Step 3.** Copy the Domemaster3D `vray_DomemasterStereo` and `vray_LatLongStereo` source code folders into the vray cameras source code folder. 

**Step 4.** Set the compiling mode to "release" and compile the source code in Visual Studio 2013 with the following project files:

`vray_DomemasterStereo.vcxproj`  
`vray_LatLongStereo.vcxproj`  


If you are running an older version of Visual Studio you can use the legacy Microsoft Developer Studio project file:  

`vray_DomemasterStereo.dsp`  
`vray_LatLongStereo.dsp`  


### <a name="mac-os-64-bit-compile"></a>Mac OS X 64-bit Compile ###

The first version of Vray for Mac OS X support has been added to the lens shaders. Mac OS X 10.9 Mavericks or 10.10 Yosemite is required to use the lens shaders.

**Step 1.**
Install Xcode.

**Step 2.**
Open a new terminal window and cd into the source code folder.

**Step 3.**
Copy the Vray SDK Lib and Include files into the matching folders located next to the source code files.

**Step 4.**
Use the Mac OS X makefile to compile a new `vray_DomemasterStereo.so` and `vray_LatLongStereo.so` shader:  

`make -f MakefileMavericks.osx`

**Step 5.**
You can check your compiled .so architecture with the following commands:

You can check your compiled .so architecture with the following commands:

	otool -L libvray_LatLongStereo.so  	
	lipo -info libvray_LatLongStereo.so   

	otool -L libvray_DomemasterStereo.so  
	lipo -info libvray_DomemasterStereo.so 


### <a name="linux-64-bit-compile"></a>Linux 64-bit Compile ###

**Step 1.**
Install GCC.

**Step 2.**
Open a new terminal window and cd into the source code folder.

**Step 3.**
Copy the Vray SDK Lib and Include files into the matching folders located next to the source code files.

**Step 4.**
Use the Linux makefile to compile a new `vray_DomemasterStereo.so` and `vray_LatLongStereo.so` shader:  

`make -f Makefile`
