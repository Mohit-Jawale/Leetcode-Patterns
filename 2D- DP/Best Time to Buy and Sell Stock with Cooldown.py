### look for the state diagram before solving this question.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        sell,hold,cooldown = 0,-float('inf'),0

        for price in prices:

            prev_cooldown,prev_sell,prev_hold = cooldown,sell,hold

            cooldown = max(prev_sell,prev_cooldown)

            hold = max(prev_hold,prev_cooldown-price)

            sell = price + prev_hold

        return max(sell,cooldown)    

                
        
