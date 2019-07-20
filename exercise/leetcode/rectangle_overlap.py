# -*- coding: utf-8 -*-
"""
836. Rectangle Overlap
@link https://leetcode.com/problems/rectangle-overlap/
"""
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        rec1_top_left = [rec1[0], rec1[3]]
        rec1_top_right = [rec1[2], rec1[3]]
        rec1_bottom_left = [rec1[0], rec1[1]]
        rec1_bottom_right = [rec1[2], rec1[1]]

        rec2_top_left = [rec2[0], rec2[3]]
        rec2_top_right = [rec2[2], rec2[3]]
        rec2_bottom_left = [rec2[0], rec2[1]]
        rec2_bottom_right = [rec2[2], rec2[1]]

        if (((rec1_top_right[0] > rec2_bottom_left[0] and rec1_top_right[1] > rec2_bottom_left[1])
            and (rec1_bottom_left[0] < rec2_top_right[0] and rec1_bottom_left[1] < rec2_top_right[1]))
            or ((rec1_bottom_right[0] > rec2_top_left[0] and rec1_bottom_right[1] > rec2_top_left[1])
            and (rec1_top_left[0] < rec2_bottom_right[0] and rec1_top_left[1] < rec2_bottom_right[1]))):
            return True
        else:
            return False


if __name__ == '__main__':
    rec1 = [0, 0, 1, 1]
    rec2 = [1, 0, 2, 1]
    print(Solution().isRectangleOverlap(rec1=rec1, rec2=rec2))
