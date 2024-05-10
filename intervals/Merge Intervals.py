class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        intervals = sorted(intervals,key = lambda x : x[0])
        mergedIntervals = []
        if intervals:
            mergedIntervals.append(intervals[0])
            intervals.pop(0)

        for start,end in intervals:
            lastStart,lastEnd = mergedIntervals[-1]
            ### they is overlapping b/w intervals
            if lastEnd>=start and end>=lastEnd:
                mergedIntervals[-1][1] = end
            ### this is complete overlap
            elif lastEnd>=start and end<lastEnd:
                continue
            else:
                mergedIntervals.append([start,end])
                

        return mergedIntervals




# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:

#         non_overlapping = []
#         intervals.sort()
#         i,j = 0 , 1
#         istart = intervals[i][0]
#         iend = intervals[i][1]      

#         while j<=(len(intervals)-1):
 
#             jstart = intervals[j][0]
#             jend = intervals[j][1]

#             if iend<jstart:
#                 non_overlapping.append([istart,iend])
#                 i=j
#                 j+=1
#                 istart = intervals[i][0]
#                 iend = intervals[i][1]   
#             else:    
#                 istart = min(istart,jstart)
#                 iend = max(iend,jend)
#                 j+=1
#         non_overlapping.append([istart,iend])

#         return non_overlapping


