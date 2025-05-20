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







        
