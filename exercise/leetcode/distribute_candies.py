# -*- coding: utf-8 -*-
"""
575. Distribute Candies
@link https://leetcode.com/problems/distribute-candies/
"""
from typing import List


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        return min(len(set(candies)), len(candies) // 2)


if __name__ == '__main__':
    candies = [1, 1, 2, 3]
    print(Solution().distributeCandies(candies=candies))
