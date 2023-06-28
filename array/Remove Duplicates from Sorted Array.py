
#### Good example of two pointer, swapping and fast, slow technique
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left,right = 0,1
        count = 0

        while right<=len(nums)-1:
            if nums[left]==nums[right]:
                right+=1
            else:
                left+=1
                nums[left],nums[right]=nums[right], nums[left]
                right+=1

        return left+1            
