class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        prevEnd = intervals[0][1]
        count = 0

        for start,end in intervals[1:]:
            if prevEnd>start:## there is overlapp
                count+=1
                prevEnd = min(prevEnd,end)### deleting the bigger interval bcz it might overlap with more intervals
            else:
                prevEnd = end
        
        return count

        
