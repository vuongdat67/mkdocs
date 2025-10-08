# Bài thực hành 7:	Chỉnh sửa luồng thực thi mà không thay đổi Entry Point
a.	Phân tích sơ lược
Thay vì đổi AddressOfEntryPoint như bài 5, 6 trước đó:
-	Phải tìm 1 function được gọi sớm trong notepad.exe
-	Chèn shellcode vào vùng trống của PE
-	Ghi đè 1 vài byte của function đó để nhảy đến shellcode (không chứa các API hoặc lời gọi hàm khác tiên quyết để tránh bị crash notepad)
-	Shellcode chạy xong phải nhảy đúng lại chỗ notepad khi nãy để chạy bình thường
b.	Địa chỉ Raw của hook point
Phân tích trong IDA Pro:
Bước 1: Xem các địa chỉ đề cập trong bài 5, 6 trước đó
 
Nhảy đến entrypoint ban đầu là start
Phân tích:
Entrypoint lời gọi __SEH_prolog và GetModuleHandleA
Ban đầu em dự định ghi đè 1 trong 2 hàm này nhưng khi vào xem tiếp các địa chỉ được gọi đến thì nhận ra đây có khả năng cao là đoạn code khởi tạo, chạy trước WinMain nên sẽ không được sửa.
Điều này gây khó khăn khi xác định được đoạn code nào có thể sẽ được chọn để ghi đè. Nên do đó em tìm hiểu compiler Microsoft có function prologue chuẩn là 55 8B EC, chú trọng các hexdump này để tìm kiếm trong các dãy
Tại sao phải tìm nó?
-	Để xác định ranh giới các function
-	Tìm function nào được gọi sớm trong quá trình khởi động đã nói trên
-	Thay thế 1 vài lệnh bằng jmp shellcode
 Bước 2: Tìm Function phù hợp để Patch
Tiếp nói phần trên, các địa chỉ sau đây được lọc để xác định xem nên chọn địa chỉ nào

010019E0  8B FF 55 8B EC 6A 01 6A  00 FF 35 38 98 00 01 FF

01001A20  C2 08 00 CC CC CC CC CC  8B FF 55 8B EC 51 51 8B

01001BE0  C2 04 00 CC CC CC CC CC  8B FF 55 8B EC 8B 45 08

Trong danh sách trên, nhận định rằng sub_10019E0 là địa chỉ đầu tiên, có các đặc điểm thỏa mãn, không gây crash, dễ ghi đè và đặc biệt nằm gần đầu .text section và có thể được thực hiện lời gọi hàm trong quá trình khởi tạo
Với 8B FF: mov edi, edi – Lệnh NOP mở rộng, không làm gì, dùng để can thiệp/hook function
Với 55: push ebp: lưu giá trị hiện tại vào stack thiết lập lại stack frame mới
Với 8B EC: mov ebp, esp: sao chép esp – con trỏ stack hiện tại vào ebp để hoàn thành tạo stack frame
c.	Dự định ghi đè
Ý tưởng:
-	Shellcode sẽ nằm ở vùng trống trong .rsrc x00010D40
-	Thay 5 bytes đầu của function địa chỉ 0x010019E0  bằng E9 + 4 bytes để thực hiện lệnh nhảy đến shellcode
-	Sau khi shellcode chạy xong phải thực hiện lại 5 bytes gốc và nhảy về tiếp tục function
d.	Tính toán địa chỉ
Tính toán địa chỉ nhảy từ function đến shellcode
Mở CFF vào Section Header để xem các giá trị:
 
Lưu ý các giá trị của vùng .text
.text: VA = 0x00001000, RA = 0x00000400
.data: VA = 0x00009000, RA = 0x00007C00
.rsrc: VA = 0x0000B000, RA = 0x00008400
-	Địa chỉ trong IDA Pro là địa chỉ ảo, nên cần chuyển sang địa chỉ thực trong Hxd để xác định vị trí cần ghi đè
Công thức:
Virtual Address (VA) = ImageBase + RVA = 0x01000000 + RVA = 0x010019E0  
 RVA = 0x19E0
Raw Address (RA) = RVA – Section_VA + Section_RA
RA = 0x19E0 – 0x1000 + 0x400 (phải lấy .text vì đang thuộc trong .text không phải .srsc)
= 0x0DE
Chọn địa chỉ 0x00010D40 làm địa chỉ bắt đầu ghi đè (Start_Of_Code)
Chọn địa chỉ 0x00010D80 làm địa chỉ lưu caption (Raw_Address)
Chọn địa chỉ 0x00010DD0 làm địa chỉ lưu text (Raw_Address)



Địa chỉ mới khi bắt đầu ghi đè (Chuyển từ Raw sang Virtual)
New_Entry_Point = Start_Of_Code - Section_ Raw_Address + VirtualAddress
= 0x00013940
Ở bài 5, 6 trước đó thì offset là 0x14 (20 bytes) + 0x5 (5 bytes) ghi đè = 0x19 (25 bytes)
6A 00              ; 2 bytes - push 0
68 80 39 01 01     ; 5 bytes - push caption
68 D0 39 01 01     ; 5 bytes - push text  
6A 00              ; 2 bytes - push 0
FF 15 68 12 00 01  ; 6 bytes - call MessageBoxW
                   ; ───────
                   ; TỔNG: 20 bytes (0x14)

8B FF              ; 2 bytes - mov edi,edi (khôi phục)
55                 ; 1 byte  - push ebp
8B EC              ; 2 bytes - mov ebp,esp
                   ; ───────
                   ; + 5 bytes = 0x19

