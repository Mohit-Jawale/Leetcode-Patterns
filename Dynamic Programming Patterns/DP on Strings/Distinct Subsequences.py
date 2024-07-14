### DFS + memo
### neetcode video is good if you loose intution while revising
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        m,n = len(s),len(t)

        memo = {}

        def dfs(i,j):

            if (i,j) in memo:
                return memo[(i,j)]

            if j>=n:
                return 1   
            if i>=m:
                return 0
 
            totalUniqueWays = 0

            if s[i]==t[j]:
                totalUniqueWays = (dfs(i+1,j))+(dfs(i+1,j+1))
            else:
               totalUniqueWays =  dfs(i+1,j)    

            memo[(i,j)] = totalUniqueWays
            return totalUniqueWays


        return dfs(0,0) 


#### 2d -DP

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(m+1):
            dp[i][n]=1
        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if s[i]==t[j]:
                    dp[i][j] = dp[i+1][j+1]+dp[i+1][j]
                else:
                    dp[i][j] = dp[i+1][j]
        
        return dp[0][0]
            


