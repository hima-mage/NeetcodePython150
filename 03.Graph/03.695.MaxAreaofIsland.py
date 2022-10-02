class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # get dimensions -> rows and cols
        ROWS, COLS = len(grid), len(grid[0])
        # mark visited nodes
        visit = set()
        # depth for search
        def dfs(r, c):
            if (
                r < 0 # rows is less than 0
                or r == ROWS
                or c < 0
                or c == COLS
                or grid[r][c] == 0 # if we reach water
                or (r, c) in visit # if it's in visited set
            ):
                return 0
            visit.add((r, c))
            # 1  cell we currenly visiting + the four direction
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        area = 0
        # colculate the area
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area