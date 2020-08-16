# -*- coding: utf-8 -*-
"""
1518. Water Bottles
@link https://leetcode.com/problems/water-bottles/
"""


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        result = numBottles
        emptyBottles = numBottles
        while emptyBottles >= numExchange:
            drinkBottles = int(emptyBottles / numExchange)
            result += drinkBottles
            emptyBottles = drinkBottles + int(emptyBottles % numExchange)
        return result


if __name__ == '__main__':
    # print(Solution().numWaterBottles(numBottles=9, numExchange=3))
    # print(Solution().numWaterBottles(numBottles=15, numExchange=4))
    print(Solution().numWaterBottles(numBottles=5, numExchange=5))
    # print(Solution().numWaterBottles(numBottles=2, numExchange=3))
