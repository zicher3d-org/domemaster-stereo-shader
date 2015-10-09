/*

PanoView v1.0.1 for Maxwell Render - 2015-10-09 08.14 am
by Andrew Hazelden
www.andrewhazelden.com
andrew@andrewhazelden.com

This script will send the current Maxwell Render generated panoramic 360 image directly onto your Oculus Rift HMD using your favourite media viewing tool.

Installation:

Step 1. Place this Maxwell PanoView.ms javascript file in your Maxwell 3 scripts folder:

C:\Program Files\Next Limit\Maxwell 3\scripts

Step 2. Launch Maxwell Render, and then display the script window.

Step 3. Use the "Load" button in the script window to open up the PanoView.ms script in Maxwell Render.

Step 4. Hit the "play" triangle button to run the script with you have a fulldome or latlong image in the maxwell.exe render view.

Step 5.  If any of the specific viewer tools fail to launch when selected, you may have to check that the executable path variable "viewerPath" is correct for the specific version of the viewer tool that is installed on your hard drive.

Notes:

The default operating system for PanoView is Windows.  If you are on Mac or Linux, you should change the platform variable from "Windows" to either "Mac", or "Linux" so the correct viewing program is launched.

Uncomment the media viewing tool you want to use in the mediaViewerTool() function by adding or removing the // comment symbols.

Quite a few of the viewing tools only support 8-bit per channel formats like PNG so you won't be able to display an .exr file unless you are using a program like RV that is up for the task.

This script can be launched with the -postscript:[script path] argument to run after a rendering finishes

You can optionally remove the MXI file after opening the image output in the panoramic media viewing tool using the line removeMXIFile().

The script works only in Windows but can be easily ported to other systems by changing the executable path to a Linux or Mac URL path for the viewing tool.


Required Download:

Maxwell Render 3.2
http://www.maxwellrender.com/


Optional Media Viewer Tools:

Kolor Eyes Desktop (Free) - LatLong Capable - Is the default viewing tool in PanoView
http://www.kolor.com/kolor-eyes/download/

Live View Rift (Free) - Fulldome and LatLong Capable
http://soft.viarum.com/liveviewrift/

Amateras Dome Player (Free) - Fulldome and LatLong Capable
http://www.orihalcon.co.jp/amaterasplayer/en/

Shotgun/Tweak RV Player -  LatLong Capable
http://www.tweaksoftware.com/products/rv

Assimilate Scratch Play - LatLong Capable
http://www.assimilateinc.com/products/scratch-play/

Whirligig Viewer (Free) - Fulldome and LatLong Capable
http://www.whirligig.xyz/

Adobe Speedgrade
https://www.adobe.com/products/speedgrade.html

VLC Media Player (Free)
https://www.videolan.org/vlc/

DJV View (Free)
http://djv.sourceforge.net/
*/


print("PanoView for Maxwell Render v1.0.1");
print("By Andrew Hazelden");

// Find out the current operating system platform. The platform variable should be set to either "Windows", "Mac", or "Linux".
var platform = "Windows";

// Get the Rendered image
var imageFileName = Scene.imagePath;
print("Loading Image: "  + imageFileName);

// View the Panoramic Rendering
mediaViewerTool(imageFileName);

// Optional - Remove the rendered MXI file
//removeMXIFile();


//////////////////////////////////////////////////////////////////


function mediaViewerTool(mediaFileName){
  // Choose the panoramic / media viewing tool to use
  
  kolorEyesViewer(mediaFileName);
  //liveViewRiftViewer(mediaFileName);
  //amaterasDomePlayerViewer(mediaFileName);
  //rvViewer(mediaFileName);
  //scratchViewer(mediaFileName);
  //whirligigViewer(mediaFileName);
  
  //speedgradeViewer(mediaFileName);
  //djvViewer(mediaFileName);
  //vlcViewer(mediaFileName);
}


