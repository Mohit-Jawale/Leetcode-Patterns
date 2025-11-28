class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:


        if grid[0][0]==1 or grid[-1][-1]==1:
            return -1

        moves = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]

        queue = collections.deque([[0,0,1]])

        visited = set()

        visited.add((0,0))

        while queue:
            x,y,dist = queue.popleft()

            if x == len(grid)-1 and y==len(grid[0])-1:
                return dist

            for dirX,dirY in moves:

                newX,newY = x+dirX, dirY+y
                if newX>=0 and newY>=0 and newX<len(grid) and newY<len(grid[0]) and (newX,newY) not in visited and grid[newX][newY]!=1:
                    queue.append([newX,newY,dist+1])
                    visited.add((newX,newY))
        

        return -1
