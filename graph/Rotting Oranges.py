#### remember the edges cases while applying bfs towards infinity
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        moves = [(-1,0),(0,-1),(1,0),(0,1)]
        m,n = len(grid),len(grid[0])
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j))
                elif grid[i][j]==1:
                    grid[i][j]= float('inf')
        
        while queue:

            i,j = queue.pop(0)

            for r,c in moves:
                ai,aj = i+r,j+c
                if not(ai<0 or ai>=m or aj<0 or aj>=n) and grid[ai][aj]>grid[i][j]+1:
                    grid[ai][aj]=grid[i][j]+1
                    queue.append((ai,aj))
        
        ans = max([max(row) for row in grid])
        
        if ans == 0:
            return 0
        elif ans!=float('inf'):
            return ans-2
        else:
            return -1
        

# class Solution:
#     def orangesRotting(self, grid: List[List[int]]) -> int:



#         R, C = len(grid), len(grid[0])
#         fresh = 0
#         queue = []

#         def bfs():

#             min_cnt= 0
#             nonlocal fresh,queue

#             while queue[0] and fresh>0:
                
#                 node = queue.pop(0)
             
#                 temp = []
#                 print(node)
#                 for n in node:
#                     r,c = n[0], n[1]

#                     if r+1<R and grid[r+1][c]==1:
#                         temp.append((r+1,c))
#                         fresh-=1 
#                         grid[r+1][c]=2
#                     if c+1<C and grid[r][c+1]==1:
#                         temp.append((r,c+1))
#                         fresh-=1
#                         grid[r][c+1]=2
#                     if r>=1 and grid[r-1][c]==1:
#                         temp.append((r-1,c))
#                         fresh-=1
#                         grid[r-1][c]=2
#                     if c>=1 and grid[r][c-1]==1:
#                         temp.append((r,c-1))
#                         fresh-=1
#                         grid[r][c-1]=2
                     
#                 queue.append(temp)
          
#                 min_cnt+=1

#             return min_cnt


        
#         temp2 = []
#         for r in range(R):
#             for c in range(C):
#                 if grid[r][c]==2:
#                     temp2.append([r,c])
#                 if grid[r][c]==1:
#                     fresh+=1    
#         queue.append(temp2)     
#         count = bfs()
#         if fresh==0:
#             return count
#         else:
#             return -1    

     
            
