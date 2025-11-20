class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        adjList = collections.defaultdict(list)

        for s,d,weight in flights:
            adjList[s].append((d,weight))

        queue = [[0,0,src]]
        heapq.heapify(queue) ##[weight,k,nextStop]

        visited = [[float('inf') for _ in range(k+2)] for _ in range(n)]

        visited[src][0] = 0


        while queue:

            weight,total_stops,curr_stop = heapq.heappop(queue)

            if total_stops>k+1:
                continue
    
            if curr_stop == dst:
                return weight
        
            if total_stops == k + 1:
                continue

            for nextStop,dist in adjList[curr_stop]:



                if  total_stops<=k+1 and visited[nextStop][total_stops+1]>weight+dist:
                    heapq.heappush(queue,[dist+weight,total_stops+1,nextStop])
                    visited[nextStop][total_stops+1] = dist+weight
                    


        return -1
