# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0  # var to hold result

        # make DFS algo by send root as start
        def dfs(root):
            # The nonlocal keyword is used to work with variables inside nested functions, where the variable should not belong to the inner function.
            nonlocal res

            # if root is null return 0
            if not root:
                return 0
            # keep recursion on left, right
            left = dfs(root.left)
            right = dfs(root.right)
            # result will be max of resul , sum of left and right -> the diameter
            res = max(res, left + right)
            # here of them + 1
            return 1 + max(left, right)

        dfs(root)
        return res