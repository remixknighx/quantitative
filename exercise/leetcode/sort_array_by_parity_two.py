# -*- coding: utf-8 -*-
"""
922. Sort Array By Parity II
@link https://leetcode.com/problems/sort-array-by-parity-ii/
"""
from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        result = []
        even_index = 0
        odd_index = 1
        for num in A:
            if num % 2 == 0:
                result.insert(even_index, num)
                even_index += 2
            else:
                result.insert(odd_index, num)
                odd_index += 2
        return result


if __name__ == '__main__':
    print(Solution().sortArrayByParityII(A=[4, 2, 5, 7]))
