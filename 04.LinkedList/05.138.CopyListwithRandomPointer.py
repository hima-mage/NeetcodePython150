"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}

        cur = head
        # loop to create deep copy of the current nodes
        while cur:
            copy = Node(cur.val) # deep copy of the current node
            oldToCopy[cur] = copy # hahmap to map oldNode to copy we created
            cur = cur.next

        cur = head
        while cur:
            copy = oldToCopy[cur] # get the copy from the current
            copy.next = oldToCopy[cur.next] # get next pointer  of copy to oldNode next
            copy.random = oldToCopy[cur.random] # get random pointer  of copy to oldNode random
            cur = cur.next
        return oldToCopy[head] # return head of the copylist using hashmap
