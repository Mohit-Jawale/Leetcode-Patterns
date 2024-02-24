class Solution:
    def numSquares(self, n: int) -> int:

        perfectSq = [i for i in range(1,n+1) if int(sqrt(i))*int(sqrt(i)) == i]
        
        
        def dfs(n):

            if n==0:
                return 0
            if n<0:
                return float('inf')
            
            minop = float('inf')
            for i in perfectSq:
                minop = min(dfs(n-i)+1,minop)
            
            return minop

        return dfs(n)

        dp = [float('inf')]*(n+1)
        dp[0]=0

        for i in range(1,n+1):
            for j in perfectSq:
                if i>=j:
                    dp[i] = min(dp[i-j]+1,dp[i])
        
        return dp[n]
