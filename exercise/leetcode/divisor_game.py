# -*- coding: utf-8 -*-
"""
1025. Divisor Game
@link https://leetcode.com/problems/divisor-game/
"""


class Solution:
    def divisorGame(self, N: int) -> bool:
        return N % 2 == 0


if __name__ == '__main__':
    print(Solution().divisorGame(N=2))
