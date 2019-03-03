# -*- coding: utf-8 -*-
"""
653. Two Sum IV - Input is a BST
@link https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        tree_set = set()
        queue = list()
        queue.append(root)
        while len(queue) != 0:
            node = queue.pop()
            if node is not None:
                if (k - node.val) in tree_set:
                    return True
                tree_set.add(node.val)
                queue.append(node.right)
                queue.append(node.left)
        return False


if __name__ == '__main__':
    solution = Solution()
    tree = TreeNode(5)
    tree.left = TreeNode(3)
    tree.right = TreeNode(6)
    tree.left.left = TreeNode(2)
    tree.left.right = TreeNode(4)
    tree.right.right = TreeNode(7)
    print(solution.findTarget(root=tree, k=9))

