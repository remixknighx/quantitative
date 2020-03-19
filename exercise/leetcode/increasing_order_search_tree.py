# -*- coding: utf-8 -*-
"""
897. Increasing Order Search Tree
@link https://leetcode.com/problems/increasing-order-search-tree/
"""
from tree_node import TreeNode


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        node_queue = list()
        self.add_node_to_queue(node=root, node_queue=node_queue)
        node_queue.sort()

        result = TreeNode(node_queue.pop(0))

        self.construct_tree(root=result, node_queue=node_queue)

        return result

    def construct_tree(self, root: TreeNode, node_queue: deque):
        if node_queue:
            root.right = TreeNode(node_queue.pop(0))
            self.construct_tree(root.right, node_queue)
        else:
            return

    def add_node_to_queue(self, node: TreeNode, node_queue: deque):
        if node is not None:
            node_queue.append(node.val)

        if node.left is not None:
            self.add_node_to_queue(node.left, node_queue)
        if node.right is not None:
            self.add_node_to_queue(node.right, node_queue)


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    root.right = TreeNode(6)
    root.right.right = TreeNode(8)
    root.right.right.left = TreeNode(7)
    root.right.right.right = TreeNode(9)
    print(Solution().increasingBST(root=root))
