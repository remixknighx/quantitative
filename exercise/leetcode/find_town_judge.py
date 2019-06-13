"""
997. Find the Town Judge
@link https://leetcode.com/problems/find-the-town-judge/
"""
from typing import List


class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        trust_dict = {}
        for single_trust in trust:
            count = trust_dict.get(single_trust[1])
            if not count:
                count = 1
            else:
                count += 1
            trust_dict[single_trust[1]] = count

        judge: int = -1
        judge_count: int = 0
        for (k, v) in trust_dict.items():
            if v == N-1 and not trust_dict.get(k):
                judge = k
                judge_count += 1
            if judge_count > 1:
                judge = -1
                break
        return judge


if __name__ == '__main__':
    trust = [[1,2]]
    print(Solution().findJudge(N=2, trust=trust))

