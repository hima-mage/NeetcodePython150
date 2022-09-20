# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # make DFS , which will traverse the tree until the max depth (last node and then backtracking )
        # it's used to mark each node as visisted to avoid cycle
        def dfs(root):
            # if root is null return True
            if not root:
                return [True, 0]
            # keep recusrsion for left , right tree to check their balance
            left, right = dfs(root.left), dfs(root.right)
            # balance will be true if , left tree  , right tree are balanced , and also the root tree is balanced
            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]