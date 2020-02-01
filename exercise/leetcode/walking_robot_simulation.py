# -*- coding: utf-8 -*-
"""
874. Walking Robot Simulation
@link https://leetcode.com/problems/walking-robot-simulation/
"""
from typing import List


class Solution:

    def is_stopped(self, pos: List[int], obstacles:  List[List[int]]) -> bool:
        for obstacle in obstacles:
            if pos[0] == obstacle[0] and pos[1] == obstacle[1]:
                return True
        return False

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obst = {tuple(i) for i in obstacles}
        ans = 0
        x, y, dx, dy = 0, 0, 0, 1
        # north: 0, 1
        # south: 0, -1
        # east: 1, 0
        # west: -1, 0
        for i in commands:
            if i == -1:
                dx, dy = dy, -dx
            elif i == -2:
                dx, dy = -dy, dx
            else:
                while i:
                    _x, _y = x + dx, y + dy
                    if (_x, _y) not in obst:
                        x, y, ans = _x, _y, max(ans, _x * _x + _y * _y)
                    i -= 1
        return ans


if __name__ == '__main__':
    commands = [4,-1,4,-2,4]
    obstacles = [[2,4]]
    print(Solution().robotSim(commands=commands, obstacles=obstacles))
