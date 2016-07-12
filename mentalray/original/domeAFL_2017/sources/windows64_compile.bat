@ECHO OFF
REM Andrew's Mental Ray Shader Compile Script 
REM Version 2.0

ECHO. Started compiling the mental ray shader
cl /c /O2 /MD /W3 -DWIN_NT -DBIT64 domeAFL_FOV_Stereo.c domeAFL_FOV.c domeAFL_WxH.c test_texture.c

ECHO. Linking Shader
link /manifest /nologo /nodefaultlib:LIBC.LIB /OPT:NOREF /DLL /INCREMENTAL:NO "C:\Program Files\Autodesk\mentalrayForMaya2016Beta7\devkit\lib\shader.lib" /OUT:domeAFL_FOV_Stereo.dll domeAFL_FOV_Stereo.obj domeAFL_FOV.obj domeAFL_WxH.obj test_texture.obj 



