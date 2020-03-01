# -*- coding: utf-8 -*-
"""
324. Wiggle Sort II
@link https://leetcode.com/problems/wiggle-sort-ii/
"""
from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        if not nums:
            return
        nums.sort()

        L = len(nums)
        boundary = L // 2 if L % 2 == 0 else L // 2 + 1
        small_nums = nums[:boundary]
        large_nums = nums[boundary:]
        small_nums, large_nums = small_nums[::-1], large_nums[::-1]

        j, k = 0, 0
        for i in range(L):
            if i % 2 == 0:
                nums[i] = small_nums[j]
                j += 1
            else:
                nums[i] = large_nums[k]
                k += 1


if __name__ == '__main__':
    nums = [1, 5, 1, 1, 6, 4]
    print(Solution().wiggleSort(nums=nums))


