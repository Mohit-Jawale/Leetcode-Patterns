### dfs + memo
### dp solution is easy thats y not added here same as buy stock 2
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:


        memo = {}
        def dfs(i,buy):

            if (i,buy) in memo:
                return memo[(i,buy)]

            if i>=len(prices):
                return 0

            if buy:
                profit = -prices[i]+dfs(i+1,False)
                skipBuy = dfs(i+1,True)
                profit = max(profit,skipBuy)
            else:
                profit = prices[i]+dfs(i+1,True) - fee
                skipSell = dfs(i+1,False)
                profit = max(profit,skipSell)
                
            memo[(i,buy)] = profit
            return profit
        
        return dfs(0,True)
            

        
