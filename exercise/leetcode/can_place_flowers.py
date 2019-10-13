# -*- coding: utf-8 -*-
"""
605. Can Place Flowers
@link https://leetcode.com/problems/can-place-flowers/
"""
from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        ans = 0
        num = 1
        for x in flowerbed:
            if x == 0:
                num += 1
            else:
                if num > 0:
                    ans += (num - 1) // 2
                num = 0
        if num != 0:
            ans += num // 2
        return ans >= n


if __name__ == '__main__':
    flowerbed = [0, 0, 1, 0, 1]
    print(Solution().canPlaceFlowers(flowerbed=flowerbed, n=1))