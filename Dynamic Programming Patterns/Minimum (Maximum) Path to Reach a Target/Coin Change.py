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
