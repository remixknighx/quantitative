# -*- coding: utf-8 -*-
"""
521. Longest Uncommon Subsequence I
@link https://leetcode.com/problems/longest-uncommon-subsequence-i/
"""


class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return -1 if a == b else max(len(a), len(b))


if __name__ == '__main__':
    print(Solution().findLUSlength(a='aba', b='cdcd'))
