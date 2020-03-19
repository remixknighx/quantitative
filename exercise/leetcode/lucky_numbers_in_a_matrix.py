# -*- coding: utf-8 -*-
"""
1380. Lucky Numbers in a Matrix
@link https://leetcode.com/problems/lucky-numbers-in-a-matrix/
"""
from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        mins = [min(subitem) for subitem in matrix]
        maxs = [max(subitem) for subitem in zip(*matrix)]

        return [ii for ii in mins for jj in maxs if ii == jj]


if __name__ == '__main__':
    matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]
    print(Solution().luckyNumbers(matrix=matrix))
