# author : linkedin.com/in/anuraggupta29
# date   : 30-07-2025

# byte_string = "61,58,5,73,51,12,160,2"  # space or comma separated byte(8 bits)
byte_string = "61 56 7 33 2 31 0 0"       # space or comma separated byte(8 bits)

def byteToByteHex(byte_string):
    byte_string = byte_string.replace(",", " ")
    byte_array = byte_string.split()
    hex_result_array = []

    for byte in byte_array:
        byte_hex = f"{int(byte):02x}"
        hex_result_array.append(byte_hex)

    hex_result_string = " ".join(hex_result_array)
    return hex_result_string


hex_result_string = byteToByteHex(byte_string)

print()
#print("Converted To Byte Hex : ")
print(hex_result_string)
print()