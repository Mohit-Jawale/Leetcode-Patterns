class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        
        def get_mintues(time):

            hours,minutes = map(int,time.split(':'))
            return hours*60 + minutes
        

        minutes = [get_mintues(time) for time in timePoints]

        minutes.sort()

        min_diff = float('inf')

        for i in range(len(minutes)-1):
            min_diff = min(min_diff,minutes[i+1]-minutes[i])
        
        min_diff = min(min_diff,1440-(minutes[-1]-minutes[0]))
        return min_diff
