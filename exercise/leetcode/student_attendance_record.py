# -*- coding: utf-8 -*-
"""
551. Student Attendance Record I
@link https://leetcode.com/problems/student-attendance-record-i/
"""
import re


class Solution:
    def checkRecord(self, s: str) -> bool:
        return False if len(re.findall('A', s)) >= 2 or len(re.findall('L{3,}', s)) > 0 else True


if __name__ == '__main__':
    print(Solution().checkRecord(s='ALLL'))
