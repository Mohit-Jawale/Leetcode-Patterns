class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        

        indegree = defaultdict(int)
        adjList = defaultdict(list)

        for i,j in edges:
            if i == destination:
                return False
            adjList[j].append(i)
            indegree[i]+=1
        
        queue = collections.deque([destination])
        
        while queue:
            node = queue.popleft()

            if node == source:
                return True

            for neighbour in adjList[node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)
        

        return False
