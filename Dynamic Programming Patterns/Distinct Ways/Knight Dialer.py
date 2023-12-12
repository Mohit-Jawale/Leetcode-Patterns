### DFS + memo

class Solution:
    def knightDialer(self, n: int) -> int:

        nums = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
        moves = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]

        ROW,COL = len(nums),len(nums[0])

        MOD = pow(10,9)+7

        memo = {}

        def dfs(i,j,n):

            if (nums[i][j],n) in memo:
                return memo[(nums[i][j],n)]

            if nums[i][j] in ['*','#']:
                return 0

            if n==1:
                return 1

            totalNo = 0

            for r,c in moves:
                if 0<= i+r < ROW and 0<= j+c <COL:
                    totalNo+=dfs(i+r,j+c,n-1)

            memo[(nums[i][j],n)] = totalNo % MOD
            return memo[(nums[i][j],n)]        

        ans = 0
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                if nums[i][j] not in ['*','#']:
                    ans+=dfs(i,j,n) % MOD

        return ans % MOD
### 3d- dp solution

class Solution:
    def knightDialer(self, n: int) -> int:
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
        moves = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]
        ROW, COL = len(nums), len(nums[0])
        MOD = 10**9 + 7

        # Initialize DP table
        dp = [[[0 for _ in range(n + 1)] for _ in range(COL)] for _ in range(ROW)]

        # Base cases
        for i in range(ROW):
            for j in range(COL):
                if nums[i][j] not in ['*', '#']:
                    dp[i][j][1] = 1

        # Fill the DP table
        for step in range(2, n + 1):
            for i in range(ROW):
                for j in range(COL):
                    if nums[i][j] not in ['*', '#']:
                        for r, c in moves:
                            ni, nj = i + r, j + c
                            if 0 <= ni < ROW and 0 <= nj < COL:
                                dp[i][j][step] = (dp[i][j][step] + dp[ni][nj][step - 1]) % MOD

        # Sum up the results
        ans = 0
        for i in range(ROW):
            for j in range(COL):
                ans = (ans + dp[i][j][n]) % MOD

        return ans


        
