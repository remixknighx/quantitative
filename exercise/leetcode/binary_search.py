# -*- coding: utf-8 -*-
"""
704. Binary Search
@link https://leetcode.com/problems/binary-search/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums_length = len(nums)
        start = 0
        end = nums_length - 1
        mid = int(nums_length / 2)
        while start <= end:
            if target == nums[int(mid)]:
                return mid
            elif target < nums[int(mid)]:
                end = mid - 1
            elif target > nums[int(mid)]:
                start = mid + 1
            mid = int((start + end) / 2)
        return -1


if __name__ == '__main__':
    # nums = [-1, 0, 3, 5, 9, 12]
    # target = 9
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(Solution().search(nums=nums, target=target))
