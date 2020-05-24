# -*- coding: utf-8 -*-
"""
1399. Count Largest Group
@link https://leetcode.com/problems/count-largest-group/
"""


class Solution:
    def countLargestGroup(self, n: int) -> int:
        num_dict = dict()
        max_digit_sum = 0
        for num in range(1, n + 1):
            digit_sum = num
            if digit_sum >= 10:
                 digit_sum = self.calSumDigit(num=num)

            num_dict.setdefault(digit_sum, 0)
            num_dict[digit_sum] += 1
            if num_dict[digit_sum] > max_digit_sum:
                max_digit_sum = num_dict[digit_sum]

        result = 0
        for (k, v) in num_dict.items():
            if v == max_digit_sum:
                result += 1
        return result

    def calSumDigit(self, num: int):
        result = 0
        while num / 10 != 0:
            result += int(num % 10)
            num /= 10
        result += int(num)
        return result


if __name__ == '__main__':
    print(Solution().countLargestGroup(n=13))
    print(Solution().countLargestGroup(n=2))
    print(Solution().countLargestGroup(n=15))
    print(Solution().countLargestGroup(n=24))
