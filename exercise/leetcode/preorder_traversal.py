# -*- coding: utf-8 -*-
"""
589. N-ary Tree Preorder Traversal
@link https://leetcode.com/problems/n-ary-tree-preorder-traversal/
"""
from typing import List
from tree_node import Node


class Solution:
    def __init__(self):
        self.result = []

    def preorder(self, root: Node) -> List[int]:
        if root is None:
            return
        self.result.append(root.val)
        if root.children is not None:
            for node in root.children:
                self.preorder(node)
        return self.result


if __name__ == '__main__':
    root = Node(val=1, children=[Node(val=3, children=[Node(val=5, children=None), Node(val=6, children=None)]), Node(val=2, children=None), Node(val=4, children=None)])
    print(Solution().preorder(root=None))
