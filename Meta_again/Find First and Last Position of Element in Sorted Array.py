class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:


        ans = []

        left,right = 0,len(nums)

        ### lower bound

        def lower_bound(left,right):

            while left<right:

                mid = left+(right-left)//2

                if nums[mid]>=target:
                    right = mid
                else:
                    left = mid+1
            
            return left if left<len(nums) and nums[left]==target else -1
        
        ### upper bound

        def upper_bound(left,right):

            while left<right:

                mid = left+(right-left)//2

                if nums[mid]>target:
                    right = mid
                else:
                    left = mid+1
            
            return left-1 if left-1>=0  and nums[left-1]==target else -1


        first_index = lower_bound(0,len(nums))
        last_index = upper_bound(0,len(nums))

        ans = [first_index,last_index]

        return ans
            

            


        
