# -*- coding: utf-8 -*-
"""
703. Kth Largest Element in a Stream
@link https://leetcode.com/problems/kth-largest-element-in-a-stream/
"""
from typing import List
import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.pool = nums
        self.size = len(self.pool)
        self.k = k
        heapq.heapify(self.pool)
        while self.size > k:
            heapq.heappop(self.pool)
            self.size -= 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.size < self.k:
            heapq.heappush(self.pool, val)
            self.size += 1
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


if __name__ == '__main__':
    k = 3
    arr = [4, 5, 8, 2]
    obj = KthLargest(k=k, nums=arr)
    print(obj.add(3))
    print(obj.add(5))
    print(obj.add(10))
    print(obj.add(9))
    print(obj.add(4))
