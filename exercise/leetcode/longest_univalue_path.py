# -*- coding: utf-8 -*-

"""
687. Longest Univalue Path
@link https://leetcode.com/problems/longest-univalue-path/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.ans = 0

        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans


if __name__ == '__main__':
    node_1 = TreeNode(x=1)
    node_2 = TreeNode(x=4)
    node_3 = TreeNode(x=5)
    node_4 = TreeNode(x=4)
    node_5 = TreeNode(x=4)
    node_6 = TreeNode(x=5)
    node_1.left = node_2
    node_1.right = node_3
    node_2.left = node_4
    node_2.right = node_5
    node_3.right = node_6
    print(Solution().longestUnivaluePath(node_1))
