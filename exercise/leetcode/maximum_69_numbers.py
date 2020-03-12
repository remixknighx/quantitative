# -*- coding: utf-8 -*-
"""
1323. Maximum 69 Number
@link https://leetcode.com/problems/maximum-69-number/
"""


class Solution:
    def maximum69Number (self, num: int) -> int:
        max_num = num
        num_str = str(num)
        for i in range(0, len(num_str)):
            temp_num = self.replace(num_str, i)
            max_num = max(max_num, int(temp_num))

        return max_num

    def replace(self, num_str, pos) -> str:
        num_list = list(num_str)
        if num_list[pos] == '6':
            num_list[pos] = '9'
        else:
            num_list[pos] = '6'
        return ''.join(num_list)


if __name__ == '__main__':
    print(Solution().maximum69Number(num=9996))
