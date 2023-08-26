### DFS + memo

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        memo = {}

        def dfs(n):

            if n==0:
                return cost[n]
            if n<0:
                return 0

            if n in memo:
                return memo[n]    

            memo[n] = cost[n]+min(dfs(n-1),dfs(n-2))

            return memo[n]

        return min(dfs(n-1),dfs(n-2))

## 1d dp

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        dp = [0] *n

        dp[0]=cost[0]
        dp[1]=cost[1]

        for i in range(2,n):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])

        return min(dp[n-1],dp[n-2])  



        
