### this is the most natural implementation of this problem draw tree->code dfs -> convert dfs into dp(bottom up solution)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        
        def dfs(i):

            if i >= len(cost):
                return 0

            if i in memo:
                return memo[i]

            minCost = min(dfs(i + 1), dfs(i + 2)) + (cost[i] if i > -1 else 0)

            memo[i] = minCost
            return minCost
        
        return dfs(-1)

        dp = [0]*(len(cost)+2)
        dp[len(cost)] = 0
        dp[len(cost)+1] = 0
        for i in reversed(range(len(cost))):
            dp[i] = min(dp[i+1],dp[i+2])+cost[i]


        return min(dp[0],dp[1])
            
