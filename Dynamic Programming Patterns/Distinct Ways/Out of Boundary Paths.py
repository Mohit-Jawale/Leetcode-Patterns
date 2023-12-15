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
