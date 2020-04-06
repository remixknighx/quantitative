# -*- coding: utf-8 -*-
"""
1361. Validate Binary Tree Nodes
@link https://leetcode.com/problems/validate-binary-tree-nodes/
"""
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.count = n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.count -= 1
            self.parent[px] = py


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        inDegree = [0] * n

        uf = UnionFind(n)
        for parent, nodes in enumerate(zip(leftChild, rightChild)):
            l, r = nodes
            if l != -1:
                inDegree[l] += 1
                uf.union(l, parent)

            if r != -1:
                inDegree[r] += 1
                uf.union(r, parent)

        return sum(inDegree) == n - 1 and uf.count == 1


if __name__ == '__main__':
    print(Solution().validateBinaryTreeNodes(n=4, leftChild=[1, -1, 3, -1], rightChild=[2, -1, -1, -1]))
