# -*- coding: utf-8 -*-
"""
558. Quad Tree Intersection
@link https://leetcode.com/problems/quad-tree-intersection/
"""


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def intersect(self, quadTree1: Node, quadTree2: Node) -> Node:
        if quadTree1.isLeaf:
            return quadTree1.val and quadTree1 or quadTree2
        elif quadTree2.isLeaf:
            return quadTree2.val and quadTree2 or quadTree1
        else:
            tl: Node = self.intersect(quadTree1=quadTree1.topLeft, quadTree2=quadTree2.topLeft)
            tr: Node = self.intersect(quadTree1=quadTree1.topRight, quadTree2=quadTree2.topRight)
            bl: Node = self.intersect(quadTree1=quadTree1.bottomLeft, quadTree2=quadTree2.bottomLeft)
            br: Node = self.intersect(quadTree1=quadTree1.bottomRight, quadTree2=quadTree2.bottomRight)

            if tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and tl.val == tr.val == bl.val == br.val:
                return Node(val=tl.val, isLeaf=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)
            else:
                return Node(val=False, isLeaf=False, topLeft=tl, topRight=tr, bottomLeft=bl, bottomRight=br)


if __name__ == '__main__':
    tree_a: Node = Node(isLeaf=False, val=None,
                        topLeft=Node(isLeaf=True, val=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None),
                        topRight=Node(isLeaf=True, val=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None),
                        bottomLeft=Node(isLeaf=True, val=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None),
                        bottomRight=Node(isLeaf=True, val=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None))
    tree_b: Node = Node(isLeaf=False, val=None,
                        topLeft=Node(isLeaf=True, val=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None),
                        topRight=Node(isLeaf=False, val=None,
                                      topLeft=Node(isLeaf=True, val=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None),
                                      topRight=Node(isLeaf=True, val=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None),
                                      bottomLeft=Node(isLeaf=True, val=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None),
                                      bottomRight=Node(isLeaf=True, val=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None)),
                        bottomLeft=Node(isLeaf=True, val=True, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None),
                        bottomRight=Node(isLeaf=True, val=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None))
    result: Node = Solution().intersect(quadTree1=tree_a, quadTree2=tree_b)

