#!/usr/bin/python3
'''0-validate_utf8.py'''


def validUTF8(data):
    '''Checks if a list of integers are valid UTF-8 codepoints.'''
    num_bytes_following = 0

    for num in data:
        byte = num & 0xFF
        if num_bytes_following:
            if byte >> 6 != 0b10:
                return False
            num_bytes_following -= 1
        else:
            if byte >> 7 == 0:
                num_bytes_following = 0
            elif byte >> 5 == 0b110:
                num_bytes_following = 1
            elif byte >> 4 == 0b1110:
                num_bytes_following = 2
            elif byte >> 3 == 0b11110:
                num_bytes_following = 3
            else:
                return False

    return num_bytes_following == 0
