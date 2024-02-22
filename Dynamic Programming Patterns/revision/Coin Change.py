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

    #### how to convert
        ### Step 1: make dp by analyising amount as we can see its 1-DP problem
        ### Step 2: look for base case in your dfs set that in the above dp
        ### Step 3: convert the dfs call or reccurance relation into dp and see how the flow is in top-down it will be opposite


      
        dp = [float('inf')]*(amount+1) ### Step 1
        dp[amount] = 0 ### Step 2
        for i in reversed(range(len(dp))): ### step 3
            for j in range(len(coins)):
                if i+coins[j]<=amount:
                    dp[i]=min(dp[i+coins[j]]+1,dp[i])

        return dp[0] if dp[0] != float('inf') else -1
