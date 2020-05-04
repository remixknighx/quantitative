# -*- coding: utf-8 -*-
"""
866. Prime Palindrome
@link https://leetcode.com/problems/prime-palindrome/
"""


class Solution:
    def primePalindrome(self, N: int) -> int:
        def isPrime(x):
            if x < 2 or x % 2 == 0:
                return x == 2
            for i in range(3, int(x ** 0.5) + 1, 2):
                if x % i == 0:
                    return False
            return True

        if N <= 2:
            return 2

        if 8 <= N <= 11:
            return 11
        for x in range(int(10 ** (len(str(N)) / 2)), 10 ** 5):
            y = int(str(x) + str(x)[-2::-1])
            if y >= N and isPrime(y):
                return y


if __name__ == '__main__':
    print(Solution().primePalindrome(N=1))
    print(Solution().primePalindrome(N=2))


