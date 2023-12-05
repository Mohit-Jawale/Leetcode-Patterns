### here bisect is used because while creating decision tree I released I need next days in the days for which the array needs to travel
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        

        memo = {}
        def dfs(i):
            
            if i>=len(days):
                return 0

            if i in memo:
                return memo[i]
            minCost = min(dfs(i+1)+costs[0],dfs(bisect_left(days,days[i]+7))+costs[1],dfs(bisect_left(days,days[i]+30))+costs[2])
            memo[i] = minCost
            return minCost

        return dfs(0)     

## 1DP solution
## the max trick is worth noting

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        dp = [0]*(days[-1]+1)
        days = set(days)
        for day in range(1,len(dp)):
            
            if day not in days:
                dp[day]=dp[day-1]
            else:
                cost1 = dp[max(day-1,0)]+costs[0]
                cost7 = dp[max(day-7,0)]+costs[1]
                cost30 = dp[max(day-30,0)]+costs[2]

                dp[day]=min(cost1,cost7,cost30)

        return dp[-1]        





        
