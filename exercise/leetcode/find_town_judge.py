"""
997. Find the Town Judge
@link https://leetcode.com/problems/find-the-town-judge/
"""
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0] * (N + 1)
        for k, v in trust:
            count[k] -= 1
            count[v] += 1
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1


if __name__ == '__main__':
    trust = [[1, 2]]
    print(Solution().findJudge(N=2, trust=trust))

