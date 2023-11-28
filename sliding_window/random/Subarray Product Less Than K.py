class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k==0:
            return 0

        left,right = 0,0
        ans = 0
        prod = 1

        while right<len(nums):

            prod*=nums[right]

            while left<=right and  prod>=k:
                prod//=nums[left]
                left+=1

            ans += right-left+1
            right+=1

        return ans        
