# -*- coding: utf-8 -*-
"""
1446. Consecutive Characters
@link https://leetcode.com/problems/consecutive-characters/
"""


class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        last_character = s[0]
        max_count = 1
        result = 0
        for i in range(1, len(s)):
            if s[i] == last_character:
                max_count += 1
            else:
                max_count = 1
                last_character = s[i]
            if max_count > result:
                result = max_count
        return result


if __name__ == '__main__':
    print(Solution().maxPower(s='leetcode'))
    print(Solution().maxPower(s='abbcccddddeeeeedcba'))
    print(Solution().maxPower(s='triplepillooooow'))
    print(Solution().maxPower(s='hooraaaaaaaaaaay'))
    print(Solution().maxPower(s='tourist'))
