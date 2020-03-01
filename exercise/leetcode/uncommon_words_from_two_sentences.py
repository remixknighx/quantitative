# -*- coding: utf-8 -*-
"""
884. Uncommon Words from Two Sentences
@link https://leetcode.com/problems/uncommon-words-from-two-sentences/
"""
from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        word_dict = {}
        for A_word in A.split(' '):
            if word_dict.get(A_word) is None:
                word_dict.setdefault(A_word, 1)
            else:
                word_dict[A_word] += 1

        for B_word in B.split(' '):
            if word_dict.get(B_word) is None:
                word_dict.setdefault(B_word, 1)
            else:
                word_dict[B_word] += 1

        result = []
        for (k, v) in word_dict.items():
            if v == 1:
                result.append(k)
        return result


if __name__ == '__main__':
    A = "this apple is sweet"
    B = "this apple is sour"
    print(Solution().uncommonFromSentences(A=A, B=B))
