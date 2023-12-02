## This is Top-down or DFS + memo approach

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)-1
        n = len(grid[0])-1
        memo = {}
        def dfs(i,j):
    
            if i==0 and j==0:
                return grid[i][j]

            if i<0 or j<0:
                return float('inf')

            if (i,j) in memo:
                return memo[(i,j)]    

            minSum = min(dfs(i,j-1),dfs(i-1,j))+grid[i][j]

            memo[(i,j)] = minSum
            
            return minSum

        return dfs(m,n)    

## This Bottom-down

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        

        for i in range(0,m):
            for j in range(0,n):
                if i==0 and j==0:
                    continue
                if i==0:
                    grid[i][j]+=grid[i][j-1]
                elif j==0:
                    grid[i][j]+=grid[i-1][j]
                else:            
                    grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j] 

        return grid[m-1][n-1]        
        
