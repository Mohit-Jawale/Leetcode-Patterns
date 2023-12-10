### DFS + memo
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        memo = {}
        def dfs(i,j):
            
            if (i,j) in memo:
                return memo[(i,j)]

            if i==m-1 and j == n-1:
                return 1

            if i>=m or j>=n:
                return 0

            totalPaths = dfs(i+1,j)+dfs(i,j+1)
            
            memo[(i,j)] = totalPaths
            return totalPaths

        return dfs(0,0)    

## 2d DP

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0 for _ in range(n)]for _ in range(m)]

        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i==0 or j==0:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]

        return dp[-1][-1]
                        
        
