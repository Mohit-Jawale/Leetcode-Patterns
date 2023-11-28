class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        ones,zeros = 0,0
        left,right = 0,0

        ans = 0

        while right<len(nums):

            if nums[right]==1:
                ones+=1
            elif nums[right]==0:
                zeros+=1

            while left<=right and zeros>k:
                if nums[left]==1:
                    ones-=1
                elif nums[left]==0:
                    zeros-=1
                left+=1

            ans = max(right-left+1,ans)
            right+=1

        return ans                       

        
        
