REM Andrew's Mental Ray Shader Compile Script 
REM Version 1.0

ECHO. Started compiling the mental ray shader
cl /c /O2 /MD /W3 -DWIN_NT -DBIT64 latlong_lens.cpp latlong_lens_dll.cpp

ECHO. Linking Shader
link /nodefaultlib:LIBC.LIB /OPT:NOREF /DLL /OUT:latlong_lens.dll latlong_lens.obj "c:\Program Files\Autodesk\Maya2011\devkit\mentalray\lib\nt\shader.lib"