function kolorEyesViewer(mediaFileName){
  // Kolor Eyes Desktop
  var viewerPath = "";
  
  if(platform == "Windows"){
    // Running on Windows
    //viewerPath = "C:\Program Files\Kolor\KolorEyes 1.4\KolorEyes_x64.exe";
    viewerPath = "C:\Program Files\Kolor\KolorEyes 1.5\KolorEyes_x64.exe";
  }else if(platform == "Mac"){
    // Running on Mac
    //viewerPath = "/Applications/Kolor Eyes.app/Contents/MacOS/KolorEyes";
   //viewerPath = "/Applications/Kolor Eyes 1.4.app/Contents/MacOS/KolorEyes";
    viewerPath = "/Applications/Kolor Eyes 1.5.app/Contents/MacOS/KolorEyes"
  }else if(platform == "Linux"){
    // Running on Linux
    // Kolor Eyes is not available for Linux yet
    viewerPath = "KolorEyes";
  }else{
    print("There is an invalid operating system platform defined in the platform variable at the top of the code.");
    return;
  }

  // Build an array with the command line arguments passed to Kolor Eyes. We pass two arguments:
  // The Oculus Rift direct to fullscreen --demo mode, and the image path for the latlong panorama

  var args = new Array;
  args[0] = "--demo";
  args[1] = mediaFileName;
  Maxwell.launchProcess(viewerPath, args);
  
  print("[Launching Kolor Eyes on " + platform + "]");
  print("[Launching Command] " + viewerPath);
  print("[Args] "  + args);
} 


function amaterasDomePlayerViewer(mediaFileName){
  // Amateras Dome Player
  var viewerPath = "";
  
  if(platform == "Windows"){
    // Running on Windows
    viewerPath = "C:\Program Files\amateras320\bin\AmaterasDomePlayer.exe";
  }else if(platform == "Mac"){
    // Running on Mac
    viewerPath = "/Applications/Amateras3/Amateras.app/Contents/MacOS/Amateras";
  }else if(platform == "Linux"){
    // Running on Linux
    viewerPath = "amateras";
  }else{
    print("There is an invalid operating system platform defined in the platform variable at the top of the code.");
    return;
  }
  
  // Build an array with the command line arguments passed to Amateras Dome Player. We pass one argument:
  // The image path for the latlong panorama

  var args = new Array;
  args[0] = mediaFileName;
  Maxwell.launchProcess(viewerPath, args);
  
  print("[Launching Amateras Dome Player on " + platform + "]");
  print("[Launching Command] " + viewerPath);
  print("[Args] "  + args);
}


function djvViewer(mediaFileName){
  // DJV Viewer
  // Note there is a bug in DJV 1.1.0 that causes an issue loading still imagery since the additional of MP4 video playback.
  // You should go back to the previous version of the DJV program if the renderings don't load correctly for you.

  var viewerPath = "";
  
  if(platform == "Windows"){
    // Running on Windows
    viewerPath = "C:\Program Files\djv-1.0.5-Windows-64\bin\djv_view.exe";
    //viewerPath = "C:\Program Files\djv-1.1.0-Windows-64\bin\djv_view.exe";
  }else if(platform == "Mac"){
    // Running on Mac
    //viewerPath = "/Applications/djv-OSX-64.app/Contents/MacOS/djv-1.0.5-OSX-64";
    viewerPath = "/Applications/djv-1.0.5-OSX-64.app/Contents/MacOS/djv-1.0.5-OSX-64";
    //viewerPath = "/Applications/djv-1.1.0-OSX-64.app/Contents/MacOS/djv-1.1.0-OSX-64";
  }else if(platform == "Linux"){
    // Running on Linux
    viewerPath = "djv-view";
  }else{
    print("There is an invalid operating system platform defined in the platform variable at the top of the code.");
    return;
  }
  
  // Build an array with the command line arguments passed to DJV. We pass one argument:
  // The image path for the latlong panorama

  var args = new Array;
  args[0] = mediaFileName;
  Maxwell.launchProcess(viewerPath, args);
  
  print("[Launching DJV Viewer on " + platform + "]");
  print("[Launching Command] " + viewerPath);
  print("[Args] "  + args);
}


