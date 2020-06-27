class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

