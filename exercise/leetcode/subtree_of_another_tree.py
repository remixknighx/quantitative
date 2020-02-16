# -*- coding: utf-8 -*-
"""
985. Sum of Even Numbers After Queries
@link https://leetcode.com/problems/sum-of-even-numbers-after-queries/
"""
from tree_node import TreeNode


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        res_s = []
        self.helper_pstOrder(s, res_s)
        # print(res_s)
        res_t = []
        self.helper_pstOrder(t, res_t)
        # print(res_t)
        return ''.join(res_t) in ''.join(res_s)

    def helper_preOrder(self, cur, res):
        if not cur:
            res.append('(*)')
            return
        res.append('(' + str(cur.val) + ')')
        self.helper_preOrder(cur.left, res)
        self.helper_preOrder(cur.right, res)
        return

    def helper_inOrder(self, cur, res):
        if not cur:
            res.append('(*)')
            return
        self.helper_inOrder(cur.left, res)
        res.append('(' + str(cur.val) + ')')
        self.helper_inOrder(cur.right, res)
        return

    def helper_pstOrder(self, cur, res):
        if not cur:
            res.append('(*)')
            return
        self.helper_pstOrder(cur.left, res)
        self.helper_pstOrder(cur.right, res)
        res.append('(' + str(cur.val) + ')')
        return


if __name__ == '__main__':
    s = TreeNode(3)
    s.left = TreeNode(4)
    s.right = TreeNode(5)
    s.left.left = TreeNode(1)
    s.right.left = TreeNode(2)

    t = TreeNode(3)
    t.left = TreeNode(1)
    t.right = TreeNode(2)

    # s = TreeNode(1)
    # s.left = TreeNode(1)
    #
    # t = TreeNode(1)

    print(Solution().isSubtree(s=s, t=t))

    # sub_list = ["1", "2", "3"]
    # list_total = ["5", "4", "6", "1", "2", "3", "5"]
    # print('*'.join(sub_list))
