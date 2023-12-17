## Dfs+memo
## we are multipling bcz we have to find out total ways of arrange x and y items together.

class Solution:
    def numTrees(self, n: int) -> int:

        memo = {}
        def dfs(n):

            if n in memo:
                return memo[n]

            if n==0 or n==1:
                return 1

            totalBST=0

            for i in range(1,n+1):
                totalBST+=dfs(i-1) * dfs(n-i)

            memo[n] = totalBST

            return totalBST

        return dfs(n)        

        
