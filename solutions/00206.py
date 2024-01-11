"""
206. Reverse Linked List
https://leetcode.com/problems/reverse-linked-list/description/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_new = None
        node_curr = head
        while node_curr is not None:
            if node_curr is not None:
                head_new = ListNode(val=node_curr.val, next=head_new)
            node_curr = node_curr.next
        return head_new