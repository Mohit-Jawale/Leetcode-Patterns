class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m,n = len(matrix),len(matrix[0])

        memo = {}

        visited = set()

        def dfs(i,j,prev):

            if i<0 or j<0 or i>=m or j>=n or (i,j) in visited:
                return 0
                
            if prev>=matrix[i][j]:
                return 0

            if (i,j) in memo:
                return memo[(i,j)]

            visited.add((i,j))

            right = dfs(i+1,j,matrix[i][j])+1
            left = dfs(i-1,j,matrix[i][j])+1
            up = dfs(i,j+1,matrix[i][j])+1
            down = dfs(i,j-1,matrix[i][j])+1

            visited.remove((i,j))

            memo[(i,j)] = max(right,left,up,down)

            return memo[(i,j)]

        LIPM = 1
        for i in range(m):
            for j in range(n):
                LIPM = max(dfs(i,j,-float('inf')),LIPM)
        
        return LIPM

