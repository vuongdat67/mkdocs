## Code tìm shellcode nhưng bị window ghi đè sau mỗi lần build IAT 

??? note "Code"

    
    ``` cpp title="Bai8.cpp" linenums="1" hl_lines="1"
    #include <iostream>
    #include <iomanip>
    using namespace std;

    void PrintLE(unsigned int val) {
        for (int i = 0; i < 4; i++)
            cout << hex << uppercase << setw(2) << setfill('0') 
                << ((val >> (i*8)) & 0xFF) << " ";
    }

    void PrintHexString(const char* str) {
        while (*str) {
            cout << hex << uppercase << setw(2) << setfill('0') 
                << (int)(unsigned char)*str << " 00 ";
            str++;
        }
        cout << "00 00"; // null terminator
    }

    int main() {
        cout << "=== HOOK READFILE - TINH TOAN DIA CHI ===" << endl;
        
        // === CÁC THAM SỐ CỐ ĐỊNH ===
        unsigned int ImageBase = 0x01000000;
        unsigned int rsrc_VA = 0x0000B000;
        unsigned int rsrc_RA = 0x00008400;
        unsigned int msgbox_VA = 0x01001268;
        
        // === ĐỊA CHỈ RAW CỦA CÁC VÙNG ===
        unsigned int shellcode_RA = 0x10D40;
        unsigned int backup_RA = 0x10D60;
        unsigned int caption_RA = 0x10D80;
        unsigned int text_RA = 0x10DD0;
        
        // === CHUYỂN ĐỔI RAW → VIRTUAL ===
        unsigned int shellcode_VA = ImageBase + (shellcode_RA - rsrc_RA + rsrc_VA);
        unsigned int backup_VA = ImageBase + (backup_RA - rsrc_RA + rsrc_VA);
        unsigned int caption_VA = ImageBase + (caption_RA - rsrc_RA + rsrc_VA);
        unsigned int text_VA = ImageBase + (text_RA - rsrc_RA + rsrc_VA);
        
        cout << "\n=== DIA CHI VIRTUAL ===" << endl;
        cout << "Shellcode VA: 0x" << hex << uppercase << shellcode_VA << endl;
        cout << "Backup VA:    0x" << hex << uppercase << backup_VA << endl;
        cout << "Caption VA:   0x" << hex << uppercase << caption_VA << endl;
        cout << "Text VA:      0x" << hex << uppercase << text_VA << endl;
        
        // === BƯỚC 1: GHI ĐÈ IAT ===
        cout << "\n=== BUOC 1: PATCH IAT READFILE ===" << endl;
        cout << "Tai dia chi 0x500 (hoac dia chi IAT ban tim duoc), ghi:" << endl;
        cout << "   ";
        PrintLE(shellcode_VA);
        cout << endl;
        cout << "   (dia chi shellcode little-endian)" << endl;
        
        // === BƯỚC 2: BACKUP READFILE GỐC ===
        cout << "\n=== BUOC 2: BACKUP READFILE GOC ===" << endl;
        cout << "Tai dia chi 0x10D60, ghi dia chi ReadFile goc tu IAT" << endl;
        cout << "   (VD: 0E 18 80 7C - phai xem trong HxD tai 0x500)" << endl;
        
        // === BƯỚC 3: SHELLCODE ===
        cout << "\n=== BUOC 3: SHELLCODE TAI 0x10D40 ===" << endl;
        cout << "6A 00 68 ";
        PrintLE(caption_VA);
        cout << "68 ";
        PrintLE(text_VA);
        cout << "6A 00 FF 15 ";
        PrintLE(msgbox_VA);
        cout << "FF 25 ";
        PrintLE(backup_VA);
        cout << endl;
        
        // Giải thích từng phần
        cout << "\nGIAI THICH:" << endl;
        cout << "6A 00                 = push 0 (uType)" << endl;
        cout << "68 ";
        PrintLE(caption_VA);
        cout << " = push caption" << endl;
        cout << "68 ";
        PrintLE(text_VA);
        cout << " = push text" << endl;
        cout << "6A 00                 = push 0 (hWnd)" << endl;
        cout << "FF 15 ";
        PrintLE(msgbox_VA);
        cout << " = call MessageBoxW" << endl;
        cout << "FF 25 ";
        PrintLE(backup_VA);
        cout << " = jmp [backup] (goi ReadFile goc)" << endl;
        
        // === BƯỚC 4: CAPTION ===
        cout << "\n=== BUOC 4: CAPTION TAI 0x10D80 ===" << endl;
        cout << "Unicode (UTF-16LE): ";
        PrintHexString("ReadFile Hook");
        cout << endl;
        
        // === BƯỚC 5: TEXT ===
        cout << "\n=== BUOC 5: TEXT TAI 0x10DD0 ===" << endl;
        cout << "Unicode (UTF-16LE): ";
        PrintHexString("Dang doc file...");
        cout << endl;
        
        // === TỔNG KẾT ===
        cout << "\n=== TONG KET CÁC DIA CHI CAN GHI ===" << endl;
        cout << "1. IAT (0x500):      ";
        PrintLE(shellcode_VA);
        cout << endl;
        cout << "2. Backup (0x10D60): [Dia chi ReadFile goc tu IAT]" << endl;
        cout << "3. Shell (0x10D40):  [Hex o tren]" << endl;
        cout << "4. Caption (0x10D80):[Text Unicode]" << endl;
        cout << "5. Text (0x10DD0):   [Text Unicode]" << endl;
        
        return 0;
    }
    ```