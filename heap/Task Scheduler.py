class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        lookup = Counter(tasks)
        maxHeap = [-i for i in lookup.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = []

        while queue or maxHeap:
            time+=1
 

            if maxHeap:
                top = heapq.heappop(maxHeap) + 1
                if top!=0:
                    queue.append((top,time+n))

            if queue and queue[0][1]==time:
                heapq.heappush(maxHeap,queue.pop(0)[0])

        return time            
