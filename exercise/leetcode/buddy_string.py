# -*- coding: utf-8 -*-
"""
859. Buddy Strings
@link https://leetcode.com/problems/buddy-strings/
"""


class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        if A == B:
            return len(A) > len(set(B))
        else:
            pairs = []
            for a, b in zip(A, B):
                if a != b:
                    pairs.append((a, b))
                    if len(pairs) > 2:
                        return False
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1]


if __name__ == '__main__':
    A = 'aaaaaaabc'
    B = 'aaaaaaacb'
    print(Solution().buddyStrings(A=A, B=B))
