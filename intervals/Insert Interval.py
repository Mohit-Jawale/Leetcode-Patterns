
### Note the Algorithm to check if interval is on left or right or need to merge

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        x,y = newInterval
        ans = []

        for index,interval in enumerate(intervals):
            start = interval[0]
            end = interval[1]
            if y<start:
                ans.append([x,y])
                return ans +intervals[index:]
            elif x>end:
                ans.append([start,end])
            #merge    
            else:
                x = min(x,start)
                y = max(y,end)

        ans.append([x,y])
        
        return ans            
