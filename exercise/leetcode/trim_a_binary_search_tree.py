# -*- coding: utf-8 -*-
"""
669. Trim a Binary Search Tree
@link https://leetcode.com/problems/trim-a-binary-search-tree/
"""
from tree_node import TreeNode


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def trim(node):
            if not node:
                return
            if node.val < L:
                return trim(node.right)
            elif node.val > R:
                return trim(node.left)
            else:
                node.left, node.right = trim(node.left), trim(node.right)
                return node
        return trim(root)


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(0)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    root.left.left = TreeNode(1)
    trim_node = Solution().trimBST(root=root, L=1, R=3)
    print(trim_node)
