
## Bài 5: tính toán địa chỉ

6A 00
68 X -  Caption 
68 Y  - Text
6A 00
FF 15 Z

add-of-entry= 0x739D
image-base=0x1000000
--> Sum= 0x100739D = virtual-add (old-entry-point)
text:
virtualsize=0x7748
virtualadd=0x1000
rawsize=0x7800
rawadd=0x400

data:
virtualsize=0x1BA8
virtualadd=0x9000
rawsize=0x0800
rawadd=0x7C00

rsrc:
virtualsize=0x8958
virtualadd=0xB000 x
rawsize=0x8A00
rawadd=0x8400 x


Virtualsize - load size mem
virtual-add = load add mem
rawsize= size section
rawadd = add section

Z= 01001268
0x320 - start - code
0x360 - caption
0x380 - text

offset = raw-add - section-raw-add = virtual-add - section-virtual-add


caption - rawadd = X -  virtualadd
0x360 - 0x8400 = X - 0xB000
--> X = 0x2f60 --> X= X+imagebase = 0x1002f60

text - rawadd = Y -  virtualadd
0x380 - 0x8400 = Y - 0xB000
--> Y = 0x2f80 --> Y = Y+imagebase = 0x1002f80

new-entry-point= virtualrawadd-rawadd+virtualadd= 0x2f20
virtual-add-new-entry-point = imagebase+0x2f20= 0x1002f20


can 5 bytes

old-entry-point = 5+ relative_Virtual-add+ jum-Virtual-add
0x100739D	= 5+ relative_Virtual-add + 0x2f20+0x14 (14 bytes offset)
--> relative_Virtual-add = 0x1004464 = R


X = 0x1002f60
Y = 0x1002f80
Z= 01001268
R = 0x1004464




push 0                   ; 6a 00  
push Caption             ; 68       60 2f 00 01 X
push Text                ; 68       80 2f 00 01 Y
push 0                   ; 6a00  	
call [MessageBoxW]       ; ff15     68 12 00 01 Z
jmp Origianl_Entry_Point ; e9       64 44 00 01 relative_Virtual-add



IDA Pro → mở file .exe vừa compile

X = 0x80390101
Y = 0xA0390101
Z = 0x68120001
R = 0x443AFF00


6a 00 68 80 39 01 01 68 A0 39 01 01 6a 00 ff 15 68 12 00 01 e9 44 3A FF 00




6a 00 68403C010168603C01016a 00 ff 1568120001e98437FF
43 2E 6F 2E 64 2E 65 2E 20 2E 69 2E 6E 2E 6A 2E 2E 63 2E 74 2E 65 2E 64



## Bài 6: Tính toán địa chỉ

6A 00
68 X -  Caption 
68 Y  - Text
6A 00
FF 15 Z

add-of-entry= 0x739D
image-base=0x1000000
--> Sum= 0x100739D = virtual-add (old-entry-point)
text:
virtualsize=0x7748
virtualadd=0x1000
rawsize=0x7800
rawadd=0x400

data:
virtualsize=0x1BA8
virtualadd=0x9000
rawsize=0x0800
rawadd=0x7C00

rsrc:
virtualsize=0x8958
virtualadd=0xB000 x
rawsize=0x8A00
rawadd=0x8400 x


Virtualsize - load size mem
virtual-add = load add mem
rawsize= size section
rawadd = add section

Z= 01001268
0x11000 - start - code
0x11040 - caption
0x11060 - text

offset = raw-add - section-raw-add = virtual-add - section-virtual-add


caption - rawadd = X -  virtualadd
0x11040 - 0x8400 = X - 0xB000
--> X = 0x13C400 --> X= X+imagebase = 0x1013C40

text - rawadd = Y -  virtualadd
0x11060 - 0x8400 = Y - 0xB000
--> Y = 0x13C60 --> Y = Y+imagebase = 0x1013C60

new-entry-point= virtualrawadd-rawadd+virtualadd= 0x00013C00
virtual-add-new-entry-point = imagebase+0x00013C00= 0x1013C00


can 5 bytes

old-entry-point = 5+ relative_Virtual-add+ jum-Virtual-add
0x100739D	= 5+ relative_Virtual-add + 0x00013C00+0x14 (14 bytes offset)
--> relative_Virtual-add = 0xFFFF3784


X = 0x1013C40
Y = 0x1013C60
Z = 0xFFFF3784




push 0                   ; 6a 00  
push Caption             ; 68       403C0101 X
push Text                ; 68       603C0101 Y
push 0                   ; 6a00  	
call [MessageBoxW]       ; ff15     68120001 Z
jmp Origianl_Entry_Point ; e9       8437FFFF relative_Virtual-add



