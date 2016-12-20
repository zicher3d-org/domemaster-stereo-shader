-- Domemaster Stereoscopic Lens Shader Arnold MAXtoA Scripted Controller
-- 2016-12-19 8.17 PM
-- by Andrew Hazelden andrew@andrewhazelden.com and Roberto Ziche
-- -------------------------------------------------------------------
-- Todo: Customize the classid node setting line: classID:#(515151,676101)
-- 
-- NOTE: This script requires the "Domemaster3D" lens shader DLL that can be downladed from:
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
    arnold_node type:#string default:"DomemasterStereo"
    
    -- Center/Left/Right dropdown
    arnold_node_camera type:#integer default:1 ui:camera
    
    -- Valid range 0.1-360 degrees
    arnold_node_fov_angle type:#float Range:[0.1,360,180]  default:180 ui:fov_angle
    
    -- These two controls are set in scene coordinates (typically expressed visually in cm for stereographers)
    arnold_node_zero_parallax_sphere type:#worldunits default:(units.decodeValue("360cm")) ui:zero_parallax_sphere
    arnold_node_separation type:#worldunits default:(units.decodeValue("65cm")) ui:separation
    
    -- Valid range 0-90 degrees 
    arnold_node_forward_tilt type:#float Range:[0,90,0]  default:0 ui:forward_tilt
    
    -- Checkboxes
    arnold_node_tilt_compensation type:#integer default:0 ui:tilt_compensation
    arnold_node_vertical_mode type:#integer default:0 ui:vertical_mode
    
    -- These three controls need to be turned into mappable image selection fields
    arnold_node_separation_map type:#float Range:[0,1,1] default:1 ui:separation_map
    arnold_node_head_turn_map type:#float Range:[0,1,1] default:1 ui:head_turn_map
    arnold_node_head_tilt_map type:#float Range:[0,1,0.5] default:0.5 ui:head_tilt_map
    
    -- Checkboxes
    arnold_node_flip_ray_x type:#integer default:0 ui:flip_ray_x
    arnold_node_flip_ray_y type:#integer default:0 ui:flip_ray_y
  )
  
  -- Hack to touch a parameter that the camera translator "cares" about to 
  -- trigger a retranslation. Ugly, but.... works for now :D
  fn forceUpdate = 
  (
    if delegate.fov == 160 then delegate.fov = 160.001 else delegate.fov = 160    
  )
  
  rollout params "DomemasterStereo Shader Parameters"
  (
    dropdownlist camera             "Camera" items:#("Center","Left", "Right")
    spinner fov_angle               "Field of View" 
    spinner zero_parallax_sphere    "Zero Parallax Sphere" type:#worldunits
    spinner separation              "Camera Separation" type:#worldunits
    spinner forward_tilt            "Dome Forward Tilt"
    checkbutton tilt_compensation   "Dome Tilt Compensation"
    checkbutton vertical_mode       "Vertical Mode"
    spinner separation_map          "Separation Map"
    spinner head_turn_map           "Head Turn Map"
    spinner head_tilt_map           "Head Tilt Map"
    checkbutton flip_ray_x          "Flip X"
    checkbutton flip_ray_y          "Flip Y"
    
    
    -- This is a workaround for the camera being too smart, and ignoring any
    -- updates that are not in its set of "parameters I care about"
    on camera selected val do forceUpdate()
    on fov_angle selected val do forceUpdate()
    on zero_parallax_sphere selected val do forceUpdate()
    on separation selected val do forceUpdate()
    on forward_tilt selected val do forceUpdate()
    on tilt_compensation selected val do forceUpdate()
    on vertical_mode selected val do forceUpdate()
    on separation_map selected val do forceUpdate()
    on head_turn_map selected val do forceUpdate()
    on head_tilt_map selected val do forceUpdate()
    on flip_ray_x selected val do forceUpdate()
    on flip_ray_y changed val do forceUpdate()    
  )
)
