# -*- coding: utf-8 -*-
"""
976. Largest Perimeter Triangle
@link https://leetcode.com/problems/largest-perimeter-triangle/
"""
from typing import List


class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A)[::-1]
        for i in range(len(A) - 2):
            if A[i] < A[i + 1] + A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0


if __name__ == '__main__':
    A = [1,2,1]
    print(Solution().largestPerimeter(A=A))

