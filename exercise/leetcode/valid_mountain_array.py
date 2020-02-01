# -*- coding: utf-8 -*-
"""
941. Valid Mountain Array
@link https://leetcode.com/problems/valid-mountain-array/
"""
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if A is None or len(A) < 3:
            return False

        last_num = A[0]
        is_increase = False
        is_decrease = False
        for i in range(1, len(A)):
            if A[i] == last_num:
                return False
            if is_decrease is False:
                if A[i] < last_num:
                    is_decrease = True
                else:
                    is_increase = True
            else:
                if A[i] > last_num:
                    return False
            last_num = A[i]

        return is_increase and is_decrease


if __name__ == '__main__':
    A = [9,8,7,6,5,4,3,2,1,0]
    print(Solution().validMountainArray(A=A))
