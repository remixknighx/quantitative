# -*- coding: utf-8 -*-
"""
1408. String Matching in an Array
@link https://leetcode.com/problems/string-matching-in-an-array/
"""
from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = set()
        for i in range(0, len(words)):
            for j in range(i + 1, len(words)):
                if len(words[i]) <= len(words[j]):
                    if words[i] in words[j]:
                        result.add(words[i])
                else:
                    if words[j] in words[i]:
                        result.add(words[j])
        return list(result)


if __name__ == '__main__':
    print(Solution().stringMatching(words=["mass", "as", "hero", "superhero"]))
    print(Solution().stringMatching(words=["leetcode", "et", "code"]))
    print(Solution().stringMatching(words=["blue", "green", "bu"]))
