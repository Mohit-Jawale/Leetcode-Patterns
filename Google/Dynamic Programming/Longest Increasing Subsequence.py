class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:


        ####### DFS+ memo TC O(N^2) SC( N^2)
        memo = {}

        def findLIS(i,prev):


            if i>=len(nums):
                return 0

            if i in memo:
                return memo[i]
            
            longest_incresing_subsequence = 0

            for k in range(i,len(nums)):
                
                if prev<nums[k]:
                    longest_incresing_subsequence = max(findLIS(k+1,nums[k])+1,longest_incresing_subsequence)

            memo[i] = longest_incresing_subsequence
            return longest_incresing_subsequence
        

        return findLIS(0,-float('inf'))

        ###### 1 DP  TC O(N^2) SC( N^2)

        n = len(nums)
        dp = [1]*(n+1)
        
        for i in reversed(range(n)):

            for k in range(i+1,n):

                if nums[k]>nums[i]:
                    dp[i] = max(dp[k]+1,dp[i])

        
        return max(dp)

        ##### greedy with Binary Search  TC O(NLOGN) SC(N)
        tails = []

        for num in nums:
            ### finding the smallest idx just greater that the tail
            idx = bisect.bisect_left(tails,num)

            if idx == len(tails):#### outer case basically no number greater thatn num
                tails.append(num)
            else:
                tails[idx] = num
        
        return len(tails)
