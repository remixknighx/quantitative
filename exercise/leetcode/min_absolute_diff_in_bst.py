"""
530. Minimum Absolute Difference in BST
@link https://leetcode.com/problems/minimum-absolute-difference-in-bst/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        self.ans = 1e9
        self.prev = None

        def search(node):
            if node.left:
                search(node.left)
            if self.prev is not None:
                self.ans = min(self.ans, node.val - self.prev)
            self.prev = node.val
            if node.right:
                search(node.right)

        search(root)
        return self.ans


if __name__ == '__main__':
    node_1 = TreeNode(x=1)
    node_3 = TreeNode(x=3)
    node_2 = TreeNode(x=2)
    node_1.right = node_3
    node_3.left = node_2
    print(Solution().getMinimumDifference(node_1))
