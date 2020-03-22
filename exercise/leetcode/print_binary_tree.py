# -*- coding: utf-8 -*-
"""
655. Print Binary Tree
@link https://leetcode.com/problems/print-binary-tree/
"""
from tree_node import TreeNode
from typing import List


class Solution:
    # get the height of the tree with values stored in dictionary as levelorder
    def computeh(self, root):
        if not root:
            return 0
        return 1 + max(self.computeh(root.left), self.computeh(root.right))

    # updating res to give result using dfs
    def dfs(self, root, res, start, end, l):
        if root is None:
            return
        mid = (start + end) // 2
        res[l][mid] = str(root.val)  # update value
        if root.left:
            self.dfs(root.left, res, start, mid - 1, l + 1)
        if root.right:
            self.dfs(root.right, res, mid + 1, end, l + 1)

    def printTree(self, root: TreeNode) -> List[List[str]]:
        if root is None:
            return
        height = self.computeh(root)

        n = 2 ** height - 1  # column
        res = [["" for _ in range(n)] for _ in range(height)]
        self.dfs(root, res, 0, n, 0)

        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(4)
    print(Solution().printTree(root=root))
