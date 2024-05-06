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

            if nums[mid]<=target: ### find the num in the array where target is grt than eq to number.
                left = mid+1
            else:
                right = mid
        
        if left>0 and nums[left-1]==target:
            return left-1
        else:
            return -1

### find the lower bound
left,right = 0,len(nums)

while left<right:
    mid = (left+right)//2

    if nums[mid]>=target: ### find the number in the array where target is less than or eq to the number.
        right = mid
    else:
        left = mid+1

if left<len(nums) and nums[left]==target:
    return left
else:
    return -1


        

