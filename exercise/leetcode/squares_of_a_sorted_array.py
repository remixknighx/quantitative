# -*- coding: utf-8 -*-
"""
977. Squares of a Sorted Array
@link https://leetcode.com/problems/squares-of-a-sorted-array/
"""
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        result = list()
        for num in A:
            result.append(num * num)
        result.sort()
        return result


if __name__ == '__main__':
    A = [-7,-3,2,3,11]
    print(Solution().sortedSquares(A=A))
