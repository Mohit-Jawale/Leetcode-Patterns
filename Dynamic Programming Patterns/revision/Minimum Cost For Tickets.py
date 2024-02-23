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


#### be careful about the overflows
    dp = [float('inf')] * (days[-1]+1)
    dp+=[0]
    daysset = set(days)

    for i in reversed(range(days[-1]+1)):
        for j in range(len(costs)):
            if i in daysset:
                nextPass = min(i+dayMapping[j],days[-1]+1)
                dp[i] = min(dp[nextPass]+costs[j],dp[i])
            else:
                dp[i]=dp[i+1]
    
    return dp[0]


##### to use the currPAss<=i condition as it is we reverse the sign of dfs call in dp

        dp = [float('inf')]*(days[-1]+1)
        dayset = set(days)
        dp[0]=0
        currPass = 0
        for i in range(1,days[-1]+1):
            for k in range(len(costs)):
                if i in dayset and currPass<=i:
                    currPass = i-dayMapping[k]
                    dp[i] = min( dp[max(0,currPass)] + costs[k],dp[i])
                else:
                    dp[i] = dp[i-1]

        return dp[-1]



        
        



