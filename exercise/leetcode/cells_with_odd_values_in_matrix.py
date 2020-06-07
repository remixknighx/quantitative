# -*- coding: utf-8 -*-
"""
1252. Cells with Odd Values in a Matrix
@link https://leetcode.com/problems/cells-with-odd-values-in-a-matrix/
"""
from typing import List


class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        # initialize the matrix using list comprehension
        # n rows, m columns
        mat = [[0 for i in range(m)] for j in range(n)]

        while indices:
            temp_index = indices.pop()
            # add 1 to the row temp_index[0]
            for i in range(m):
                mat[temp_index[0]][i] += 1
            # add 1 to the column temp_index[1]
            for i in range(n):
                mat[i][temp_index[1]] += 1

        # count the number of odd numbers
        odd_count = 0
        for i in range(n):
            for j in range(m):
                if mat[i][j] % 2 == 1:
                    odd_count += 1

        return odd_count


if __name__ == '__main__':
    print(Solution().oddCells(n=2, m=3, indices=[[0, 1], [1, 1]]))
