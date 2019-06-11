"""
563. Binary Tree Tilt
@link https://leetcode.com/problems/binary-tree-tilt/
"""

from tree_node import TreeNode


class Solution:
    def __init__(self):
        # To avoid local variable so no over-writting in every recursive cycle
        self.res = 0

    def findTilt(self, root: TreeNode) -> int:
        # base case
        if not root:
            return 0

        # tranverse to the last node
        if root:
            self.findTilt(root.left)
            self.findTilt(root.right)

        # add the difference between two sides
        self.res += abs((root.left.val if root.left else 0) - (root.right.val if root.right else 0))

        # calculate the new node value by sum all the three nodes
        root.val += (root.left.val if root.left else 0) + (root.right.val if root.right else 0)

        return self.res


if __name__ == '__main__':
    root = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    root.left = node2
    root.right = node3
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node2.left = node4
    node2.right = node5

    print(Solution().findTilt(root))


