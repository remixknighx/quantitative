# -*- coding: utf-8 -*-
"""
1022. Sum of Root To Leaf Binary Numbers
@link https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
"""
from tree_node import TreeNode


class Solution:

    def __init__(self):
        self.binary_list = []

    def sumRootToLeaf(self, root: TreeNode) -> int:
        if root is None:
            return 0

        self.add_leaf(root, '')

        result = 0
        for bin_str in self.binary_list:
            result += int(bin_str, 2)

        return result

    def add_leaf(self, node: TreeNode, bin_str: str):
        if node.left is None and node.right is None:
            bin_str += str(node.val)
            self.binary_list.append(bin_str)
            return
        else:
            bin_str += str(node.val)

        if node.left is not None:
            self.add_leaf(node.left, bin_str)
        if node.right is not None:
            self.add_leaf(node.right, bin_str)


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(1)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(1)
    print(Solution().sumRootToLeaf(root=root))

    print(int('011', 2))