function liveViewRiftViewer(mediaFileName){
  // Live View Rift
  var viewerPath = "";
  
  if(platform == "Windows"){
    // Running on Windows
    viewerPath = "C:\Program Files (x86)\Viarum\LiveViewRift\LiveViewRift.exe";
  }else if(platform == "Mac"){
    // Running on Mac
    viewerPath = "/Applications/LiveViewRift.app/Contents/MacOS/LiveViewRift";
  }else if(platform == "Linux"){
    // Running on Linux
    viewerPath = "LiveViewRift";
  }else{
    print("There is an invalid operating system platform defined in the platform variable at the top of the code.");
    return;
  }
  
  // Build an array with the command line arguments passed to LiveViewRift. We pass one argument:
  // The image path for the latlong panorama

  var args = new Array;
  args[0] = mediaFileName;
  Maxwell.launchProcess(viewerPath, args);
  
  print("[Launching Live View Rift on " + platform + "]");
  print("[Launching Command] " + viewerPath);
  print("[Args] "  + args);
}


function scratchViewer(mediaFileName){
  // Assimilate Scratch Player
  var viewerPath = "";
  
  if(platform == "Windows"){
    // Running on Windows
    viewerPath = "C:\Program Files\Assimilate\bin64\Assimilator.exe";
  }else if(platform == "Mac"){
    // Running on Mac
    viewerPath = "/Applications/Scratch.app/Contents/MacOS/Scratch";
  }else if(platform == "Linux"){
    // Running on Linux
    viewerPath = "Assimilator";
  }else{
    print("There is an invalid operating system platform defined in the platform variable at the top of the code.");
    return;
  }
  
  // Build an array with the command line arguments passed to Scratch. We pass one argument:
  // The image path for the latlong panorama

  var args = new Array;
  args[0] = mediaFileName;
  Maxwell.launchProcess(viewerPath, args);
  
  print("[Launching Assimilate Scratch Player on " + platform + "]");
  print("[Launching Command] " + viewerPath);
  print("[Args] "  + args);
}


function speedgradeViewer(mediaFileName){
  // Adobe SpeedGrade
  var viewerPath = "";

  if(platform == "Windows"){
    // Running on Windows
    viewerPath = "C:\Program Files\Adobe\Adobe SpeedGrade CS6\SpeedGradeCmd.exe";
    viewerPath = "C:\Program Files\Adobe\Adobe SpeedGrade CC 2014\SpeedGradeCmd.exe";
    //viewerPath = "C:\Program Files\Adobe\Adobe SpeedGrade CC 2015\SpeedGradeCmd.exe";
  }else if(platform == "Mac"){
    // Running on Mac
    //viewerPath = "/Applications/Adobe SpeedGrade CS6/Adobe SpeedGrade CS6.app/Contents/MacOS/bin/SpeedGradeCmd";
    viewerPath = "/Applications/Adobe SpeedGrade CC 2014/Adobe SpeedGrade CS6.app/Contents/MacOS/bin/SpeedGradeCmd";
    //viewerPath = "/Applications/Adobe SpeedGrade CC 2015/Adobe SpeedGrade CS6.app/Contents/MacOS/bin/SpeedGradeCmd";
  }else if(platform == "Linux"){
    // Running on Linux
    viewerPath = "SpeedGradeCmd";
  }else{
    print("There is an invalid operating system platform defined in the platform variable at the top of the code.");
    return;
  }
  
  // Build an array with the command line arguments passed to SpeedGrade. We pass one argument:
  // The image path for the latlong panorama

  var args = new Array;
  args[0] = mediaFileName;
  Maxwell.launchProcess(viewerPath, args);
  
  print("[Launching Adobe SpeedGrade on " + platform + "]");
  print("[Launching Command] " + viewerPath);
  print("[Args] "  + args);
}


