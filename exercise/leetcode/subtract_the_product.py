# -*- coding: utf-8 -*-
"""
1281. Subtract the Product and Sum of Digits of an Integer
@link https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product: int = 1
        sum: int = 0
        while n//10 != 0:
            product *= n % 10
            sum += n % 10
            n //= 10
        product *= n
        sum += n
        return product - sum


if __name__ == '__main__':
    print(Solution().subtractProductAndSum(n=234))
    print(Solution().subtractProductAndSum(n=4421))
