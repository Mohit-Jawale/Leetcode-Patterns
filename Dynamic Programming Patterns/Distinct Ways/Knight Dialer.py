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

        
