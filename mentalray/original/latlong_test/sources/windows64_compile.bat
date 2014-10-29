@ECHO OFF
REM Andrew's Mental Ray Shader Compile Script 
REM Version 1.1

cd C:\Users\Andrew\Documents\GitHub\domemaster-stereo-shader\mentalray\original\latlong_test\sources

ECHO. Started compiling the mental ray shader
cl /c /O2 /MD /W3 -DWIN_NT -DBIT64 LatLong_Stereo.c

ECHO. Linking Shader
link /nodefaultlib:LIBC.LIB /OPT:NOREF /DLL /OUT:LatLong_Stereo.dll LatLong_Stereo.obj "C:\Program Files\Autodesk\mentalrayForMaya2015\devkit\lib\nt\shader.lib"