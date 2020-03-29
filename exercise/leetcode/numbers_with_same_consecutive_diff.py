# -*- coding: utf-8 -*-
"""
967. Numbers With Same Consecutive Differences
@link https://leetcode.com/problems/numbers-with-same-consecutive-differences/
"""
from typing import List


class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        result = set()
        is_even = N % 2 == 0
        for i in range(N):
            for num in range(0, 10):
                temp = ''
                if 0 <= num + K <= 9:
                    temp = str(num)
                    if num != 0:
                        temp += str(num + K)
                    if temp and ((len(temp) > 1 and not temp.startswith('0')) or (len(temp) == 1 and N == 1)):
                        if is_even:
                            result.add(int(temp * int(N/2)))
                        else:
                            result.add(int(temp * int(N / 2) + str(num)))
                if 0 <= num - K <= 9:
                    temp = str(num)
                    if num != 0:
                        temp += str(num - K)
                    if temp and ((len(temp) > 1 and not temp.startswith('0')) or (len(temp) == 1 and N == 1)):
                        if is_even:
                            result.add(int(temp * int(N/2)))
                        else:
                            result.add(int(temp * int(N / 2) + str(num)))
        return list(result)


if __name__ == '__main__':
    print(Solution().numsSameConsecDiff(N=1, K=0))
