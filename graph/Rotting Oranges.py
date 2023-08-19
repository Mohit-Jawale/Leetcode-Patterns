class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:



        R, C = len(grid), len(grid[0])
        fresh = 0
        queue = []

        def bfs():

            min_cnt= 0
            nonlocal fresh,queue

            while queue[0] and fresh>0:
                
                node = queue.pop(0)
             
                temp = []
                print(node)
                for n in node:
                    r,c = n[0], n[1]

                    if r+1<R and grid[r+1][c]==1:
                        temp.append((r+1,c))
                        fresh-=1 
                        grid[r+1][c]=2
                    if c+1<C and grid[r][c+1]==1:
                        temp.append((r,c+1))
                        fresh-=1
                        grid[r][c+1]=2
                    if r>=1 and grid[r-1][c]==1:
                        temp.append((r-1,c))
                        fresh-=1
                        grid[r-1][c]=2
                    if c>=1 and grid[r][c-1]==1:
                        temp.append((r,c-1))
                        fresh-=1
                        grid[r][c-1]=2
                     
                queue.append(temp)
          
                min_cnt+=1

            return min_cnt


        
        temp2 = []
        for r in range(R):
            for c in range(C):
                if grid[r][c]==2:
                    temp2.append([r,c])
                if grid[r][c]==1:
                    fresh+=1    
        queue.append(temp2)     
        count = bfs()
        if fresh==0:
            return count
        else:
            return -1    

     
            
