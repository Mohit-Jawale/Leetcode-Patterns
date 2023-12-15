### DFS+ memo top-down
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        ROW,COL = len(obstacleGrid),len(obstacleGrid[0])
        memo = {}
        def dfs(i,j):

            if (i,j) in memo:
                return memo[(i,j)]

            if i==ROW-1 and j==COL-1 and not obstacleGrid[i][j]==1:
                return 1

            if i>=ROW or j>=COL or obstacleGrid[i][j]==1:
                return 0

            totalPath = 0

            down = dfs(i+1,j)
            left = dfs(i,j+1) 

            totalPath = down+left
            
            memo[(i,j)]= totalPath

            return totalPath


        return dfs(0,0)


  ### bottom-up soltuion
      
        dp = [[0 for _ in range(COL+1)] for _ in range(ROW+1)]

        if not obstacleGrid[ROW-1][COL-1]==1:
            dp[ROW-1][COL-1]=1

        for i in reversed(range(ROW)):
            for j in reversed(range(COL)):
                if i==ROW-1 and j==COL-1:
                    continue
                elif obstacleGrid[i][j]!=1:
                    up = dp[i+1][j]
                    right = dp[i][j+1]
                    dp[i][j]=up+right
                else:
                    dp[i][j]=0

        return dp[0][0]                






                
        
