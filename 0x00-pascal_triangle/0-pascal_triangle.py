#!/usr/bin/python3
"""method that calculate pascal trigles"""
def pascal_triangle(n):
    '''
    function the calculate pascal tringles
    '''
    a = [[] for i in range(n)]
    if (n <= 0):
        return ""
    for i in range(n):
        for r in range(i + 1):
            if(r < i):
                if(r == 0):
                    a[i].append(1)
                else:
                    a[i].append(a[i - 1][r] + a[i -1][r - 1])
            elif(r == i):
                a[i].append(1)
    return a
