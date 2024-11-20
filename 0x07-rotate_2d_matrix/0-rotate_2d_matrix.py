#!/usr/bin/python3
'''0x07-rotate_2d_matrix'''


def rotate_2d_matrix(matrix):
    '''n x n 2D matrix, rotate it 90 degrees clockwise'''
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range(r - l):
            top, bottom = l, r
            topleft = matrix[top][l + i]
            matrix[top][l + i] = matrix[bottom - i][l]
            matrix[bottom - i][l] = matrix[bottom][r - i]
            matrix[bottom][r - i] = matrix[top + i][r]
            matrix[top + i][r] = topleft
        r -= 1
        l += 1