# -*- coding: utf-8 -*-
"""
1486. XOR Operation in an Array
@link https://leetcode.com/problems/xor-operation-in-an-array/
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        arr = [start + 2 * i for i in range(n)]
        ans = arr[0]
        for i in arr[1:]:
            ans = ans ^ i
        return ans


if __name__ == '__main__':
    print(Solution().xorOperation(n=5, start=0))
    print(Solution().xorOperation(n=4, start=3))
    print(Solution().xorOperation(n=1, start=7))
    print(Solution().xorOperation(n=10, start=5))
