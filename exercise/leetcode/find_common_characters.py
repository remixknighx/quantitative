# -*- coding: utf-8 -*-
"""
1002. Find Common Characters
@link https://leetcode.com/problems/find-common-characters/
"""
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        a = []
        for i in set(A[0]):
            a.extend([i] * min(j.count(i) for j in A))

        return a


if __name__ == '__main__':
    print(Solution().commonChars(A=["bella", "label", "roller"]))
