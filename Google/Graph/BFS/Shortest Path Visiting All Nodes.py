class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        ### Time complexity and Spaceis O(N*2^n)

        queue = collections.deque([(1<<i,i,0) for i in range(len(graph))])

        visited = set()

        while queue:

            mask,node,dist = queue.popleft()

            if mask == (1<<len(graph))-1:
                return dist

            if (mask,node) in visited:
                continue
            
            visited.add((mask,node))


            for neighbour in graph[node]:

                newMask = mask | 1<<neighbour
                queue.append((newMask,neighbour,dist+1))

        return -1
