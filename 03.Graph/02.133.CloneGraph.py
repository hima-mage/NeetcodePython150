
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {}
        # depth for search
        def dfs(node):
            # check if it's in hashmap - so it's already cloned or not  so return that cloned node
            if node in oldToNew:
                return oldToNew[node]
            # create a copy
            copy = Node(node.val)
            # added it hashmap
            oldToNew[node] = copy
            # for every neighbour make dfs -> recursively
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            # return the copy
            return copy

        return dfs(node) if node else None # to avoid null given
