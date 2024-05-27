class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        left,right = 0 , 0
        ans = 0
        ones = 0
        zeros = 0

        while right<len(nums):
            if nums[right]==0:
                zeros+=1
            elif nums[right]==1:
                ones+=1
            
            while zeros>1:
                if nums[left]==0:
                    zeros-=1
                elif nums[left]==1:
                    ones-=1
                left+=1
            
            ans = max(ans,ones)
            right+=1
        
        if zeros==0:
            return ans-1
        elif ones == 0 and ans ==0:
            return 0
        else:
            return ans
        
            
                


        
