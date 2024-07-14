## DFS + memo
### This problem can enhance thinking on dp on string
### think carryfully all the base cases and recur relation


### dfs +memo

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        
        m,n = len(s1),len(s2)

        memo = {}

        def dfs(i,j):

            if i>=m and j>=n:
                return 0
            if i>=m:
                return sum([ord(s2[k]) for k in range(j,n)])
            if j>=n:
                return sum([ord(s1[k]) for k in range(i,m)])
            if (i,j) in memo:
                return memo[(i,j)]
            
            lowestSum = float('inf')

            if s1[i]==s2[j]:
                lowestSum = min(dfs(i+1,j+1),lowestSum)
            else:
                lowestSum = min(dfs(i+1,j)+ord(s1[i]),dfs(i,j+1)+ord(s2[j]))
            
            memo[(i,j)] = lowestSum
            
            return lowestSum
        
        return dfs(0,0)

        ##### 2d-Dp
        
        dp = [[float('inf') for j in range(n+1)] for i in range(m+1)]

        ### base case 1
        dp[m][n] = 0
        ### base case 2&3
        for j in range(n+1):
            dp[m][j] = sum([ord(s2[k]) for k in range(j,n)])
        for i in range(m+1):
            dp[i][n] = sum([ord(s1[k]) for k in range(i,m)])


        for i in reversed(range(m)):
            for j in reversed(range(n)):

                if s1[i]==s2[j]:
                    dp[i][j] = min(dp[i+1][j+1],dp[i][j])
                else:
                    dp[i][j] = min(dp[i+1][j]+ord(s1[i]),dp[i][j+1]+ord(s2[j]))
        
        return dp[0][0]
            


### old dfs + memo solution
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        m,n = len(s1), len(s2)
        memo = {}

        def dfs(i,j):

            if (i,j) in memo:
                return memo[(i,j)]

            if i==m and j<n:
                return sum([ord(s2[k]) for k in range(j,n)])
            if j==n and i<m:
                return sum([ord(s1[k]) for k in range(i,m)])    
            if i==m or j==n:
                return 0

            lowestSum = 0
            if s1[i]==s2[j]:
                lowestSum = dfs(i+1,j+1)
            else:
                lowestSum = min(dfs(i,j+1) + ord(s2[j]),dfs(i+1,j) + ord(s1[i]))

            memo[(i,j)] = lowestSum
            return lowestSum

        return dfs(0,0)      


        



