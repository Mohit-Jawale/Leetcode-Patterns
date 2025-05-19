class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        counter = Counter()

        for start, end in intervals:
            counter[start]+=1
            counter[end]-=1
        
        min_number_rooms = 0
        live_meeting = 0

        for key in sorted(counter.keys()):

        
            live_meeting+=counter[key]

            min_number_rooms = max(live_meeting,min_number_rooms)
        
        return min_number_rooms


        
