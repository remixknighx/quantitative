# -*- coding: utf-8 -*-
"""
1232. Check If It Is a Straight Line
@link https://leetcode.com/problems/check-if-it-is-a-straight-line/
"""
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True
        index = 0
        try:
            index = float((coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0]))
        except ZeroDivisionError:
            index = float('inf')

        for coordinate in coordinates[2:]:
            index_single = 0
            try:
                index_single = float((coordinate[1] - coordinates[0][1]) / (coordinate[0] - coordinates[0][0]))
            except ZeroDivisionError:
                index = float('inf')

            if index_single != index:
                return False
        return True


if __name__ == '__main__':
    print(Solution().checkStraightLine(coordinates=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
    print(Solution().checkStraightLine(coordinates=[[-7, 1], [-7, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
