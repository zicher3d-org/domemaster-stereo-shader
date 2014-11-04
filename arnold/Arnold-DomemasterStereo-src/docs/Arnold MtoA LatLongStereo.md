# Arnold MtoA LatLongStereo #

## Overview ##

![Arnold Domemaster3D Shelf](images/arnold-domemaster3d-shelf.png)

The LatLongStereo shader is added to a Maya scene using the ArnoldDomemaster3D Shelf tool. 

When you run the LatLongStereo shelf tool it adds a custom ArnoldLatLongStereo camera rig to the scene that has the left and right cameras set up automatically. The left camera LatLongStereo attributes are used to drive the stereoscopic settings for both the left and right cameras. This means you only have to change the **Zero Parallax Distance** or **Camera Separation** setting in one place.

To change the LatLongStereo attributes, select the camera in your scene. Open the attribute editor and switch to the camera's shape node. The lens shader is listed in the Arnold section.

![LatLongStereo Shader Attributes](images/latlongstereo_attributes.png)

## LatLong Stereo Shader Controls ##

**Camera**: Choices are **Center**/**Left**/**Right**. Selects the camera to use for rendering. **Center** skips 90% of the calculations and gives you a highly optimized standard latlong image.

**Field of View Vertical**: Controls the vertical FOV angle (in degrees) of the rendered Latitude/Longitude image.

**Field of View Horizontal**: Controls the horizontal FOV angle (in degrees) of the rendered Latitude/Longitude image.

**Zero Parallax Distance** (focus plane): This is the distance at which the left and right camera's line of sight converges.

**Camera Separation**: The initial separation of the left and right cameras.

**Zenith Mode**: This attribute allows you to adjust the `LatLongStereo` lens shader to work with either a horizontal orientation (Zenith Mode OFF), or an upwards / vertical orientation (Zenith Mode ON) that lines up with the upright view orientation of the `Domemaster Stereo Shader` shaders.

### Custom Maps ###
**Separation Map**: A value between 0-1 that multiples the **Camera Separation**. This attribute is meant to be used with a grayscale texture mapped to the screen space. It's used to control the amount of 3D effect, and eliminate it where desired.

### Image Orientation ###

**Flip X**: Flips the view horizontally

**Flip Y**: Flips the view vertically

### Options ###

**Exposure**: This attribute allows you to control the overall brightness of the final rendered frame.

## Screen Space Texture Maps ##

You can control the stereoscopic effect seen in the LatLongStereo shader with the help of control texture maps. The `LatLong Stereo` shader's **Separation Multiplier** attribute supports control texture mapping. The images have to be applied using screen space coordinates.

