# -*- coding: utf-8 -*-
"""
724. Find Pivot Index
@link https://leetcode.com/problems/find-pivot-index/
"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        for index, num in enumerate(nums):
            right -= num
            if left == right:
                return index
            left += num
        return -1


if __name__ == '__main__':
    nums = [-1, -1, -1, 0, 1, 1]
    print(Solution().pivotIndex(nums=nums))
