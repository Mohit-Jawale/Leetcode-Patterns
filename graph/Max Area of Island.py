class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        R, C = len(grid), len(grid[0])

        count = 0
        max_area = 0
        def dfs(r,c):
            nonlocal count

            if grid[r][c]==1:

                grid[r][c] = 2
                count+=1
                if r+1<R:dfs(r+1,c)
                if c+1<C:dfs(r,c+1)
                if r>=1:dfs(r-1,c)
                if c>=1:dfs(r,c-1)


        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    count = 0
                    dfs(r,c)
                    max_area = max(max_area,count)

        return max_area            




        
