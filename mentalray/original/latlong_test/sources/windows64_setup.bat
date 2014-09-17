REM VC Setup Code
REM Version 1.0

@ECHO OFF
ECHO Setting up the Visual Studio compiling environment 

REM ADD VC directories to PATH
path=%PATH%;C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\;C:\Program Files (x86)\Microsoft Visual Studio 11.0\VC\bin\amd64\

REM Add Arnold include directory to %INCLUDE%
set INCLUDE="C:\Program Files\Autodesk\mentalrayForMaya2014\devkit\include";%INCLUDE%;

REM Setup VC for 64 bit compiling
vcvars64.bat
