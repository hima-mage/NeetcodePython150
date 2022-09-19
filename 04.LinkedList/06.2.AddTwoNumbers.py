# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy # set current node
        # carry if the sum exceed the 10's
        carry = 0
        # while there is nodes availables
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0 # get val of l1
            v2 = l2.val if l2 else 0 # get val of l2

            # new digit
            val = v1 + v2 + carry # val of the sum list will be
            carry = val // 10 # get carry of the val of node the 1's -> so it's not exceed the 10's
            val = val % 10 # get the 10's val
            cur.next = ListNode(val) # set dummy next val to be that val

            # update ptrs
            cur = cur.next # get the next node on the empty list
            l1 = l1.next if l1 else None # shift first list node by 1
            l2 = l2.next if l2 else None # shift first list node by 1

        return dummy.next # return dummy head -> as dummy just pointer