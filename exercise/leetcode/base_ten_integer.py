# -*- coding: utf-8 -*-
"""
1009. Complement of Base 10 Integer
@link https://leetcode.com/problems/complement-of-base-10-integer/
"""


class Solution:
    def bitwiseComplement(self, N: int) -> int:
        # 十进制转换成二进制
        N_binary = bin(N)[2:]
        N_binary_complent = ''
        for num in N_binary:
            N_binary_complent += str(1-int(num))
        # 二进制转换成十进制
        return int(N_binary_complent, 2)


if __name__ == '__main__':
    print(Solution().bitwiseComplement(N=10))
