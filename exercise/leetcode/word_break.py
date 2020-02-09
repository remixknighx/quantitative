# -*- coding: utf-8 -*-
"""
139. Word Break
@link https://leetcode.com/problems/word-break/
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def isindict(s, my_dict):
            if s in my_dict or not s:
                return True
            else:
                for word in my_dict:
                    if word in s:
                        left, right = s.split(word, 1)
                        if left in dp:
                            left_result = dp[left]
                        else:
                            left_result = isindict(left, my_dict)
                            dp[left] = left_result
                        if right in dp:
                            right_result = dp[right]
                        else:
                            right_result = isindict(right, my_dict)
                            dp[right] = right_result
                        if left_result and right_result:
                            return True
                    else:
                        pass
            return False

        return isindict(s, wordDict)


if __name__ == '__main__':
    s = 'cars'
    wordDict = ["car","ca","rs"]
    print(Solution().wordBreak(s=s, wordDict=wordDict))
