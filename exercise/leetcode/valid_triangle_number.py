# -*- coding: utf-8 -*-
"""
611. Valid Triangle Number
@link https://leetcode.com/problems/valid-triangle-number/
"""
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums)-1, 1, -1):
            l = 0
            r = i - 1
            while l < r:
                if nums[r] + nums[r-1] <= nums[i]:
                    break
                if nums[l] + nums[r] > nums[i]:
                    res += (r-l)
                    r -= 1
                else:
                    l += 1

        return res


if __name__ == '__main__':
    print(Solution().triangleNumber(nums=[2, 2, 3, 4]))
