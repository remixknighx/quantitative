# -*- coding: utf-8 -*-
"""
594. Longest Harmonious Subsequence
@link https://leetcode.com/problems/longest-harmonious-subsequence/
"""
from typing import List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        keys = sorted(list(dic.keys()))
        total = 0
        for i in range(len(keys) - 1):
            if keys[i] + 1 == keys[i + 1]:
                sum2 = dic[keys[i]] + dic[keys[i + 1]]
                if sum2 > total:
                    total = sum2
        return total


if __name__ == '__main__':
    nums = [1,3,2,2,5,2,3,7]
    print(Solution().findLHS(nums=nums))
