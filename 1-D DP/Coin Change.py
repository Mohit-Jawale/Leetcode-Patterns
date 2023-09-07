### dfs + memo
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        count = 0

        memo = {}

        def dfs(amount):

            if amount in memo:
                return memo[amount]

            if amount<0:
                return -1

            if amount==0:
                return 0

            min_count = float('inf')    

            for i in range(len(coins)):
                count = dfs(amount-coins[i])
                if count>=0:
                    min_count = min(count+1,min_count)

            memo[amount] = min_count
            return min_count if min_count!=float('inf') else -1


        return dfs(amount)            


### 1 dp solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        ### taking amount+1 is smart to avoid infinity
        dp = [amount+1] * (amount+1)

        dp[0] = 0

        for a in range(1,amount+1):
            for c in coins:
                if a-c>=0:
                    dp[a] = min(dp[a-c]+1,dp[a])

        return dp[amount] if dp[amount]!= amount+1 else -1            

        
