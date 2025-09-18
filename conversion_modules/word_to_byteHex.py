# author : anurag.gupta
# date   : 30-07-2025

# integer_string = "6176,5855,5,73,5112,12,160,2"  # space or comma separated integer(32 bits)
integer_string = "6176,5855,5,73,5112,12,160,2"    # space or comma separated integer(32 bits)

def wordToByteHex(integer_string):
    integer_string = integer_string.replace(",", " ")
    integer_array = integer_string.split()
    hex_result_array = []

    for integer_s in integer_array:
        integer = int(integer_s)
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


hex_result_string = wordToByteHex(integer_string)

print()
#print("Converted To Byte Hex : ")
print(hex_result_string)
print()