# -*- coding: utf-8 -*-
"""
1200. Minimum Absolute Difference
@link https://leetcode.com/problems/minimum-absolute-difference/
"""
from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        min_difference = arr[1] - arr[0]
        result = [[arr[0], arr[1]]]
        for i in range(1, len(arr) - 1):
            if min_difference > arr[i+1] - arr[i]:
                min_difference = arr[i+1] - arr[i]
                result = [[arr[i], arr[i+1]]]
            elif min_difference == arr[i + 1] - arr[i]:
                result.append([arr[i], arr[i + 1]])

        return result


if __name__ == '__main__':
    print(Solution().minimumAbsDifference(arr=[40, 11, 26, 27, -20]))
    # print(Solution().minimumAbsDifference(arr=[4, 2, 1, 3]))
    # print(Solution().minimumAbsDifference(arr=[3, 8, -10, 23, 19, -4, -14, 27]))
