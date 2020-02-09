# -*- coding: utf-8 -*-
"""
1029. Two City Scheduling
@link https://leetcode.com/problems/two-city-scheduling/
"""
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # customized sorting with key = change_cost, on ascending order
        costs.sort(key=lambda x: x[0] - x[1])

        size = len(costs)

        # Those N people on the head should go to city A
        cost_of_go_to_A = sum([costs[i][0] for i in range(size // 2)])

        # Other N people on the tail should to to city B.
        cost_of_go_to_B = sum([costs[i][1] for i in range(size // 2, size)])

        return cost_of_go_to_A + cost_of_go_to_B


if __name__ == '__main__':
    costs = [[10, 20], [30, 200], [400, 50], [30, 20]]
    print(Solution().twoCitySchedCost(costs=costs))