IDA Pro → mở file .exe vừa compile


6A 00 68 60 3C 01 01 68 40 3C 01 01 6A 00 FF 15 68 12 00 01 E9 84 37 FF FF

6A 00 68 A0 39 01 01 68 80 39 01 01 6A 00 FF 15
 68 12 00 01 E9 44 3A FF FF


## Code 

``` cpp title="Bai5.cpp" linenums="1" hl_lines="1"
#include <iostream>
#include <iomanip>
using namespace std;

// int VirtualToRaw(int virtualAddress, int rsrc_VirtualAddress, int rsrc_RawAddress) {
//     return virtualAddress - rsrc_VirtualAddress + rsrc_RawAddress;
// }

int RawToVirtual(int rawAddress, int rsrc_VirtualAddress, int rsrc_RawAddress) {
    return rawAddress - rsrc_RawAddress + rsrc_VirtualAddress;
}

void PrintHex(int value) {
    cout << " 0x" << hex << uppercase << setw(8) << setfill('0') << value << endl;
}

// print little-endian
void PrintLittleEndian(int value) {
    cout << " 0x";
    for (int i = 0; i < 4; i++) {
        cout << hex << uppercase << setw(2) << setfill('0') << ((value >> (i * 8)) & 0xFF);
    }
    cout << endl;
}

// print little-endian without 0x and space ever 2 characters
void PrintLittleEndianNoPrefix(int value) {
    for (int i = 0; i < 4; i++) {
        cout << hex << uppercase << setw(2) << setfill('0') << ((value >> (i * 8)) & 0xFF);
    }
}

int main() {
    int AddressOfEntryPoint, ImageBase, VirtualAddressOfCode;
    AddressOfEntryPoint = 0x0000739D;
    ImageBase = 0x01000000;
    VirtualAddressOfCode = AddressOfEntryPoint + ImageBase;
    //cout << "AddressOfEntryPoint:"; 
    //PrintHex(AddressOfEntryPoint);
    //cout << "ImageBase:";
    //PrintHex(ImageBase);
    //cout << "VirtualAddressOfCode:";
    //PrintHex(VirtualAddressOfCode);
    int rsrc_VirtualAddress = 0x000B000;
    //cout << "rsrc_VirtualAddress:";
    //PrintHex(rsrc_VirtualAddress);
    int rsrc_RawAddress = 0x00008400;
    //cout << "rsrc_RawAddress:";
    //PrintHex(rsrc_RawAddress);
    int startOfCode = 0x00010D40;
    cout << "StartOfCode:";
    PrintHex(startOfCode);
    int caption = startOfCode + 0x40; // X
    cout << "Caption (X):";
    PrintHex(caption);
    int text = startOfCode + 0x60; // Y
    cout << "Text (Y):";
    PrintHex(text);
    int x = RawToVirtual(caption, rsrc_VirtualAddress, rsrc_RawAddress) + ImageBase;
    int y = RawToVirtual(text, rsrc_VirtualAddress, rsrc_RawAddress) + ImageBase;
    cout << "Caption (X):";
    PrintHex(x);
    cout << "Text (Y):";
    PrintHex(y);
    cout << "Message_BoxM Z:";
    int z = 0x01001268;
    //PrintHex(z);
    int newAddressOfEntryPoint = RawToVirtual(startOfCode, rsrc_VirtualAddress, rsrc_RawAddress);
    cout << "New AddressOfEntryPoint:";
    PrintHex(newAddressOfEntryPoint);
    int jumpVirtualAddress = 0x14 + newAddressOfEntryPoint;
    int time = 0x5;
    int relativeAddressOfEntryPoint = VirtualAddressOfCode - time - newAddressOfEntryPoint - 0x14;
    cout << "Relative AddressOfEntryPoint:";
    PrintHex(relativeAddressOfEntryPoint);
    
    cout << "X =";
    PrintLittleEndian(x);
    cout << "Y =";
    PrintLittleEndian(y);
    cout << "Z =";
    PrintLittleEndian(z);
    cout <<"R =";
    PrintLittleEndian(relativeAddressOfEntryPoint);
    // shellcode
    // remove 0x and space ever 2 characters
    cout <<"6a 00 68";
    PrintLittleEndianNoPrefix(x);
    cout <<"68";
    PrintLittleEndianNoPrefix(y);
    cout <<"6a 00 ff 15";
    PrintLittleEndianNoPrefix(z);
    cout <<"e9";
    PrintLittleEndianNoPrefix(relativeAddressOfEntryPoint);
    return 0;
}
```