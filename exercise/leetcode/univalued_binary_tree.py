"""
965. Univalued Binary Tree
@link https://leetcode.com/problems/univalued-binary-tree/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        return self.doIsUnivalTree(node=root, root_val=root.val)

    def doIsUnivalTree(self, node: TreeNode, root_val: int) -> bool:
        if node is None:
            return True
        if node.val == root_val:
            return self.doIsUnivalTree(node.left, root_val) and self.doIsUnivalTree(node.right, root_val)
        else:
            return False


if __name__ == '__main__':
    root = TreeNode(4)
    node1 = TreeNode(1)
    node2 = TreeNode(1)
    root.left = node1
    root.right = node2
    node3 = TreeNode(1)
    node4 = TreeNode(1)
    node1.left = node3
    node1.right = node4
    node5 = TreeNode(1)
    node2.right = node5

    print(Solution().isUnivalTree(root))

