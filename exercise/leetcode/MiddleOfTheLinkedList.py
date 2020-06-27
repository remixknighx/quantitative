# -*- coding: utf-8 -*-
"""
876. Middle of the Linked List
@link https://leetcode.com/problems/middle-of-the-linked-list/
"""
from tree_node import ListNode


class Solution:
    # 快慢指针法查找中间节点
    def middleNode(self, head: ListNode) -> ListNode:
        fastPoint = head
        slowPoint = head
        while fastPoint is not None and fastPoint.next is not None:
            fastPoint = fastPoint.next.next
            slowPoint = slowPoint.next
        return slowPoint


if __name__ == '__main__':
    head = ListNode(val=1)
    head.next = ListNode(val=2)
    head.next.next = ListNode(val=3)
    head.next.next.next = ListNode(val=4)
    head.next.next.next.next = ListNode(val=5)
    head.next.next.next.next.next = ListNode(val=6)
    print(Solution().middleNode(head=head).val)
