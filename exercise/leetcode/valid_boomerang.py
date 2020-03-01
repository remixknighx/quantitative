# -*- coding: utf-8 -*-
"""
1037. Valid Boomerang
@link https://leetcode.com/problems/valid-boomerang/
"""
from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        p0, p1, p2 = points
        return (p2[1] - p1[1]) * (p1[0] - p0[0]) != (p1[1] - p0[1]) * (p2[0] - p1[0])

