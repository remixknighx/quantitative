# -*- coding: utf-8 -*-
"""
1403. Minimum Subsequence in Non-Increasing Order
@link https://leetcode.com/problems/minimum-subsequence-in-non-increasing-order/
"""
from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]

        total = sum(nums)
        nums.sort(reverse=True)
        min_sum = nums[0]
        result = [nums[0]]
        for i in range(1, len(nums)):
            if min_sum > total - min_sum:
                break
            min_sum += nums[i]
            result.append(nums[i])

        return result


if __name__ == '__main__':
    print(Solution().minSubsequence(nums=[4, 3, 10, 9, 8]))
    print(Solution().minSubsequence(nums=[4, 4, 7, 6, 7]))
    print(Solution().minSubsequence(nums=[10, 2, 5]))
