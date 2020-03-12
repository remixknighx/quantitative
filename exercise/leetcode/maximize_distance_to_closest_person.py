# -*- coding: utf-8 -*-
"""
849. Maximize Distance to Closest Person
@link https://leetcode.com/problems/maximize-distance-to-closest-person/
"""
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        seated_list = list()
        max_distance = 0
        first_seat = second_seat = -1
        for i in range(0, len(seats)):
            if seats[i] == 1:
                seated_list.append(i)
                if first_seat == -1:
                    first_seat = i
                else:
                    second_seat = first_seat
                    first_seat = i
                    max_distance = max(max_distance, first_seat - second_seat)

        return max(seated_list[0], len(seats) - 1 - seated_list[len(seated_list)-1], int(max_distance / 2))


if __name__ == '__main__':
    seats = [1,0,0,0]
    print(Solution().maxDistToClosest(seats=seats))
