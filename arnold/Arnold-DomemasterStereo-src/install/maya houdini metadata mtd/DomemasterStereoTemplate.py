# Domemaster Stereo Shader Template File
# 2014-09-07 08:42 am 

import pymel.core as pm
import maya.cmds as cmds
import mtoa.ui.ae.templates as templates
from mtoa.ui.ae.customShapeAttributes import CameraTemplate as CameraTemplate

def DomemasterStereoCreateCameraMode(attr):
    cmds.setUITemplate('attributeEditorPresetsTemplate', pushTemplate=True)
    cmds.attrEnumOptionMenuGrp('DomemasterStereoCameraMode', attribute=attr, label="Camera", enumeratedItem=[(0, 'Center'), (1, 'Left'), (2, 'Right')])    
    cmds.setUITemplate(popTemplate=True)

def DomemasterStereoSetCameraMode(attr):
    cmds.attrEnumOptionMenuGrp('DomemasterStereoCameraMode', edit=True, attribute=attr)

class DomemasterStereoTemplate(CameraTemplate):
  def setup(self):
    self.beginLayout("Domemaster Stereo Shader", collapse=False)
    # Create the Cameras option menu with the Center, Left, and Right views
    self.addCustom('aiCamera', DomemasterStereoCreateCameraMode, DomemasterStereoSetCameraMode)
    # Show the Camera as a numerical value where: Center=0, Left=1, and Right=2
    #self.addControl("aiCamera", label="Camera")
    self.addControl("aiFov", label="Field of View")
    self.addSeparator()
    self.addControl("aiSeparation", label="Camera Separation")
    self.addControl("aiZeroParallaxSphere", label="Zero Parallax Sphere")
    self.addControl("aiForwardTilt", label="Forward Tilt")
    self.addSeparator()
    self.addControl("aiExposure", label="Exposure")
    self.endLayout()

    self.beginLayout("Stereo Display Controls", collapse=True)
    self.endLayout()

    self.beginLayout("Custom maps", collapse=False)
    self.addControl("aiSeparationMap",  label="Separation Map")
    self.addControl("aiHeadTurnMap",  label="Head Turn Map")
    self.addControl("aiHeadRollMap",  label="Head Roll Map")
    self.endLayout()

    self.beginLayout("Image Orientation", collapse=True)
    self.beginNoOptimize()
    self.endNoOptimize()
    self.endLayout()

    self.beginLayout( "Options", collapse=True )
    #self.addCommonAttributes()
    #self.addSeparator()
    self.addControl("aiUserOptions", label="User Options")
    self.endLayout()

templates.registerTranslatorUI(DomemasterStereoTemplate, "camera", "DomemasterStereo")
templates.registerTranslatorUI(DomemasterStereoTemplate, "stereoRigCamera", "DomemasterStereo")
