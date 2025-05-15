class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:

        unique_island = set()

        m,n = len(grid),len(grid[0])


        def dfs(r,c,direction):

            nonlocal path_signature
            
            if r<0 or c<0 or r>=m or c>=n:
                return ""
            
            if grid[r][c]==1 and grid[r][c]!='#':
                grid[r][c] = '#'
                path_signature.append(direction)
                dfs(r+1,c,'D')
                dfs(r-1,c,'U')
                dfs(r,c+1,'R')
                dfs(r,c-1,'L')
                path_signature.append('*') #### this is imp, this show you have explored all the path from that position

        
        for i in range(m):
            for j in range(n):

                if grid[i][j]==1:
                    path_signature = []
                    dfs(i,j,'*')
                    unique_island.add(tuple(path_signature))

        return len(unique_island)
