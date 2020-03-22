# -*- coding: utf-8 -*-
"""
925. Long Pressed Name
@link https://leetcode.com/problems/long-pressed-name/
"""


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0

        while i < len(name):
            j, same = 0, 0
            while i + same < len(name) and name[i + same] == name[i]:
                same += 1
            while j < len(typed) and typed[j] == name[i]:
                j += 1

            if j < same:
                return False
            typed = typed[j:]
            i += same

        return True


if __name__ == '__main__':
    print(Solution().isLongPressedName(name="alex", typed="aaleex"))
    print(Solution().isLongPressedName(name="saeed", typed="ssaaedd"))
    print(Solution().isLongPressedName(name="leelee", typed="lleeelee"))
    print(Solution().isLongPressedName(name="laiden", typed="laiden"))
    print(Solution().isLongPressedName(name="kikcxmvzi", typed="kiikcxxmmvvzz"))


