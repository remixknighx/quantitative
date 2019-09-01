# -*- coding: utf-8 -*-
"""
717. 1-bit and 2-bit Characters
@link https://leetcode.com/problems/1-bit-and-2-bit-characters/
"""
from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        idx: int = 0
        last_character = True
        while idx < len(bits):
            if bits[idx] == 1:
                idx += 2
                last_character = False
            else:
                idx += 1
                last_character = True

        return last_character


if __name__ == '__main__':
    bits = [1, 1, 1, 0]
    print(Solution().isOneBitCharacter(bits=bits))