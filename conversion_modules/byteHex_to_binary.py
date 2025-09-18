# author : anurag.gupta
# date   : 30-07-2025

# byte_hex_string = "0x3d 3a 05 49 33 0c a0 02"  # space/comma separated 8bit hex number (may include 0x)
byte_hex_string = "0x3d 3a 05 49 33 0c a0 02"    # space/comma separated 8bit hex number (may include 0x)

def byteHexToBinary(byte_hex_string):
    byte_hex_string = byte_hex_string.replace("0x", " ")
    byte_hex_string = byte_hex_string.replace(",", " ")
    byte_hex_string_array = byte_hex_string.split()
    binary_string_array = []

    for hex_num in byte_hex_string_array:
        byte_value = int(hex_num, 16)
        binary_string = f"{byte_value:08b}"
        binary_string_array.append(binary_string)

    binary_string = " ".join(binary_string_array)
    return binary_string


binary_string = byteHexToBinary(byte_hex_string)

print()
#print("Converted To Binary : ")
print(binary_string)
print()