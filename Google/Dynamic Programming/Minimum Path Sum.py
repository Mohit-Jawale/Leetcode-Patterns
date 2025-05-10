class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid), len(grid[0])

        memo = {}

        def dfs(row,col):

            if not(row>=0 and  col>=0 and  row<m and col<n):
                return float('inf')
            
            if row == m-1 and col == n-1:
                return grid[row][col]
            
            if (row,col) in memo:
                return memo[(row,col)]
        

            down = dfs(row+1,col)+grid[row][col]
            right = dfs(row,col+1)+grid[row][col]

            memo[(row,col)]= min(down,right)

            return memo[(row,col)]
        
        return dfs(0,0)



        
