## dfs + memo
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        memo = {}

        def dfs(i,j,k):

            if (i,j,k) in memo:
                return memo[(i,j,k)]
            if i<0 or j<0 or i>=n or j>=n:
                return 0
            if k==0:
                return 1
            if k<0:
                return 0

            totalMoves = 0
  
            up = dfs(i-2,j-1,k-1)+dfs(i-2,j+1,k-1)
            down = dfs(i+2,j-1,k-1)+dfs(i+2,j+1,k-1)
            right = dfs(i+1,j+2,k-1)+dfs(i-1,j+2,k-1)
            left = dfs(i+1,j-2,k-1)+dfs(i-1,j-2,k-1)

            totalMoves+=(up+down+right+left)/8

            memo[(i,j,k)]= totalMoves

            return totalMoves

        return dfs(row,column,k)    




