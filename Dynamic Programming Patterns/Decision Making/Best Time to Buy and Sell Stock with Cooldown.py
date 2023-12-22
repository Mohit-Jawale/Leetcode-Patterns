class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        memo = {}
        def dfs(i,buy):

            if (i,buy) in memo:
                return memo[(i,buy)]

            if i>=n:
                return 0

            if buy:
                profit = -prices[i]+dfs(i+1,False)
                skipBuy = dfs(i+1,True)
                profit = max(profit,skipBuy)
            else:
                profit = prices[i]+dfs(i+2,True)
                skipSell = dfs(i+1,False)
                profit = max(profit,skipSell)

            memo[(i,buy)] = profit
            return profit


        return dfs(0,True)
        
