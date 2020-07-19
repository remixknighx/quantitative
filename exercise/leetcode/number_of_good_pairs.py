# -*- coding: utf-8 -*-
"""
1512. Number of Good Pairs
@link https://leetcode.com/problems/number-of-good-pairs/
"""
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1

        return count


if __name__ == '__main__':
    print(Solution().numIdenticalPairs(nums=[1, 2, 3, 1, 1, 3]))
    print(Solution().numIdenticalPairs(nums=[1, 1, 1, 1]))
    print(Solution().numIdenticalPairs(nums=[1, 2, 3]))
