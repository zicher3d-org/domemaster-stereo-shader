# Domemain Stereo Shader Template File
# 2014-10-31 6:38 pm

import pymel.core as pm
import maya.cmds as cmds
import mtoa.ui.ae.templates as templates
#from mtoa.ui.ae.customShapeAttributes import CameraTemplate as CameraTemplate

def DomemainStereoCreateCameraMode(attr):
    cmds.setUITemplate('attributeEditorPresetsTemplate', pushTemplate=True)
    cmds.attrEnumOptionMenuGrp('DomemainStereoCameraMode', attribute=attr, label="Camera", enumeratedItem=[(0, 'Center'), (1, 'Left'), (2, 'Right')])    
    cmds.setUITemplate(popTemplate=True)

def DomemainStereoSetCameraMode(attr):
    cmds.attrEnumOptionMenuGrp('DomemainStereoCameraMode', edit=True, attribute=attr)

#class DomemainStereoTemplate(CameraTemplate):
class DomemainStereoTemplate(templates.AttributeTemplate):
  def setup(self):
    self.beginLayout("Domemain Stereo Shader", collapse=False)
    # Create the Cameras option menu with the Center, Left, and Right views
    self.addCustom('aiCamera', DomemainStereoCreateCameraMode, DomemainStereoSetCameraMode)
    self.addControl("aiFovAngle", label="Field of View")
    self.addSeparator()
    self.addControl("aiZeroParallaxSphere", label="Zero Parallax Sphere")
    self.addControl("aiSeparation", label="Camera Separation")
    self.addControl("aiForwardTilt", label="Dome Forward Tilt")
    self.addSeparator()
    self.addControl("aiTiltCompensation", label="Dome Tilt Compensation")
    self.addControl("aiVerticalMode", label="Vertical Mode")
    
    self.beginLayout("Stereo Display Controls", collapse=True)
    self.endLayout()
    
    self.beginLayout("Custom maps", collapse=False)
    self.addControl("aiSeparationMap",  label="Separation Map")
    self.addControl("aiHeadTurnMap",  label="Head Turn Map")
    self.addControl("aiHeadTiltMap",  label="Head Tilt Map")
    self.endLayout()
    
    self.beginLayout("Image Orientation", collapse=True)
    self.beginNoOptimize()
    self.addControl("aiFlipRayX", label="Flip X")
    self.addControl("aiFlipRayY", label="Flip Y")
    self.endNoOptimize()
    self.endLayout()
    
    self.beginLayout( "Options", collapse=False)
    self.addControl("aiExposure", label="Exposure")
    self.addControl("aiFocusDistance", label="Focal Distance")
    self.addControl("aiApertureSize", label="Aperture Size")
    self.addControl("aiApertureBlades", label="Aperture Blades")
    self.addControl("aiApertureBladeCurvature", label="Aperture Blade Curvature")
    self.addControl("aiApertureRotation", label="Aperture Rotation")
    self.addControl("aiApertureAspectRatio", label="Aperture Aspect Ratio")
    self.addControl("aiShutterStart", label="Shutter Start")
    self.addControl("aiShutterEnd", label="Shutter End")
    self.addControl("aiRollingShutterDuration", label="Rolling Shutter Duration")
    self.addControl("aiUserOptions", label="User Options")
    self.endLayout()
    
    self.endLayout()

templates.registerTranslatorUI(DomemainStereoTemplate, "camera", "DomemainStereo")
#templates.registerTranslatorUI(DomemainStereoTemplate, "stereoRigCamera", "DomemainStereo")
