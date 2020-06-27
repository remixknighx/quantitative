# -*- coding: utf-8 -*-
"""
746. Min Cost Climbing Stairs
@link https://leetcode.com/problems/min-cost-climbing-stairs/
"""
from typing import List


class Solution:

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)

        for i in range(2, len(cost)):
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2])

        return cost[-1]


if __name__ == '__main__':
    # print(Solution().minCostClimbingStairs(cost=[10, 15]))
    print(Solution().minCostClimbingStairs(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
