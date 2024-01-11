"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Fast and Slow Pointers
        """
        temp = ListNode(val="temp", next=head)
        fast = slow = temp

        for _ in range(n):
            fast = fast.next

        while fast.next is not None:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        head = temp.next
        return head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(val="temp", next=head)
        curr = temp
        delete_prev = curr
        delete_node = curr.next
        delete_idx = 0
        while curr.next is not None:
            if delete_idx == n:
                delete_prev = delete_prev.next
                delete_node = delete_node.next
            if delete_idx < n:
                delete_idx += 1
            curr = curr.next
        if delete_prev is not None and delete_node is not None:
            delete_prev.next = delete_node.next
        head = temp.next
        return head
