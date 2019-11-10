# -*- coding: utf-8 -*-
"""
1154. Day of the Year
@link https://leetcode.com/problems/day-of-the-year/
"""


class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day, leap = self.leap_year(date=date)
        feb = 28
        if leap:
            feb = 29
        full_month = [0, 31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return sum(full_month[:month]) + day

    def leap_year(self, date):
        year, month, day = [int(item) for item in date.split('-')]
        if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
            return (year, month, day, True)
        else:
            return (year, month, day, False)


if __name__ == '__main__':
    print(Solution().dayOfYear(date="2019-01-09"))
    print(Solution().dayOfYear(date="2003-03-01"))
    print(Solution().dayOfYear(date="2004-03-01"))