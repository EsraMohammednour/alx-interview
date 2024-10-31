#!/usr/bin/python3
'''0-validate_utf8.py'''


def validUTF8(data):
    '''Checks if a list of integers are valid UTF-8 codepoints.'''
    num_bytes_following = 0

    for num in data:
        if num_bytes_following:
            if num >> 6 != 0b10:
                return False
            num_bytes_following -= 1
        else:
            if num >> 7 == 0b0:
                num_bytes_following = 0
            elif num >> 5 == 0b110:
                num_bytes_following = 1
            elif num >> 4 == 0b1110:
                num_bytes_following = 2
            elif num >> 3 == 0b11110:
                num_bytes_following = 3
            else:
                return False

    return True
