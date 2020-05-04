# -*- coding: utf-8 -*-
"""
1189. Maximum Number of Balloons
@link https://leetcode.com/problems/maximum-number-of-balloons/
"""
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        text_count = Counter(text)
        b_cnt = text_count.get('b')
        a_cnt = text_count.get('a')
        l_cnt = 0
        o_cnt = 0
        if text_count.get('l') is not None:
            l_cnt = int(text_count.get('l')/2)
        if text_count.get('o') is not None:
            o_cnt = int(text_count.get('o')/2)
        n_cnt = text_count.get('n')

        if b_cnt is None or a_cnt is None or n_cnt is None:
            return 0
        return min(b_cnt, a_cnt, l_cnt, o_cnt, n_cnt)


if __name__ == '__main__':
    print(Solution().maxNumberOfBalloons(text='loonbalxballpoon'))
    print(Solution().maxNumberOfBalloons(text='leetcode'))
