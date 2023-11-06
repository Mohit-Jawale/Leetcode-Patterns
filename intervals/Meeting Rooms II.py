
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        rooms=0
        ans = 0
        s,e = 0,0

        while s<len(intervals):

            if start[s]<end[e]:
                s+=1
                rooms+=1
            else:
                e+=1
                rooms-=1
            ans = max(ans,rooms)

        return ans            

        

        
