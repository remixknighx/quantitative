# -*- coding: utf-8 -*-
"""
1221. Split a String in Balanced Strings
@link https://leetcode.com/problems/split-a-string-in-balanced-strings/
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = index = left_num = right_num = 0

        while True:
            if s[index] == 'L':
                left_num += 1
            else:
                right_num += 1

            if left_num == right_num:
                result += 1
                left_num = right_num = 0

            index += 1
            if index == len(s):
                break
        return result


if __name__ == '__main__':
    s = "RLRRRLLRLL"
    print(Solution().balancedStringSplit(s=s))
