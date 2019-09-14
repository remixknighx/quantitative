# -*- coding: utf-8 -*-
"""
637. Average of Levels in Binary Tree
@link https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""
from typing import List
from tree_node import TreeNode


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        treenode_list = []
        treenode_list.append(root)
        while len(treenode_list) != 0:
            sum: float = 0
            num = len(treenode_list)
            for idx in range(0, num):
                node = treenode_list.pop(0)
                sum += node.val
                if node.left is not None: treenode_list.append(node.left)
                if node.right is not None: treenode_list.append(node.right)
            result.append(sum/num)
        return result


if __name__ == '__main__':
    root = TreeNode(x=3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    print(Solution().averageOfLevels(root=root))
