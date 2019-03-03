# -*- coding: utf-8 -*-
"""
645. Set Mismatch
@link https://leetcode.com/problems/set-mismatch/
"""
from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # 先将数组进行排序
        nums.sort()
        dup = -1
        missing = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                dup = nums[i]
            elif nums[i] > nums[i-1] + 1:
                missing = nums[i-1] + 1
        if nums[len(nums) - 1] != len(nums):
            missing = len(nums)
        return list([dup, missing])


if __name__ == '__main__':
    solution = Solution()
    nums_list = [1, 2, 4, 4]
    print(solution.findErrorNums(nums=nums_list))

