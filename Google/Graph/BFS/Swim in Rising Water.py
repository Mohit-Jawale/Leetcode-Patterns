class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        ##### apply dkitras algo on matrix
        ##### bfs+heap+infinity distane array
        #### step 1 : declare the infinity matrix
        #### step2: start from (0,0) bfs with queue and fill the matrix

        #### this is modified version of djiktras algorithm

        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        ROWS, COLS = len(grid), len(grid[0]) 

        queue = []
        
        visited = set()

        queue.append((grid[0][0],0,0))
    
        heapq.heapify(queue)


        while queue:

            max_elevation_so_far,row,col = heapq.heappop(queue)

            if (row == ROWS-1 and col == COLS-1):
                return max_elevation_so_far
                        
           
            for i,j in directions:

                newRow , newCol = row+i , col+j

                if newRow>=0 and newCol>=0 and newRow<ROWS and newCol<COLS: 
                    if (newRow,newCol) not in visited:
                        visited.add((newRow,newCol))
                        newCost = max(max_elevation_so_far,grid[newRow][newCol])
                        heapq.heappush(queue,(newCost,newRow,newCol))
        

        
       
          
               
        

        


                        









        
