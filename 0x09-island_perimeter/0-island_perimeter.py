#!/usr/bin/python3
'''Island parameter'''
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    ''' funaction that calculate the parameter of the island'''
    visit = set()

    def dfs(i, j):
        ''' function that return perimeter'''
        if i >= len(grid) or \
           j >= len(grid[0]) or \
           i < 0 or j < 0 or grid[i][j] == 0:
            return 1
        if (i, j) in visit:
            return 0
        visit.add((i, j))
        per = dfs(i, j + 1)
        per += dfs(i + 1, j)
        per += dfs(i, j - 1)
        per += dfs(i - 1, j)
        return per
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]:
                return dfs(i, j)
