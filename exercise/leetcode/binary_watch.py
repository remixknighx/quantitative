# -*- coding: utf-8 -*-
"""
401. Binary Watch
@link https://leetcode.com/problems/binary-watch/
"""
from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        return ['%d:%02d' % (h, m)
                for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == num]


def findNumber(arr, k):
    if (arr is None or len(arr) == 0) or k is None:
        return 'NO'
    if k in arr:
        return 'YES'
    return 'NO'


def oddNumbers(l, r):
    result = []
    for num in range(l, r+1):
        if num % 2 == 1:
            result.append(num)
    return result


if __name__ == '__main__':
    print(oddNumbers(3, 9))
