# -*- coding: utf-8 -*-
"""
593. Valid Square
@link https://leetcode.com/problems/valid-square/
"""
from typing import List
import math


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if self.isValidTri(p1=p1, p2=p2, p3=p3) and self.isValidTri(p1=p4, p2=p2, p3=p3) and self.isValidTri(p1=p1, p2=p4, p3=p3):
            return True
        else:
            return False

    def isValidTri(self, p1: List[int], p2: List[int], p3: List[int]):
        p1p2 = math.pow(p2[1] - p1[1], 2) + math.pow(p2[0] - p1[0], 2)
        p2p3 = math.pow(p2[1] - p3[1], 2) + math.pow(p2[0] - p3[0], 2)
        p1p3 = math.pow(p1[1] - p3[1], 2) + math.pow(p1[0] - p3[0], 2)
        maxDis = max(p1p2, p1p3, p2p3)
        a = 0
        b = 0
        if p1p2 == maxDis:
            a = p2p3
            b = p1p3
        if p2p3 == maxDis:
            a = p1p2
            b = p1p3
        if p1p3 == maxDis:
            a = p1p2
            b = p2p3

        if a == 0 or b == 0 or maxDis == 0:
            return False

        return a + b == maxDis and a == b


if __name__ == '__main__':
    print(Solution().validSquare(p1=[2, 2], p2=[2, 1], p3=[1, 2], p4=[1, 0]))
