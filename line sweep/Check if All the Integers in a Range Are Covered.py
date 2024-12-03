class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:


        diff_arr = [0]*52

        for s,e in ranges:
            diff_arr[s]+=1
            diff_arr[e+1]-=1
        

        for i in range(1,52):

            diff_arr[i]+=diff_arr[i-1]

            if i>=left and i<=right and diff_arr[i]<=0:
                return False
        
        return True


        
       
        







        
