# -*- coding: utf-8 -*-
"""
643. Maximum Average Subarray I
@link https://leetcode.com/problems/maximum-average-subarray-i/
"""
from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum = 0
        for i in range(0, k):
            sum += nums[i]
        res = sum
        for i in range(k, len(nums)):
            sum += nums[i] - nums[i-k]
            res = max(res, sum)
        return res/k


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    print(solution.findMaxAverage(nums=nums, k=k))
