### DFS + memo
class Solution:
    def climbStairs(self, n: int) -> int:
        
        memo = {}
        def dfs(n):

            if n in memo:
                return memo[n]
            if n==0:
                return 1
            if n<0:
                return 0 
                    
            totalWays = dfs(n-1)+dfs(n-2)

            memo[n]= totalWays
            return totalWays


        return dfs(n)
