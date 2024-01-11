"""
707. Design Linked List
https://leetcode.com/problems/design-linked-list/description/
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        self.node_temp = ListNode(val="temp", next=None)

    def __repr__(self):
        node_list = []
        node_curr = self.node_temp.next
        while node_curr is not None:
            node_list.append(node_curr.val)
            node_curr = node_curr.next
        return str(node_list)

    def get(self, index: int) -> int:
        node_curr = self.node_temp
        for _ in range(index+1):
            node_curr = node_curr.next
            if node_curr is None:
                break
        if node_curr is not None:
            val = node_curr.val
        else:
            val = -1
        # print("get", index, val)
        return val

    def addAtHead(self, val: int) -> None:
        self.node_temp.next = ListNode(val=val, next=self.node_temp.next)
        # print("addAtHead", val, self.__repr__())
        return

    def addAtTail(self, val: int) -> None:
        node_curr = self.node_temp
        while node_curr.next is not None:
            node_curr = node_curr.next
        node_curr.next = ListNode(val=val, next=None)
        # print("addAtTail", val, self.__repr__())
        return

    def addAtIndex(self, index: int, val: int) -> None:
        node_curr = self.node_temp
        for _ in range(index):
            node_curr = node_curr.next
            if node_curr is None:
                break
        if node_curr is not None:
            node_curr.next = ListNode(val=val, next=node_curr.next)         
        # print("addAtIndex", index, val, self.__repr__())
        return

    def deleteAtIndex(self, index: int) -> None:
        node_curr = self.node_temp
        for _ in range(index):
            node_curr = node_curr.next
            if node_curr is None:
                break
        if node_curr is not None and node_curr.next is not None:
            node_curr.next = node_curr.next.next       
        # print("deleteAtIndex", index, self.__repr__())
        return
