# -*- coding: utf-8 -*-
"""
706. Design HashMap
@link https://leetcode.com/problems/design-hashmap/
"""


class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None


class MyHashMap:

    def __init__(self):
        self.n = 10000
        self.arr = [None] * self.n

    def put(self, key: int, value: int) -> None:
        idx = key % self.n

        if self.arr[idx] is None:
            self.arr[idx] = ListNode(key, value)
        else:
            head = self.arr[idx]
            tail = None
            while head:
                if head.pair[0] == key:
                    head.pair = (key, value)
                    return
                if not head.next:
                    tail = head
                # iterate to next
                head = head.next
            # add new member
            tail.next = ListNode(key, value)

    def get(self, key: int) -> int:
        idx = key % self.n
        head = self.arr[idx]
        while head:
            if head.pair[0] == key:
                return head.pair[1]
            head = head.next

        return -1

    def remove(self, key: int) -> None:
        idx = key % self.n

        head = self.arr[idx]
        prev = None
        while head:
            if head.pair[0] == key:
                if prev is None:
                    # first one case
                    self.arr[idx] = head.next
                    return
                else:
                    # none first one case
                    prev.next = head.next
                    return

            # iterate next
            prev = head
            head = head.next

