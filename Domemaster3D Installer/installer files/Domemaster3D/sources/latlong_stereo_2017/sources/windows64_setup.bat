@ECHO OFF
REM VC Setup Code
REM Version 2.0

ECHO Setting up the Visual Studio compiling environment 
ECHO.

REM Add mental ray include directory to %include%
set include=%include%;C:\Program Files\NVIDIA Corporation\mentalray for Maya 2017\devkit\include

REM ADD VC directories to PATH & Setup VC for 64 bit compiling

REM VC 10.0
REM path = %PATH%;C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\;C:\Program Files (x86)\Microsoft Visual Studio 10.0\VC\bin\
REM vcvarsall.bat amd64

REM VC 11
REM path=%PATH%;C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\;C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\bin\amd64\
REM vcvars64.bat

REM VC12
path=%PATH%;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\amd64
vcvars64.bat amd64

REM "C:\Program Files (x86)\Microsoft Visual Studio 12.0\Common7\Tools\VsDevCmd.bat"
