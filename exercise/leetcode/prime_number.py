# -*- coding: utf-8 -*-
"""
762. Prime Number of Set Bits in Binary Representation
@link https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/
"""

import math


class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        count_result: int = 0
        for num in range(L, R+1):
            if self.is_prime(num=num):
                count_result += 1
        return count_result

    def is_prime(self, num: int) -> bool:
        bin_num: str = bin(num)
        zero_count: int = 0
        for char in bin_num:
            if char == '1':
                zero_count += 1

        if zero_count <= 1:
            return False

        for i in range(2, int(math.sqrt(zero_count)) + 1):
            if zero_count % i == 0:
                return False

        return True


if __name__ == '__main__':
    print(Solution().countPrimeSetBits(L=10, R=15))

