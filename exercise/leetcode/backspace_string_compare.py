# -*- coding: utf-8 -*-
"""
844. Backspace String Compare
@link https://leetcode.com/problems/backspace-string-compare/
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S_list = self.get_final_string(text=S)
        T_list = self.get_final_string(text=T)
        if len(S_list) != len(T_list):
            return False
        for i in range(0, len(S_list)):
            if S_list[i] != T_list[i]:
                return False
        return True

    def get_final_string(self, text: str):
        str_stack = []
        for i in range(0, len(text)):
            if text[i] == '#':
                if len(str_stack) != 0:
                    str_stack.pop(len(str_stack)-1)
            else:
                str_stack.append(text[i])
        return str_stack


if __name__ == '__main__':
    print(Solution().backspaceCompare(S='ab#c', T='ad#c'))
    print(Solution().backspaceCompare(S='ab##', T='ad##'))
    print(Solution().backspaceCompare(S='a##c', T='#a#c'))
    print(Solution().backspaceCompare(S='a#c', T='b'))