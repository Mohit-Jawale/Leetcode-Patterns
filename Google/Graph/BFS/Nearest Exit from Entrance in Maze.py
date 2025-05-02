class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        
        Rows, Cols = len(maze), len(maze[0])

        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        queue = collections.deque([[entrance[0],entrance[1],0]])

        visited = set()


        while queue:

            x,y, distance = queue.popleft()
        
            if (x==0 or x==Rows-1 or y==0 or y==Cols-1) and entrance!=[x,y]:
                return distance 

            if (x,y) in visited:
                continue
            
            visited.add((x,y))

            for i,j in directions:

                newX,newY = x+i,y+j

                if newX>=0 and newX<Rows and newY>=0 and newY<Cols:

                    if maze[newX][newY]=='+':
                        continue
                    if maze[newX][newY] == '.' and maze[newX][newY] not in visited:
                        queue.append([newX,newY,distance+1])
                        

        return -1


