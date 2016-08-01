REM Andrew's Mental Ray Shader Compile Script 
REM Version 2.0

cd %USERPROFILE%"\Documents\GitHub\domemaster-stereo-shader\mentalray\original\latlong_lens_2017"

ECHO. Started compiling the mental ray shader
cl /c /O2 /MD /W3 -DWIN_NT -DBIT64 latlong_lens.cpp latlong_lens_dll.cpp "C:\Program Files\NVIDIA Corporation\mentalray for Maya 2017\devkit\shaders\shader.c"

ECHO. Linking Shader
link /manifest /nologo /nodefaultlib:LIBC.LIB /OPT:NOREF /DLL /INCREMENTAL:NO /OUT:latlong_lens.dll latlong_lens_dll.obj latlong_lens.obj shader.obj