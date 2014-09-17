REM VC Setup Code
REM Version 1.0

ECHO. mental ray shader build script
ECHO.

REM ADD VC directories to PATH
path = %PATH%;C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\;C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin\

REM Add mental ray include directory to %include%
set include = %include%;C:\Program Files\Autodesk\Maya2011\devkit\mentalray\include\

REM Setup VC for 64 bit compiling
vcvarsall.bat amd64
