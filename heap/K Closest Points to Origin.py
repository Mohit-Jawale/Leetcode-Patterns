import heapq as hq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        distances = []
        ans = []
        for x,y in points:
            distances.append((math.sqrt((x*x)+(y*y)),[x,y]))

        hq.heapify(distances)

        while len(ans)<k:
            ans.append(hq.heappop(distances)[1])

        return ans    


