# -*- coding: utf-8 -*-
"""
1436. Destination City
@link https://leetcode.com/problems/destination-city/
"""
from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        src_city = []
        dest_city = []
        for path in paths:
            if path[0] in dest_city:
                dest_city.remove(path[0])
            else:
                src_city.append(path[0])
            if path[1] in src_city:
                src_city.remove(path[1])
            else:
                dest_city.append(path[1])
        return dest_city[0]


if __name__ == '__main__':
    print(Solution().destCity(paths=[["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
    print(Solution().destCity(paths=[["B", "C"], ["D", "B"], ["C", "A"]]))
    print(Solution().destCity(paths=[["A", "Z"]]))
