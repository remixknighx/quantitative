# -*- coding: utf-8 -*-
"""
1018. Binary Prefix Divisible By 5
@link https://leetcode.com/problems/binary-prefix-divisible-by-5/
"""
from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        result = []
        temp_str = ''
        for i in range(0, len(A)):
            temp_str += str(A[i])
            if int(temp_str, 2) % 5 == 0:
                result.append(True)
            else:
                result.append(False)
        return result


if __name__ == '__main__':
    print(Solution().prefixesDivBy5(A=[0, 1, 1]))
    print(Solution().prefixesDivBy5(A=[1, 1, 1]))
    print(Solution().prefixesDivBy5(A=[0, 1, 1, 1, 1, 1]))
    print(Solution().prefixesDivBy5(A=[1, 1, 1, 0, 1]))
