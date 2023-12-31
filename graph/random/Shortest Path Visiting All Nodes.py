### First of all this is amazing question, its has amazing multi-bfs + bitmasking concept which I called Advanced BFS search
### each bit in the bitmask represent stage
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        n = len(graph)
        queue = collections.deque([(1<<i,i,0)for i in range(n)])
        visited = set((1<<i,i) for i in range(n))
        
        while queue:
            print(queue)
            mask,node,dist = queue.popleft()
            
            if mask == (1<<n)-1:
                return dist

            for neighbour in graph[node]:
                newMask = mask | (1<<neighbour)
                if (newMask,neighbour) not in visited:
                    queue.append((newMask,neighbour,dist+1))
                    visited.add((newMask,neighbour))


        
