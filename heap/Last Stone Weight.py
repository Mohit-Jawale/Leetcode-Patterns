### max is reverse of min heap remember this 


import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [i*-1 for i in stones]
        hq.heapify(stones)
       
        while len(stones)>1:
            stone1 = hq.heappop(stones)*(-1)
            stone2 = hq.heappop(stones)*(-1)
            if stone1 == stone2:
                continue
            else:
                hq.heappush(stones,(-1)*(stone1-stone2))

        return -stones[0] if len(stones)==1 else 0         

