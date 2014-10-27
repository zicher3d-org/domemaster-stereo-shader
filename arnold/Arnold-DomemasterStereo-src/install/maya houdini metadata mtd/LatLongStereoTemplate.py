# LatLong Stereo Shader Template File
# 2014-10-25 04.38 pm

import pymel.core as pm
import maya.cmds as cmds
import mtoa.ui.ae.templates as templates
from mtoa.ui.ae.customShapeAttributes import CameraTemplate as CameraTemplate

def LatLongStereoCreateCameraMode(attr):
    cmds.setUITemplate('attributeEditorPresetsTemplate', pushTemplate=True)
    cmds.attrEnumOptionMenuGrp('LatLongStereoCameraMode', attribute=attr, label="Camera", enumeratedItem=[(0, 'Center'), (1, 'Left'), (2, 'Right')])    
    cmds.setUITemplate(popTemplate=True)

def LatLongStereoSetCameraMode(attr):
    cmds.attrEnumOptionMenuGrp('LatLongStereoCameraMode', edit=True, attribute=attr)

class LatLongStereoTemplate(CameraTemplate):
  def setup(self):
    self.beginLayout("LatLong Stereo Shader", collapse=False)
    # Create the Cameras option menu with the Center, Left, and Right views
    self.addCustom('aiCamera', LatLongStereoCreateCameraMode, LatLongStereoSetCameraMode)
    self.addControl("aiFovVertAngle", label="Field of View Vertical")
    self.addControl("aiFovHorizAngle", label="Field of View Horizontal")
    self.addSeparator()
    self.addControl("aiParallaxDistance", label="Zero Parallax Distance")
    self.addControl("aiSeparation", label="Camera Separation")
    self.addControl("aiZenithMode", "Zenith Mode")
    self.addSeparator()
    self.addControl("aiExposure", label="Exposure")
    self.endLayout()

    self.beginLayout("Stereo Display Controls", collapse=True)
    self.endLayout()

    self.beginLayout("Custom maps", collapse=False)
    self.addControl("aiSeparationMap",  label="Separation Map")
    self.endLayout()

    self.beginLayout("Image Orientation", collapse=True)
    self.beginNoOptimize()
    self.addControl("aiFlipRayX", label="Flip X")
    self.addControl("aiFlipRayY", label="Flip Y")
    self.endNoOptimize()
    self.endLayout()

    self.beginLayout( "Options", collapse=True )
    #self.addCommonAttributes()
    #self.addSeparator()
    self.addControl("aiUserOptions", label="User Options")
    self.endLayout()

templates.registerTranslatorUI(LatLongStereoTemplate, "camera", "LatLongStereo")
templates.registerTranslatorUI(LatLongStereoTemplate, "stereoRigCamera", "LatLongStereo")
