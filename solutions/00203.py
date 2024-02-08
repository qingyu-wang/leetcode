"""
203. Remove Linked List Elements
https://leetcode.com/problems/remove-linked-list-elements/description/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        head_temp = ListNode(val="temp", next=head)

        # Check following nodes
        curr_node = head_temp
        while curr_node is not None and curr_node.next is not None:
            if curr_node.next.val == val:
                curr_node.next = curr_node.next.next
            else:
                curr_node = curr_node.next

        head = head_temp.next
        return head


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Check head
        while head is not None and head.val == val:
            head = head.next

        # Check following nodes
        curr_node = head
        while curr_node is not None:
            next_node = curr_node.next
            if next_node is not None and next_node.val == val:
                curr_node.next = next_node.next
            else:
                curr_node = next_node

        return head
