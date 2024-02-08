"""
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/description/
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
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA = 0
        curr = headA
        while curr is not None:
            lenA += 1
            curr = curr.next

        lenB = 0
        curr = headB
        while curr is not None:
            lenB += 1
            curr = curr.next
        
        if lenA > lenB:
            curr = headA
        else:
            curr = headB
        for _ in range(abs(lenA-lenB)):
            curr = curr.next
        if lenA > lenB:
            headA = curr
        else:
            headB = curr
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        if headA == headB:
            inter = headA
        else:
            inter = None

        return inter
