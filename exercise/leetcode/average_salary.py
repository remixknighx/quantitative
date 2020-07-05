# -*- coding: utf-8 -*-
"""
1491. Average Salary Excluding the Minimum and Maximum Salary
@link https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
"""
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        return sum([i for i in salary if i != max(salary) and i != min(salary)]) / (len(salary) - 2)


if __name__ == '__main__':
    print(Solution().average(salary=[4000, 3000, 1000, 2000]))
    print(Solution().average(salary=[1000, 2000, 3000]))
    print(Solution().average(salary=[6000, 5000, 4000, 3000, 2000, 1000]))
    print(Solution().average(salary=[8000, 9000, 2000, 3000, 6000, 1000]))
