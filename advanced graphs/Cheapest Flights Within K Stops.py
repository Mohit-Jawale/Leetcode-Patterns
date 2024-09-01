class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        

        adjList = collections.defaultdict(list)

        for u,v,w in flights:
            adjList[u].append((v,w))

        queue = collections.deque([(src,0,k+1)])


        dist = [float('inf')]*n
        dist[src]=0

        while queue:

            node,price,k = queue.popleft()

            for neighbour,cost in adjList[node]:
                if dist[neighbour]>cost+price and k>0:
                    dist[neighbour] = cost+price
                    queue.append((neighbour,dist[neighbour],k-1))
        

        return dist[dst] if dist[dst] != float('inf') else -1



