# -*- coding: utf-8 -*-
"""
1480. Running Sum of 1d Array
@link https://leetcode.com/problems/running-sum-of-1d-array/
"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        last_sum = 0
        for num in nums:
            last_sum += num
            result.append(last_sum)

        return result


if __name__ == '__main__':
    print(Solution().runningSum(nums=[1, 2, 3, 4]))
