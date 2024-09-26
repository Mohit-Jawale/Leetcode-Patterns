class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:


        m,n = len(grid),len(grid[0])

        queue = collections.deque([])


        def dfs(r,c,mark):
            nonlocal queue
            if r<0 or c<0 or r>=m or c>=n:
                return
            if grid[r][c] == mark or grid[r][c]==0:
                return 
            
            if grid[r][c]==1:
                grid[r][c] = mark
                if mark == '#':
                    queue.append((r,c,0))
                dfs(r,c+1,mark)
                dfs(r+1,c,mark)
                dfs(r-1,c,mark)
                dfs(r,c-1,mark)
            
                
        flag = 0

        for i in range(m):
            for j in range(n):

                if grid[i][j]==1 and flag==0:
                    dfs(i,j,'#')
                    flag=1
                elif grid[i][j]==1 and flag==1:
                    dfs(i,j,'*')
                    flag=0

        visited = set()

        while queue:

            temp = []
            for r,c,dist in queue:
                for i,j in [(0,1),(1,0),(-1,0),(0,-1)]:
                    ai,aj = r+i,j+c

                    if not(ai<0 or aj<0 or ai>=m or aj>=n) and grid[ai][aj] not in ['#'] and (ai,aj) not in visited:
                        if grid[ai][aj]=='*':
                            return dist
                        else:
                            temp.append((ai,aj,dist+1))
                            visited.add((ai,aj))
        
            queue = temp

                

        
