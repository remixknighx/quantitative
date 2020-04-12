# -*- coding: utf-8 -*-
"""
1346. Check If N and Its Double Exist
@link https://leetcode.com/problems/check-if-n-and-its-double-exist/
"""
from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) > 1:
            return True
        for m in arr:
            n = 2 * m
            if n != m and n in arr:
                return True
        return False


if __name__ == '__main__':
    # print(Solution().checkIfExist(arr=[10, 2, 5, 3]))
    # print(Solution().checkIfExist(arr=[7, 1, 14, 11]))
    print(Solution().checkIfExist(arr=[-2, 0, 10, -19, 4, 6, -8]))
    print(Solution().checkIfExist(arr=[0, 0]))
