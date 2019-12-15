# -*- coding: utf-8 -*-
"""
896. Monotonic Array
@link https://leetcode.com/problems/monotonic-array/
"""
from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        lis = [True, True]
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                lis[0] = False
            elif A[i] < A[i-1]:
                lis[1] = False
            if not(lis[0] or lis[1]):
                return False
        return True


if __name__ == '__main__':
    A = [11, 11, 9, 4, 3, 3, 3, 1, -1, -1, 3, 3, 3, 5, 5, 5]
    print(Solution().isMonotonic(A=A))
