# -*- coding: utf-8 -*-
"""
238. Product of Array Except Self
@link https://leetcode.com/problems/product-of-array-except-self/
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        temp = 1
        for num in nums:
            result.append(temp)
            temp *= num

        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= temp
            temp *= nums[i]
        return result


if __name__ == '__main__':
    print(Solution().productExceptSelf(nums=[0, 0]))
