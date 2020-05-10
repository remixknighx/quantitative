# -*- coding: utf-8 -*-
"""
1295. Find Numbers with Even Number of Digits
@link https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
"""
from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count


if __name__ == '__main__':
    nums = [555, 901, 482, 1771]
    print(Solution().findNumbers(nums=nums))
