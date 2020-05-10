# -*- coding: utf-8 -*-
"""
1417. Reformat The String
@link https://leetcode.com/problems/reformat-the-string/
"""


class Solution:
    def reformat(self, s: str) -> str:
        digit_list = []
        str_list = []
        for c in s:
            if c.isdigit():
                digit_list.append(c)
            else:
                str_list.append(c)
        if abs(len(digit_list) - len(str_list)) > 1:
            return ''

        flag = (len(digit_list) > len(str_list))

        res = []
        for i in range(len(s)):
            if flag:
                res.append(digit_list.pop())
            else:
                res.append(str_list.pop())
            flag = not flag

        return ''.join(res)


if __name__ == '__main__':
    print('a'.isdigit())
    print(Solution().reformat(s='a0b1c2'))
