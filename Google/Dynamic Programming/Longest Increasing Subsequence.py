class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # memo = {}

        # def findLIS(i,prev):


        #     if i>=len(nums):
        #         return 0

        #     if i in memo:
        #         return memo[i]
            
        #     longest_incresing_subsequence = 0

        #     for k in range(i,len(nums)):
                
        #         if prev<nums[k]:
        #             longest_incresing_subsequence = max(findLIS(k+1,nums[k])+1,longest_incresing_subsequence)

        #     memo[i] = longest_incresing_subsequence
        #     return longest_incresing_subsequence
        

        # return findLIS(0,-float('inf'))


        n = len(nums)
        dp = [1]*(n+1)
        
        for i in reversed(range(n)):

            for k in range(i+1,n):

                if nums[k]>nums[i]:
                    dp[i] = max(dp[k]+1,dp[i])

        
        return max(dp)
        
