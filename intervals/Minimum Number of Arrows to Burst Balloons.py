class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:


        points.sort()
        prevEnd = points[0][1]
        count=0

        for start,end in points[1:]:
            if prevEnd>=start:
                count+=1
                prevEnd = min(prevEnd,end)
            else:
                prevEnd = end
        
        return len(points) - count


