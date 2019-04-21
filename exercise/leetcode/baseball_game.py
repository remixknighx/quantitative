# -*- coding: utf-8 -*-
"""
682. Baseball Game
@link https://leetcode.com/problems/baseball-game/
"""
from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        score: int = 0
        num_stack: List = []
        for single_str in ops:
            round_score: int = 0
            if single_str == '+':
                round_score = num_stack[len(num_stack) - 1] + num_stack[len(num_stack) - 2]
                score = score + round_score
                num_stack.append(round_score)
            elif single_str == 'D':
                round_score = num_stack[len(num_stack) - 1] * 2
                score += round_score
                num_stack.append(round_score)
            elif single_str == 'C':
                score -= num_stack.pop()
            else:
                # 数组中该值为数字
                round_score = int(single_str)
                score += round_score
                num_stack.append(round_score)
        return score


if __name__ == '__main__':
    ops: List = ['5', '-2', '4', 'C', 'D', '9', '+', '+']
    print(Solution().calPoints(ops=ops))

