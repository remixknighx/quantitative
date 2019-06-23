# -*- coding: utf-8 -*-
"""
938. Range Sum of BST
@link https://leetcode.com/problems/range-sum-of-bst/
"""

from tree_node import TreeNode


class Solution:

    def __init__(self):
        self.res = 0

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if not root:
            return

        if root.val < L:
            self.rangeSumBST(root=root.right, L=L, R=R)
        elif root.val > R:
            self.rangeSumBST(root=root.left, L=L, R=R)
        else:
            self.res += root.val
            self.rangeSumBST(root=root.left, L=L, R=R)
            self.rangeSumBST(root=root.right, L=L, R=R)

        return  self.res


if __name__ == '__main__':
    root: TreeNode = TreeNode(10)
    root.left: TreeNode = TreeNode(5)
    root.right: TreeNode = TreeNode(15)
    root.left.left: TreeNode = TreeNode(3)
    root.left.right: TreeNode = TreeNode(7)
    root.right.right: TreeNode = TreeNode(18)
    print(Solution().rangeSumBST(root=root, L=7, R=15))

