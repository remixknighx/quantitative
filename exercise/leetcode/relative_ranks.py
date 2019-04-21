# -*- coding: utf-8 -*-
"""
506 Relative Ranks
@link https://leetcode.com/problems/relative-ranks/
"""

from typing import List
from collections import *


class Solution:
    def findRelativeRanks(self, num: List[int]) -> List[str]:
        origin_num = num.copy()
        num.sort(reverse=True)
        rank_map = dict()
        count = 0
        for i in range(len(num)):
            count += 1
            if i == 0:
                rank_map[num[i]] = 'Gold Medal'
            elif i == 1:
                rank_map[num[i]] = 'Silver Medal'
            elif i == 2:
                rank_map[num[i]] = 'Bronze Medal'
            else:
                rank_map[num[i]] = str(count)

        result = list()
        for i in range(len(origin_num)):
            result.append(rank_map[origin_num[i]])
        return result


if __name__ == '__main__':
    num = [5, 4, 3, 2, 1]
    solution = Solution()
    print(solution.findRelativeRanks(num))
