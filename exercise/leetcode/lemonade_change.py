# -*- coding: utf-8 -*-
"""
860. Lemonade Change
@link https://leetcode.com/problems/lemonade-change/
"""
from typing import List
from collections import defaultdict


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        received_money = defaultdict(int)
        for bill in bills:
            received_money[bill] += 1
            if bill == 10:
                if received_money[5] == 0:
                    return False
                else:
                    received_money[5] -= 1
            if bill == 20:
                if received_money[10] == 0 and received_money[5] >= 3:
                    received_money[5] -= 3
                elif received_money[10] >= 1 and received_money[5] >= 1:
                    received_money[10] -= 1
                    received_money[5] -= 1
                else:
                    return False
        return True


if __name__ == '__main__':
    print(Solution().lemonadeChange(bills=[5, 5, 10, 20, 5, 5, 5, 5, 5, 5, 5, 5, 5, 10, 5, 5, 20, 5, 20, 5]))
