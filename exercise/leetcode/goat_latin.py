# -*- coding: utf-8 -*-
"""
824. Goat Latin
@link https://leetcode.com/problems/goat-latin/
"""


class Solution:
    def toGoatLatin(self, S: str) -> str:
        s_list = S.split(' ')
        result = ''
        for i in range(0, len(s_list)):
            temp = ''
            if s_list[i].lower().startswith('a') or s_list[i].lower().startswith('e') or s_list[i].lower().startswith('i') or s_list[i].lower().startswith('o') or s_list[i].lower().startswith('u'):
                temp += s_list[i] + 'ma'
            else:
                temp += s_list[i][1:] + s_list[i][0] + 'ma'

            temp += 'a' * (i+1)
            result += temp + ' '

        return result[:-1]


if __name__ == '__main__':
    print(Solution().toGoatLatin(S="Each word consists of lowercase and uppercase letters only"))
    # print('abdfd'.startswith('a'))
