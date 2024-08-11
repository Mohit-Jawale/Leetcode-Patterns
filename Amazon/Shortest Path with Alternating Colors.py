class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        

        adjList = defaultdict(list)

        for i,j in redEdges:
            adjList[i].append((j,1))
        for i,j in blueEdges:
            adjList[i].append((j,2))

        queue = collections.deque([])
        queue.append((0,0,0))
        visited = set()
        visited.add((0,0))
        ans = [-1]*n

        while queue:

            node, currColor,dist = queue.popleft()
  
            if ans[node]==-1:
                ans[node]=dist
          
            for neighbour,nextColor in adjList[node]:

                if (neighbour,nextColor) not in visited:
                    
                    if currColor == 0:
                        visited.add((neighbour,nextColor))
                        queue.append((neighbour,nextColor,dist+1))
                        
                    elif currColor == 1 and nextColor == 2:
                        visited.add((neighbour,nextColor))
                        queue.append((neighbour,nextColor,dist+1))

                    elif currColor==2 and nextColor == 1:
                        visited.add((neighbour,nextColor))
                        queue.append((neighbour,nextColor,dist+1))
      


        return(ans)

            
        
