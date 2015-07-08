@ECHO OFF

ECHO.
ECHO Domemaster Shader For Arnold Installer
ECHO Version 1.0 - 2015-02-13 
ECHO ---------------------------------------------------
ECHO.

cd C:\solidangle\Arnold-DomemasterStereo-src\source\DomemasterWxH\

ECHO Installing the shader Files:
ECHO -------------------------------------
ECHO DomemasterWxH.dll and DomemasterWxH.mtd
copy DomemasterWxH.dll C:\solidangle\mtoadeploy\2015\shaders
copy DomemasterWxH.mtd C:\solidangle\mtoadeploy\2015\shaders

ECHO. 
ECHO. 
ECHO Installing the AE Template File:
ECHO -------------------------------------
ECHO DomemasterWxHTemplate.py
copy DomemasterWxHTemplate.py C:\solidangle\mtoadeploy\2015\scripts\mtoa\ui\ae

ECHO. 
ECHO Installation Complete.
ECHO. 
PAUSE