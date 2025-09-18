#author     : linkedin.com/in/anuraggupta29
#date       : 30-07-2025
#description: This script decodes MAC headers for multiple lines of input

import os
from mac_header_decoder import macUlHeaderDecoder
from lcid_mapping import lcid_map
from conversion_modules.byte_to_byteHex import byteToByteHex

print(os.getcwd()) # make sure you are in correct directory

packets = open('files/packets.txt', 'r')  # input file containing packets to decode

open('files/decoded_result.txt', 'w').close()  # clear the result file
resultFile = open('files/decoded_result.txt', 'w')  # result file

count = 0
lcid_count = [0] * 32

for pdu in packets:
    byte_hex = byteToByteHex(pdu)  # if input is in bytes, use this function to convert to hex
    decoded_header = macUlHeaderDecoder(byte_hex, 10000)  # tbs_size data not available so putting as 10000

    resultFile.write("\n\nCount : {}, Packet : {}\n".format(count, pdu))
    for subheader in decoded_header:
        resultFile.write(str(subheader) + '\n')

        if "LCID" in subheader:  # statistics
            lcid_count[subheader["LCID"]] += 1

    count += 1
    if (count % 10000 == 0):
        print("Processed " + str(count) + " packets")

for lcid in range(32):
    print("LCID : {}, Count : {}, Description : {}".format(
        lcid, lcid_count[lcid], lcid_map[lcid][3]))