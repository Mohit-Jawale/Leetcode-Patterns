### this is hard problem but conceptual if understand the bitmasking basics. BFS is simople
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:


        Rows,Cols = len(grid),len(grid[0])

        startCell = ()

        keys = 0

        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        for i in range(Rows):
            for j in range(Cols):

                if grid[i][j]=='@':
                    startCell = (i,j)
                
                if 'a'<=grid[i][j]<='f':
                    keys+=1
                    


        queue = collections.deque([[startCell[0],startCell[1],0,0]])

        visited = set()

        while queue:
            
            x,y,totalKeys,moves = queue.popleft()


            if totalKeys == (1<<keys)-1:
                return moves

            if (x,y,totalKeys) in visited:
                continue
            
            visited.add((x,y,totalKeys))


            for i,j in directions:

                newX,newY = x+i, y+j

                if newX>=0 and newX<Rows and newY>=0 and newY<Cols:

                    if grid[newX][newY]=='#':
                        continue
                    
                    newKeys = totalKeys

                    if 'a'<= grid[newX][newY] <='f':

                        newKeys = newKeys | (1<< (ord(grid[newX][newY])-ord('a')))
                    
            
                    if 'A' <= grid[newX][newY] <= 'F':

                        if not (totalKeys & (1<< (ord(grid[newX][newY].lower())-ord('a')))):
                            continue
                    
                    queue.append([newX,newY,newKeys,moves+1])
        return -1


                    
                        




        
