# -*- coding: utf-8 -*-
import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 0:
            return False
        sum = 0
        SQRT = (int)(math.sqrt(num))
        for n in range(1, SQRT + 1):
            if num % n == 0:
                sum += n + num // n

        sum -= num  # Handling 1 * num scenario

        if num == SQRT ** 2:
            sum -= SQRT  # Handling 5*5 = 25 . We are adding 5 two times.

        return True if sum == num else False


if __name__ == '__main__':
    num: int = 28
    solution = Solution()
    print(solution.checkPerfectNumber(num))
