# -*- coding: utf-8 -*-
"""
1304. Find N Unique Integers Sum up to Zero
@link https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
"""
from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        if n % 2 == 1:
            result.append(0)
            n -= 1
        for i in range(0, int(n/2)):
            result.append(i+1)
            result.append(-i-1)
        return result


if __name__ == '__main__':
    print(Solution().sumZero(n=3))
