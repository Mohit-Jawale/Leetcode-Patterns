class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:

        '''
        theif - > 1
        empty ->0

        2 1 1
        3 2 1
        4 2 2

        multi source BFS from theif
        BFS+maxheap

        '''

        
        ROWS, COLS = len(grid), len(grid[0])

        if grid[0][0]==1 or grid[ROWS-1][COLS-1]==1:
            return 0

        queue = collections.deque([])

        theifs = set()

        for row in range(ROWS):
            for col in range(COLS):

                if grid[row][col]==0:
                    grid[row][col]=float('inf')
                if grid[row][col]==1:
                    grid[row][col]=0
                    queue.append((row,col))
                    theifs.add((row,col))
        
        directions = [(1,0),(0,1),(-1,0),(0,-1)]



        while queue:

            i,j = queue.popleft()

            for dr,dc in directions:

                newRow,newCol = dr+i,dc+j

                if newRow>=0 and newCol>=0 and newRow<ROWS and newCol<COLS:


                    if grid[newRow][newCol]>grid[i][j]+1 :
                        grid[newRow][newCol] = grid[i][j]+1
                        queue.append((newRow,newCol))
        

        priority_queue = [(-grid[0][0],0,0)]

        heapq.heapify(priority_queue)

        visited = set()

        while priority_queue:

            
            saftey_factor,row,col = heapq.heappop(priority_queue)

            if row == ROWS-1 and col==COLS-1:
                return -saftey_factor

            if (row,col) in visited:
                continue
            
            visited.add((row,col))

            for dr,dc in directions:

                newRow,newCol = dr+row,dc+col

                if newRow>=0 and newCol>=0 and newRow<ROWS and newCol<COLS and (newRow,newCol) not in theifs:
                    
                    new_min_safety_factor = min(grid[newRow][newCol],-saftey_factor)
                    heapq.heappush(priority_queue,(-new_min_safety_factor,newRow,newCol))



        return 0



        
        

        


        
