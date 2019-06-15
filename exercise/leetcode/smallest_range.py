# -*- coding: utf-8 -*-

from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        A.sort()
        smallest_difference = A[len(A)-1] - A[0]

        if smallest_difference <= 2 * K:
            smallest_difference = 0
        else:
            smallest_difference = (A[len(A)-1] - K) - (A[0] + K)
        return smallest_difference


if __name__ == '__main__':
    print(Solution().smallestRangeI(A=[1], K=0))
