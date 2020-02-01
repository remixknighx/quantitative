# -*- coding: utf-8 -*-
"""
916. Word Subsets
@link https://leetcode.com/problems/word-subsets/
"""
from typing import List


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        table = {}
        uni = []
        for b in B:
            for letter in b:

                if letter not in table:
                    table[letter] = b.count(letter)

                elif b.count(letter) > table[letter]:
                    table[letter] = b.count(letter)

        for a in A:
            flag = True
            for c, n in table.items():
                if (c not in a) or a.count(c) < n:
                    flag = False
                    break

            if flag:
                uni.append(a)
        return uni


if __name__ == '__main__':
    print('eeee'.count('e'))
    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["e", "o"]
    print(Solution().wordSubsets(A=A, B=B))
