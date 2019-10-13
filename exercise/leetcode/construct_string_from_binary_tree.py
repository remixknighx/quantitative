"""
606. Construct String from Binary Tree
@link https://leetcode.com/problems/construct-string-from-binary-tree/
"""
# -*- coding: utf-8 -*-
from tree_node import TreeNode


class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t:
            self.s = str(t.val)

            def helper(t):
                if not t.left and not t.right:
                    return
                if t.left:
                    self.s += '(' + str(t.left.val)
                    helper(t.left)
                    self.s += ')'
                else:
                    self.s += '()'
                if t.right:
                    self.s += '(' + str(t.right.val)
                    helper(t.right)
                    self.s += ')'
            helper(t)
            return self.s
        else:
            return ''


if __name__ == '__main__':
    root = TreeNode(x=1)
    root.left = TreeNode(x=2)
    root.right = TreeNode(x=3)
    root.left.left = TreeNode(x=4)
    print(Solution().tree2str(t=root))
