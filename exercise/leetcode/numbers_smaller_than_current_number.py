# -*- coding: utf-8 -*-
"""
1365. How Many Numbers Are Smaller Than the Current Number
@link https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
"""
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums_copy = nums.copy()
        nums_copy.sort()
        nums_sort_dict = {}
        count = 0
        for i in range(0, len(nums_copy)):
            if nums_sort_dict.get(nums_copy[i]) is None:
                nums_sort_dict[nums_copy[i]] = count
            count += 1

        result = []
        for num in nums:
            result.append(nums_sort_dict.get(num))

        return result


if __name__ == '__main__':
    print(Solution().smallerNumbersThanCurrent(nums=[8, 1, 2, 2, 3]))
    print(Solution().smallerNumbersThanCurrent(nums=[6, 5, 4, 8]))
    print(Solution().smallerNumbersThanCurrent(nums=[7, 7, 7, 7]))
