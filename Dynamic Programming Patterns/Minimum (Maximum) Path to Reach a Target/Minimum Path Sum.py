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
        
