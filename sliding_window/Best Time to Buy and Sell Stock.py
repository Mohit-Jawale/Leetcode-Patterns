#### remember about why left = right why not left+=1

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left, right = 0,1

        if len(prices)==1:
            return 0

        max_profit = 0 

        while right<len(prices):
            if prices[right]<=prices[left]:
                left = right
                right+=1
                
            else:
                max_profit = max(prices[right]-prices[left],max_profit)
                right+=1

        return max_profit        


        


        


