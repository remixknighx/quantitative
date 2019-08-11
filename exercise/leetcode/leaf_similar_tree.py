# -*- coding: utf-8 -*-
"""
872. Leaf-Similar Trees
@link https://leetcode.com/problems/leaf-similar-trees/
"""
from tree_node import TreeNode
from typing import List


class Solution:
    def __init__(self):
        self.root1_leaf = []
        self.root2_leaf = []

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.add_leaf(root=root1, root_leaf=self.root1_leaf)
        self.add_leaf(root=root2, root_leaf=self.root2_leaf)
        if len(self.root1_leaf) == len(self.root2_leaf):
            for idx in range(0, len(self.root1_leaf)):
                if self.root1_leaf[idx] != self.root2_leaf[idx]:
                    return False
            return True
        else:
            return False

    def add_leaf(self, root: TreeNode, root_leaf: List):
        if root.left is None and root.right is None:
            root_leaf.append(root.val)
            return
        if root.left is not None:
            self.add_leaf(root.left, root_leaf=root_leaf)
        if root.right is not None:
            self.add_leaf(root.right, root_leaf=root_leaf)


if __name__ == '__main__':
    root1: TreeNode = TreeNode(1)
    root1.left = TreeNode(2)
    # root1: TreeNode = TreeNode(3)
    # root1.left = TreeNode(5)
    # root1.right = TreeNode(1)
    # root1.left.left = TreeNode(6)
    # root1.left.right = TreeNode(2)
    # root1.left.right.left = TreeNode(7)
    # root1.left.right.right = TreeNode(4)
    # root1.right.left = TreeNode(9)
    # root1.right.right = TreeNode(8)

    root2: TreeNode = TreeNode(2)
    root2.left = TreeNode(2)
    # root2.right = TreeNode(1)
    # root2.left.left = TreeNode(6)
    # root2.left.right = TreeNode(2)
    # root2.left.right.left = TreeNode(7)
    # root2.left.right.right = TreeNode(4)
    # root2.right.left = TreeNode(9)
    # root2.right.right = TreeNode(8)

    print(Solution().leafSimilar(root1=root1, root2=root2))

