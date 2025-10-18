---
title: hook dll
tags: [reverse, hooking, PE, notepad]
---

??? note "Code"

    
    ```cpp title="hook.cpp" linenums="1"
    #include <windows.h>

    #pragma comment(lib, "user32.lib")

    typedef BOOL(WINAPI* WriteFile_t)(HANDLE, LPCVOID, DWORD, LPDWORD, LPOVERLAPPED);
    WriteFile_t OriginalWriteFile = NULL;

    BOOL WINAPI HookedWriteFile(HANDLE hFile, LPCVOID lpBuffer, DWORD nNumberOfBytesToWrite,
        LPDWORD lpNumberOfBytesWritten, LPOVERLAPPED lpOverlapped) {
        MessageBoxW(NULL, L"23520281", L"MSSV", MB_OK);
        return OriginalWriteFile(hFile, lpBuffer, nNumberOfBytesToWrite,
            lpNumberOfBytesWritten, lpOverlapped);
    }

    BOOL HookIAT() {
        HMODULE hModule = GetModuleHandle(NULL);
        if (!hModule) return FALSE;

        PIMAGE_DOS_HEADER pDosHeader = (PIMAGE_DOS_HEADER)hModule;
        if (pDosHeader->e_magic != IMAGE_DOS_SIGNATURE) return FALSE;

        PIMAGE_NT_HEADERS pNtHeaders = (PIMAGE_NT_HEADERS)((BYTE*)hModule + pDosHeader->e_lfanew);
        if (pNtHeaders->Signature != IMAGE_NT_SIGNATURE) return FALSE;

        DWORD importRVA = pNtHeaders->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_IMPORT].VirtualAddress;
        if (!importRVA) return FALSE;

        PIMAGE_IMPORT_DESCRIPTOR pImportDesc = (PIMAGE_IMPORT_DESCRIPTOR)((BYTE*)hModule + importRVA);

        while (pImportDesc->Name) {
            LPCSTR dllName = (LPCSTR)((BYTE*)hModule + pImportDesc->Name);

            if (_stricmp(dllName, "KERNEL32.dll") == 0) {
                PIMAGE_THUNK_DATA pThunk = (PIMAGE_THUNK_DATA)((BYTE*)hModule + pImportDesc->FirstThunk);
                PIMAGE_THUNK_DATA pOrigThunk = (PIMAGE_THUNK_DATA)((BYTE*)hModule + pImportDesc->OriginalFirstThunk);

                while (pThunk->u1.Function && pOrigThunk->u1.Function) {
                    if (!(pOrigThunk->u1.Ordinal & IMAGE_ORDINAL_FLAG)) {
                        PIMAGE_IMPORT_BY_NAME pImport = (PIMAGE_IMPORT_BY_NAME)((BYTE*)hModule + pOrigThunk->u1.AddressOfData);

                        if (strcmp(pImport->Name, "WriteFile") == 0) {
                            DWORD oldProtect;
                            VirtualProtect(&pThunk->u1.Function, sizeof(DWORD), PAGE_READWRITE, &oldProtect);

                            OriginalWriteFile = (WriteFile_t)pThunk->u1.Function;
                            pThunk->u1.Function = (DWORD_PTR)HookedWriteFile;

                            VirtualProtect(&pThunk->u1.Function, sizeof(DWORD), oldProtect, &oldProtect);
                            return TRUE;
                        }
                    }
                    pThunk++;
                    pOrigThunk++;
                }
            }
            pImportDesc++;
        }
        return FALSE;
    }

    BOOL APIENTRY DllMain(HMODULE hModule, DWORD reason, LPVOID lpReserved) {
        if (reason == DLL_PROCESS_ATTACH) {
            DisableThreadLibraryCalls(hModule);
            HookIAT();
        }
        return TRUE;
    }
    ```