# -*- coding: utf-8 -*-
"""
949. Largest Time for Given Digits
@link https://leetcode.com/problems/largest-time-for-given-digits/
"""
from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        ans: str = ''
        for i in range(0, len(A)):
            for j in range(0, len(A)):
                if i == j:
                    continue
                for k in range(0, len(A)):
                    if i == k or j == k:
                        continue
                    h = str(A[i]) + str(A[j])
                    m = str(A[k]) + str(A[6-i-j-k])
                    t = '' + h + ':' + m
                    if h <= '23' and m <= '59' and ans <= t:
                        ans = t
        return ans


if __name__ == '__main__':
    digit_list = [5, 5, 5, 5]
    print(Solution().largestTimeFromDigits(A=digit_list))