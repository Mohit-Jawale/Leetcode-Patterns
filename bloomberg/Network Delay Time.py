class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_list = defaultdict(list)

        for s,d,w in times:
            adj_list[s].append((d,w))

        minHeap = [(0,k)]
        visited = [float('inf')]*(n+1)
        visited[k] = 0

        while minHeap:

            w1,node = heapq.heappop(minHeap)           

            for neighbour,weight in adj_list[node]:

                if weight+w1<visited[neighbour]:
                    heapq.heappush(minHeap,(w1+weight,neighbour))
                    visited[neighbour] = weight+w1

        visited[0]=-1
        ans = max(visited)   
        return ans if ans!=float('inf') else -1 





        
