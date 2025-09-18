# author : linkedin.com/in/anuraggupta29
# date   : 30-07-2025
# description : LCID Mapping Table
#
# LCID <= 12 correspond to SDUs and have variable length
# MAC CE LCID 22,23,24,25 have variable length
# LCID 16 is extended LCID and it is not supported
# F2 Bit as 1 is also not supported
# Subheader size is different from payload size. Eg Long BSR has subheader size as 1 and payload size as 3.

lcid_map = [
    ( 0, -1, "00000", "CCCH" ),
    ( 1, -1, "00001", "Logical Channel 1" ),
    ( 2, -1, "00010", "Logical Channel 2" ),
    ( 3, -1, "00011", "Logical Channel 3" ),
    ( 4, -1, "00100", "Logical Channel 4" ),
    ( 5, -1, "00101", "Logical Channel 5" ),
    ( 6, -1, "00110", "Logical Channel 6" ),
    ( 7, -1, "00111", "Logical Channel 7" ),
    ( 8, -1, "01000", "Logical Channel 8" ),
    ( 9, -1, "01001", "Logical Channel 9" ),
    (10, -1, "01010", "Logical Channel 10" ),
    (11, -1, "01011", "CCCH for Category0 UE" ),
    (12, -1, "01100", "CCCH for BL UE with frequency Hopping" ),
    (13,  1, "01101", "Data Volume and Extended Power Headroom Report" ),
    (14,  1, "01110", "GNSS Validity Duration Report" ),
    (15,  2, "01111", "Timing Advance Report" ),
    (16, -1, "10000", "Extended logical channel ID field" ),
    (17,  1, "10001", "DCQR and AS RAI" ),
    (18,  4, "10010", "AUL confirmation (4 octets)" ),
    (19,  1, "10011", "AUL confirmation (1 octet)" ),
    (20,  2, "10100", "Recommended bit rate query" ),
    (21,  0, "10101", "SPS confirmation" ),
    (22, -1, "10110", "Truncated Sidelink BSR" ),
    (23, -1, "10111", "Sidelink BSR" ),
    (24, -1, "11000", "Dual Connectivity Power Headroom Report" ),
    (25, -1, "11001", "Extended Power Headroom Report" ),
    (26,  1, "11010", "Power Headroom Report" ),
    (27,  2, "11011", "C-RNTI" ),
    (28,  1, "11100", "Truncated BSR" ),
    (29,  1, "11101", "Short BSR" ),
    (30,  3, "11110", "Long BSR" ),
    (31,  0, "11111", "Padding" ),
]