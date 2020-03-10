# -*- coding: utf-8 -*-
"""
633. Sum of Square Numbers
@link https://leetcode.com/problems/sum-of-square-numbers/
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        ref, x = set(), 0
        while x * x <= c:
            ref.add(x * x)
            if c - x * x in ref:
                return True
            x += 1
        return False


if __name__ == '__main__':
    print(Solution().judgeSquareSum(c=5))
    print(Solution().judgeSquareSum(c=3))
