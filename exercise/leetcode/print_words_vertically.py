# -*- coding: utf-8 -*-
"""
1324. Print Words Vertically
@link https://leetcode.com/problems/print-words-vertically/
"""
from typing import List


class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(" ")
        rows = len(max(s, key=lambda k: len(k)))
        cols = len(s)
        list_str = [[" " for _ in range(cols)] for _ in range(rows)]

        for ind, str_ in enumerate(s):
            for i in range(len(str_)):
                list_str[i][ind] = str_[i]

        return ["".join(chars).rstrip() for chars in list_str]


if __name__ == '__main__':
    s = "TO BE OR NOT TO BE"
    print(Solution().printVertically(s=s))
