# -*- coding: utf-8 -*-
"""
933. Number of Recent Calls
@link https://leetcode.com/problems/number-of-recent-calls/
"""
import collections


class RecentCounter:

    def __init__(self):
        self.p = collections.deque()

    def ping(self, t):
        self.p.append(t)
        while self.p[0] < t - 3000:
            self.p.popleft()
        return len(self.p)


if __name__ == '__main__':
    obj = RecentCounter()
    obj.ping()