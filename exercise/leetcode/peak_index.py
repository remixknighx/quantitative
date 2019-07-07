# -*- coding: utf-8 -*-
"""
852. Peak Index in a Mountain Array
@link https://leetcode.com/problems/peak-index-in-a-mountain-array/
"""
from typing import List


class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        result: int = -1
        for idx in range(0, len(A) - 1):
            if A[idx] > A[idx + 1]:
                result = idx
                break
        return result


if __name__ == '__main__':
    peak_list = [0, 2, 1, 0]
    print(Solution().peakIndexInMountainArray(A=peak_list))