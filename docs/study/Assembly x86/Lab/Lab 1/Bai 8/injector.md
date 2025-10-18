---
title: injector
tags: [reverse, hooking, PE, notepad]
---

??? note "Code"

    
    ``` cpp title="injector.cpp" linenums="1" hl_lines="1"

    #include <windows.h>
    #include <tlhelp32.h>
    #include <stdio.h>

    DWORD GetProcessIdByName(const wchar_t* name) {
        HANDLE hSnap = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);
        if (hSnap == INVALID_HANDLE_VALUE) return 0;

        PROCESSENTRY32W pe = { sizeof(pe) };
        if (Process32FirstW(hSnap, &pe)) {
            do {
                if (_wcsicmp(pe.szExeFile, name) == 0) {
                    CloseHandle(hSnap);
                    return pe.th32ProcessID;
                }
            } while (Process32NextW(hSnap, &pe));
        }
        CloseHandle(hSnap);
        return 0;
    }

    BOOL InjectDLL(DWORD pid, const char* dllPath) {
        HANDLE hProc = OpenProcess(PROCESS_ALL_ACCESS, FALSE, pid);
        if (!hProc) return FALSE;

        SIZE_T len = strlen(dllPath) + 1;
        LPVOID pMem = VirtualAllocEx(hProc, NULL, len, MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
        if (!pMem) {
            CloseHandle(hProc);
            return FALSE;
        }

        if (!WriteProcessMemory(hProc, pMem, dllPath, len, NULL)) {
            VirtualFreeEx(hProc, pMem, 0, MEM_RELEASE);
            CloseHandle(hProc);
            return FALSE;
        }

        HMODULE hKernel = GetModuleHandleA("kernel32.dll");
        LPVOID pLoadLib = (LPVOID)GetProcAddress(hKernel, "LoadLibraryA");

        HANDLE hThread = CreateRemoteThread(hProc, NULL, 0, (LPTHREAD_START_ROUTINE)pLoadLib, pMem, 0, NULL);
        if (hThread) {
            WaitForSingleObject(hThread, INFINITE);
            CloseHandle(hThread);
        }

        VirtualFreeEx(hProc, pMem, 0, MEM_RELEASE);
        CloseHandle(hProc);
        return hThread != NULL;
    }

    int main() {
        printf("=== DLL Injector ===\n");

        char dllPath[MAX_PATH];
        GetCurrentDirectoryA(MAX_PATH, dllPath);
        strcat_s(dllPath, "\\hook.dll");

        if (GetFileAttributesA(dllPath) == INVALID_FILE_ATTRIBUTES) {
            printf("hook.dll not found!\n");
            system("pause");
            return 1;
        }

        DWORD pid = GetProcessIdByName(L"notepad.exe");
        if (!pid) {
            printf("Notepad not found! Open it first.\n");
            system("pause");
            return 1;
        }

        printf("Notepad PID: %d\nInjecting...\n", pid);

        if (InjectDLL(pid, dllPath)) {
            printf("[SUCCESS] Hook injected!\nTry Ctrl+S in Notepad.\n");
        }
        else {
            printf("[FAILED] Injection failed!\n");
        }

        system("pause");
        return 0;
    }
    ```