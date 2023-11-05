class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:

        n = len(present)
        # Initialize the DP table with 0s
        dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
        
        # Build the table in bottom up manner
        for i in range(1, n + 1):
            for j in range(budget + 1):
                # Profit if we don't buy the current stock
                not_buy = dp[i - 1][j]
                # Profit if we buy the current stock
                buy = 0
                # Check if the current budget can buy the i-th stock or if the stock is free
                if j >= present[i - 1] or present[i - 1] == 0:
                    profit = future[i - 1] - present[i - 1]
                    if present[i - 1] == 0:
                        # If the stock is free, we can always take its profit
                        buy = dp[i - 1][j] + profit
                    else:
                        # Otherwise, we can only take its profit if we have enough budget
                        buy = dp[i - 1][j - present[i - 1]] + profit
                # Take the maximum of buying or not buying the current stock
                dp[i][j] = max(not_buy, buy)
        
        # The last cell will have the answer
        return dp[n][budget]
            
