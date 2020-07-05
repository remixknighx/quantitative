# -*- coding: utf-8 -*-
"""
1502. Can Make Arithmetic Progression From Sequence
@link https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/
"""
from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        if len(arr) < 2:
            return True
        step = arr[1] - arr[0]
        for i in range(1, len(arr)-1):
            if (arr[i+1] - arr[i]) != step:
                return False
        return True


if __name__ == '__main__':
    print(Solution().canMakeArithmeticProgression(arr=[3, 5, 1]))
    print(Solution().canMakeArithmeticProgression(arr=[1, 2, 4]))
