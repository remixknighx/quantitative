# -*- coding: utf-8 -*-
"""
1115. Print FooBar Alternately
@link https://leetcode.com/problems/print-foobar-alternately/
"""
from threading import Semaphore


class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Semaphore(1)
        self.bar_lock = Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()


if __name__ == '__main__':
    pool = Semaphore(0)
    pool.acquire()
    print("pool")
    pool.release()
