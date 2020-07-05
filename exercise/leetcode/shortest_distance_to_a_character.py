# -*- coding: utf-8 -*-
"""
821. Shortest Distance to a Character
@link https://leetcode.com/problems/shortest-distance-to-a-character/
"""
from typing import List


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        targets = []
        for i in range(0, len(S)):
            if S[i] == C:
                targets.append(i)

        result = []
        for i in range(0, len(S)):
            if S[i] != C:
                result.append(min([abs(i - j) for j in targets]))
            else:
                result.append(0)

        return result


if __name__ == '__main__':
    print(Solution().shortestToChar(S='loveleetcode', C='e'))
