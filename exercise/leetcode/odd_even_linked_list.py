# -*- coding: utf-8 -*-
"""
328. Odd Even Linked List
@link https://leetcode.com/problems/odd-even-linked-list/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return

        odd = head
        even = head.next

        ohead = head
        ehead = head.next

        while even and even.next:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = ehead

        return ohead


if __name__ == '__main__':
    head = ListNode(2)
    head.next = ListNode(1)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(5)
    head.next.next.next.next = ListNode(6)
    head.next.next.next.next.next = ListNode(4)
    head.next.next.next.next.next.next = ListNode(7)
    result = Solution().oddEvenList(head=head)
    print(result)
