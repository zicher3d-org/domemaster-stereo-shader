# Microsoft Developer Studio Project File - Name="vraydomemasterstereo" - Package Owner=<4>
# Microsoft Developer Studio Generated Build File, Format Version 6.00
# ** DO NOT EDIT **

# TARGTYPE "Win32 (x86) Dynamic-Link Library" 0x0102

CFG=vraydomemasterstereo - Win32 Max Release Official
!MESSAGE This is not a valid makefile. To build this project using NMAKE,
!MESSAGE use the Export Makefile command and run
!MESSAGE 
!MESSAGE NMAKE /f "vraydomemasterstereo.mak".
!MESSAGE 
!MESSAGE You can specify a configuration when running NMAKE
!MESSAGE by defining the macro CFG on the command line. For example:
!MESSAGE 
!MESSAGE NMAKE /f "vraydomemasterstereo.mak" CFG="vraydomemasterstereo - Win32 Max Release Official"
!MESSAGE 
!MESSAGE Possible choices for configuration are:
!MESSAGE 
!MESSAGE "vraydomemasterstereo - Win32 Debug" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE "vraydomemasterstereo - Win32 Max Release Official" (based on "Win32 (x86) Dynamic-Link Library")
!MESSAGE 

# Begin Project
# PROP AllowPerConfigDependencies 0
# PROP Scc_ProjName ""
# PROP Scc_LocalPath ""
CPP=xicl6.exe
MTL=midl.exe
RSC=rc.exe

!IF  "$(CFG)" == "vraydomemasterstereo - Win32 Debug"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "camera___Win32_Max6_Release"
# PROP BASE Intermediate_Dir "camera___Win32_Max6_Release"
# PROP BASE Ignore_Export_Lib 0
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\build\vraydomemasterstereo\debug\x64"
# PROP Intermediate_Dir "..\..\build\vraydomemasterstereo\debug\x64"
# PROP Ignore_Export_Lib 0
# PROP Target_Dir ""
# ADD BASE CPP /nologo /MD /W3 /GX /O2 /I "C:\Program Files\Autodesk\3ds Max 2015 SDK\maxsdk\include" /I "..\..\include\vray" /I "..\..\include\vutils" /I "..\..\include\rayserver" /I "..\..\include\resman" /I "..\..\include\imagesamplers" /I "..\..\include\imagefilters" /I "..\..\include\plugman" /I "..\..\include\putils" /D "WIN32" /D "NDEBUG" /D "_WINDOWS" /D "_MBCS" /D "_USRDLL" /D "camera_EXPORTS" /YX /FD /c
# ADD CPP /nologo /MD /W3 /GX /O2 /I "C:\Program Files\Autodesk\3ds Max 2015 SDK\maxsdk\include" /I "..\..\..\include" /D "WIN32" /D "NDEBUG" /D "_WINDOWS" /D "_MBCS" /D "_USRDLL" /D "camera_EXPORTS" /YX /FD /Qvc7 /c
# ADD BASE MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# ADD MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# ADD BASE RSC /l 0x809 /d "NDEBUG"
# ADD RSC /l 0x809 /d "NDEBUG"
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=xilink6.exe
# ADD BASE LINK32 vray2015.lib paramblk2.lib maxutil.lib core.lib geom.lib comctl32.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /base:"0x08C40000" /dll /machine:AMD64 /out:"C:\Program Files\Autodesk\3ds Max 2015\plugins\vrayplugins\vraydomemasterstereo2015.dlr" /libpath:"C:\Program Files\Autodesk\3ds Max 2015 SDK\maxsdk\lib\x64\Release" /libpath:"..\..\lib" /release
# SUBTRACT BASE LINK32 /pdb:none
# ADD LINK32 vrender2015.lib vray2015.lib paramblk2.lib maxutil.lib core.lib geom.lib comctl32.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib mesh.lib gfx.lib putils_s.lib /nologo /base:"0x08C40000" /dll /machine:AMD64 /out:"C:\Program Files\Autodesk\3ds Max 2015\plugins\vrayplugins\vraydomemasterstereo2015.dlo" /libpath:"..\..\..\lib\x64" /libpath:"..\..\..\lib\x64\vc11" /release
# SUBTRACT LINK32 /pdb:none

!ELSEIF  "$(CFG)" == "vraydomemasterstereo - Win32 Max Release Official"

