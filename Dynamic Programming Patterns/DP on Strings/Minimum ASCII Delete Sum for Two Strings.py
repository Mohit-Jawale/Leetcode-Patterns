## DFS + memo
### This problem can enhance thinking on dp on string
### think carryfully all the base cases and recur relation
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


        



