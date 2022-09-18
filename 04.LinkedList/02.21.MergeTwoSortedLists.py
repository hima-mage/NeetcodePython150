# Definition for singly-linked list.
from typing import Optional


class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # to avoid the edge case of insert into empty list
        dummy = ListNode() # create linkedlist empty to store the output list to it
        tail = dummy # set tail to be equal to that linkedlist
        # while the two listNode not empty
        while list1 and list2:
            # if listNode.val are equals
            if list1.val < list2.val:
                tail.next = list1 # set tail.next to the lower val -> list1
                list1 = list1.next # and convert list1 to be the next node
            else:
                tail.next = list2 # set tail.next to the lower val -> list2
                list2 = list2.next  # and convert list2 to be the next node
            tail = tail.next # shoul be update whatever the condition

        # what if list2 is empty
        if list1:
            tail.next = list1
        # what if list2 is empty
        elif list2:
            tail.next = list2

        return dummy.next