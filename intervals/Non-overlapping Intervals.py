### remember the case that we have to remove the min end of two overlapping intervals bcz the bigger one might overlap again


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort()
        count = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if prevEnd> start:
                count+=1
                prevEnd = min(prevEnd,end)
            else:
                 prevEnd = end

        return count         

