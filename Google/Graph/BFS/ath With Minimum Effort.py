import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:


        Rows,Cols = len(heights), len(heights[0])

        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        queue = [(0,0,0)] ### (totaleffort,x,y)

        effort = [[float('inf') for _ in range(Cols)]  for _ in range(Rows)]
        effort[0][0] = 0

        heapq.heapify(queue)
    

        while queue:


            total_efforts,x,y = heapq.heappop(queue)


            if x==Rows-1 and y==Cols-1:
                return total_efforts

            for i,j in directions:

                newX,newY = x+i , y+j

                if newX>=0 and newX<Rows and newY>=0 and newY<Cols:

                    diff = abs(heights[newX][newY] - heights[x][y])
                    new_effort = max(total_efforts, diff)

                    if new_effort<effort[newX][newY]:
                        effort[newX][newY] = new_effort
                        heapq.heappush(queue,(new_effort,newX,newY))


        return -1


        
