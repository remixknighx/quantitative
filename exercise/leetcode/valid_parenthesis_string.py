# -*- coding: utf-8 -*-
"""
678. Valid Parenthesis String
@link https://leetcode.com/problems/valid-parenthesis-string/
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        c = 0
        a = 0
        for n in s:
            if n == "(":
                c += 1
            if n == ")":
                c -= 1
            if n == "*":
                a += 1
            if (c + a) < 0:
                return False
        c = 0
        a = 0
        for n in reversed(s):
            if n == "(":
                c += 1
            if n == ")":
                c -= 1
            if n == "*":
                a -= 1
            if (c + a) > 0:
                return False
        return True


if __name__ == '__main__':
    print(Solution().checkValidString(s='(*)'))
