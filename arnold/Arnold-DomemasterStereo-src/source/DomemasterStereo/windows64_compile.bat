@ECHO OFF
ECHO Arnold Shader Compiling Script 
ECHO Version 1.0 - 2016-08-04 
ECHO ---------------------------------------
ECHO.
REM go to the compiling directory
cd C:\solidangle\Arnold-DomemasterStereo-src\source\DomemasterStereo\

ECHO  Compiling the Arnold Shader
cl /c /O2 /MD /W3 -DWIN_NT -DBIT64 DomemasterStereo.cpp

ECHO Linking Arnold Shader
link /nodefaultlib:LIBC.LIB /OPT:NOREF /DLL /OUT:DomemasterStereo.dll DomemasterStereo.obj "C:\solidangle\Arnold-4.2.14.0-windows\lib\ai.lib"