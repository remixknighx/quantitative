# -*- coding: utf-8 -*-
"""
987. Vertical Order Traversal of a Binary Tree
@link https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
"""
from tree_node import TreeNode
from typing import List


class Solution:

    def __init__(self):
        self.node_dict = {}

    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        self.set_node_dict(node=root, pos=[0, 0])
        pos_x_list = list(self.node_dict.keys())
        pos_x_list.sort()
        result = []
        for pos_x in pos_x_list:
            pos_y_list = list(self.node_dict[pos_x].keys())
            pos_y_list.sort(reverse=True)
            single_result = []
            for pos_y in pos_y_list:
                value_list = self.node_dict[pos_x][pos_y]
                for val in value_list:
                    single_result.append(val)
            result.append(single_result)
        return result

    def set_node_dict(self, node: TreeNode, pos: List[int]):
        if self.node_dict.get(pos[0]) is None:
            self.node_dict.setdefault(pos[0], {pos[1]: [node.val]})
        else:
            exist_node = dict(self.node_dict.get(pos[0]))
            if exist_node.get(pos[1]) is None:
                exist_node.setdefault(pos[1], [node.val])
            else:
                exist_node_value = list(exist_node[pos[1]])
                exist_node_value.append(node.val)
                exist_node_value.sort()
                exist_node[pos[1]] = exist_node_value
            self.node_dict[pos[0]] = exist_node

        if node.left is not None:
            self.set_node_dict(node=node.left, pos=[pos[0] - 1, pos[1] - 1])
        if node.right is not None:
            self.set_node_dict(node=node.right, pos=[pos[0] + 1, pos[1] - 1])


if __name__ == '__main__':
    # root1 = TreeNode(3)
    # root1.left = TreeNode(9)
    # root1.right = TreeNode(20)
    # root1.right.left = TreeNode(15)
    # root1.right.right = TreeNode(7)
    # print(Solution().verticalTraversal(root=root1))
    #
    # root2 = TreeNode(1)
    # root2.left = TreeNode(2)
    # root2.right = TreeNode(3)
    # root2.left.left = TreeNode(4)
    # root2.left.right = TreeNode(5)
    # root2.right.left = TreeNode(6)
    # root2.right.right = TreeNode(7)
    # print(Solution().verticalTraversal(root=root2))

    root3 = TreeNode(0)
    root3.left = TreeNode(8)
    root3.right = TreeNode(1)
    root3.right.left = TreeNode(3)
    root3.right.right = TreeNode(2)
    root3.right.left.right = TreeNode(4)
    root3.right.left.right.right = TreeNode(7)
    root3.right.right.left = TreeNode(5)
    root3.right.right.left.left = TreeNode(6)
    print(Solution().verticalTraversal(root=root3))

    # test_dict = {-1: 3, -2: 4}
    # sort_test_dict = list(test_dict.keys())
    # sort_test_dict.sort()
    # print(sort_test_dict)

