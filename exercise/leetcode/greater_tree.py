"""
538.Convert BST to Greater Tree
@link https://leetcode.com/problems/convert-bst-to-greater-tree/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    cur_sum: int = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.travel(root)
        return root

    def travel(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        if root.right:
            self.travel(root.right)
        self.cur_sum += root.val
        root.val = self.cur_sum
        if root.left:
            self.travel(root.left)


if __name__ == '__main__':
    node_1 = TreeNode(5)
    node_2 = TreeNode(2)
    node_3 = TreeNode(13)
    node_1.left = node_2
    node_1.right = node_3
    print(Solution().convertBST(node_1))

