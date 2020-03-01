# -*- coding: utf-8 -*-
"""
1207. Unique Number of Occurrences
@link https://leetcode.com/problems/unique-number-of-occurrences/
"""
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr_dict = {}
        for num in arr:
            if arr_dict.get(num) is None:
                arr_dict.setdefault(num, 1)
            else:
                arr_dict[num] += 1

        return len(arr_dict) == len(set(arr_dict.values()))


if __name__ == '__main__':
    arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    print(Solution().uniqueOccurrences(arr=arr))

