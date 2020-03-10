# -*- coding: utf-8 -*-
"""
1337. The K Weakest Rows in a Matrix
@link https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/
"""
from typing import List
from collections import *


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        line_dict = defaultdict(list)
        for index, value in enumerate(mat):
            line_count = Counter(value)
            if line_count.get(1) is None:
                line_dict[index] = 0
            else:
                line_dict[index] = line_count.get(1)

        result = [k for k, v in sorted(line_dict.items(), key=lambda item: item[1])]

        return result[:k]


if __name__ == '__main__':
    mat = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 0], [0, 0, 0, 0]]
    k = 3
    print(Solution().kWeakestRows(mat=mat, k=k))

    # test_dict = defaultdict(list)
    # test_dict[1].append(12)
    # print(test_dict)
