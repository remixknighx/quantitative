# -*- coding: utf-8 -*-
"""
657. Robot Return to Origin
@link https://leetcode.com/problems/robot-return-to-origin/
"""


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R"):
            return True
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.judgeCircle(moves='UDDUURLRLLRRUDUDLLRLURLRLRLUUDLULRULRLDDDUDDDDLRRDDRDRLRLURRLLRUDURULULRDRDLURLUDRRLRLDDLUUULUDUUUUL'))

