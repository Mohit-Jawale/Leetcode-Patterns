### This has good use of two pointer technique and the left<=right eqaul condition is critical.

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        left = 0
        right = len(nums)-1
        count=0

        while left<=right:
            if nums[left] == val:
                nums[left],nums[right] = nums[right], nums[left]
                right-=1
            else:
                count+=1 
                left+=1
           
       
        return count      


        
