# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # set current to head , and prev to none as initial val
        prev , curr = None , head

        while curr:
            temp = curr.next # get next element -> store it
            curr.next = prev # set the next of current to prev  -> this means first element will poit to none which made it end of list
            prev = curr # set prev to be current
            curr = temp # get current to be next element in linked list
        return  prev