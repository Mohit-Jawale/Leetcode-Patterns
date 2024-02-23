class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        dayMapping = {0:1,1:7,2:30}
        memo = {}
        def dfs(i,currPass):

            if i>=len(days):
                return 0

            if (currPass) in memo:
                return memo[(currPass)]
            
            minCost = float('inf')

            for k in range(len(costs)):

                if currPass<=days[i]:
                    newValidPass = days[i]+dayMapping[k]
                    minCost = min( dfs(i+1,newValidPass) + costs[k],minCost)
                else:
                    minCost = min(dfs(i+1,currPass),minCost)

            memo[(currPass)] = minCost
            return minCost

        return dfs(0,0)


        
        



