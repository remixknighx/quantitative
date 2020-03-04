# -*- coding: utf-8 -*-
"""
1184. Distance Between Bus Stops
@link https://leetcode.com/problems/distance-between-bus-stops/
"""
from typing import List


class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        sum_distance = sum(distance)
        if start < destination:
            clockwise_distance = self.calculate_distance(distance=distance, start=start, destination=destination)
        else:
            clockwise_distance = self.calculate_distance(distance=distance, start=destination, destination=start)
        return min(clockwise_distance, sum_distance - clockwise_distance)

    def calculate_distance(self, distance: List[int], start: int, destination: int) -> int:
        result_distance = 0
        for i in range(start, destination):
            result_distance += distance[i]
        return result_distance


if __name__ == '__main__':
    distance = [7,10,1,12,11,14,5,0]
    start = 7
    destination = 2
    print(Solution().distanceBetweenBusStops(distance=distance, start=start, destination=destination))
