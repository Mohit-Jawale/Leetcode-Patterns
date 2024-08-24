class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:



        m,n = len(grid),len(grid[0])
        moves = [[1,0],[0,1],[-1,0],[0,-1]]

        def dfs(i,j):

            nonlocal island
            if i<0 or j<0 or i>=m or j>=n:
                return
            
            if grid[i][j]==1:
                grid[i][j]='#'
                island.add((i,j))
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)
        
        for r in range(m):
            for c in range(n):
                island = set()
                if grid[r][c]==1:
                    dfs(r,c)
                count = len(island)

                for u,v in island:
                    grid[u][v]=(count,(r,c))

        maxIsland = 1
        flag = 0
   
        for r in range(m):
            for c in range(n):
                uniquePath = set()
                ans = 0
                if grid[r][c]==0:
                    flag = 1
                    for i,j in moves:
                        ar,ac = r+i,j+c
                        if not (ar<0 or ac<0 or ar>=m or ac>=n) and grid[ar][ac]!=0:
                            
                            uniquePath.add(grid[ar][ac])

                for i,j in list(uniquePath):
                    ans+=i
                    
                maxIsland = max(maxIsland,ans+1)

        return maxIsland if flag == 1 else grid[0][0][0]


        
