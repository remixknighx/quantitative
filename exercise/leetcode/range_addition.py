# -*- coding: utf-8 -*-
"""
598. Range Addition II
@link https://leetcode.com/problems/range-addition-ii/
"""

from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:
            return m * n
        return min(op[0] for op in ops) * min(op[1] for op in ops)


if __name__ == '__main__':
    print(Solution().maxCount(m=3, n=3, ops=[[2, 2], [3, 3]]))
