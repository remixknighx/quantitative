# -*- coding: utf-8 -*-
"""
989. Add to Array-Form of Integer
@link https://leetcode.com/problems/add-to-array-form-of-integer/
"""
from typing import List


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        A_str = ''
        for single_num in A:
            A_str += str(single_num)
        result = int(A_str) + K
        return list(map(int, str(result)))


if __name__ == '__main__':
    A = [9,9,9,9,9,9,9,9,9,9]
    K = 1
    print(Solution().addToArrayForm(A=A, K=K))
