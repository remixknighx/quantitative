# -*- coding: utf-8 -*-
"""
893. Groups of Special-Equivalent Strings
@link https://leetcode.com/problems/groups-of-special-equivalent-strings/
"""
from typing import List


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        return len(set("".join(sorted(s[0::2])) + "".join(sorted(s[1::2])) for s in A))
