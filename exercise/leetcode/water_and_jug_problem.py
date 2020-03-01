# -*- coding: utf-8 -*-
"""
365. Water and Jug Problem
@link https://leetcode.com/problems/water-and-jug-problem/
"""
import math


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if x == 0 and y == 0 and z == 0:
            return True
        return x + y >= z and z % math.gcd(x, y) == 0


if __name__ == '__main__':
    x = 3
    y = 5
    z = 4
    print(Solution().canMeasureWater(x=x, y=y, z=z))
