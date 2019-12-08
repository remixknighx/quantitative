# -*- coding: utf-8 -*-
"""
784. Letter Case Permutation
@link https://leetcode.com/problems/letter-case-permutation/
"""
from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if S[0].isalpha():
            res = [S[0].upper(), S[0].lower()]
        else:
            res = [str(S[0])]
        for i in range(1, len(S)):
            upper_list = []
            lower_list = []
            if S[i].isalpha():
                for j in range(0, len(res)):
                    upper_list.append(res[j] + S[i].upper())
                    lower_list.append(res[j] + S[i].lower())
                res.clear()
                res = upper_list + lower_list
            else:
                for j in range(0, len(res)):
                    res[j] += str(S[i])

        return res


if __name__ == '__main__':
    print(Solution().letterCasePermutation(S='12345'))