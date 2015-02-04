"""
Arnold Domemaster3D Startup Code Version 1.6.1
2015-01-31 09.28 am
by Andrew Hazelden

"""

#Find the name of the stereo camera rig
def findArnoldDomeRig():
  import maya.cmds as cmds

  rigs = cmds.stereoRigManager(listRigs=True)
  print ("Stereo Camera rigs:")
  for rig in rigs:
    defs = cmds.stereoRigManager(rigDefinition=rig)
    print 'Rig "'+ rig +'": (language '+defs[0]+') create callback: '+defs[1]
    #Check for
    if (rig == "ArnoldDomeStereoCamera"):
      return 1
      
  return 0

#Find the name of the stereo camera rig
def findArnoldLatLongRig():
  import maya.cmds as cmds

  rigs = cmds.stereoRigManager(listRigs=True)
  print ("Stereo Camera rigs:")
  for rig in rigs:
    defs = cmds.stereoRigManager(rigDefinition=rig)
    print 'Rig "'+ rig +'": (language '+defs[0]+') create callback: '+defs[1]
    #Check for
    if (rig == "ArnoldLatLongStereoCamera"):
      return 1
      
  return 0

def getMayaVersionDome():
  import maya.mel as mel
  import maya.cmds as cmds

  #Check what Maya version is active
  #Check if we are running Maya 2011 or higher
  mayaVersion = mel.eval("getApplicationVersionAsFloat;")
  #Test this GUI using the Maya 2010 - non-docked GUI mode
  #mayaVersion = 2010;

  #Write out the current Maya version number
  print("Maya " + str(mayaVersion) + " detected.\n")
  return mayaVersion


#Check if a DomeStereoCamera rig exists in the scene  
def addNewArnoldDomeRig():
  import maya.mel as mel
  import maya.cmds as cmds
  
  if (findArnoldDomeRig() == 0):
    print ("An ArnoldDomeStereoCamera rig has been added to the stereoRigManager.")
    # Register the DomeStereoCamera rig type
    # add[rig, language, createProcedure]
    # cameraSetFunc=[rig,callback] 
    # Add the custom rig
    #cmds.evalDeferred("cmds.stereoRigManager(add=['ArnoldDomeStereoCamera', 'Python', 'arnoldDomeStereoRig.createRig'])")
    cmds.stereoRigManager(add=['ArnoldDomeStereoCamera', 'Python', 'arnoldDomeStereoRig.createRig'])
    # Add the custom callback set for Maya 2011+
    mayaVersion = getMayaVersionDome()
    if (mayaVersion >= 2011):
      #cmds.evalDeferred("cmds.stereoRigManager(cameraSetFunc=['ArnoldDomeStereoCamera','arnoldDomeStereoRig.attachToCameraSet'] )")
      cmds.stereoRigManager(cameraSetFunc=['ArnoldDomeStereoCamera','arnoldDomeStereoRig.attachToCameraSet'])
    
    #Make the new rig the default rig
    #cmds.evalDeferred("cmds.stereoRigManager(defaultRig='ArnoldDomeStereoCamera')")
    cmds.stereoRigManager(defaultRig='ArnoldDomeStereoCamera')
  else:
    print ("An ArnoldDomeStereoCamera rig already exists in the stereoRigManager.")


#Check if a LatLongStereoCamera rig exists in the scene  
def addNewArnoldLatLongRig():
  import maya.mel as mel
  import maya.cmds as cmds
  
  if (findArnoldLatLongRig() == 0):
    print ("An ArnoldLatLongStereoCamera rig has been added to the stereoRigManager.")
    # Register the ArnoldLatLongStereoCamera rig type
    # add[rig, language, createProcedure]
    # cameraSetFunc=[rig,callback] 
    # Add the custom rig
    #cmds.evalDeferred("cmds.stereoRigManager(add=['ArnoldLatLongStereoCamera', 'Python', 'arnoldLatLongStereoRig.createRig'])")
    cmds.stereoRigManager(add=['ArnoldLatLongStereoCamera', 'Python', 'arnoldLatLongStereoRig.createRig'])
    # Add the custom callback set for Maya 2011+
    mayaVersion = getMayaVersionDome()
    if (mayaVersion >= 2011):
      #cmds.evalDeferred("cmds.stereoRigManager(cameraSetFunc=['ArnoldLatLongStereoCamera','arnoldLatLongStereoRig.attachToCameraSet'] )")
      cmds.stereoRigManager(cameraSetFunc=['ArnoldLatLongStereoCamera','arnoldLatLongStereoRig.attachToCameraSet'] )
    
    #Make the new rig the default rig
    #cmds.evalDeferred("cmds.stereoRigManager(defaultRig='ArnoldLatLongStereoCamera')")
    cmds.stereoRigManager(defaultRig='ArnoldLatLongStereoCamera')
  else:
    print ("An ArnoldLatLongStereoCamera rig already exists in the stereoRigManager.")

# Load the Domemaster3D menu system in the rendering menu set    
# def addNewDomeMenu():
  # import maya.mel as mel
  # print("Loading the Domemaster3D menu items...")
  # mel.eval('source "domeMenu.mel";')
  # mel.eval('createDomemaster3DMenu();')

  
# Load the new stereo Arnold stereo rigs
def deferredLoadArnoldRig():
  # Make sure the rigs don't exist yet
  if (findArnoldLatLongRig() == 0):
    cmds.evalDeferred("addNewArnoldLatLongRig()")
  
  if (findArnoldDomeRig() == 0):
    cmds.evalDeferred("addNewArnoldDomeRig()")
  
#----------------------------------------------------------------------------
# Main Domemaster3D Start up function  
#----------------------------------------------------------------------------

# Stop Maya from running the python code twice by looking if it is __main__
if (__name__ == '__main__'):
  import maya.cmds as cmds

  # Add the Domemaster3D Stereo & LatLong_Stereo camera Rig
  #import arnoldDomeStereoRig
  #import arnoldLatLongStereoRig

  """
  Maya tip on detecting Maya Batch mode is from Michael Scarpa's blog post "MEL Sillyness":
  http://www.scarpa.name/2010/12/16/mel-sillyness/
  """

  # Check if Maya is running in batch mode or with a GUI
  import maya.OpenMaya
  isMayaInBatchMode = maya.OpenMaya.MGlobal.mayaState() == maya.OpenMaya.MGlobal.kBatch
  # isMayaInBatchMode = 1 means Batch Mode, 0 means GUI mode
  if(isMayaInBatchMode == False):
    print("The Arnold Domemaster3D Shader is running in GUI mode.")
    # Make sure the stereo plug-in is loaded
    cmds.evalDeferred("cmds.loadPlugin('stereoCamera', quiet=True)")
    
    # Load the new stereo Arnold stereo rigs
    cmds.evalDeferred("deferredLoadArnoldRig()")
    
    # Load the Domemaster3D menu system in the rendering menu set
    #cmds.evalDeferred("addNewDomeMenu()")
  else:
    print("The Arnold Domemaster3D Shader is running in batch mode.")



  # Make sure the Arnold plugin was loaded
  # if not (cmds.pluginInfo("mtoa",q=True,loaded=True)):
     # cmds.loadPlugin("mtoa")
  # else:
     # pass
   
# ---------------------------------------------------------------------
# End Domemaster3D Startup Code
# ---------------------------------------------------------------------
