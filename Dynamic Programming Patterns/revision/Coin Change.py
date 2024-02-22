class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
  
        def dfs(total):
    
            if total==amount:
                return 0
            if total in memo:
                return memo[total]

            minCoins = float('inf')
            for i in range(len(coins)):

                if total+coins[i]<=amount:
                    minCoins = min(dfs(total+coins[i])+1,minCoins)

            memo[total] = minCoins
            return minCoins 
        
        ans = dfs(0)
        return ans if ans != float('inf') else -1



      
        dp = [float('inf')]*(amount+1)
        dp[amount] = 0
        for i in reversed(range(len(dp))):
            for j in range(len(coins)):
                if i+coins[j]<=amount:
                    dp[i]=min(dp[i+coins[j]]+1,dp[i])

        return dp[0] if dp[0] != float('inf') else -1
