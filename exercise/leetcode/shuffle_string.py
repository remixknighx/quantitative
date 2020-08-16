# -*- coding: utf-8 -*-
"""
1528. Shuffle String
@link https://leetcode.com/problems/shuffle-string/
"""
from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        pairs = list(zip(list(s), indices))
        return ''.join([x[0] for x in sorted(pairs, key=(lambda x: x[1]))])


if __name__ == '__main__':
    print(Solution().restoreString(s='codeleet', indices=[4, 5, 6, 7, 0, 2, 1, 3]))
