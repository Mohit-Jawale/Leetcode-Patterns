class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
 
        zeroPtr = 0

        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i],nums[zeroPtr] = nums[zeroPtr],nums[i]
                zeroPtr+=1
          


 
        
                
                


        

        
