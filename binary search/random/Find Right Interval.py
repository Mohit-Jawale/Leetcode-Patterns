##### there are lots of things going on be careful understand the question and plan all step ahead
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:


        sorted_intervals = sorted(intervals,key = lambda x: x[0])

        startPoints = {}
        for index,interval in enumerate(intervals):
            startPoints[interval[0]] =index
        

        results = [-1]*len(intervals)

        for index,interval in enumerate(intervals):

            idx = bisect_left(sorted_intervals,[interval[1],-float('inf')])

            ##avoid overflow if all elements are smaller than the interval
            if idx!=len(intervals):
                results[index] = startPoints[sorted_intervals[idx][0]]
        
        return results

        
