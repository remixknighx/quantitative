# -*- coding: utf-8 -*-
"""
1185. Day of the Week
@link https://leetcode.com/problems/day-of-the-week/
"""


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        num_leap_years = (year - 1969) // 4  # 1972 is leap
        full_year_days = (year - 1971) * 365 + num_leap_years
        full_month_days = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]  # len is 13
        total_days = full_year_days + full_month_days[month] + day
        if ((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)) and month > 2:
            total_days += 1

        weekdays = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
        return weekdays[total_days % 7 - 1]


if __name__ == '__main__':
    print(Solution().dayOfTheWeek(day=31, month=8, year=2019))
    print(Solution().dayOfTheWeek(day=18, month=7, year=1999))