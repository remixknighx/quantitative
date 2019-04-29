# -*- coding: utf-8 -*-

"""
509. Fibonacci Number
@link https://leetcode.com/problems/fibonacci-number/
"""


class Solution:
    def fib(self, N: int) -> int:
        if N == 0 or N == 1:
            return N
        return self.fib(N - 1) + self.fib(N - 2)


if __name__ == '__main__':
    print(Solution().fib(N=2))
    print(Solution().fib(N=3))
    print(Solution().fib(N=4))
    print(Solution().fib(N=5))
