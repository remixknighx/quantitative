# -*- coding: utf-8 -*-
"""
628. Maximum Product of Three Numbers
@link https://leetcode.com/problems/maximum-product-of-three-numbers/
"""
from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max([nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1]])


if __name__ == '__main__':
    print(Solution().maximumProduct(nums=[1, 2, 3]))
    print(Solution().maximumProduct(nums=[1, 2, 3, 4]))
    print(Solution().maximumProduct(nums=[-4, 3, 2, 1, 60]))
