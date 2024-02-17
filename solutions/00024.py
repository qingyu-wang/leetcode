"""
24. Swap Nodes in Pairs
https://leetcode.com/problems/swap-nodes-in-pairs/description/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time:   O(n)
    Space:  O(1)
    """
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(val="temp", next=head)
        slow = temp
        fast = temp
        while True:
            if slow is None or slow.next is None or slow.next.next is None:
                break
            fast = slow.next.next
            slow.next.next = fast.next
            fast.next = slow.next
            slow.next = fast
            slow = slow.next.next
        return temp.next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(val="temp", next=head)
        curr = temp
        while curr.next is not None and curr.next.next is not None:
            nd_1 = curr.next
            nd_2 = curr.next.next
            nd_1.next = nd_2.next
            nd_2.next = nd_1
            curr.next = nd_2
            curr = curr.next.next
        head = temp.next
        return head
