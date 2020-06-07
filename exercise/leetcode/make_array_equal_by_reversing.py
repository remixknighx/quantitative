# -*- coding: utf-8 -*-
"""
1460. Make Two Arrays Equal by Reversing Sub-arrays
@link https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
"""
from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        if len(target) != len(arr):
            return False
        target.sort()
        arr.sort()
        for t, a in zip(target, arr):
            if t != a:
                return False
        return True


if __name__ == '__main__':
    print(Solution().canBeEqual(target=[1, 2, 3, 4], arr=[2, 4, 1, 3]))
