# -*- coding: utf-8 -*-
"""
1374. Generate a String With Characters That Have Odd Counts
@link https://leetcode.com/problems/generate-a-string-with-characters-that-have-odd-counts/
"""


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 != 0:
            return 'a' * n
        else:
            return "a" * (n - 1) + 'b'


if __name__ == '__main__':
    print(Solution().generateTheString(n=2))
