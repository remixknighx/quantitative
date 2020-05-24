# -*- coding: utf-8 -*-
"""
744. Find Smallest Letter Greater Than Target
@link https://leetcode.com/problems/find-smallest-letter-greater-than-target/
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        result = ''
        for letter in letters:
            if letter > target:
                result = letter
                break
        if len(result) == 0:
            result = letters[0]
        return result


if __name__ == '__main__':
    print(Solution().nextGreatestLetter(letters=['c', 'f', 'j'], target='a'))
    print(Solution().nextGreatestLetter(letters=['c', 'f', 'j'], target='c'))
    print(Solution().nextGreatestLetter(letters=['c', 'f', 'j'], target='d'))
    print(Solution().nextGreatestLetter(letters=['c', 'f', 'j'], target='g'))
    print(Solution().nextGreatestLetter(letters=['c', 'f', 'j'], target='j'))
    print(Solution().nextGreatestLetter(letters=['c', 'f', 'j'], target='k'))
