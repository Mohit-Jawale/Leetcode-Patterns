class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        

        adjList = collections.defaultdict(list)

        for index,value in enumerate(equations):
            start,end = value
            adjList[start].append((end,values[index]))
            adjList[end].append((start,1/values[index]))

        
        def bfs(start,end):

            queue = collections.deque([[start,1]])
            visited = set()
            

            while queue:

                node,value = queue.popleft()

                if node == end :
                    return value
               
                for neighbour,weight in adjList[node]:
                    if neighbour not in visited:
                        queue.append([neighbour,value*weight])
                        visited.add(node)

        
            return -1.0
        

        ans = []

        for start,end in queries:
            if start in adjList and end in adjList:
                ans.append(bfs(start,end))
            else:
                ans.append(-1.0)
        return ans
                

                
