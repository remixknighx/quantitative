# -*- coding: utf-8 -*-
"""
1317. Convert Integer to the Sum of Two No-Zero Integers
@link https://leetcode.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers/
"""
from typing import List


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if str(i).find('0') == -1 and str(n - i).find('0') == -1:
                return [i, n-i]


if __name__ == '__main__':
    print(Solution().getNoZeroIntegers(n=4102))