# PROP BASE Use_MFC 0
# PROP BASE Use_Debug_Libraries 0
# PROP BASE Output_Dir "camera___Win32_Max6_Release_Official"
# PROP BASE Intermediate_Dir "camera___Win32_Max6_Release_Official"
# PROP BASE Ignore_Export_Lib 0
# PROP BASE Target_Dir ""
# PROP Use_MFC 0
# PROP Use_Debug_Libraries 0
# PROP Output_Dir "..\..\build\vraydomemasterstereo\max2015\x64\official"
# PROP Intermediate_Dir "..\..\build\vraydomemasterstereo\max2015\x64\official"
# PROP Ignore_Export_Lib 0
# PROP Target_Dir ""
# ADD BASE CPP /nologo /MD /W3 /GX /O2 /I "C:\Program Files\Autodesk\3ds Max 2015 SDK\maxsdk\include" /I "..\..\include\vray" /I "..\..\include\vutils" /I "..\..\include\rayserver" /I "..\..\include\resman" /I "..\..\include\imagesamplers" /I "..\..\include\imagefilters" /I "..\..\include\plugman" /I "..\..\include\putils" /D "WIN32" /D "NDEBUG" /D "_WINDOWS" /D "_MBCS" /D "_USRDLL" /D "camera_EXPORTS" /YX /FD /c
# ADD CPP /nologo /MD /W3 /GX /Zi /O2 /I "C:\Program Files\Autodesk\3ds Max 2015 SDK\maxsdk\include" /I "..\..\..\include" /D "WIN32" /D "NDEBUG" /D "_WINDOWS" /D "_MBCS" /D "_USRDLL" /D "camera_EXPORTS" /YX /FD /c
# ADD BASE MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# ADD MTL /nologo /D "NDEBUG" /mktyplib203 /win32
# ADD BASE RSC /l 0x809 /d "NDEBUG"
# ADD RSC /l 0x809 /d "NDEBUG"
BSC32=bscmake.exe
# ADD BASE BSC32 /nologo
# ADD BSC32 /nologo
LINK32=xilink6.exe
# ADD BASE LINK32 vray.lib paramblk2.lib maxutil.lib core.lib geom.lib comctl32.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib /nologo /base:"0x08C40000" /dll /machine:AMD64 /out:"C:\Program Files\Autodesk\3ds Max 2015\plugins\vrayplugins\vraydomemasterstereo2015.dlr" /libpath:"C:\Program Files\Autodesk\3ds Max 2015 SDK\maxsdk\lib\x64\Release" /libpath:"..\..\lib" /release
# SUBTRACT BASE LINK32 /pdb:none
# ADD LINK32 vrender2015.lib vray.lib paramblk2.lib maxutil.lib core.lib geom.lib comctl32.lib kernel32.lib user32.lib gdi32.lib winspool.lib comdlg32.lib advapi32.lib shell32.lib ole32.lib oleaut32.lib uuid.lib odbc32.lib odbccp32.lib mesh.lib gfx.lib putils_s.lib vutils_s.lib /base:"0x08C40000" /dll /pdb:"..\..\pdb\vraydomemasterstereo2015.pdb" /debug /machine:AMD64 /def:".\plugin.def" /out:"..\..\vrayplugins\vraydomemasterstereo2015.dlo" /libpath:"C:\Program Files\Autodesk\3ds Max 2015 SDK\maxsdk\lib\x64\Release" /libpath:"..\..\..\lib\x64" /libpath:"..\..\..\lib\x64\vc11" /release
# SUBTRACT LINK32 /nologo /pdb:none

!ENDIF 

# Begin Target

# Name "vraydomemasterstereo - Win32 Debug"
# Name "vraydomemasterstereo - Win32 Max Release Official"
# Begin Group "Source Files"

# PROP Default_Filter "cpp;c;cxx;rc;def;r;odl;idl;hpj;bat"
# Begin Source File

SOURCE=.\plugin.def

!IF  "$(CFG)" == "vraydomemasterstereo - Win32 Debug"

!ELSEIF  "$(CFG)" == "vraydomemasterstereo - Win32 Max Release Official"

# PROP Exclude_From_Build 1

!ENDIF 

# End Source File
# Begin Source File

SOURCE=.\vraydomemasterstereo.cpp
# End Source File
# End Group
# Begin Group "Header Files"

# PROP Default_Filter "h;hpp;hxx;hm;inl"
# End Group
# Begin Group "Resource Files"

# PROP Default_Filter "ico;cur;bmp;dlg;rc2;rct;bin;rgs;gif;jpg;jpeg;jpe"
# End Group
# End Target
# End Project
