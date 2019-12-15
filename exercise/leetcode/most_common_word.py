# -*- coding: utf-8 -*-
"""
819. Most Common Word
@link https://leetcode.com/problems/most-common-word/
"""
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuations = "!?,;."
        for p in punctuations:
            paragraph = paragraph.replace(p, " ")
        paragraph = paragraph.replace("' ", " ")

        # Convert paragraph into words.
        paragraph = paragraph.lower().split()
        # Convert banned from list to set for O(1) query
        banned = set(banned)

        # Count the frequency of each of word and track maximum
        counter = {}
        max_count = 0
        frequent_word = ""
        for word in paragraph:
            if word not in banned:
                counter[word] = counter.get(word, 0) + 1
                if counter[word] > max_count:
                    max_count = counter[word]
                    frequent_word = word

        return frequent_word


if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ['hit']
    print(Solution().mostCommonWord(paragraph=paragraph, banned=banned))