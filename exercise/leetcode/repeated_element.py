# -*- coding: utf-8 -*-
"""
961. N-Repeated Element in Size 2N Array
@link https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
"""
from typing import List


class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        N_size = A.__len__()/2
        list_dict = dict()
        for num in A:
            if num not in list_dict.keys():
                list_dict[num] = 1
            else:
                list_dict[num] += 1

        for k in list_dict.keys():
            if list_dict[k] == N_size:
                return k

        return 0


if __name__ == '__main__':
    A = [2,1,2,5,3,2]
    print(Solution().repeatedNTimes(A=A))
