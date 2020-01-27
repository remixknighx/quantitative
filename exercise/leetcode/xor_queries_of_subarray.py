# -*- coding: utf-8 -*-
"""
1310. XOR Queries of a Subarray
@link https://leetcode.com/problems/xor-queries-of-a-subarray/
"""
from typing import List


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        it = enumerate(arr)
        i, cumV = next(it)
        for i, v in it:
            cumV ^= v
            arr[i] = cumV
        result = []
        arr.append(0)
        for l, r in queries:
            result.append(arr[r] ^ arr[l - 1])
        return result


if __name__ == '__main__':
    arr = [4,8,2,10]
    queries = [[2,3],[1,3],[0,0],[0,3]]
    print(Solution().xorQueries(arr=arr, queries=queries))
