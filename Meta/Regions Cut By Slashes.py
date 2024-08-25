class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:


        row1,col1 = len(grid),len(grid[0])

        row2,col2 = 3*row1, 3*col1

        grid2 = [[0]*col2 for _ in range(row2)]


        for i in range(row1):
            for j in range(col1):
                r2,c2 = 3*i,3*j
                if grid[i][j]=='/':
                    grid2[r2][c2+2]=1
                    grid2[r2+1][c2+1]=1
                    grid2[r2+2][c2]=1

                elif grid[i][j]=='\\':
                    grid2[r2][c2]=1
                    grid2[r2+1][c2+1]=1
                    grid2[r2+2][c2+2]=1

   
        def dfs(r,c):
 
            if r<0 or c<0 or r>=row2 or c>=col2:
                return
            if grid2[r][c]==1 or grid2[r][c]=='#':
                return

            if grid2[r][c]==0:
                grid2[r][c] = "#"
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)


        
        count = 0

        for i in range(row2):
            for j in range(col2):

                if grid2[i][j]==0:
                    dfs(i,j)
                    count+=1
    
        return count
        
