# -*- coding: utf-8 -*-
"""
1356. Sort Integers by The Number of 1 Bits
@link https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
"""
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(sorted(arr), key=lambda x: bin(x).count("1"))


if __name__ == '__main__':
    print(Solution().sortByBits(arr=[0, 1, 2, 3, 4, 5, 6, 7, 8]))
