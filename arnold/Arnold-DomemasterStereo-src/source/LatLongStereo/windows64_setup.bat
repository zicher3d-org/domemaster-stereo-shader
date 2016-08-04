@ECHO OFF
ECHO Setting up the Visual Studio compiling environment 

REM ADD VC directories to PATH
path=%PATH%;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\;C:\Program Files (x86)\Microsoft Visual Studio 12.0\VC\bin\amd64\

REM Add Arnold include directory to %INCLUDE%
set INCLUDE=C:\solidangle\Arnold-4.2.14.0-windows\include\;%INCLUDE%;

REM Setup VC for 64 bit compiling
vcvars64.bat

