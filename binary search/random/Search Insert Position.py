class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left,right = 0,len(nums)

        while left<right:
            mid = left+ (right-left)//2
            ### find min position where the target is grter than equal to rest of the numbers
            if target<=nums[mid]:
                right = mid
            else:
                left = mid+1

        return left            
