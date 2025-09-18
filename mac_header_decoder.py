# Author: linkedin.com/in/anuraggupta29
# Date: 30-07-2025
# Description: This script decodes MAC headers for UL

# Hex to Decode ---------------------------
# #byte_hex = "3d 3a 05 49 33 0c a0 02"

from lcid_mapping import lcid_map

# enter only in byteHex for mat. Use other modules if conversion to byteHex Required
byte_hex_local = "3d 3a 05 49 33 0c a0 02"

tbs_size_local = 49

#-------------------------------------------


def macUlHeaderDecoder(byte_hex, tbs_size):

    def getByteArray(byte_hex):
        byte_hex = byte_hex.replace("0x", " ")
        byte_hex = byte_hex.replace(" ", " ")
        return [int(bh, 16) for bh in byte_hex.split()]

    def getLcid(byte):
        return byte & 0x1f

    def hasNextHeaderE(byte):
        return (byte >> 5) & 1

    def getSduLengthTypeF2(byte):
        return (byte >> 6) & 1

    def getSduLengthTypeF(byte):
        return (byte >> 7) & 1
    
    def getSduLengthF0(byte):
        return byte & 0x7f

    def getSduLengthF1(byte1, byte2):
        return ((byte1 & 0x7f) << 8) + byte2

    byte_array = getByteArray(byte_hex)

    decoded_header = []  # result

    total_packet_size = 0
    extension_bit = 1
    error = False

    byte_idx = 0
    header_idx = 0

    while (not error) and extension_bit and (byte_idx < len(byte_array)):
        byte = byte_array[byte_idx]
        lcid = getLcid(byte)
        extension_bit = hasNextHeaderE(byte)
        f2_bit = getSduLengthTypeF2(byte)
        message = ""
        payload_size = -1
        header_size = 1
        subheader_description = lcid_map[lcid][3]
        f_bit = -1
        header_idx += 1

        if f2_bit:
            error = True
            message = "Error1: F2 Bit not supported. Stopping processing."
            #print(message)

        elif (lcid == 16):
            error = True
            message = "Error2: Extended LCID not supported. Stopping processing."
            #print(message)

        elif (lcid <= 12) or (lcid >= 22 and lcid <= 25):
            # LCID 22,23,24,25 are variable length MAC CEs
            # MAC LCID <= 12 needs to be sent to RLC (it has logical channel and common channel header information)

            byte_idx += 1

            if byte_idx < len(byte_array):
                if extension_bit:
                    header_size += 1
                    byte2 = byte_array[byte_idx]
                    f_bit = getSduLengthTypeF(byte2)

                    if f_bit:
                        byte_idx += 1

                        if byte_idx < len(byte_array):
                            header_size += 1
                            byte3 = byte_array[byte_idx]
                            payload_size = getSduLengthF1(byte2, byte3)
                        else:
                            message = "Error3: Not enough bytes to decode the packet."
                            #print(message)
                            error = True
                    else:
                        payload_size = getSduLengthF0(byte2)
                else:
                    # if last subheader, all remaining bytes will be payload
                    payload_size = tbs_size - total_packet_size - header_size
            else:
                message = "Error4: Not enough bytes to decode the packet."
                #print(message)
                error = True

        elif(lcid>12):
            # fixed size MAC CEs
            payload_size = lcid_map[lcid][1]

        if(lcid>12 and lcid<26):
            message += " Warning: MAC Control Element with LCID {} is present.".format(lcid)

        subheader_data = {
            "Header Index" : header_idx,
            "Sub Header" : subheader_description,
            "LCID" : lcid,
            "Header Size": header_size,
            "Payload Size": payload_size,
            "Extension Bit": extension_bit,
            "Message": message,
            "F2 Bit": f2_bit,
            "F Bit": f_bit
        }

        decoded_header.append(subheader_data)

        total_packet_size += (header_size + payload_size)
        byte_idx += 1


    if (not error):
        subheader_data = {
            "Padding Stats": "",
            "TB Size": tbs_size,
            "Total Decoded Size": total_packet_size,
            "Padding Size (exclude Padding CE)": tbs_size - total_packet_size
        }
    else:
        subheader_data = {
            "Padding Stats": "Error was detected in decoding"
        }

    decoded_header.append(subheader_data)
    
    return decoded_header


decoded_header = macUlHeaderDecoder(byte_hex_local, tbs_size_local)  # Final result

print()
for subheader in decoded_header:
    print(subheader)
print()