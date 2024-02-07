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

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