E9 XX XX XX XX     ; 5 bytes – jmp thay 8B FF 55 8B EC
Tính toán relative offset cho JMP
Công thức: target = current_address + 5 + offset
Vậy lệnh nhảy phải cộng thêm 0x5 từ 0x14 nữa tại vì phải ghi đè thêm 5 bytes từ địa chỉ thực 0x0DE vừa tính 
JMP_BACK = 0x00013940 – (0x010019E0+5)  
= 0x11F5B
Chuyển sang little_endian: 5B 1F 01 00
Vậy tại 0x0DE trong Hxd ghi đè để đi đến shellcode
E9 5B 1F 01 00
Tương tự bài 6, nhưng đổi 1 tí ở địa chỉ Text là 0x10DD0:
Với X, Y, Z các các bytes địa chỉ dạng little-endian(x86) cần tìm để ghi đè
Chuyển từ Raw sang Virtual của Caption và Text:
X = Raw_Address – Section_ Raw_Address + VirtualAddress
= 0x00010D80 - 0x00008400 + 0x0000B000
= 0x00013980
X = X + ImageBase = 0x00013980 + 0x01000000
=0x01013980


Y = Raw_Address – Section_ Raw_Address + VirtualAddress
= 0x00010DD0 - 0x00008400 + 0x0000B000
Y = Y + ImageBase = 0x010139D0 + 0x01000000
=0x010139D0
Z = 0x01001268 của Message_Box
Địa chỉ mới khi bắt đầu ghi đè (Chuyển từ Raw sang Virtual)
d.1.	Chuyển sang little_endian
X = 0x80390101
Y = 0xD0390101
Z = 0x68120001
Xử lý phần JMP shellcode đến return về phần code bị ghi đè để thực hiện tiếp chương trình notepad:
Phần địa chỉ tiếp theo cần nhảy về sau khi bị ghi đè ảo: VA = 0x19E0+ 5 = 0x19E5
Vị trí lệnh JMP khi thực hiện shellcode = 0x00013940 + 0x19 = 0x01013959
offset = return_VA - (jmp_instruction_VA + 5)
       = 0x010019E5 - (0x01013959 + 5)
       = 0x010019E5 - 0x0101395E
       = 0xFFFE6087
Shellcode:
6A 00 68 80 39 01 01 68 D0 39 01 01 6A 00 FF 15 68 12 00 01 8B FF 55 8B EC E9 87 E0 FE FF
Tổng kết:
; === Hiển thị MessageBox ===
6A 00              push 0                 ; uType
68 80 39 01 01     push 0x01013980        ; lpCaption
68 D0 39 01 01     push 0x010139A0        ; lpText
6A 00              push 0                 ; hWnd
FF 15 68 12 00 01  call [0x01001268]      ; MessageBoxW

; === Trampoline: khôi phục 5 bytes gốc ===
8B FF              mov edi, edi
55                 push ebp
8B EC              mov ebp, esp

; === Nhảy về tiếp function ===
E9 87 60 FE FF     jmp 0x010019E5


## Code 

``` cpp title="Bai7.cpp" linenums="1" hl_lines="1"
#include <iostream>
#include <iomanip>
using namespace std;

void PrintLE(int val) {
    for (int i = 0; i < 4; i++)
        cout << hex << uppercase << setw(2) << setfill('0') 
             << ((val >> (i*8)) & 0xFF) << " ";
}

int main() {
    int hook_VA = 0x010019E0;
    int shellcode_VA = 0x01013940;
    
    // === JMP 1: Từ function → shellcode ===
    int jmp1 = shellcode_VA - (hook_VA + 5);
    cout << "PATCH tại 0x0DE0: E9 ";
    PrintLE(jmp1);
    cout << endl;
    
    // === Shellcode ===
    int caption_VA = 0x01013980;
    int text_VA = 0x010139A0;
    int msgbox_VA = 0x01001268;
    
    // === JMP 2: Từ shellcode → sau hook ===
    int return_VA = hook_VA + 5;  // 0x010019E5
    
    // Tính vị trí lệnh JMP trong shellcode:
    // 6A 00           (2)
    // 68 XX XX XX XX  (5)
    // 68 XX XX XX XX  (5)
    // 6A 00           (2)
    // FF 15 XX XX XX XX (6)
    // 8B FF           (2)
    // 55              (1)
    // 8B EC           (2)
    // E9              (ở đây)
    // TỔNG: 2+5+5+2+6+2+1+2 = 25 = 0x19
    
    int jmp_pos = shellcode_VA + 0x19;
    int jmp2 = return_VA - (jmp_pos + 5);

    cout << "\nShellcode tại 0x10D40:\n";
    cout << "6A 00 68 ";
    PrintLE(caption_VA);
    cout << "68 ";
    PrintLE(text_VA);
    cout << "6A 00 FF 15 ";
    PrintLE(msgbox_VA);
    cout << "8B FF 55 8B EC E9 ";
    PrintLE(jmp2);
    cout << endl;
    
    // Kiểm tra tính toán
    cout << "\n=== KIỂM TRA ===" << endl;
    cout << "Hook VA: 0x" << hex << hook_VA << endl;
    cout << "Return VA: 0x" << hex << return_VA << endl;
    cout << "JMP instruction VA: 0x" << hex << jmp_pos << endl;
    cout << "Target (should = Return VA): 0x" << hex << (jmp_pos + 5 + jmp2) << endl;
    
    return 0;
}
```