## dfs+memo
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:


        memo = {}
        def dfs(i,j):

            if i==len(triangle)-1:
                return triangle[i][j]
            if (i,j) in memo:
                return memo[(i,j)]

            minPath = min(dfs(i+1,j),dfs(i+1,j+1))+triangle[i][j]
            memo[(i,j)]= minPath
            return minPath    

        return dfs(0,0)
## dp

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        dp = [[float('inf') for j in range(len(triangle[-1]))] for i in range(len(triangle))]


        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if j>i:
                    continue
                if i==0:
                    dp[i][j] = triangle[i][j]
                elif j==0:
                    dp[i][j]=dp[i-1][j] + triangle[i][j]
                else:
                    dp[i][j]=min(dp[i-1][j],dp[i-1][j-1])+triangle[i][j]


        return min(dp[-1])            


