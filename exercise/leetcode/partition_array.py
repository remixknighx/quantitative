# -*- coding: utf-8 -*-
"""
1013. Partition Array Into Three Parts With Equal Sum
@link https://leetcode.com/problems/partition-array-into-three-parts-with-equal-sum/
"""
from typing import List


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        s = sum(A)
        if s % 3 != 0:
            return False
        s /= 3
        targets = [2 * s, s]
        acc = 0
        for a in A:
            acc += a
            if acc == targets[-1]:
                targets.pop()
            if not targets:
                return True
        return False


if __name__ == '__main__':
    partition_array: List[int] = [3,3,6,5,-2,2,5,1,-9,4]
    print(Solution().canThreePartsEqualSum(partition_array))
