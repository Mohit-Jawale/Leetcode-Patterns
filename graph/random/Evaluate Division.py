class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        adjList = defaultdict(list)
        for index,value in enumerate(equations):
            i,j = value
            adjList[i].append((j,values[index]))
            adjList[j].append((i,1/values[index]))
        
        def bfs(node,destinationNode):

            if node not in adjList or destinationNode not in adjList:
                return -1.0
            queue = [(node,1)]
            visited = set()

            while queue:
                node,w = queue.pop(0)

                if node == destinationNode:
                    return w

                for neighbour in adjList[node]:
                    n,weight = neighbour
                    if neighbour not in visited:
                        queue.append((n,weight*w))
                        visited.add(neighbour)
            return -1.0
        ans = []
        for i,j in queries:
            ans.append(bfs(i,j))
        
        return ans
