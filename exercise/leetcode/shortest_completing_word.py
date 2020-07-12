# -*- coding: utf-8 -*-
"""
748. Shortest Completing Word
@link https://leetcode.com/problems/shortest-completing-word/
"""
from typing import List
from collections import Counter


class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        al = 'abcdefghijklmnopqrstuvwxyz'
        let = {}
        for letter in licensePlate:
            ch = letter.lower()
            if ch in let and ch in al:
                let[ch] += 1
            elif ch in al:
                let[ch] = 1
        result = ''
        for word in words:
            flag = True
            word_count = Counter(word)
            for (k,v) in let.items():
                if word_count.get(k) is None or word_count.get(k) < v:
                    flag = False
                    break
            if flag:
                if len(result) == 0 or len(result) > len(word):
                    result = word
        return result


if __name__ == '__main__':
    print(Solution().shortestCompletingWord(licensePlate="1s3 PSt", words=["step", "steps", "stripe", "stepple"]))
