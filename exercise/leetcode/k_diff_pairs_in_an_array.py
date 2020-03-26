# -*- coding: utf-8 -*-
"""
532. K-diff Pairs in an Array
@link https://leetcode.com/problems/k-diff-pairs-in-an-array/
"""
from typing import List
from collections import Counter


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        r = 0
        if k >= 0:
            c = Counter(nums)
            for i in c:
                if (k == 0 and c[i] > 1) or (k != 0 and i + k in c):
                    r += 1
        return r


if __name__ == '__main__':
    nums = [1,1,1,1,1]
    k = 0
    print(Solution().findPairs(nums=nums, k=k))
