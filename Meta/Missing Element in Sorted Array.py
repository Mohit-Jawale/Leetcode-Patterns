class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:


        left,right = 0,len(nums)-1
        index = -1

        while left<=right:

            mid = left+ (right-left)//2

            value = nums[mid]-nums[0] - mid

            if value<k:
                left = mid+1
            else:
                right = mid-1
                
        ### here left is total elements in the array , k-1 is total missing number
        return nums[0]+left+k-1


             

        
