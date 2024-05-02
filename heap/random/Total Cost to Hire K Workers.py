class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:

        firstCandidates = []
        lastCandidates = []
        firstPtr,secondPtr = 0,len(costs)-1

        if len(costs)>candidates*2:
            for num in costs[:candidates]:
                heapq.heappush(firstCandidates,num)
            for num in costs[-candidates:]:
                heapq.heappush(lastCandidates,num)
            firstPtr+=candidates
            secondPtr-=candidates
        else:
            for num in costs[:candidates]:
                heapq.heappush(firstCandidates,num)
            for num in costs[candidates:]:
                heapq.heappush(lastCandidates,num)
            firstPtr = secondPtr
            secondPtr = 0

        cost = 0
        
        while k>0:
            k-=1
            if firstCandidates and not lastCandidates:
                cost+=heapq.heappop(firstCandidates)
            elif not firstCandidates and lastCandidates:
                cost+=heapq.heappop(lastCandidates)
            else:
                
                if firstCandidates[0]<=lastCandidates[0]:
                    cost+=heapq.heappop(firstCandidates)
                    if firstPtr<=secondPtr:
                        heapq.heappush(firstCandidates,costs[firstPtr])
                        firstPtr+=1
                else:
                    cost+=heapq.heappop(lastCandidates)
                    if firstPtr<=secondPtr:
                        heapq.heappush(lastCandidates,costs[secondPtr])
                        secondPtr-=1
        
        return cost



        






        
