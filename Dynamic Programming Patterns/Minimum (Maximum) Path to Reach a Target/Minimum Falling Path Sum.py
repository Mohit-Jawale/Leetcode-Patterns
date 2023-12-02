## DFS + memo, When I was solving this problem it just came to me that I have to call dfs in for loop bcz there are no one position where it
## has to end.

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}
        def dfs(i,j):

            if i<0 or j<0 or j>=(len(matrix[0])):
                return float('inf')
            if i==0:
                return matrix[i][j]

            if (i,j) in memo:
                return memo[(i,j)]    
           
            minCost = min(dfs(i-1,j+1),dfs(i-1,j),dfs(i-1,j-1)) + matrix[i][j]

            memo[(i,j)]= minCost

            return minCost

        ans = float('inf')
        for k in range(0,len(matrix[0])):
            ans = min(dfs(len(matrix)-1,k),ans)

        return ans            

### DP solution bottom up-
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        
        m = len(matrix)
        n = len(matrix[0])

        for i in range(0,m):
            for j in range(0,n):
                
                if i==0:
                    continue
                elif j==0:
                    matrix[i][j]=min(matrix[i-1][j],matrix[i-1][j+1])+ matrix[i][j]
                elif j==n-1:
                    matrix[i][j]=min(matrix[i-1][j],matrix[i-1][j-1])+ matrix[i][j]
                else:
                    matrix[i][j]=min(matrix[i-1][j],matrix[i-1][j-1],matrix[i-1][j+1])+ matrix[i][j]

        return min(matrix[m-1])            

