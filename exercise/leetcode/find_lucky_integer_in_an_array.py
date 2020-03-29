# -*- coding: utf-8 -*-
"""
1394. Find Lucky Integer in an Array
@link https://leetcode.com/problems/find-lucky-integer-in-an-array/
"""
from typing import List
from collections import Counter


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_cnt = Counter(arr)
        result = -1
        for k,v in arr_cnt.items():
            if k == v and k > result:
                result = k
        return result


if __name__ == '__main__':
    print(Solution().findLucky(arr=[7, 7, 7, 7, 7, 7, 7]))
