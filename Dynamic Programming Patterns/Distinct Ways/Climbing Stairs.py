### DFS + memo
class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def dfs(n):

            if n in memo:
                return memo[n]
            if n==0:
                return 1
            if n<0:
                return 0 
                    
            totalWays = dfs(n-1)+dfs(n-2)

            memo[n]= totalWays
            return totalWays


        return dfs(n)


## 1 DP
class Solution:
    def climbStairs(self, n: int) -> int:

        if n==1:
            return 1
        dp = [0]*(n+1)

        dp[0]=1
        dp[1]=1

        for i in range(2,len(dp)):
            dp[i]= dp[i-1]+dp[i-2]

        return dp[-1]

        

