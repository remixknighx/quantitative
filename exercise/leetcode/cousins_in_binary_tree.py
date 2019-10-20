# -*- coding: utf-8 -*-
"""
993. Cousins in Binary Tree
@link https://leetcode.com/problems/cousins-in-binary-tree/
"""
from tree_node import TreeNode
from collections import deque


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        queue = deque([root])
        parents = []
        while queue:
            temp = deque()
            while queue:
                node = queue.popleft()
                for child in (node.left, node.right):
                    if child is None:
                        continue
                    temp.append(child)
                    if child.val in (x, y):
                        parents.append(node.val)
            if parents:
                if len(parents) == 2:
                    return parents[0] != parents[1]
                else:
                    return False
            queue = temp


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print(Solution().isCousins(root=root, x=4, y=3))
