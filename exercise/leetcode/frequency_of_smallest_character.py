# -*- coding: utf-8 -*-
"""
1170. Compare Strings by Frequency of the Smallest Character
@link https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/
"""
from typing import List


class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        result: List = []
        word_count_list = []
        for word in words:
            word_count_list.append(self.findSmallestFrequency(word=word))
        for query in queries:
            smallest_count = self.findSmallestFrequency(word=query)
            smaller_count = 0
            for word_count in word_count_list:
                if smallest_count < word_count:
                    smaller_count += 1
            result.append(smaller_count)
        return result

    def findSmallestFrequency(self, word: str) -> int:
        smallest_char = 'z'
        count: int = 0
        for single_char in word:
            if smallest_char > single_char:
                smallest_char = single_char
                count = 1
            elif smallest_char == single_char:
                count += 1

        return count


if __name__ == '__main__':
    queries = ['cbd']
    words = ['zaaaz']
    print(Solution().numSmallerByFrequency(queries=queries, words=words))