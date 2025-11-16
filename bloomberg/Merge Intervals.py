class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        start,end = intervals[0][0],intervals[0][1]
        mergerd = []

        for nxtStart,nxtEnd in intervals[1:]:

            if nxtStart<=end and nxtEnd>=end:## partial overlap
                start = min(start,nxtStart)
                end = max(end,nxtEnd)
            elif nxtStart<end and nxtEnd<end: ## overshadow
                continue
            else: ### mutually exculsive
                mergerd.append([start,end])
                start,end = nxtStart,nxtEnd
        
        mergerd.append([start,end])

        return mergerd


        
