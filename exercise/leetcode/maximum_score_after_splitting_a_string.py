# -*- coding: utf-8 -*-
"""
1422. Maximum Score After Splitting a String
@link https://leetcode.com/problems/maximum-score-after-splitting-a-string/
"""


class Solution:
    def maxScore(self, s: str) -> int:
        result = 0
        for i in range(1, len(s)):
            left = s[0:i]
            right = s[i:]
            if left.count('0') + right.count('1') > result:
                result = left.count('0') + right.count('1')
        return result


if __name__ == '__main__':
    s = '1111'
    print(Solution().maxScore(s=s))
