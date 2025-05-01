class Solution:
    def minCost(self, grid: List[List[int]]) -> int:


        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        lookup = {(0,1):1,
        (0,-1):2,
        (1,0):3,
        (-1,0):4
        }

        m,n = len(grid),len(grid[0])

        queue = collections.deque([(0,0,0)]) ###(x,y,cost)

        visited = set()

        while queue:

            x,y,cost = queue.popleft()

            if x==m-1 and y == n-1:
                return cost

            if (x,y) in visited:
                continue
            
            visited.add((x,y))

            for i,j in directions:

                newX,newY = x+i, y+j

                if newX>=0 and newX<m and newY>=0 and newY<n:

                    if grid[x][y] == lookup[(i,j)]:### free
                        queue.appendleft((newX,newY,cost))
                    else:### cost
                        queue.append((newX,newY,cost+1))
            






        
