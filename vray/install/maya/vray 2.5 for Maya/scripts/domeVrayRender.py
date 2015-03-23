"""
domeVrayRender.py
Domemaster3D for Vray for Maya v1.6.3
2015-02-28 2.11 am
by Andrew Hazelden
-----------------------------

This script will prepare a Vray Scene for rendering in Maya using the DomemasterStereo or LatLongStereo shaders.

Run the python code using:
import domeVrayRender
reload(domeVrayRender)
domeVrayRender.domeVrayTranslator()

"""

# Find out the current camera's name 
# Example: camera = domeGetCamera()
def domeGetCamera():
  import re
  import vray.utils as vr
   
  nodes = vr.findByType('CameraDefault')
  #nodeListSize = len(nodes)
  #print("Nodes Length: " + str(nodeListSize))
  if nodes[0] is None:
    print("The Camera List is Empty!")
    return "None"
  else:
    cameraPlugin = str(nodes[0])
    # cameraPlugin Result: Plugin('RenderCamLeftShape')
  
  # Get the camera name from the Plugin text string
  matches=re.findall(r"\'(.+?)\'",cameraPlugin)
  camera = matches[0]
  # Result: perspShape
  #print('Active Render Camera: ' + camera)
  return camera
 
 
 # Find out the current stereo camera view
 # Example: stereo_view = domeGetStereoView()
def domeGetStereoView():
  # Find out the current camera's name 
  camera = domeGetCamera()

  stereo_view = 0
  if 'Left' in camera:
    #print('Detected Left Camera')
    stereo_view = 1
  elif 'Right' in camera:
    #print('Detected Right Camera')
    stereo_view = 2
  elif 'None' in camera:
    #print('Rendering as the Center Camera')
    stereo_view = 0
  else:
    #print('Rendering as the Center Camera')
    stereo_view = 0
    
  return stereo_view

  
# Check if the LatLongStereo Vray Extra Attributes Exist
def domeVrayHasLatLongStereoAttrs():
  # Check if the vrayLatLongStereoOn Attr Exists
  if domeVrayGetAttrNumValue("vrayLatLongStereoOn") == 1:
    print("This is a LatLongStereo Camera.")
    return 1
  else:
    #print("This is not a LatLongStereo Camera.")
    return 0
    
# Check if the DomemasterStereo Vray Extra Attributes Exist
def domeVrayHasDomemasterStereoAttrs():
  # Check if the vrayDomemasterStereoOn Attr Exists
  if domeVrayGetAttrNumValue("vrayDomemasterStereoOn") == 1:
    print("This is a DomemasterStereo Camera.")
    return 1
  else:
    #print("This is not a DomemasterStereo Camera.")
    return 0

# Check if a vray camera extra attribute exists and get it's current string value
# Example: extraAttr = domeVrayGetAttrStringValue(flip_x)
def domeVrayGetAttrStringValue(attrName):
  import maya.cmds as cmds
  
  # Find out the current camera's name 
  camera = domeGetCamera()
  
  # Check if the Vray Extra Attribute Exists
  attrFullName = (camera+"."+attrName)
  if cmds.objExists(attrFullName):
    attrValue = cmds.getAttr(attrFullName)
    print("["+ attrFullName + "] " + str(attrValue))
    return attrValue
  else:
    #print("The \"" + attrFullName + "\" attribute does not exist.\n")
    return ""
    
    
# Check if a vray camera extra attribute exists and get it's current int value
# Example: extraAttr = domeVrayGetAttrNumValue(flip_x)
def domeVrayGetAttrNumValue(attrName):
  import maya.cmds as cmds
  
  # Find out the current camera's name 
  camera = domeGetCamera()
  
  # Check if the Vray Extra Attribute Exists
  attrFullName = (camera+"."+attrName)
  if cmds.objExists(attrFullName):
    attrValue = cmds.getAttr(attrFullName)
    print("["+ attrFullName + "] " + str(attrValue))
    return attrValue
  else:
    #print("The \"" + attrFullName + "\" attribute does not exist.\n")
    return ""
    
 # Configure the vray lens shader is based upon the current camera's Vray Extra attributes
