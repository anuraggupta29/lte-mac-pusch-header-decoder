# LTE MAC PUSCH Header Decoder

This repository provides a set of tools to decode **LTE MAC PUSCH (Physical Uplink Shared Channel)** headers.  
It helps analyze the MAC header structure of data transmitted over LTE networks and is particularly useful for debugging and protocol analysis.

---

## Features
- Convert raw packet data to hex format
- Decode LTE MAC PUSCH headers (LCID, Header Size, Payload Size, Extension Bits, etc.)
- Handle multiple packets in a single file
- Identify and display padding statistics
- Simple CLI-based workflow

---

## Usage Example


### Example Input
```text
Get the header data in comma or space separated byte, word, word hex or byte hex.
Byte example:
61 56 7 33 2 31 0 0
```

---

### **Step 1: Convert Data to ByteHex**
Use `byte_to_byteHex.py` to convert raw packet data to hex. (or use other conversion script for word/wordhex)

Example Output:
```text
Converted To Byte Hex:
3d 3a 05 49 33 0c a0 02
```

---

### **Step 2: Decode the MAC Header**
Run `mac_header_decoder.py` to decode the converted hex data (provide the byte hex as input string).

Example Output:
```
{'Header Index': 1, 'Sub Header': 'Short BSR', 'LCID': 29, 'Header Size': 1, 'Payload Size': 1, 'Extension Bit': 1, 'Message': '', 'F2 Bit': 0, 'F Bit': -1}
{'Header Index': 2, 'Sub Header': 'Power Headroom Report', 'LCID': 26, 'Header Size': 1, 'Payload Size': 1, 'Extension Bit': 1, 'Message': '', 'F2 Bit': 0, 'F Bit': -1}
{'Header Index': 3, 'Sub Header': 'Logical Channel 5', 'LCID': 5, 'Header Size': 1, 'Payload Size': 44, 'Extension Bit': 0, 'Message': '', 'F2 Bit': 0, 'F Bit': -1}    
{'Padding Stats': '', 'TB Size': 49, 'Total Decoded Size': 49, 'Padding Size (exclude Padding CE)': 0}

```

---

### **Step 3: Decode Multiple Packets**
```
To decode multiple packets from a file, use file multiline_mac_header_decoder.py
```

---

## Scripts Provided
- **byte_to_byteHex.py** → Converts 8-bit bytes to byte hex format  
- **word_to_byteHex.py** → Converts 32-bit words to byte hex format  
- **wordHex_to_byteHex.py** → Converts word hex to byte hex  
- **byteHex_to_binary.py** → Converts byte hex to binary  

---

## 🛠 Installation & Setup

Clone the repository:
```bash
git clone https://github.com/your-username/lte-mac-pusch-decoder.git
cd lte-mac-pusch-decoder
```

Run the decoder scripts as needed using VS Code or any Terminal (Python must be installed)

---

## Author
- **Anurag Gupta**  
  [LinkedIn](https://www.linkedin.com/in/anuraggupta29/) | [GitHub](https://github.com/anuraggupta29)