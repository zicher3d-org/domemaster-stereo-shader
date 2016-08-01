REM Andrew's Mental Ray Shader Compile Script 
REM Version 1.1

cd C:\Users\Andrew\Documents\GitHub\domemaster-stereo-shader\mentalray\Domemaster3D Installer\installer files\Domemaster3D\sources\latlong_lens_sources

ECHO. Started compiling the mental ray shader
cl /c /O2 /MD /W3 -DWIN_NT -DBIT64 latlong_lens.cpp latlong_lens_dll.cpp

ECHO. Linking Shader
link /nodefaultlib:LIBC.LIB /OPT:NOREF /DLL /OUT:latlong_lens.dll latlong_lens.obj "c:\Program Files\Autodesk\Maya2011\devkit\mentalray\lib\nt\shader.lib"