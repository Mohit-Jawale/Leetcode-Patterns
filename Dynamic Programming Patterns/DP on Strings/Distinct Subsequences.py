### DFS + memo
### neetcode video is good if you loose intution while revising
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        m,n = len(s),len(t)

        memo = {}

        def dfs(i,j):

            if (i,j) in memo:
                return memo[(i,j)]

            if j>=n:
                return 1   
            if i>=m:
                return 0
 
            totalUniqueWays = 0

            if s[i]==t[j]:
                totalUniqueWays = (dfs(i+1,j))+(dfs(i+1,j+1))
            else:
               totalUniqueWays =  dfs(i+1,j)    

            memo[(i,j)] = totalUniqueWays
            return totalUniqueWays


        return dfs(0,0)       


