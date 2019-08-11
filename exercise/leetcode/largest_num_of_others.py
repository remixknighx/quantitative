# -*- coding: utf-8 -*-
"""
747. Largest Number At Least Twice of Others
@link https://leetcode.com/problems/largest-number-at-least-twice-of-others/
"""
from typing import List


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        ans: int = -1
        for i in range(0, len(nums)):
            flag: bool = True
            for j in range(0, len(nums)):
                if i == j:
                    continue
                if nums[i] < 2 * nums[j]:
                    flag = False
                    break
            if flag:
                if nums[i] >= ans:
                    ans = i

        return ans


if __name__ == '__main__':
    nums = [1,2,3,4,5]
    print(Solution().dominantIndex(nums=nums))