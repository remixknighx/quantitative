# -*- coding: utf-8 -*-
"""
696. Count Binary Substrings
@link https://leetcode.com/problems/count-binary-substrings/
"""


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        chunks, consecutive, res = [], 1, 0
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                consecutive += 1
            else:
                chunks.append(consecutive)
                consecutive = 1
        chunks.append(consecutive)
        for i in range(1, len(chunks)):
            res += min(chunks[i], chunks[i - 1])
        return res


if __name__ == '__main__':
    print(Solution().countBinarySubstrings('10101'))

