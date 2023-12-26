class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0]==1 or grid[-1][-1]!=0:
            return -1
        m,n = len(grid),len(grid[0])

        moves = [(-1,0),(0,-1),(1,0),(0,1),(-1,1),(1,-1),(1,1),(-1,-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    grid[i][j]=float('inf')
        
       
        grid[0][0]=0
        queue = [(0,0)]
        while queue:
            i,j  = queue.pop(0)

            for r,c in moves:
                ai,aj = i+r,j+c
                if not (ai<0 or ai>=m or aj<0 or aj>=n) and grid[ai][aj]>grid[i][j]+1:
                    grid[ai][aj] = grid[i][j]+1
                    queue.append((ai,aj))
        

        return grid[-1][-1]+1 if grid[-1][-1]!=float('inf') else -1

        
