# -*- coding: utf-8 -*-
"""
98. Validate Binary Search Tree
@link https://leetcode.com/problems/validate-binary-search-tree/
"""
from tree_node import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.check(root=root,  min=-float('inf'),  max=float('inf'))

    def check(self, root: TreeNode, min, max):
        if not root:
            return True

        if min >= root.val or max <= root.val:
            return False

        return self.check(root.left, min, root.val) and self.check(root.right, root.val, max)

    # def isValidBST(self, root: TreeNode) -> bool:
    #
    #     if not root: return True
    #
    #     left_result = self.isValidLeft(root.val, root.left)
    #     right_result = self.isValidRight(root.val, root.right)
    #
    #     if left_result is False or right_result is False:
    #         return False
    #     else:
    #         return self.isValidBST(root.right) and self.isValidBST(root.left)
    #
    # def isValidRight(self, val, right_node: TreeNode) -> bool:
    #     if right_node is None:
    #         return True
    #
    #     if val >= right_node.val:
    #         return False
    #
    #     return self.isValidRight(val=val, right_node=right_node.right) and self.isValidRight(val=val, right_node=right_node.left)
    #
    # def isValidLeft(self, val, left_node: TreeNode) -> bool:
    #     if left_node is None:
    #         return True
    #
    #     if val <= left_node.val:
    #         return False
    #
    #     return self.isValidLeft(val=val, left_node=left_node.right) and self.isValidLeft(val=val, left_node=left_node.left)


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    # root.left.left = TreeNode(0)
    # root.left.right = TreeNode(2)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print(Solution().isValidBST(root=root))

"""
   3
 1   5
0 2 4 6
"""