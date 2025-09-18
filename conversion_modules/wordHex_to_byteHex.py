# author : anurag.gupta
# date   : 30-07-2025

# word_hex_string = "0x12345678 0xffff0000"  # space/comma separated 32bit hex number (may include 0x)
word_hex_string = "0x12345678 0xffff0000"    # space/comma separated 32bit hex number (may include 0x)

def wordHexToByteHex(word_hex_string):
    word_hex_string = word_hex_string.replace("0x", " ")
    word_hex_string = word_hex_string.replace(",", " ")
    word_hex_string_array = word_hex_string.split()
    hex_result_array = []

    for word_hex in word_hex_string_array:
        integer = int(word_hex, 16)
        #         byte1     byte2    byte3    byte4
        # bit     31-24     23-16    15-8     7-0
        byte1 = (integer & 0xFF000000) >> 24
        byte2 = (integer & 0x00FF0000) >> 16
        byte3 = (integer & 0x0000FF00) >> 8
        byte4 = (integer & 0x000000FF)

        byte_hex1 = f"{byte1:02x}"
        byte_hex2 = f"{byte2:02x}"
        byte_hex3 = f"{byte3:02x}"
        byte_hex4 = f"{byte4:02x}"

        hex_result_array.append(byte_hex1)
        hex_result_array.append(byte_hex2)
        hex_result_array.append(byte_hex3)
        hex_result_array.append(byte_hex4)

    hex_result_string = " ".join(hex_result_array)
    return hex_result_string


hex_result_string = wordHexToByteHex(word_hex_string)

print()
#print("Converted To Byte Hex : ")
print(hex_result_string)
print()