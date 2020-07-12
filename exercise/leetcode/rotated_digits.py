# -*- coding: utf-8 -*-
"""
788. Rotated Digits
@link https://leetcode.com/problems/rotated-digits/
"""


class Solution:
    def rotatedDigits(self, N: int) -> int:
        total = 0
        for num in range(1, N + 1):
            good = False
            digits = [int(digits) for digits in str(num)]
            for dig in digits:
                if dig in (2, 5, 6, 9):
                    good = True
                elif dig in (3, 4, 7):
                    good = False
                    break
            if good is True:
                total += 1
        return total


if __name__ == '__main__':
    print(Solution().rotatedDigits(N=26))
