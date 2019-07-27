# -*- coding: utf-8 -*-
"""
1046. Last Stone Weight
@link https://leetcode.com/problems/last-stone-weight/
"""
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse=True)
        while len(stones) > 1:
            stone_y = stones.pop(0)
            stone_x = stones.pop(0)
            stones.append((stone_y - stone_x))
            stones.sort(reverse=True)

        if len(stones) == 0:
            return 0
        else:
            return stones[0]


if __name__ == '__main__':
    stones = [2, 7, 4, 1, 8, 1]
    print(Solution().lastStoneWeight(stones=stones))
