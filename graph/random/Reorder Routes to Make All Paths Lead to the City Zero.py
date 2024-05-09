class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:

        inConnections = set([(i,j) for i,j in connections])

        adjList = collections.defaultdict(list)

        for i,j in connections:
            adjList[i].append(j)
            adjList[j].append(i)
        
        visited = set()
        minNum = 0
        def dfs(node):

            nonlocal minNum
            if node in visited:
                return

            visited.add(node)

            for neighbour in adjList[node]:
                if neighbour not in visited:
                    if (neighbour,node) not in inConnections:
                        minNum+=1
                    dfs(neighbour)
            
        
        dfs(0)
        return minNum


        
