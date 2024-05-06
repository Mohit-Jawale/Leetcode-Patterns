class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        ans  = [-1,-1]
        ## lower bound

        left,right = 0,len(nums)

        while left<right:

            mid = left+(right-left)//2

            if nums[mid]>=target:
                right = mid
            else:
                left = mid+1
        
        if left<len(nums) and nums[left]==target:
            ans[0]=left
        else:
            ans[0]=-1
        
        ### upper bound

        
        left,right = 0,len(nums)

        while left<right:

            mid = left+(right-left)//2

            if nums[mid]<=target:
                left = mid+1
            else:
                right = mid
        
        if left>0 and nums[left-1]==target:
            ans[1]=left-1
        else:
            ans[1]=-1
    

        return ans
               
        


        
