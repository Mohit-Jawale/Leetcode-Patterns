class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # memo = {}

        # def minStepsToGetCoins(total):

        #     if total>amount:
        #         return float('inf')
            
        #     if total==amount:
        #         return 0
            
        #     if total in memo:
        #         return memo[total]
            
        #     minSteps = float('inf')

        #     for coin in coins:

        #         minSteps = min(minStepsToGetCoins(total+coin)+1,minSteps)
            
        #     memo[total] = minSteps
        #     return memo[total]

        # ans =  minStepsToGetCoins(0)

        # return ans if ans!=float('inf') else -1


        dp = [float('inf')]* (amount+1)

        dp[amount] = 0
        
        for total in reversed(range(amount)):

            for coin in coins:

                if total+coin<=amount:
                    dp[total] = min(dp[total+coin]+1,dp[total])
        
        return dp[0] if dp[0]!=float('inf') else -1
