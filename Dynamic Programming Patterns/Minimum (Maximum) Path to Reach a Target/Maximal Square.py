## This problem has amazing trick of min
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        
        count = 0

        memo = {}

        def dfs(i,j):

            nonlocal count

            if i>=len(matrix) or j>=len(matrix[0]) or matrix[i][j]=="0":
                return 0
            if (i,j) in memo:
                return memo[(i,j)]

            down = dfs(i+1,j) 
            right= dfs(i,j+1)
            diagonal = dfs(i+1,j+1)

            memo[(i,j)] = min(down,right,diagonal)+1

            return memo[(i,j)]

        maxSq = 0
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if matrix[i][j] == "1":
                    maxSq = max(maxSq,dfs(i,j))


        return maxSq * maxSq         
## 2 DP solution

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        n,m = len(matrix[0]),len(matrix)
        dp = [[0 for j in range(n+1)] for i in range(m+1)]

        max_area = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1]=="1":
                    dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    max_area = max(max_area,dp[i][j])
        
        return max_area*max_area


            
             
