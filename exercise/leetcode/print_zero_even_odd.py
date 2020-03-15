"""
1116. Print Zero Even Odd
@link https://leetcode.com/problems/print-zero-even-odd/
"""
from threading import Lock


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.zero_lock = Lock()
        self.even_lock = Lock()
        self.odd_lock = Lock()

        # Initially, even and odd need to wait for 0, so we acquire these locks to prevent
        # execution.
        self.even_lock.acquire()
        self.odd_lock.acquire()

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.zero_lock.acquire()
            printNumber(0)
            if i % 2 == 0:
                self.odd_lock.release()
            else:
                self.even_lock.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n + 1):
            if i % 2 == 0:
                self.even_lock.acquire()
                printNumber(i)
                self.zero_lock.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            if i % 2 == 1:
                self.odd_lock.acquire()
                printNumber(i)
                self.zero_lock.release()


if __name__ == '__main__':
    zeroEvenOdd = ZeroEvenOdd(n=2)
    zeroEvenOdd.zero(printNumber=print)
