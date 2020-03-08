# -*- coding: utf-8 -*-
"""
1089. Duplicate Zeros
@link https://leetcode.com/problems/duplicate-zeros/
"""
from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        count = 0
        arr_data = arr[0]
        while True:
            if arr_data != 0:
                count += 1
            else:
                arr_data = arr[count+1]
                arr[count+1] = 0
                count += 2
                for i in range(count, len(arr)):
                    temp = arr[i]
                    arr[i] = arr_data
                    arr_data = temp
            if count+1 >= len(arr):
                break
            arr_data = arr[count]

        print(arr)


if __name__ == '__main__':
    print(Solution().duplicateZeros(arr=[1,0,2,3,0,4,5,0]))
