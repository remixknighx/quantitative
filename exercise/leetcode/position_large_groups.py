# -*- coding: utf-8 -*-
"""
830. Positions of Large Groups
@link https://leetcode.com/problems/positions-of-large-groups/
"""

from typing import List


class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        res: List[List[int]] = []
        start: int = 0
        end: int = 0
        count: int = 1
        for i in range(1, len(S)):
            if S[i-1] == S[i]:
                count += 1
                end = i
            else:
                if count >= 3:
                    res.append([start, end])
                count = 1
                start = i

        if count >= 3:
            res.append([start, end])

        return res


if __name__ == '__main__':
    print(Solution().largeGroupPositions(S='abcdddeeeeaabbbcd'))