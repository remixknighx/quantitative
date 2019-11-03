# -*- coding: utf-8 -*-
"""
1160. Find Words That Can Be Formed by Characters
@link https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
"""
from typing import List


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result: int = 0
        for word in words:
            temp_char = chars
            is_contain = True
            for word_char in word:
                if word_char in temp_char:
                    temp_char = temp_char.replace(word_char, '', 1)
                else:
                    is_contain = False
                    break
            if is_contain: result += len(word)
        return result


if __name__ == '__main__':
    test_str = 'aaaa'
    print(test_str.replace('a', '', 1))
    print(Solution().countCharacters(words=["cat", "bt", "hat", "tree"], chars="atach"))
    print(Solution().countCharacters(words=["hello", "world", "leetcode"], chars="welldonehoneyr"))
