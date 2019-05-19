# -*- coding: utf-8 -*-
"""
671. Second Minimum Node In a Binary Tree
@link https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    second_min: int = -1
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.do_find_second_min(root)
        return self.second_min

    def do_find_second_min(self, root: TreeNode):
        if not root.left:
            return
        if root.left.val > root.val:
            if self.second_min == -1 or self.second_min > root.left.val:
                self.second_min = root.left.val

        if root.right.val > root.val:
            if self.second_min == -1 or self.second_min > root.right.val:
                self.second_min = root.right.val

        self.do_find_second_min(root.left)
        self.do_find_second_min(root.right)


if __name__ == '__main__':
    node_root = TreeNode(2)
    node_2 = TreeNode(2)
    node_3 = TreeNode(2)
    node_4 = TreeNode(2)
    node_5 = TreeNode(2)
    node_root.left = node_2
    node_root.right = node_3
    node_3.left = node_4
    node_3.right = node_5
    print(Solution().findSecondMinimumValue(node_root))

