class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        memo = {}
        def dfs(i,buy,transactions):

            if (i,buy,transactions) in memo:
                return memo[(i,buy,transactions)]

            if i>=n or transactions>=2:
                return 0

            if buy:
                profit = -prices[i] + dfs(i+1,False,transactions)
                skipBuy = dfs(i+1,True,transactions)
                profit = max(profit,skipBuy)
            else:
                profit = prices[i] + dfs(i+1,True,transactions+1)
                skipSell = dfs(i+1,False,transactions)
                profit = max(profit,skipSell)

            memo[(i,buy,transactions)] = profit
            return profit

        return dfs(0,True,0)   
        
