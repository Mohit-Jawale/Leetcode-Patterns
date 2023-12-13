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

### 2d-dp solution here observer the loops are reversed

class Solution:
    def knightDialer(self, n: int) -> int:

        nums = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
        moves = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[-1,2],[1,-2],[-1,-2]]

        ROW,COL = len(nums),len(nums[0])

        MOD = pow(10,9)+7

                    
        dp = [[0 for _ in range(n+1)] for _ in range(10)]
        
        dp_to_num_mapper = {}
        for r in range(ROW):
            for c in range(COL):
                if nums[r][c] not in ['*','#']:
                    dp_to_num_mapper[nums[r][c]]=(r,c)

        for i in range(10):
            dp[i][1]=1

        ### here when we draw the table we realised that we need prev col first to fill the n
        ### thats y we swap the loop... the iteration in vertical rather than horizontal.
        for j in range(2,n+1):
            for i in range(10):
                ar,ac = dp_to_num_mapper[i]
                for r,c in moves:
                    if 0<= ar+r < ROW and 0<= ac+c <COL and nums[ar+r][ac+c] not in ['*','#']:
                        dp[i][j]+=dp[nums[ar+r][ac+c]][j-1] % MOD

        totalNo = 0 
        for i in range(len(dp)):
            totalNo+=dp[i][-1] % MOD

        return  totalNo % MOD               

        
