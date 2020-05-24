# -*- coding: utf-8 -*-
"""
1389. Create Target Array in the Given Order
@link https://leetcode.com/problems/create-target-array-in-the-given-order/
"""
from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = list()
        for i in range(0, len(nums)):
            target.insert(index[i], nums[i])
        return target


if __name__ == '__main__':
    nums = [1]
    index = [0]
    print(Solution().createTargetArray(nums=nums, index=index))
