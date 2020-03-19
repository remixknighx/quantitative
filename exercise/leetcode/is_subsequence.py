# -*- coding: utf-8 -*-
"""
392. Is Subsequence
@link https://leetcode.com/problems/is-subsequence/
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = -1
        for ch in s:
            i = t.find(ch, i + 1)
            if i == -1:
                return False
        return True


if __name__ == '__main__':
    print(Solution().isSubsequence(s="axc", t="ahbgdc"))
