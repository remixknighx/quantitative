# -*- coding: utf-8 -*-
"""
796. Rotate String
@link https://leetcode.com/problems/rotate-string/
"""


class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if len(A) == 0 and len(B) == 0:
            return True
        for i in range(0, len(A)):
            if A[i:] + A[0:i] == B:
                return True
        return False


if __name__ == '__main__':
    print(Solution().rotateString(A='abcde', B='cdeab'))
    print(Solution().rotateString(A='abcde', B='abced'))
    print(Solution().rotateString(A='', B=''))
