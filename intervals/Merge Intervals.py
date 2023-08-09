class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        non_overlapping = []
        intervals.sort()
        i,j = 0 , 1
        istart = intervals[i][0]
        iend = intervals[i][1]      

        while j<=(len(intervals)-1):
 
            jstart = intervals[j][0]
            jend = intervals[j][1]

            if iend<jstart:
                non_overlapping.append([istart,iend])
                i=j
                j+=1
                istart = intervals[i][0]
                iend = intervals[i][1]   
            else:    
                istart = min(istart,jstart)
                iend = max(iend,jend)
                j+=1
        non_overlapping.append([istart,iend])

        return non_overlapping


