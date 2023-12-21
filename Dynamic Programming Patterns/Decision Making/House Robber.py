### dfs + memo

class Solution:
    def rob(self, nums: List[int]) -> int:

        memo = {}

        def dfs(i):

            if i in memo:
                return memo[i]
            if i==0:
                return nums[i]
            if i==1:
                return max(nums[i-1],nums[i])

            maxAmount = max(dfs(i-2)+nums[i],dfs(i-1))

            memo[i] = maxAmount
            return maxAmount


        return dfs(len(nums)-1)

  ## 1D-DP
      
        n = len(nums)
        dp = [0] * (n)
        if n == 1:
            return nums[0]
        if n == 2:    
            return max(nums[0],nums[1])
            
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2,n):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])

        return dp[n-1]    




        
