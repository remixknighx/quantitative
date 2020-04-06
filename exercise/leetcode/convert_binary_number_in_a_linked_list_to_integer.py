# -*- coding: utf-8 -*-
"""
1290. Convert Binary Number in a Linked List to Integer
@link https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        head_list = ''
        while head is not None:
            head_list += str(head.val)
            head = head.next

        return int(head_list, 2)


if __name__ == '__main__':
    head = ListNode(0)
    head.next = ListNode(0)
    # head.next.next = ListNode(1)
    print(Solution().getDecimalValue(head=head))
