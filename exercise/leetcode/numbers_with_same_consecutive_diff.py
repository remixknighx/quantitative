# -*- coding: utf-8 -*-
"""
967. Numbers With Same Consecutive Differences
@link https://leetcode.com/problems/numbers-with-same-consecutive-differences/
"""
from typing import List
from collections import defaultdict


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        # if N == 1, answer is always [0,...,9]
        if N == 1:
            return [i for i in range(0, 10)]

        # if K == 0, answer is always like [11,...,99]
        if K == 0:
            return [
                sum([
                    i * (10 ** p)
                    for p in range(N)
                ])
                for i in range(1, 10)
            ]

        # Make next digit candidate map
        # if K = 4 m is like below
        # {
        #   0: [4],
        #   1: [5],
        #   2: [6],
        #   3: [7],
        #   4: [0, 8],
        #   5: [1, 9],
        #   6: [2],
        #   7: [3],
        #   8: [4],
        #   9: [5]
        # }
        m = defaultdict(list)
        for i in range(0, 10):
            if i + K < 10:
                m[i].append(i + K)
            if i - K >= 0:
                m[i].append(i - K)

        # Using DFS
        # stack initial values are first digit candidate (1,...,9)
        stack = [
            [k]
            for k in m.keys()
            if k != 0
        ]
        ans = []
        while stack:
            path = stack.pop()
            if len(path) == N:
                v = sum([n * (10 ** i) for i, n in enumerate(path[::-1])])
                ans.append(v)
            else:
                # add next digit candidate to stack
                candidates = m[path[-1]]
                for c in candidates:
                    stack.append(path + [c])
        return ans


if __name__ == '__main__':
    print(Solution().numsSameConsecDiff(N=2, K=1))
