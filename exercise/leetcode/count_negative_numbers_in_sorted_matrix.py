# -*- coding: utf-8 -*-
"""
1351. Count Negative Numbers in a Sorted Matrix
@link https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
"""
from typing import List


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count: int = 0
        for i in range(0, len(grid)):
            row = grid[i]
            for j in range(0, len(row)):
                if row[j] < 0:
                    count += 1
        return count


if __name__ == '__main__':
    print(Solution().countNegatives(grid=[[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]))
    print(Solution().countNegatives(grid=[[3, 2], [1, 0]]))
    print(Solution().countNegatives(grid=[[1, -1], [-1, -1]]))
    print(Solution().countNegatives(grid=[[-1]]))
