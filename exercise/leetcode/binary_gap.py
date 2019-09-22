# -*- coding: utf-8 -*-
"""
868. Binary Gap
@link https://leetcode.com/problems/binary-gap/
"""


class Solution:
    def binaryGap(self, N: int) -> int:
        N_str = str(bin(N))
        result = 0
        for i in range(0, len(N_str)):
            if N_str[i] == '1':
                for j in range(i+1, len(N_str)):
                    if N_str[j] == '1':
                        distance = j - i
                        if distance > result:
                            result = distance
                        break
        return result


if __name__ == '__main__':
    print(Solution().binaryGap(N=22))
    print(Solution().binaryGap(N=5))
    print(Solution().binaryGap(N=6))
    print(Solution().binaryGap(N=8))
