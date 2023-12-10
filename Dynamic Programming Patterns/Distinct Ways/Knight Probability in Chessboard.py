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


##  3d - dp 
        
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(k+1)]

        moves = [(2, 1), (1, 2), (-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1)]

        dp[0][row][column] = 1

        for move in range(1,k+1):
            for i in range(n):
                for j in range(n):
                    for dr,dc in moves:
                        if 0 <= i + dr < n and 0 <= j + dc < n:
                            dp[move][i][j] += dp[move - 1][i + dr][j + dc] / 8

        return sum(dp[k][r][c] for r in range(n) for c in range(n)) 




