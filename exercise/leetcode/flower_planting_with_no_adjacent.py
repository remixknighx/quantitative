# -*- coding: utf-8 -*-
"""
1042. Flower Planting With No Adjacent
@link https://leetcode.com/problems/flower-planting-with-no-adjacent/
"""
from typing import List


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        """
              :type N: int
              :type paths: List[List[int]]
              :rtype: List[int]
        """
        res = [0] * N
        graph = [[] for i in range(N)]
        for path in paths:
            graph[path[0] - 1].append(path[1] - 1)
            graph[path[1] - 1].append(path[0] - 1)
        for i in range(N):
            neighbor_colors = []
            for neighbor in graph[i]:
                neighbor_colors.append(res[neighbor])
            for color in range(1, 5):
                if color in neighbor_colors:
                    continue
                res[i] = color
                break
        return res


if __name__ == '__main__':
    print(Solution().gardenNoAdj(N=3, paths=[[1, 2], [2, 3], [3, 1]]))
    print(Solution().gardenNoAdj(N=4, paths=[[1, 2], [3, 4]]))
