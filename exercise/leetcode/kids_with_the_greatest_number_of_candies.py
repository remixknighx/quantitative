# -*- coding: utf-8 -*-
"""
1431. Kids With the Greatest Number of Candies
@link https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/
"""
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)
        result = []
        for candy in candies:
            if candy + extraCandies >= max_candy:
                result.append(True)
            else:
                result.append(False)
        return result


if __name__ == '__main__':
    print(Solution().kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3))
    print(Solution().kidsWithCandies(candies=[4, 2, 1, 1, 2], extraCandies=1))
    print(Solution().kidsWithCandies(candies=[12, 1, 12], extraCandies=10))
