# -*- coding: utf-8 -*-
"""
376. Wiggle Subsequence
@link https://leetcode.com/problems/wiggle-subsequence/
"""
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        diff = []
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                diff.append(1)
            elif nums[i] < nums[i - 1]:
                diff.append(-1)
            else:
                diff.append(0)

        count = n
        prev = 0
        for j in range(n - 1):
            if diff[j] == 0:
                count -= 1
            else:
                if diff[j] == prev:
                    count -= 1
                prev = diff[j]
        return count


if __name__ == '__main__':
    nums = [1, 5, 4]
    print(Solution().wiggleMaxLength(nums=nums))
