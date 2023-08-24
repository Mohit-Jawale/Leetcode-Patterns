class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_list = defaultdict(list)

        for s,d,w in times:
            adj_list[s].append((d,w))

        minHeap = [(0,k)]
        visited = set()
        t = 0

        while minHeap:

            w1,node = heapq.heappop(minHeap)
            
            if node in visited:
                continue

            visited.add(node)
            t = max(w1,t)
            for neighbour in adj_list[node]:
                if neighbour[0] not in visited:
                    heapq.heappush(minHeap,(w1+neighbour[1],neighbour[0]))

        return t if len(visited)==n else -1           





        
