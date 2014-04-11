/******************************************************************************
* latlong_lens for mental ray by Ralf Habel 
* ralf.habel@vi-motion.de
******************************************************************************/

#define WIN32_LEAN_AND_MEAN
#include <windows.h>


BOOL APIENTRY DllMain(HANDLE hModule,
                      DWORD  ul_reason_for_call,
                      LPVOID lpReserved)
{
	switch (ul_reason_for_call)
	{
		case DLL_PROCESS_ATTACH:
		case DLL_THREAD_ATTACH:
		case DLL_THREAD_DETACH:
		case DLL_PROCESS_DETACH:
		break;
	}
	return TRUE;
}
