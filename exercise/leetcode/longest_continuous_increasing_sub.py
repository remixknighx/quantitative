# -*- coding: utf-8 -*-
"""
674. Longest Continuous Increasing Subsequence
@link https://leetcode.com/problems/longest-continuous-increasing-subsequence/
"""
from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        max_length: int = 0
        for i in range(0, len(nums)):
            count: int = 1
            for j in range(i+1, len(nums)):
                if nums[j] > nums[j-1]:
                    count += 1
                else:
                    break
            if count > max_length:
                max_length = count
        return max_length


if __name__ == '__main__':
    nums = [2,2,2,2,2]
    print(Solution().findLengthOfLCIS(nums=nums))

