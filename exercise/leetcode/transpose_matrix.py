# -*- coding: utf-8 -*-
"""
867. Transpose Matrix
@link https://leetcode.com/problems/transpose-matrix/
"""
from typing import List


class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        result = [[] for i in range(A[0].__len__())]
        A_width = A[0].__len__()
        A_height = A.__len__()
        for x in range(0, A_width):
            for y in range(0, A_height):
                result[x].append(A[y][x])
        return result


if __name__ == '__main__':
    A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    # result = [[] for i in range(3)]
    print(Solution().transpose(A=A))
