
class Solution:
    def numSquares(self, n: int) -> int:

        perfectSquares = [i for i in range(n,0,-1) if int(sqrt(i))*int(sqrt(i))==i]
        memo = {}

        def dfs(n):
            if n==0:
                return 0
            if n<0:
                return float('inf')
            if n in memo:
                return memo[n]
            minSQ = float('inf')

            for i in perfectSquares:
 
                minSQ = min(minSQ,dfs(n-i)+1)

            memo[n]= minSQ
            return minSQ  

        return dfs(n)            
        
