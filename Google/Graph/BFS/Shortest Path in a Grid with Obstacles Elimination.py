https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/description/
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:

        ### min number steps - > bfs 

        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        m,n = len(grid),len(grid[0])

        grid[0][0] = 0

        queue = collections.deque([(0,0,k,0)])

        visited = set()

        while queue:
            
            x,y,k_left,steps = queue.popleft()

            if x == m-1 and y == n-1:
                return steps

            if (x,y,k_left) in visited:
                continue
                
            visited.add((x,y,k_left))

            for i,j in directions:

                newX,newY = x+i,y+j

                if newX>=0 and newX<m and newY>=0 and newY<n:

                    new_k_left = k_left - grid[newX][newY]
                    state = (newX,newY,new_k_left)

                    if new_k_left>=0 and state not in visited:
                
                        queue.append((newX,newY,new_k_left,steps+1))


        return -1






     
        
