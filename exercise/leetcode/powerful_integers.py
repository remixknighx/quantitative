# -*- coding: utf-8 -*-
"""
970. Powerful integers
@link https://leetcode.com/problems/powerful-integers/
"""
from typing import List


class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        s = set()
        stack = [(0, 0)]
        while stack:
            i, j = stack.pop()
            t = x ** i + y ** j
            if t <= bound:
                s.add(t)
                if x > 1:
                    stack.append((i+1, j))
                if y > 1:
                    stack.append((i, j + 1))
        return list(s)


if __name__ == '__main__':
    print(Solution().powerfulIntegers(x=2, y=3, bound=10))
