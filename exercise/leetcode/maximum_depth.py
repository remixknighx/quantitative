"""
559. Maximum Depth of N-ary Tree
@link https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
"""


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: Node) -> int:
        if not root:
            return 0
        else:
            depth: int = 0
            for child in root.children:
                tem = self.maxDepth(child)
                if tem > depth:
                    depth = tem
            return depth + 1


if __name__ == '__main__':
    root_2 = Node(val=2, children=[])
    root_4 = Node(val=4, children=[])
    root_5 = Node(val=5, children=[])
    root_6 = Node(val=6, children=[])
    root_3 = Node(val=3, children={root_5, root_6})
    root = Node(val=1, children={root_3, root_2, root_4})
    print(Solution().maxDepth(root=root))


