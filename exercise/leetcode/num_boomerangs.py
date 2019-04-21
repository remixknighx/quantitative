# -*- coding: utf-8 -*-
"""
447. Number of Boomerangs
@link https://leetcode.com/problems/number-of-boomerangs/
"""
from typing import List
from collections import Counter


class Solution:
    # 计算两个点之间的距离
    def distance(self, p1, p2):
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        points_len = len(points)
        res = 0
        for i in range(points_len):
            dis_dict = Counter()
            for j in range(points_len):
                if i != j:
                    distance_temp = self.distance(points[i], points[j])
                    dis_dict[distance_temp] = dis_dict[distance_temp] + 1

            for k, v in dis_dict.items():
                if v > 1:
                    res = res + v * (v - 1)

        return res


if __name__ == '__main__':
    points = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]
    solution = Solution()
    print(solution.numberOfBoomerangs(points=points))
