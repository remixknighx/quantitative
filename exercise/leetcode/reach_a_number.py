# -*- coding: utf-8 -*-
"""
754. Reach a Number
@link https://leetcode.com/problems/reach-a-number/
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        step: int = 0
        sum: int = 0
        while sum < target:
            step += 1
            sum += step

        while (sum - target) % 2 != 0:
            step += 1
            sum += step

        return step


if __name__ == '__main__':
    print(Solution().reachNumber(3))
