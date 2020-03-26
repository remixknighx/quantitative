# -*- coding: utf-8 -*-
"""
888. Fair Candy Swap
@link https://leetcode.com/problems/fair-candy-swap/
"""
from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        diff = int((sum(A) - sum(B)) / 2)
        A_dict = {}
        for num_A in A:
            A_dict.setdefault(num_A-diff, num_A)

        for num_B in B:
            if A_dict.get(num_B) is not None:
                return [A_dict.get(num_B), num_B]

        return []


if __name__ == '__main__':
    print(Solution().fairCandySwap(A=[1, 2, 5], B=[2, 4]))
