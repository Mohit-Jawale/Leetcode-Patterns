class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:


        '''
        At most k meetings
        '''

        meetings = sorted(zip(startTime,endTime))


        meetings = [[-1,0],*meetings,[eventTime, eventTime + 1]]

        n = len(meetings)

        free_time = [meetings[i][0] - meetings[i-1][1] for i in range(1,n)]

        
        window_sum = sum(free_time[:k+1])
        max_free_time = window_sum

        left,right = 0,k+1
        #### if there are k meeting you can move then you can make k+1 gaps
        while right<len(free_time):
            
            window_sum+=free_time[right] - free_time[left]
            max_free_time = max(max_free_time,window_sum)
            right+=1
            left+=1

        return max_free_time




        
