from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        m, n = len(grid), len(grid[0])
        queue = []

        # Adding land cells (1s) to the queue and marking water cells (0s) with infinity
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
                else:
                    grid[i][j] = float('inf')

        # Edge case: All 1s or all 0s
        if not queue or len(queue) == m * n:
            return -1

        # BFS to find the maximum distance from each cell to the nearest 1
        while queue:
            i, j = queue.pop(0)
            for r, c in moves:
                ai, aj = i + r, j + c
                if not (ai<0 or ai>=m or aj<0 or aj>=n) and grid[i][j] + 1 < grid[ai][aj]:
                    grid[ai][aj] = grid[i][j] + 1
                    queue.append((ai, aj))

        # Finding the maximum distance in the grid
        max_distance = max(max(row) for row in grid)
        return max_distance - 1 

