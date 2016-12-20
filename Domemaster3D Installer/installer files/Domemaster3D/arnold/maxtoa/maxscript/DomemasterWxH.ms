-- Domemaster WxH Lens Shader Arnold MAXtoA Scripted Controller
-- 2016-12-19 8.17 PM
-- by Andrew Hazelden andrew@andrewhazelden.com and Roberto Ziche
-- -------------------------------------------------------------------
-- Todo: Customize the classid node setting line: classID:#(515151,676102)
-- 
-- NOTE: This script requires the "Domemaster3D" lens shader DLL that can be downladed from:
-- https://github.com/zicher3d-org/domemaster-stereo-shader/
-- -------------------------------------------------------------------

plugin Camera arnold_domemaster_wxh_camera
extends:FreeCamera
name:"DomemasterWxH Cam"
classID:#(515151,676102)
category:"Arnold"
replaceUI:true
(
  parameters main rollout:params
  (
    arnold_node type:#string default:"DomemasterWxH"
    
    arnold_node_diameter type:#float Range:[0.1,9999,1] default:1 ui:diameter
    arnold_node_height type:#float Range:[0.0001,9999,0.5] default:0.5 ui:height
    
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
    spinner diameter                "Diameter"
    spinner height                  "Height" 
    checkbutton flip_ray_x          "Flip X"
    checkbutton flip_ray_y          "Flip Y"
    
    
    -- This is a workaround for the camera being too smart, and ignoring any
    -- updates that are not in its set of "parameters I care about"
    on diameter selected val do forceUpdate()
    on height selected val do forceUpdate()
    on flip_ray_x selected val do forceUpdate()
    on flip_ray_y changed val do forceUpdate()    
  )
)
