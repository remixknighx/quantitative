# -*- coding: utf-8 -*-
"""
840. Magic Squares In Grid
@link https://leetcode.com/problems/magic-squares-in-grid/
"""
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        if not grid: return 0
        cnt = 0
        m, n = len(grid), len(grid[0])
        for i in range(m - 2):
            for j in range(n - 2):
                if self.magic_grid(grid, i, j): cnt += 1
        return cnt

    def magic_grid(self, grid, i, j):
        target = 15
        _sum3 = _sum4 = 0
        _set = set()
        for k in range(3):
            _sum1 = 0
            _sum2 = 0
            _sum3 += grid[i + k][j + k]
            _sum4 += grid[i + 2 - k][j + k]
            for l in range(3):
                _set.add(grid[i + k][j + l])
                _sum1 += grid[i + k][j + l]
                _sum2 += grid[i + l][j + k]
            if _sum1 != target or _sum2 != target: return False
        if _sum3 != target or _sum4 != target: return False
        return _set == set(range(1, 10))


if __name__ == '__main__':
    grid = [[4, 3, 8, 4],
            [9, 5, 1, 9],
            [2, 7, 6, 2]]
    print(Solution().numMagicSquaresInside(grid=grid))
