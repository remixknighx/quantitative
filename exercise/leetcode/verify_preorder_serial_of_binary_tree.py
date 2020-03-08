# -*- coding: utf-8 -*-
"""
331. Verify Preorder Serialization of a Binary Tree
@link https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
"""
from collections import deque


class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        preorder = deque(preorder.split(','))

        def verify(p):
            if not p:
                return False

            val = preorder.popleft()
            if val != "#":
                # 遍历左右两个节点
                return verify(p) and verify(p)

            return True

        return verify(preorder) and len(preorder) == 0


if __name__ == '__main__':
    print(Solution().isValidSerialization(preorder='9,3,4,#,#,1,#,#,2,#,6,#,#'))

    print(Solution().isValidSerialization(preorder='9,#,#,1'))
