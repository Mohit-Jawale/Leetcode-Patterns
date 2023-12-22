class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        minPrice = prices[0]
        for curr_price in prices:
            minPrice = min(minPrice,curr_price)
            profit = curr_price - minPrice
            maxProfit = max(maxProfit,profit)

        return maxProfit


            


