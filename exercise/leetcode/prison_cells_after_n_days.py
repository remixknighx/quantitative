# -*- coding: utf-8 -*-
"""
957. Prison Cells After N Days
@link https://leetcode.com/problems/prison-cells-after-n-days/
"""
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        cur, first_day, count = [0] * 8, None, 0
        while N:
            for c in range(1, 7):
                if cells[c - 1] == cells[c + 1]:
                    cur[c] = 1
                else:
                    cur[c] = 0

            if count == 0:  # copy first day
                first_day = cur[:]
            elif cur == first_day:
                N %= count # 等于第一天的时候再重复一遍

            cells = cur[:]
            count += 1
            N -= 1
        return cur


if __name__ == '__main__':
    # print(Solution().prisonAfterNDays(cells=[0, 1, 0, 1, 1, 0, 0, 1], N=7))
    print(Solution().prisonAfterNDays(cells=[1, 0, 0, 1, 0, 0, 1, 0], N=1000000000))

