@ECHO OFF
REM Andrew's Mental Ray Shader Compile Script 
REM Version 2.0

cd %USERPROFILE%"\Documents\GitHub\domemaster-stereo-shader\mentalray\original\latlong_stereo_2017\sources"

ECHO. Started compiling the mental ray shader
cl /c /O2 /MD /W3 -DWIN_NT -DBIT64 LatLong_Stereo.c  "C:\Program Files\NVIDIA Corporation\mentalray for Maya 2017\devkit\shaders\shader.c"

ECHO. Linking Shader
link /manifest /nologo /nodefaultlib:LIBC.LIB /OPT:NOREF /DLL /INCREMENTAL:NO /OUT:LatLong_Stereo.dll LatLong_Stereo.obj shader.obj