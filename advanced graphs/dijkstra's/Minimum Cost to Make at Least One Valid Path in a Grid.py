class Solution:
    def minCost(self, grid: List[List[int]]) -> int:

        m,n = len(grid),len(grid[0])
        adjList = collections.defaultdict(list)


        for i in range(m):
            for j in range(n):


                if i<m and grid[i][j]==3:
                    adjList[(i,j)].append((i+1,j,0))
                elif i<m and grid[i][j]!=3:
                    adjList[(i,j)].append((i+1,j,1))
                else:
                    adjList[(i,j)].append((i+1,j,float('inf')))


                if j<n and grid[i][j]==1:
                    adjList[(i,j)].append((i,j+1,0))
                elif j<n and grid[i][j]!=1:
                    adjList[(i,j)].append((i,j+1,1))
                else:
                    adjList[(i,j)].append((i,j+1,float('inf')))

                
                if j>0 and grid[i][j]==2:
                    adjList[(i,j)].append((i,j-1,0))
                elif j>0 and grid[i][j]!=2:
                    adjList[(i,j)].append((i,j-1,1))
                else:
                    adjList[(i,j)].append((i,j-1,float('inf')))
                

                if i>0 and  grid[i][j]==4:
                    adjList[(i,j)].append((i-1,j,0))
                elif i>0 and  grid[i][j]!=4:
                    adjList[(i,j)].append((i-1,j,1))
                else:
                    adjList[(i,j)].append((i-1,j,float('inf')))
        
        
        queue = [(w,s,e) for s,e,w in adjList[(0,0)]]
        heapq.heapify(queue)
        visited = set()

        while queue:
          
            w,s,e = heapq.heappop(queue)

            if (s,e) in visited:
                continue

            visited.add((s,e))

            if s==m-1 and e == n-1:
                return w

            for s1,e1,w1 in adjList[(s,e)]:
                if (s1,e1) not in visited:
                    heapq.heappush(queue,(w+w1,s1,e1))
        
        return 0
            

        

        








                

                

        
