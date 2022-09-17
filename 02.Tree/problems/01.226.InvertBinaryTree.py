# Definition for binary tree node.
class TreeNode:
    def __init__(self, val=0 , left=None , right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def invertTree(self, root:TreeNode) -> TreeNode:
        # if the root is empty then return None
        if not root:
            return None

        # swap the childern
        tmp = root.left # just temperory value to swap
        root.left = root.right
        root.right = tmp
        # recursion -> for both left and right -> deal with each subTree to reverse it
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
