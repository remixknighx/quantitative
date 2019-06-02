# -*- coding: utf-8 -*-
"""
728. Self Dividing Numbers
@link https://leetcode.com/problems/self-dividing-numbers/
"""

from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        for num in range(left, right + 1):
            if self.is_dividing_number(num=num):
                result.append(num)

        return result


    def is_dividing_number(self, num: int) -> bool:
        return ('0' not in str(num)) and all(num % int(digit) == 0 for digit in str(num))


if __name__ == '__main__':
    print(Solution().selfDividingNumbers(left=1, right=22))
