"""
Domemaster3D Startup Code Version 1.7
2015-07-08
by Andrew Hazelden
"""

#Find the name of the stereo camera rig
def findDomeRig():
  import maya.cmds as cmds

  rigs = cmds.stereoRigManager(listRigs=True)
  print ("Stereo Camera rigs:")
  for rig in rigs:
    defs = cmds.stereoRigManager(rigDefinition=rig)
    print 'Rig "'+ rig +'": (language '+defs[0]+') create callback: '+defs[1]
    #Check for
    if (rig == "DomeStereoCamera"):
      return 1
      
  return 0

#Find the name of the stereo camera rig
def findLatLongRig():
  import maya.cmds as cmds

  rigs = cmds.stereoRigManager(listRigs=True)
  print ("Stereo Camera rigs:")
  for rig in rigs:
    defs = cmds.stereoRigManager(rigDefinition=rig)
    print 'Rig "'+ rig +'": (language '+defs[0]+') create callback: '+defs[1]
    #Check for
    if (rig == "LatLongStereoCamera"):
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
def addNewDomeRig():
  import maya.mel as mel
  import maya.cmds as cmds
  #import domeStereoRig as domeStereoRig
  
  if (findDomeRig() == 0):
    print ("A DomeStereoCamera rig has been added to the stereoRigManager.")
    # Register the DomeStereoCamera rig type
    # add[rig, language, createProcedure]
    # cameraSetFunc=[rig,callback] 
    # Add the custom rig
    cmds.evalDeferred("cmds.stereoRigManager(add=['DomeStereoCamera', 'Python', 'domeStereoRig.createRig'])")
    # Add the custom callback set for Maya 2011+
    mayaVersion = getMayaVersionDome()
    if (mayaVersion >= 2011):
      cmds.evalDeferred("cmds.stereoRigManager(cameraSetFunc=['DomeStereoCamera','domeStereoRig.attachToCameraSet'] )")
    
    #Make the new rig the default rig
    cmds.evalDeferred("cmds.stereoRigManager(defaultRig='DomeStereoCamera')")
  else:
    print ("A DomeStereoCamera rig already exists in the stereoRigManager.")
  #else:
   # Maya 2010 or older was detected
   #print ("The Domemaster3D stereo rig feature requires Maya 2011 and newer.")

#Check if a LatLongStereoCamera rig exists in the scene  
def addNewLatLongRig():
  import maya.mel as mel
  import maya.cmds as cmds
  #import LatLongStereoRig
  
  if (findLatLongRig() == 0):
    print ("A LatLongStereoCamera rig has been added to the stereoRigManager.")
    # Register the LatLongStereoCamera rig type
    # add[rig, language, createProcedure]
    # cameraSetFunc=[rig,callback] 
    # Add the custom rig
    cmds.evalDeferred("cmds.stereoRigManager(add=['LatLongStereoCamera', 'Python', 'LatLongStereoRig.createRig'])")
    # Add the custom callback set for Maya 2011+
    mayaVersion = getMayaVersionDome()
    if (mayaVersion >= 2011):
      cmds.evalDeferred("cmds.stereoRigManager(cameraSetFunc=['LatLongStereoCamera','LatLongStereoRig.attachToCameraSet'] )")
    
    #Make the new rig the default rig
    cmds.evalDeferred("cmds.stereoRigManager(defaultRig='LatLongStereoCamera')")
  else:
    print ("A LatLongStereoCamera rig already exists in the stereoRigManager.")
  #else:
   # Maya 2010 or older was detected
   #print ("The LatLong_Stereo stereo rig feature requires Maya 2011 and newer.")
    
# Load the Domemaster3D menu system in the rendering menu set    
def addNewDomeMenu():
  import maya.mel as mel
  print("Loading the Domemaster3D menu items...")
  mel.eval('source "domeMenu.mel";')
  mel.eval('createDomemaster3DMenu();')

#----------------------------------------------------------------------------
# Main Domemaster3D Start up function  
#----------------------------------------------------------------------------

# Stop Maya from running the python code twice by looking if it is __main__
if (__name__ == '__main__'):
  import maya.cmds as cmds
  import maya.mel as mel

  #Check OS platform for Windows/Mac/Linux
  import platform
    
  # Add the Domemaster3D Stereo & LatLong_Stereo camera Rig
  import domeStereoRig
  import LatLongStereoRig


  """
  Maya tip on detecting Maya Batch mode is from Michael Scarpa's blog post "MEL Sillyness":
  http://www.scarpa.name/2010/12/16/mel-sillyness/
  """

  # Check if Maya is running in batch mode or with a GUI
  import maya.OpenMaya
  isMayaInBatchMode = maya.OpenMaya.MGlobal.mayaState() == maya.OpenMaya.MGlobal.kBatch
  # isMayaInBatchMode = 1 means Batch Mode, 0 means GUI mode
  if(isMayaInBatchMode == False):
    print("The Domemaster3D Shader is running in GUI mode.")
    # Make sure the stereo plug-in is loaded
    cmds.evalDeferred("cmds.loadPlugin('stereoCamera', quiet=True)")
    cmds.evalDeferred("addNewDomeRig()")
    cmds.evalDeferred("addNewLatLongRig()")
    # Load the Domemaster3D menu system in the rendering menu set
    cmds.evalDeferred("addNewDomeMenu()")
    
  else:
    print("The Domemaster3D Shader is running in batch mode.")

  # Make sure the mental ray plugin was loaded
  #if not (cmds.pluginInfo("Mayatomr",q=True,loaded=True)):
  #    cmds.loadPlugin("Mayatomr")
  #else:
  #    pass

# ---------------------------------------------------------------------
# End Domemaster3D Startup Code
# ---------------------------------------------------------------------
