# -*- coding: utf-8 -*-
"""
1114. Print in Order
"""
from threading import Semaphore


class Foo:
    def __init__(self):
        self.two = Semaphore(0)
        self.three = Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        printFirst()
        self.two.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.two:
            printSecond()
            self.three.release()

    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.three:
            printThird()