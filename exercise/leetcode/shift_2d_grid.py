# -*- coding: utf-8 -*-
"""
1260. Shift 2D Grid
@link https://leetcode.com/problems/shift-2d-grid/
"""
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        move = m * n - k
        return [[grid[(i + (j + move) // n) % m][(j + move) % n] for j in range(n)] for i in range(m)]


if __name__ == '__main__':
    print(Solution().shiftGrid(grid=[[1, 2, 3], [4, 5, 6], [7, 8, 9]], k=1))
