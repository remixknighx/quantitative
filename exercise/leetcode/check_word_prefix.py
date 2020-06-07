# -*- coding: utf-8 -*-
"""
1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
@link https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
"""


class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word_list = sentence.split(' ')
        for i in range(0, len(word_list)):
            if word_list[i].startswith(searchWord):
                return i + 1
        return -1


if __name__ == '__main__':
    print(Solution().isPrefixOfWord(sentence='i love eating burger', searchWord='burg'))
    print(Solution().isPrefixOfWord(sentence='this problem is an easy problem', searchWord='pro'))
    print(Solution().isPrefixOfWord(sentence='i am tired', searchWord='you'))
    print(Solution().isPrefixOfWord(sentence='i use triple pillow', searchWord='pill'))
    print(Solution().isPrefixOfWord(sentence='hello from the other side', searchWord='they'))
