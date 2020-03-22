# -*- coding: utf-8 -*-
"""
1352. Product of the Last K Numbers
@link https://leetcode.com/problems/product-of-the-last-k-numbers/
"""


class ProductOfNumbers:

    def __init__(self):
        self.products = []

    def add(self, num: int) -> None:
        if num == 0:
            self.products.clear()
        else:
            if len(self.products) == 0:
                self.products.append(num)
            else:
                self.products.append(num * self.products[len(self.products) - 1])

    def getProduct(self, k: int) -> int:
        if k > len(self.products):
            return 0
        elif k == len(self.products):
            return self.products[len(self.products) - 1]
        else:
            return int(self.products[len(self.products) - 1] / self.products[len(self.products) - k - 1])


if __name__ == '__main__':
    productOfNumbers = ProductOfNumbers()
    productOfNumbers.add(3)
    productOfNumbers.add(0)
    productOfNumbers.add(2)
    productOfNumbers.add(5)
    productOfNumbers.add(4)
    print(productOfNumbers.getProduct(2))
    print(productOfNumbers.getProduct(3))
    print(productOfNumbers.getProduct(4))
    productOfNumbers.add(8)
    print(productOfNumbers.getProduct(2))
