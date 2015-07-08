@ECHO OFF

ECHO.
ECHO Domemaster Shader For Arnold Installer
ECHO ---------------------------------------------------
ECHO.

cd C:\solidangle\Arnold-DomemasterStereo-src\source\LatLongStereo\

ECHO Installing the shader Files:
ECHO -------------------------------------
ECHO LatLongStereo.dll and LatLongStereo.mtd
copy LatLongStereo.dll C:\solidangle\mtoadeploy\2015\shaders
copy LatLongStereo.mtd C:\solidangle\mtoadeploy\2015\shaders

ECHO. 
ECHO. 
ECHO Installing the AE Template File:
ECHO -------------------------------------
ECHO LatLongStereoTemplate.py
copy LatLongStereoTemplate.py C:\solidangle\mtoadeploy\2015\scripts\mtoa\ui\ae

ECHO. 
ECHO Installation Complete.
ECHO. 
PAUSE