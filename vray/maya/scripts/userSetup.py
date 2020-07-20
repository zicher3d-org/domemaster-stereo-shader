"""
Vray Domemain3D Startup Code Version 2.1
2016-07-26 04.41 PM
by Andrew Hazelden
"""

# Find the name of the stereo camera rig
def findVrayDomeRig():
  import maya.cmds as cmds

  rigs = cmds.stereoRigManager(listRigs=True)
  print ("Stereo Camera rigs:")
  for rig in rigs:
    defs = cmds.stereoRigManager(rigDefinition=rig)
    print 'Rig "'+ rig +'": (language '+defs[0]+') create callback: '+defs[1]
    # Check for rig
    if (rig == "VrayDomemainStereoCamera"):
      return 1
      
  return 0


# Find the name of the stereo camera rig
def findVrayLatLongRig():
  import maya.cmds as cmds

  rigs = cmds.stereoRigManager(listRigs=True)
  print ("Stereo Camera rigs:")
  for rig in rigs:
    defs = cmds.stereoRigManager(rigDefinition=rig)
    print 'Rig "'+ rig +'": (language '+defs[0]+') create callback: '+defs[1]
    # Check for rig
    if (rig == "VrayLatLongStereoCamera"):
      return 1
      
  return 0

def getMayaVersionDome():
  import maya.mel as mel
  import maya.cmds as cmds

  # Check what Maya version is active
  # Check if we are running Maya 2011 or higher
  mayaVersion = mel.eval("getApplicationVersionAsFloat;")
  # Test this GUI using the Maya 2010 - non-docked GUI mode
  #mayaVersion = 2010;

  # Write out the current Maya version number
  print("Maya " + str(mayaVersion) + " detected.\n")
  return mayaVersion


# Check if a DomemainStereoCamera rig exists in the scene  
def addNewVrayDomeRig():
  import maya.mel as mel
  import maya.cmds as cmds
  
  if (findVrayDomeRig() == 0):
    print ("An VrayDomemainStereoCamera rig has been added to the stereoRigManager.")
    # Register the DomemainStereoCamera rig type
    # add[rig, language, createProcedure]
    # cameraSetFunc=[rig,callback] 
    # Add the custom rig
    #cmds.evalDeferred("cmds.stereoRigManager(add=['VrayDomemainStereoCamera', 'Python', 'vrayDomemainStereoRig.createRig'])")
    cmds.stereoRigManager(add=['VrayDomemainStereoCamera', 'Python', 'vrayDomemainStereoRig.createRig'])
    # Add the custom callback set for Maya 2011+
    mayaVersion = getMayaVersionDome()
    if (mayaVersion >= 2011):
      #cmds.evalDeferred("cmds.stereoRigManager(cameraSetFunc=['VrayDomemainStereoCamera','vrayDomemainStereoRig.attachToCameraSet'] )")
      cmds.stereoRigManager(cameraSetFunc=['VrayDomemainStereoCamera','vrayDomemainStereoRig.attachToCameraSet'])
    
    # Make the new rig the default rig
    #cmds.evalDeferred("cmds.stereoRigManager(defaultRig='VrayDomemainStereoCamera')")
    cmds.stereoRigManager(defaultRig='VrayDomemainStereoCamera')
  else:
    print ("An VrayDomemainStereoCamera rig already exists in the stereoRigManager.")


# Check if a LatLongStereoCamera rig exists in the scene  
def addNewVrayLatLongRig():
  import maya.mel as mel
  import maya.cmds as cmds
  
  if (findVrayLatLongRig() == 0):
    print ("A VrayLatLongStereoCamera rig has been added to the stereoRigManager.")
    # Register the VrayLatLongStereoCamera rig type
    # add[rig, language, createProcedure]
    # cameraSetFunc=[rig,callback] 
    # Add the custom rig
    #cmds.evalDeferred("cmds.stereoRigManager(add=['VrayLatLongStereoCamera', 'Python', 'vrayLatLongStereoRig.createRig'])")
    cmds.stereoRigManager(add=['VrayLatLongStereoCamera', 'Python', 'vrayLatLongStereoRig.createRig'])
    # Add the custom callback set for Maya 2011+
    mayaVersion = getMayaVersionDome()
    if (mayaVersion >= 2011):
      #cmds.evalDeferred("cmds.stereoRigManager(cameraSetFunc=['VrayLatLongStereoCamera','vrayLatLongStereoRig.attachToCameraSet'] )")
      cmds.stereoRigManager(cameraSetFunc=['VrayLatLongStereoCamera','vrayLatLongStereoRig.attachToCameraSet'] )
    
    # Make the new rig the default rig
    #cmds.evalDeferred("cmds.stereoRigManager(defaultRig='VrayLatLongStereoCamera')")
    cmds.stereoRigManager(defaultRig='VrayLatLongStereoCamera')
  else:
    print ("An VrayLatLongStereoCamera rig already exists in the stereoRigManager.")
    
    
    
# Load the Vray Domemain3D menu system in the rendering menu set    
def addNewVrayDomeMenu():
  import maya.mel as mel
  print("Loading the Vray Domemain3D menu items...")
  mel.eval('source "vrayDomeMenu.mel";')
  mel.eval('createVrayDomemain3DMenu();')

  
# Load the new Vray stereo rigs
def deferredLoadVrayRig():
  # Make sure the rigs don't exist yet
  if (findVrayLatLongRig() == 0):
    cmds.evalDeferred("addNewVrayLatLongRig()")

  if (findVrayDomeRig() == 0):
    cmds.evalDeferred("addNewVrayDomeRig()")

#----------------------------------------------------------------------------
# Main Domemain3D Start up function  
#----------------------------------------------------------------------------

# Stop Maya from running the python code twice by looking if it is __main__
if (__name__ == '__main__'):
  import maya.cmds as cmds

  # Add the Domemain3D Stereo & LatLong_Stereo camera Rig
  #import vrayDomemainStereoRig
  #import vrayLatLongStereoRig

  """
  Maya tip on detecting Maya Batch mode is from Michael Scarpa's blog post "MEL Sillyness":
  http://www.scarpa.name/2010/12/16/mel-sillyness/
  """

  # Check if Maya is running in batch mode or with a GUI
  import maya.OpenMaya
  isMayaInBatchMode = maya.OpenMaya.MGlobal.mayaState() == maya.OpenMaya.MGlobal.kBatch
  # isMayaInBatchMode = 1 means Batch Mode, 0 means GUI mode
  if(isMayaInBatchMode == False):
    print("The Vray Domemain3D Shader is running in GUI mode.")
    # Make sure the stereo plug-in is loaded
    cmds.evalDeferred("cmds.loadPlugin('stereoCamera', quiet=True)")
    
    # Load the new Vray stereo rigs
    cmds.evalDeferred("deferredLoadVrayRig()")
    
    # Load the Vray Domemain3D menu system in the rendering menu set
    cmds.evalDeferred("addNewVrayDomeMenu()")
  else:
    print("The Vray Domemain3D Shader is running in batch mode.")

  
  # Make sure the Vray plugin was loaded
  # if not (cmds.pluginInfo("vrayformaya",q=True,loaded=True)):
     # cmds.loadPlugin("vrayformaya")
  # else:
     # pass
   
# ---------------------------------------------------------------------
# End Vray Domemain3D Startup Code
# ---------------------------------------------------------------------
