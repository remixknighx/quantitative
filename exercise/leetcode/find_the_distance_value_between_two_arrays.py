# -*- coding: utf-8 -*-
"""
1385. Find the Distance Value Between Two Arrays
@link https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
"""
from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        result = 0
        for num1 in arr1:
            flag = True
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    flag = False
                    break

            if flag:
                result += 1
        return result


if __name__ == '__main__':
    print(Solution().findTheDistanceValue(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2))
