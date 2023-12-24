class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:

        m,n = len(grid),len(grid[0])

        def dfs(i,j):

            if i<0 or i>=m or j<0 or j>=n:
                return False
            if grid[i][j]==1 or grid[i][j]==2:
                return True

            grid[i][j]=2    

            down = dfs(i+1,j)
            right = dfs(i,j+1)
            up = dfs(i-1,j)
            left = dfs(i,j-1)
            return (left and up and right and down)

        count = 0

        for i in range(1,m-1):
            for j in range(1,n-1):
                if grid[i][j]==0 and grid[i][j]!=2:
                    boundryFlag = dfs(i,j)
                    if boundryFlag:
                        count+=1

        return count


        
