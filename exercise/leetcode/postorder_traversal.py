# -*- coding: utf-8 -*-
"""
590. N-ary Tree Postorder Traversal
@link https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""
from tree_node import Node
from typing import List


class Solution:
    def __init__(self):
        self.result = []

    def postorder(self, root: Node) -> List[int]:
        if root is not None:
            if root.children is None:
                self.result.append(root.val)
                return
        else:
            return

        for node in root.children:
            self.postorder(root=node)

        self.result.append(root.val)
        return self.result


if __name__ == '__main__':
    root = Node(val=1, children=[Node(val=3, children=[Node(val=5, children=None), Node(val=6, children=None)]),
                                 Node(val=2, children=None), Node(val=4, children=None)])
    print(Solution().postorder(root=root))