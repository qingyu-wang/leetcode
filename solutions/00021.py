"""
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/description/
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time:  O(n)
        Space: O(1)
        """
        tmp = ListNode()
        cur = tmp

        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1  = list1.next
            else:
                cur.next = list2
                list2  = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        else:
            cur.next = list2

        return tmp.next

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time:  O(n)
        Space: O(n)
        """
        list0 = None

        while True:
            if not list1 and not list2:
                break
            elif not list1:
                val = list2.val
                list2 = list2.next
            elif not list2:
                val = list1.val
                list1 = list1.next
            else:
                if list1.val < list2.val:
                    val = list1.val
                    list1 = list1.next
                else:
                    val = list2.val
                    list2 = list2.next

            if not list0:
                list0 = ListNode(val=val, next=None)
                cur = list0
            else:
                cur.next = ListNode(val=val, next=None)
                cur = cur.next

        return list0