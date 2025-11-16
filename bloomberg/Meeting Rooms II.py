class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:


        meetings = []

        for start,end in intervals:
            meetings.append((start,+1))
            meetings.append((end,-1))

        
        meetings.sort(key = lambda x:(x[0],x[1]))

        minConferenceRooms = 0
        activeRooms = 0

        for time,event_type in meetings:
            
            if event_type == 1:
                activeRooms+=1
            else:
                activeRooms-=1
            
            minConferenceRooms = max(minConferenceRooms,activeRooms)
        
        return minConferenceRooms
            






        
