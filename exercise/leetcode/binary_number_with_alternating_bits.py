# -*- coding: utf-8 -*-
"""
693. Binary Number with Alternating Bits
@link https://leetcode.com/problems/binary-number-with-alternating-bits/
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        n_bit_str = str(bin(n))[2:]
        for i in range(0, len(n_bit_str)-1):
            if n_bit_str[i] == n_bit_str[i+1]:
                return False
        return True


if __name__ == '__main__':
    print(Solution().hasAlternatingBits(n=5))
    print(Solution().hasAlternatingBits(n=7))
    print(Solution().hasAlternatingBits(n=11))
    print(Solution().hasAlternatingBits(n=10))
