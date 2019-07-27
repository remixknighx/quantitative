# -*- coding: utf-8 -*-
"""
812. Largest Triangle Area
@link https://leetcode.com/problems/largest-triangle-area/
"""
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res: float = 0
        for i in points:
            for j in points:
                for k in points:
                    res = max(res, 0.5 * abs(i[0] * j[1] + j[0] * k[1] + k[0] * i[1] - j[0] * i[1] - k[0] * j[1] - i[0] * k[1]))
        return res


if __name__ == '__main__':
    points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    print(Solution().largestTriangleArea(points=points))

