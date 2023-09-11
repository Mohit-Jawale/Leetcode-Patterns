### DFS + memo
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:


        memo = {}
        def dfs(i,j):

            nonlocal memo

            if i>=m or j>=n:
                return 0

            if i == m-1 and j==n-1:
                return 1

            if (i,j) in memo:
                return memo[(i,j)]    

            count = 0

            count += dfs(i+1,j)+dfs(i,j+1) 

            memo[(i,j)]=count

            return count       
        
        return dfs(0,0)

  #### 2d -dp 
  class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [ [0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i-1<0 or j-1<0:
                    dp[i][j] = 1
                else:
                    dp[i][j]= dp[i-1][j]+dp[i][j-1]    

        return dp[m-1][n-1]
                    
                
