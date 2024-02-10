class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:



        left,right = 0,len(arr)-1

        while right - left >=k:
            
            ### imagine this is on [2,1,0,1,2] is the abs diff so if now if value at left if grt then right move left bcz we want smaller value
            if abs(x - arr[left]) > abs(x - arr[right]):
                left+=1
            else:
                right-=1

        return arr[left:right+1]      
        




        
