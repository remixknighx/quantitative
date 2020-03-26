# -*- coding: utf-8 -*-
"""
1370. Increasing Decreasing String
@link https://leetcode.com/problems/increasing-decreasing-string/
"""


class Solution:
    def sortString(self, s: str) -> str:
        result = []
        s = list(s)
        flag = True
        while len(s) != 0:
            if flag:
                temp = sorted(set(s))
            else:
                temp = sorted(set(s), reverse=True)
            for ch in temp: s.remove(ch)
            result.extend(temp)
            flag = not flag
        return "".join(result)


if __name__ == '__main__':
    s_list = list('leetcode')
    s_list.sort()
    result = ''
    print(Solution().sortString(s='leetcode'))
