# -*- coding: utf-8 -*-
"""
1051. Height Checker
@link https://leetcode.com/problems/height-checker/
"""
from typing import List


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(h1 != h2 for h1, h2 in zip(heights, sorted(heights)))


if __name__ == '__main__':
    num_list = [1, 1, 4, 2, 1, 3]
    print(Solution().heightChecker(num_list))
