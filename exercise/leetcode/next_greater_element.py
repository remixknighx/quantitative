# -*- coding: utf-8 -*-
"""
496. Next Greater Element I
#link https://leetcode.com/problems/next-greater-element-i/
"""
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result: List[int] = []
        for i in range(0, len(nums1)):
            if nums1[i] not in nums2:
                result.append(-1)
            else:
                start = nums2.index(nums1[i], 0, len(nums2))
                if start + 1 == len(nums2):
                    result.append(-1)
                    continue
                for j in range(start+1, len(nums2)):
                    if nums2[j] > nums1[i]:
                        result.append(nums2[j])
                        break
                    if j == len(nums2) - 1:
                        result.append(-1)
        return result


if __name__ == '__main__':
    nums1 = [1, 3, 5, 2, 4]
    nums2 = [5, 4, 3, 2, 1]
    print(Solution().nextGreaterElement(nums1=nums1, nums2=nums2))