def domeVrayTranslator():
  import maya.cmds as cmds
  import vray.utils as vr
  
  # Find out the current camera name
  #camera = "perspShape"
  camera = domeGetCamera()

  
  # Make sure there is an active camera
  if camera == "None":
    print('The active render camera is unknown: ' + camera)
  else:
    print('Active Render Camera: ' + camera)
    # Find out the current stereo camera view
    stereo_view = domeGetStereoView()
    if stereo_view is None:
      # Show this as a center view as a fallback on a "NoneType" error
      stereo_view = 0
    
    if domeVrayHasLatLongStereoAttrs() == 1:
      # LatLongStereo Lens Shader Setup
      LatLongStereo = vr.create("LatLongStereo", "LatLongStereo")
      
      # Check if the shader was found
      if LatLongStereo is None:
        print("The LatLongStereo shader did not load correctly!")
        return -1
      else:
        #print(camera + " has a LatLongStereo lens shader applied.")
        cameraAttr = domeVrayGetAttrNumValue("vrayLatLongStereoCamera")
        #Use the camera name to set the stereo camera view value
        #LatLongStereo.set("camera", stereo_view)
        #Use the Vray Extra Attribute to set the stereo camera view value
        LatLongStereo.set("camera", cameraAttr)
        
        fov_vert_angle = domeVrayGetAttrNumValue("vrayLatLongStereoFovVertAngle")
        LatLongStereo.set("fov_vert_angle",fov_vert_angle)
        
        fov_horiz_angle = domeVrayGetAttrNumValue("vrayLatLongStereoFovHorizAngle")
        LatLongStereo.set("fov_horiz_angle", fov_horiz_angle)
        
        parallax_distance = domeVrayGetAttrNumValue("vrayLatLongStereoParallaxDistance")
        LatLongStereo.set("parallax_distance", parallax_distance)
        
        separation = domeVrayGetAttrNumValue("vrayLatLongStereoSeparation")
        LatLongStereo.set("separation", separation)
        
        zenith_mode  = domeVrayGetAttrNumValue("vrayLatLongStereoZenithMode")
        LatLongStereo.set("zenith_mode", zenith_mode)
        
        # These are colors with three double values
        LatLongStereo.set("separation_map", 1.0)
        LatLongStereo.set("head_tilt_map", 0.5)
        
        flip_x = domeVrayGetAttrNumValue("vrayLatLongStereoFlipX")
        LatLongStereo.set("flip_x", flip_x)
        
        flip_y = domeVrayGetAttrNumValue("vrayLatLongStereoFlipY")
        LatLongStereo.set("flip_y", flip_y)
     
    elif domeVrayHasDomemasterStereoAttrs() == 1:
      # DomemasterStereo  Lens Shader Setup
      DomemasterStereo = vr.create("DomemasterStereo", "DomemasterStereo")
      
      # Check if the shader was found
      if DomemasterStereo is None:
        print("The DomemasterStereo shader did not load correctly!")
        return -1
      else:
        #print(camera + " has a DomemasterStereo lens shader applied.")
        cameraAttr = domeVrayGetAttrNumValue("vrayDomemasterStereoCamera")
        #Use the camera name to set the stereo camera view value
        #DomemasterStereo.set("camera", stereo_view)
        #Use the Vray Extra Attribute to set the stereo camera view value
        DomemasterStereo.set("camera", cameraAttr)
        
        fov_angle = domeVrayGetAttrNumValue("vrayDomemasterStereoFovAngle")
        DomemasterStereo.set("fov_angle", fov_angle)
        
        zero_parallax_sphere = domeVrayGetAttrNumValue("vrayDomemasterStereoZeroParallaxSphere")
        DomemasterStereo.set("zero_parallax_sphere", zero_parallax_sphere)
        
        separation = domeVrayGetAttrNumValue("vrayDomemasterStereoSeparation")
        DomemasterStereo.set("separation", separation)
        
        forward_tilt = domeVrayGetAttrNumValue("vrayDomemasterStereoForwardTilt")
        DomemasterStereo.set("forward_tilt", forward_tilt)
        
        tilt_compensation = domeVrayGetAttrNumValue("vrayDomemasterStereoTiltCompensation")
        DomemasterStereo.set("tilt_compensation", tilt_compensation)
        
        vertical_mode = domeVrayGetAttrNumValue("vrayDomemasterStereoVerticalMode")
        DomemasterStereo.set("vertical_mode", vertical_mode)
        
        DomemasterStereo.set("separation_map", 1.0)
        DomemasterStereo.set("head_turn_map", 1.0)
        DomemasterStereo.set("head_tilt_map", 0.5)
        
        flip_x = domeVrayGetAttrNumValue("vrayDomemasterStereoFlipX")
        DomemasterStereo.set("flip_x", flip_x)
        
        flip_y = domeVrayGetAttrNumValue("vrayDomemasterStereoFlipY")
        DomemasterStereo.set("flip_y", flip_y)
      

#Check what version of Maya is active
def getMayaVersionDome():
  import maya.cmds as cmds
  import maya.mel as mel

  #Check if we are running Maya 2011 or higher
  mayaVersion = mel.eval("getApplicationVersionAsFloat;")

  #Debug Test Mode
  #Test this GUI using the Maya 2010 - non-docked GUI mode
  #mayaVersion = 2010;

  #Write out the current Maya version number
  print("Maya " + str(mayaVersion) + " detected.\n")
  
  return mayaVersion


"""
A python function to get the current object's shape node

getObjectShapeNode("stereoCamera")
# Result: [u'stereoCameraCenterCamShape', u'stereoCameraFrustum'] # 

"""

def getObjectShapeNode ( object ) :
    import maya.cmds as cmds
    return cmds.listRelatives( object, children=True , shapes=True)


"""
A python function to get the current object's parent node

getObjectParentNode("nurbsSphereShape1")
# Result:  [u'nurbsSphere1'] #

"""

def getObjectParentNode ( object ) :
    import maya.cmds as cmds
    return cmds.listRelatives( object, parent=True)
