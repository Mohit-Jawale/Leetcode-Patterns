### dfs+memo

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        moves = [(-1,0),(1,0),(0,1),(0,-1)]
        MOD = pow(10,9)+7

        memo = {}
        def dfs(i,j,maxMove):
            
            if (i,j,maxMove) in memo:
                return memo[(i,j,maxMove)]

            if not (0<=i<m and 0<=j<n) and maxMove>=0:
                return 1
            if maxMove<0:
                return 0

            totalMoves = 0
            for r,c in moves:
                totalMoves+=dfs(i+r,j+c,maxMove-1) % MOD

            memo[(i,j,maxMove)] = totalMoves

            return totalMoves

        return dfs(startRow,startColumn,maxMove) % MOD



## 3d dp 
### draw the state and table to understand the recurrance relation
        dp = [[[0 for _ in range(maxMove+1)]for _ in range(n)] for _ in range(m)]

        dp[startRow][startColumn][0] = 1
        count = 0

        for k in range(maxMove):
            for i in range(m):
                for j in range(n):
                    if dp[i][j][k]>0:
                        for r,c in moves:
                            ai,aj = i+r,j+c
                            if 0<=ai<m and 0<=aj<n:
                                dp[ai][aj][k+1]+=dp[i][j][k] % MOD
                            else:
                                count+=dp[i][j][k] % MOD

        return count % MOD
