# -*- coding: utf-8 -*-
"""
720. Longest Word in Dictionary
@link https://leetcode.com/problems/longest-word-in-dictionary/
"""
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        A = {}
        maxlen = 0
        maxword = ''
        words = sorted(words, key=len)
        for c in words:
            l = len(c)
            if A.get(c[:-1]) or l == 1:
                A[c] = l
                if maxlen == l:
                    maxword = min(maxword, c)
                elif l > maxlen:
                    maxword = c
                    maxlen = l
        return maxword


if __name__ == '__main__':
    words = ["w","wo","wor","worl", "world"]
    print(Solution().longestWord(words=words))