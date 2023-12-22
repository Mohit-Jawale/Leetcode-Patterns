### dfs + memo
### this is good starting probleming for decision making and state analysis
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def dfs(i,buy):

            if (i,buy) in memo:
                return memo[(i,buy)]

            if i>=len(prices):
                return 0
            
            if buy:
                ### decide to buy
                profit = -prices[i]+dfs(i+1,False)
                skipBuy = dfs(i+1,True)
                profit = max(profit,skipBuy)
            else:
                ### decide to sell
                profit = prices[i]+dfs(i+1,True)
                skipSell = dfs(i+1,False)
                profit = max(profit,skipSell)
            
            memo[(i,buy)] = profit
            return profit
        
        return dfs(0,True)
        
### 2d -dp
        n = len(prices)
        dp = [[0 for _ in range(2)] for _ in range(n+1)]

        for i in reversed(range(n)):
            for buy in range(2):
                if buy == 1:
                    ### decide to buy
                    profit = -prices[i]+dp[i+1][0]
                    skipBuy = dp[i+1][1]
                    dp[i][buy] = max(profit,skipBuy)
                else:
                    ### decide to sell
                    profit = prices[i]+dp[i+1][1]
                    skipSell = dp[i+1][0]
                    dp[i][buy] = max(profit,skipSell)
        
        return dp[0][1]
### space optimization
        sellNext,buyNext = 0, 0
        sellCurr,buyCurr = 0,0

        for i in reversed(range(n)):
            for buy in range(2):
                if buy == 1:
                    ### decide to buy
                    profit = -prices[i]+ sellNext
                    skipBuy = buyNext
                    buyCurr = max(profit,skipBuy)
                else:
                    ### decide to sell
                    profit = prices[i]+buyNext
                    skipSell = sellNext
                    sellCurr = max(profit,skipSell)
            
            sellNext,buyNext = sellCurr,buyCurr

        return buyCurr


        
