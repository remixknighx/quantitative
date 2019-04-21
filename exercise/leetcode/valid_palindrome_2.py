# -*- coding: utf-8 -*-
"""
680. Valid Palindrome 2
@link https://leetcode.com/problems/valid-palindrome-ii/
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.helper(0, len(s) - 1, s, False)

    def helper(self, left: int, right: int, s: str, had_mistake: bool) -> bool:
        if left >= right:
            return True
        elif s[left] == s[right]:
            return self.helper(left+1, right-1, s, had_mistake)
        elif had_mistake:
            return False
        else:
            return self.helper(left+1, right, s, True) or self.helper(left, right-1, s, True)


if __name__ == '__main__':
    print(Solution().validPalindrome('eeccccbebaeeabebccceea'))
