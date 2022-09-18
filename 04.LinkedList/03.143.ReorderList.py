# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle - idk if the list is even or odd
        slow, fast = head, head.next
        # so if fast reach the last element -> slow will be  in the middle
        # slow ->1 fast -> 2 ,  slow ->2 fast -> 4 , slow ->3 fast -> 6 , slow ->4 fast -> 8 , etc
        while fast and fast.next:
            slow = slow.next # jump 1
            fast = fast.next.next # jump 2

        # reverse second half - get nth first - second half of the list will be after the slow -> slow.next
        second = slow.next
        prev = slow.next = None
        # reverse it
        while second:
            tmp = second.next # temp will the next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next # get next index of each lists -> we have two lists now
            first.next = second # set first next to second which is first element in second element
            second.next = tmp1 # set the second->next to first->next
            first, second = tmp1, tmp2 # set first and second to the next indexes in their lists