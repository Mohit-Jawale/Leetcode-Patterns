
#### great questions for line sweep

#### refer this for intuition -:https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/solutions/6171514/python3-c-java-go-sweep-line-detailed-solution/?envType=company&envId=google&favoriteSlug=google-thirty-days
class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:


        horizontal_axis, vertical_axis = Counter(), Counter()

        for sx,sy,ex,ey in rectangles:
            horizontal_axis[sx+0.1]+=1
            horizontal_axis[ex]-=1
            vertical_axis[sy+0.1]+=1
            vertical_axis[ey]-=1
        

        def lineSweep(area):

            prev_area = curr_area = count = 0

            sorted_area = list(sorted(area.items()))

            for k,v in sorted_area:

                prev_area = v
                curr_area += v

                if prev_area!=0 and curr_area==0:
                    count+=1
                    
            return True if count>2 else False
        
        return lineSweep(horizontal_axis) or lineSweep(vertical_axis)


        