function vlcViewer(mediaFileName){
  // VLC
  var viewerPath = "";
  var args = new Array;
    
  if(platform == "Windows"){
    // Running on Windows
    viewerPath = "C:\Program Files (x86)\VideoLAN\VLC\vlc.exe";
    args[0] = "--started-from-file";
  	args[1] = mediaFileName;
  }else if(platform == "Mac"){
    // Running on Mac
    viewerPath = "/Applications/VLC.app/Contents/MacOS/VLC";
    args[0] = mediaFileName;
  }else if(platform == "Linux"){
    // Running on Linux
    viewerPath = "vlc";
    args[0] = mediaFileName;
  }else{
    print("There is an invalid operating system platform defined in the platform variable at the top of the code.");
    return;
  }
  
  // Build an array with the command line arguments passed to VLC. We pass two arguments:
  // The command "--started-from-file", and the image path for the latlong panorama



  Maxwell.launchProcess(viewerPath, args);
  
  print("[Launching VLC on " + platform + "]");
  print("[Launching Command] " + viewerPath);
  print("[Args] "  + args);
}


function rvViewer(mediaFileName){
  // Shotgun / Tweak RV
  var viewerPath = "";
  
  if(platform == "Windows"){
    // Running on Windows
    viewerPath = "C:\Program Files\rv-win64-x86-64-6.2.4\bin\rv.exe";
  }else if(platform == "Mac"){
    // Running on Mac
    viewerPath = "/Applications/RV64.app/Contents/MacOS/RV64";
  }else if(platform == "Linux"){
    // Running on Linux
    viewerPath = "rv";
  }else{
    print("There is an invalid operating system platform defined in the platform variable at the top of the code.");
    return;
  }
  
  // Build an array with the command line arguments passed to RV. We pass two arguments:
  // The -fullscreen mode, and the image path for the latlong panorama

  var args = new Array;
  args[0] = "-fullscreen";
  args[1] = mediaFileName;
  Maxwell.launchProcess(viewerPath, args);
  
  print("[Launching RV Player on " + platform + "]");
  print("[Launching Command] " + viewerPath);
  print("[Args] "  + args);
}


function whirligigViewer(mediaFileName){
  // Whirligig
  var viewerPath = "";
  
  if(platform == "Windows"){
    // Running on Windows
    viewerPath = "C:\Program Files\Whirligig\Whirligig64bit.exe";
  }else if(platform == "Mac"){
    // Running on Mac
    viewerPath = "/Applications/Whirligig.app/Contents/MacOS/Whirligig";
  }else if(platform == "Linux"){
    // Running on Linux
    viewerPath = "Whirligig";
  }else{
    print("There is an invalid operating system platform defined in the platform variable at the top of the code.");
    return;
  }
  
  // Build an array with the command line arguments passed to Whirligig. We pass four arguments:
  // The "-feature" command, then image path for the latlong panorama, then the "-projection" setting, and finally the panoramic format

  // LatLong
  var projectionMode = "barrel360";
  
  // Angular Fisheye 140 degree
  var projectionMode = "fisheye140";  
    
  // Angular Fisheye 180 degree / Domemaster 180
  var projectionMode = "fisheye180";  
  
  // Angular Fisheye 240 degree
  var projectionMode = "fisheye240";
  
  // Angular Fisheye 360 degree
  var projectionMode = "fisheye360"; 
  
  // Rectangular
  var projectionMode = "flatscreen";
  
  var args = new Array;
  args[0] = "-feature";
  args[1] = mediaFileName;
  args[2] = "-projection";
  args[3] = projectionMode;
  Maxwell.launchProcess(viewerPath, args);
  
  print("[Launching Whirligig on " + platform + "]");
  print("[Launching Command] " + viewerPath);
  print("[Args] "  + args);
}


function removeMXIFile(){
  // Remove MXI file
  var mxiPath = Scene.mxiPath;
  FileManager.removeFile(mxiPath);
}
