class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:


        counter = {}

        for s,e in intervals:
            counter[s]= counter.get(s,0)+1
            counter[e]=counter.get(e,0)-1
        
        min_rooms = -float('inf')
        count = 0
        for point in sorted(counter.keys()):

            count+=counter[point]
            if count>min_rooms:
                min_rooms = max(count,min_rooms)
        
        return min_rooms


            


        
        


       
