class Solution:
    def search(self, nums: List[int], target: int) -> int:

        ### this is normal bs
        left = 0
        right = len(nums)-1
        
        while left<=right:

            middle = (left+right)//2

            if nums[middle]==target:
                return middle
            else:
                if nums[middle]>target:
                    right = middle-1
                else:
                    left = middle+1
         

        return -1  
        

#### This is upper bound variation
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left,right = 0,len(nums)

        while left<right:
            mid = (left+right)//2

            if nums[mid]<=target:
                left = mid+1
            else:
                right = mid
        
        if left>0 and nums[left-1]==target:
            return left-1
        else:
            return -1

        

