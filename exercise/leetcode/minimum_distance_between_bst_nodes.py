# -*- coding: utf-8 -*-
"""
783. Minimum Distance Between BST Nodes
@link https://leetcode.com/problems/minimum-distance-between-bst-nodes/
"""
from tree_node import TreeNode
import sys


class Solution:

    def minDiffInBST(self, root: TreeNode) -> int:
        self.min = float('inf')
        self.prev = None
        self.helper(root)
        return self.min

    def helper(self, node):
        if not node:
            return

        self.helper(node.left)

        if self.prev:
            self.min = min(self.min, abs(node.val - self.prev.val))

        self.prev = node
        self.helper(node.right)


if __name__ == '__main__':
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(6)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    print(Solution().minDiffInBST(root=root))
