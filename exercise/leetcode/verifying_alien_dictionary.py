# -*- coding: utf-8 -*-
"""
953. Verifying an Alien Dictionary
@link https://leetcode.com/problems/verifying-an-alien-dictionary/
"""
from typing import List


class Solution:

    def is_sorted(self, first_char, second_char, order):
        if first_char != '' and second_char == '':
            return False
        return order.index(first_char) <= order.index(second_char)

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(0, len(words) - 1):
            first_word = words[i]
            second_word = words[i+1]
            for j in range(0, len(first_word)):
                if j >= len(second_word):
                    return False
                if first_word[j] != second_word[j]:
                    if self.is_sorted(first_word[j], second_word[j], order):
                        break
                    else:
                        return False
        return True


if __name__ == '__main__':
    words = ["hello","leetcode"]

    order = "hlabcdefgijkmnopqrstuvwxyz"
    print(Solution().isAlienSorted(words=words, order=order))
