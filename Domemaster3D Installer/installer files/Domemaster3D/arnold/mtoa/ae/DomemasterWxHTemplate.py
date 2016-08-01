# Domemaster WxH Shader Template File
# 2015-01-31 09.29 am

import pymel.core as pm
import maya.cmds as cmds
import mtoa.ui.ae.templates as templates
#from mtoa.ui.ae.customShapeAttributes import CameraTemplate as CameraTemplate


#class DomemasterWxHTemplate(CameraTemplate):
class DomemasterWxHTemplate(templates.AttributeTemplate):
  def setup(self):
    self.beginLayout("Domemaster WxH Shader", collapse=False)
    # Create the Cameras option menu with the Center, Left, and Right views

    self.addControl("aiDiameter", label="Diameter")
    self.addControl("aiHeight", label="Height")
    #self.addControl("aiViewOffset", label="View Offset")

    self.beginLayout("WxH Display Controls", collapse=True)
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

templates.registerTranslatorUI(DomemasterWxHTemplate, "camera", "DomemasterWxH")
