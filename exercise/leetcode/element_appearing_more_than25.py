# -*- coding: utf-8 -*-
"""
1287. Element Appearing More Than 25% In Sorted Array
@link https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/
"""
from typing import List
from collections import *


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        num_count = Counter(arr)
        return num_count.most_common(1)[0][0]


if __name__ == '__main__':
    print(Solution().findSpecialInteger(arr=[1, 2, 2, 6, 6, 6, 6, 7, 10]))
