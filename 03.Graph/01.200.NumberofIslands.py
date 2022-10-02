from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands


# BFS Version From Video - breadth for search
class SolutionBFS:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if the grid is already empty then it has no islands
        if not grid:
            return 0
        # get number of rows and cols
        rows, cols = len(grid), len(grid[0])
        # mark the visited island
        visited = set()
        # number of islands found
        islands = 0
        # it's not recursive algorithm - it's iterative
        def bfs(r, c):
            # the needed data-structure to use as memory -> queue is perfect one
            q = deque()
            visited.add((r, c)) # mark as visited
            q.append((r, c)) # added to queue
            # while the queue not empty -> this means we will expand our island
            while q:
                # get from the queue
                row, col = q.popleft()
                # the four directions i can go to [right - left - above - below]
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                # for every direction - dr row - dc column
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    # check if the move i make is in range and also if it's land and not visited so added to our island
                    if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))
        # for every single row
        for r in range(rows):
            # for every single column
            for c in range(cols):
                # if it's island and not visited before so i can increment number of islands found
                if grid[r][c] == "1" and (r, c) not in visited:
                    # run BFS
                    bfs(r, c)
                    # increment number of the islands
                    islands += 1

        return islands