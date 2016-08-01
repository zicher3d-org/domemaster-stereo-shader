@ECHO OFF
REM Andrew's Mental Ray Shader Compile Script 
REM Version 2.0


ECHO. Started compiling the mental ray shader

ECHO. Linking Shader
link /manifest /nologo /nodefaultlib:LIBC.LIB /OPT:NOREF /DLL /INCREMENTAL:NO /OUT:domeAFL_FOV_Stereo.dll domeAFL_FOV_Stereo.obj domeAFL_FOV.obj domeAFL_WxH.obj test_texture.obj shader.obj

