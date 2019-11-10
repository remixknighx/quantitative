# -*- coding: utf-8 -*-
"""
543. Diameter of Binary Tree
@link https://leetcode.com/problems/diameter-of-binary-tree/
"""
from tree_node import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def get_root_length(root):
            if root:
                return 1 + max(get_root_length(root.left), get_root_length(root.right))
            return 0

        def compute_length(root):
            if root:
                return max(get_root_length(root.left) + get_root_length(root.right),
                           compute_length(root.left), compute_length(root.right))
            return 0

        if root:
            return compute_length(root)
        return 0


if __name__ == '__main__':
    tree = TreeNode(x=1)
    tree.left = TreeNode(x=2)
    tree.right = TreeNode(x=3)
    tree.left.left = TreeNode(x=4)
    tree.left.right = TreeNode(x=5)
    print(Solution().diameterOfBinaryTree(root=tree))