"""
142. Linked List Cycle II
https://leetcode.com/problems/linked-list-cycle-ii/description/
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

    Floyd's Cycle Detection
    https://www.youtube.com/watch?v=wjYnzkAhcNk&ab_channel=NeetCode
    https://www.programmercarl.com/0142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.html
    """
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while True:
            if fast is None or fast.next is None or fast.next.next is None:
                return None
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        slow = head
        pos = 0
        while True:
            if fast == slow:
                return slow
            slow = slow.next
            fast = fast.next
            pos += 1
