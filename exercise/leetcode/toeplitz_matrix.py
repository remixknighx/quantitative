# -*- coding: utf-8 -*-
"""
766. Toeplitz Matrix
@link https://leetcode.com/problems/toeplitz-matrix/
"""
from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        width = matrix[0].__len__()
        height = matrix.__len__()

        for x in range(height):
            for y in range(width):
                temp_x = x + 1
                temp_y = y + 1
                while temp_y < width and temp_x < height:
                    if matrix[temp_x][temp_y] != matrix[x][y]:
                        return False
                    else:
                        temp_x += 1
                        temp_y += 1

        return True


if __name__ == '__main__':
    matrix = [[11, 74, 0, 93], [40, 11, 74, 7]]
    print(Solution().isToeplitzMatrix(matrix=matrix))
