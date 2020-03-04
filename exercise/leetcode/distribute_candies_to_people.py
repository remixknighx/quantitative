# -*- coding: utf-8 -*-
"""
1103. Distribute Candies to People
@link https://leetcode.com/problems/distribute-candies-to-people/
"""
from typing import List


class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        result = [0] * num_people
        count = 1
        to_break = False
        while True:
            for i in range(0, num_people):
                if count > candies:
                    result[i] += candies
                    to_break = True
                    break
                result[i] += count
                candies -= count
                count += 1
            if to_break:
                break
        return result


if __name__ == '__main__':
    candies = 10
    num_people = 3
    print(Solution().distributeCandies(candies=candies, num_people=num_people))
