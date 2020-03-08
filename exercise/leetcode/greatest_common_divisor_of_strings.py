# -*- coding: utf-8 -*-
"""
1071. Greatest Common Divisor of Strings
@link https://leetcode.com/problems/greatest-common-divisor-of-strings/
"""
import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        result = (str1 if len(str1) < len(str2) else str2)[0:math.gcd(len(str1), len(str2))]
        if self.checkCommonStr(str1, result) and self.checkCommonStr(str2, result):
            return result
        else:
            return ''

    def checkCommonStr(self, test_str: str, result: str) -> bool:
        temp_result = ''
        for i in range(0, int(len(test_str)/len(result))):
            temp_result += result
        return temp_result == test_str


if __name__ == '__main__':
    print(Solution().gcdOfStrings(str1="abaabaaba", str2="aba"))
    print(Solution().gcdOfStrings(str1="LEET", str2="CODE"))
    print(Solution().gcdOfStrings(str1="ABCABC", str2="ABC"))
