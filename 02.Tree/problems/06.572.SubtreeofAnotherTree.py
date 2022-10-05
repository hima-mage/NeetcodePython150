# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        # if t empty -> success O(1)
        if not t:
            return True
        # if s empty -> success O(1)
        if not s:
            return False
        # check if they same then it's subtree O(v+e)
        if self.sameTree(s, t):
            return True
        #  check if the t is subtree of any subtree of the original s
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def sameTree(self, s, t):
        # if the tree is empy
        if not s and not t:
            # they technical same
            return True
        # compare them
        if s and t and s.val == t.val:
            # recursion -> compare left by left -> right by right
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)
        return False