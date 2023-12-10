### DFS + Memo
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        memo = {}

        def dfs(target,n):

            if (target,n) in memo:
                return memo[(target,n)]

            if target==0 and n==0:
                return 1 

            if n==0 or target<0:
                return 0

            totalWays = 0

            for j in range(1,k+1):
                totalWays += dfs(target-j,n-1)

            memo[(target,n)] = totalWays   

            return memo[(target,n)]    


        return dfs(target,n)%(pow(10,9)+7)
        
 ## 2d - DP
dp = [[0 for _ in range(target+1)] for _ in range(n+1)]

dp[0][0]=1
MOD = pow(10,9)+7

for dice in range(1,len(dp)):
    for t in range(1,len(dp[0])):
        for p in range(1,k+1):
            if (t-p)>=0:
                dp[dice][j] += dp[dice-1][t-p]%(MOD)


return dp[-1][-1]%MOD           

