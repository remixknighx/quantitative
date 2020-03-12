# -*- coding: utf-8 -*-
"""
1030. Matrix Cells in Distance Order
@link https://leetcode.com/problems/matrix-cells-in-distance-order/
"""
from typing import List
import math


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        result_dict = dict()
        for row in range(0, R):
            for col in range(0, C):
                distance = math.fabs(row - r0) + math.fabs(col - c0)
                result_dict[str(row) + "," + str(col)] = distance

        result = list()
        for k, v in sorted(result_dict.items(), key=lambda item: item[1]):
            result.append([int(str(k).split(',')[0]), int(str(k).split(',')[1])])
        return result


if __name__ == '__main__':
    R = 2
    C = 3
    r0 = 1
    c0 = 2
    print(Solution().allCellsDistOrder(R=R, C=C, r0=r0, c0=c0))
