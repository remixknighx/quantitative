# -*- coding: utf-8 -*-

"""
686. Repeated String Match
@link https://leetcode.com/problems/repeated-string-match/
"""


def repeatedStringMatch(A: str, B: str) -> int:
    count: int = 1
    repeated_str: str = A
    while True:
        if B in repeated_str:
            return count
        elif len(repeated_str) > len(B) + len(A):
            break
        else:
            count += 1
            repeated_str += A
    return -1


if __name__ == '__main__':
    print(repeatedStringMatch(A='abc', B='cabcabca'))
