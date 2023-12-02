## This is top-down or DFS + memo approach

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    
        memo = {}
        def dfs(n):

            if n==0 or n==1:
                return cost[n]
            if n in memo:
                return memo[n]

            minCost = min(dfs(n-1),dfs(n-2)) + (cost[n] if n<len(cost) else 0)

            memo[n]= minCost
            return minCost

        return dfs(len(cost))     

## This is bottom-up approach
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
    
        dp = [0]*(len(cost)+1)

        dp[0]=cost[0]
        dp[1]=cost[1]
            
        for i in range(2,len(cost)+1):
    
            dp[i] = min(dp[i-1],dp[i-2]) + (cost[i] if i<len(cost) else 0)


        return dp[-1]   
        
        
