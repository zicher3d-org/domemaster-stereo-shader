-- Domemaster Stereoscopic Lens Shader Arnold MAXtoA Scripted Controller
-- 2016-12-30 11.34 PM
-- by Andrew Hazelden andrew@andrewhazelden.com and Roberto Ziche
-- -------------------------------------------------------------------
-- Todo: Customize the classid node setting line: classID:#(515151,676101)
-- 
-- NOTE: This script requires the "Domemaster3D" lens shader DLL that can be downloaded from:
-- https://github.com/zicher3d-org/domemaster-stereo-shader/
-- -------------------------------------------------------------------

plugin Camera arnold_domemaster_stereo_camera
extends:FreeCamera
name:"DomemasterStereo Cam"
classID:#(515151,676101)
category:"Arnold"
replaceUI:true
(
  parameters main rollout:params
  (
    arnold_node                     type:#string          default:"DomemasterStereo"
    
    -- Center/Left/Right dropdown
    arnold_node_camera              type:#integer         default:1   ui:camera_sel
    
    -- Valid range 0.1-360 degrees
    arnold_node_fov_angle           type:#float           default:180 ui:fov_angle
   
    -- These two controls are set in scene coordinates (typically expressed visually in cm for stereographers)
    arnold_node_zero_parallax_sphere type:#worldunits     default:(units.decodeValue("10m"))  ui:zero_parallax_sphere
    arnold_node_separation          type:#worldunits      default:(units.decodeValue("65mm")) ui:separation
    
    -- Valid range 0-90 degrees 
    arnold_node_forward_tilt        type:#float           default:0.0 ui:forward_tilt
    
    -- Checkboxes
    arnold_node_tilt_compensation   type:#integer         default:0   ui:tilt_compensation
    arnold_node_vertical_mode       type:#integer         default:0   ui:vertical_mode
    
    -- These three controls need to be turned into mappable image selection fields
    arnold_node_separation_map      type:#float           default:1.0 ui:separation_map
    arnold_node_head_turn_map       type:#float           default:1.0 ui:head_turn_map
    arnold_node_head_tilt_map       type:#float           default:0.5 ui:head_tilt_map
    
    -- Checkboxes
    arnold_node_flip_ray_x          type:#integer         default:0   ui:flip_ray_x
    arnold_node_flip_ray_y          type:#integer         default:0   ui:flip_ray_y
  )
  
  -- Hack to touch a parameter that the camera translator "cares" about to 
  -- trigger a retranslation. Ugly, but.... works for now :D
  fn forceUpdate = 
  (
    if delegate.fov == 160 then delegate.fov = 160.001 else delegate.fov = 160    
  )
  
  rollout params "DomemasterStereo Shader Parameters"
  (
    dropdownlist camera_sel         "Camera"                items:#("Center","Left", "Right")
    spinner fov_angle               "Field of View"         type:#float       range:[0.0,360.0,180.0]
    spinner zero_parallax_sphere    "Zero Parallax Sphere"  type:#worldunits  range:[-1e+12,1e+12,0.0]
    spinner separation              "Camera Separation"     type:#worldunits  range:[-1e+12,1e+12,0.0]
    spinner forward_tilt            "Dome Forward Tilt"     range:[0.0,90.0,0.0]
    checkbutton tilt_compensation   "Dome Tilt Compensation"
    checkbutton vertical_mode       "Vertical Mode"
    spinner separation_map          "Separation Map"        range:[0.0,1.0,0.0]
    spinner head_turn_map           "Head Turn Map"         range:[0.0,1.0,0.0]
    spinner head_tilt_map           "Head Tilt Map"         range:[0.0,1.0,0.0]
    checkbutton flip_ray_x          "Flip X"
    checkbutton flip_ray_y          "Flip Y"
    
    -- This is a workaround for the camera being too smart, and ignoring any
    -- updates that are not in its set of "parameters I care about"
    
    -- Note: dropdownlists use "selected" and spinners use "changed"
    
    on camera_sel                   selected val do forceUpdate()
    on fov_angle                    changed val do forceUpdate()
    on zero_parallax_sphere         changed val do forceUpdate()
    on separation                   changed val do forceUpdate()
    on forward_tilt                 changed val do forceUpdate()
    on tilt_compensation            changed val do forceUpdate()
    on vertical_mode                changed val do forceUpdate()
    on separation_map               changed val do forceUpdate()
    on head_turn_map                changed val do forceUpdate()
    on head_tilt_map                changed val do forceUpdate()
    on flip_ray_x                   changed val do forceUpdate()
    on flip_ray_y                   changed val do forceUpdate()    
  )
)
