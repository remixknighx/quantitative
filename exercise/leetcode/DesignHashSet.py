# -*- coding: utf-8 -*-
"""
705. Design HashSet
@link https://leetcode.com/problems/design-hashset/
"""


class MyHashSet:

    def __init__(self):
        self.hashset = set()

    def add(self, key: int) -> None:
        self.hashset.add(key)

    def remove(self, key: int) -> None:
        try:
            self.hashset.remove(key)
        except:
            pass

    def contains(self, key: int) -> bool:
        return key in self.hashset
