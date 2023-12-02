## dfs+memo

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        

        memo = {}
        def dfs(amount):
            
            if amount==0:
                return 0
            if amount in memo:
                return memo[amount]    
   
            minCost = float('inf')

            for i in coins:
                if i<=amount:
                    minCost = min(dfs(amount-i)+1,minCost)
                    
            memo[amount]=minCost
            return minCost 

        ans = dfs(amount)   
        return ans if ans != float('inf') else -1

## 1D- DPb bottom up

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [float('inf')]*(amount+1)

        dp[0]=0
        
        for amount in range(1,amount+1):
            for coin in coins:
                if coin<=amount:
                    dp[amount]=min(dp[amount],dp[amount-coin]+1)

        return dp[-1] if dp[-1]!=float('inf') else -1          

