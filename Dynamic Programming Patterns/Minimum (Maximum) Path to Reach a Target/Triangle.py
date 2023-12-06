class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:


        memo = {}
        def dfs(i,j):

            if i==len(triangle)-1:
                return triangle[i][j]
            if (i,j) in memo:
                return memo[(i,j)]

            minPath = min(dfs(i+1,j),dfs(i+1,j+1))+triangle[i][j]
            memo[(i,j)]= minPath
            return minPath    

        return dfs(0,0)
        
