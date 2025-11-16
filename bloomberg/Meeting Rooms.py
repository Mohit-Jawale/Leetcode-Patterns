class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:

        meetings = []
        for start,end in intervals:
            meetings.append((start,+1))
            meetings.append((end,-1))

        meetings.sort(key = lambda x :(x[0],x[1]))
        count = 0

        for time,event_type in meetings:

            if event_type==1:
                count+=1
            else:
                count-=1
            
            if count>1:
                return False
        
        return True


        
