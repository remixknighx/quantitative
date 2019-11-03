# -*- coding: utf-8 -*-
"""
832. Flipping an Image
@link https://leetcode.com/problems/flipping-an-image/
"""
from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        result = []
        for single_list in A:
            single_list.reverse()
            single_result = []
            for single_word in single_list:
                single_result.append(0 if single_word == 1 else 1)
            result.append(single_result)
        return result


if __name__ == '__main__':
    print(Solution().flipAndInvertImage(A=[[1, 1, 0], [1, 0, 1], [0, 0, 0]]))
    print(Solution().flipAndInvertImage(A=[[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]]))
