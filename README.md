# Domemaster3D - End of Support #

As life happens, both Andrew Hazelden and I (Roberto Ziche) need to move on and slow down the amount of the time we spend volunteering on the development of the Domemaster Stereo Shader. It was a nice project and had a surprisingly good adoption rate since my original experiment in mental ray ( http://www.robertoziche.com/domemaster/ ) back in 2010. And I have to thank Andrew for building an amazing Domemaster3D toolset around it, for regularly posting updates of the toolset with Windows/Linux/Mac based installer packages, and promoting it for all these years.

Since both the Domemaster and Latlong lens shaders still include some unique functionality for omni-directional stereo rendering that no one else provides at the moment, we are hoping that production users who need these tools going forward could join the GitHub project as a contributor to help pick up the development effort on creating bug fixes and to assist with the end user support especially for the stereo 3D planetarium production community that this toolset was designed for.

This is a summary of the project status:

1) The most full featured version of the Domemaster and Latlong stereo lens shaders, where I think I implemented all the features I could think of, is the V-ray 3.x for 3ds Max source code. It works nicely in 3ds Max up to version 2018.

2) The Mental Ray version of the lens shaders should work with the recently released Mental Ray 3.14 for Maya/3ds Max/Standalone products. These lens shaders include support for GPU accelerated GI Next rendering and has ray differential sampling built-in. These modes work in Maya for sure, but there has not been extensive testing done in 3ds Max 2018. We assume the Mental Ray lens shaders will keep working for an extended period of time without the need to be re-compiled for the next few releases of Mental Ray 3.x.

3) The Arnold for Maya version of the lens shaders won't work with Arnold 5 as Solid Angle redesigned the rendering APIs. So don't expect the Domemaster3D toolset to work with Maya 2018 since it only includes Arnold 5.

4) The V-Ray 3.x for Maya version of the lens shaders is still a beta and lacks the tools for easily applying screen space stereo control maps. It's also missing some of the more advanced controls found in the V-Ray for 3ds Max version.

We are always available for clarifications, basic support, and to facilitate people who want to join onto the Domemaster Stereo Shader project as a GitHub contributor and help take over the development efforts going forward.

Roberto and Andrew


\<original readme\>

# Domemaster Stereo Shader #

Domemaster3D is a suite of fulldome stereo and LatLong stereo production lens shaders for Mental Ray (3DS Max, Maya, Softimage, Mental Ray Standalone), Vray (Maya, 3DS Max, Vray Standalone), Arnold (MtoA, SItoA, C4DtoA, HtoA, Kick), and a version of the lens model comes integrated in Maxwell Render 3.2+.

The core developers of the Domemaster3D rendering tools are [Roberto Ziche](http://www.robertoziche.com/) and [Andrew Hazelden](http://www.andrewhazelden.com/).  

*The Domemaster3D shaders are distributed under the BSD license.*

**Arnold 5 Compatibility Note:** The new Arnold 5 release has changed their lens shader system. At this point in time the current Domemaster3D shaders are not compatible with Arnold 5. If you need a lens shader today that works with Arnold 5 it is recommended you use the new built-in "VR Camera" module provided by Solid Angle directly.

## Download the Domemaster3D GUI/Manual Installers ##

**Domemaster3D for Max/Maya**  
The GitHub releases tab has the downloads for the latest graphical installers for the Domemaster3D for Max/Maya releases, along with a zipped manual install version:
[https://github.com/zicher3d-org/domemaster-stereo-shader/releases](https://github.com/zicher3d-org/domemaster-stereo-shader/releases)

**Domemaster3D for Softimage**  
The [Domemaster3D for Softimage release can be downloaded here](https://github.com/zicher3d-org/domemaster-stereo-shader/releases/tag/v1.6SI).

## Domemaster3D Raw Files ##

The raw files that are copied to disk by the Domemaster3D Max/Maya installer program can be [found in the repository here](https://github.com/zicher3d-org/domemaster-stereo-shader/tree/master/Domemaster3D%20Installer/installer%20files/Domemaster3D).

## Wiki Documentation Quick Links ##

Check out the Domemaster Stereo Shader [Wiki index page for documentation](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki) on the panoramic rendering toolset. A [Japanese translated version of the wiki](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/%E6%97%A5%E6%9C%AC%E8%AA%9E%E7%89%88%EF%BC%9A-Home) is also available too.

To get started quickly you can read the wiki summary of the [3DS Max Domemaster Stereo Shader](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/3DS-Max-Domemaster3D-Install), the [Maya Domemaster3D Shelf](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/Maya-Domemaster3D-Shelf)  and [Softimage Domemaster3D Toolbar](https://github.com/zicher3d-org/domemaster-stereo-shader/wiki/Softimage-Domemaster3D-Toolbar) features.

**Note:** Vray and Arnold versions of the shaders are currently under development.

----------

Repository for the domemaster stereo shader (all versions)

