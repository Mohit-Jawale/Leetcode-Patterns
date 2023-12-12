## dfs + memo.... this solution has small trick i is not really required for memozation....you will know if you draw tree
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        memo = {}

        def dfs(i,target):

            if (target) in memo:
                return memo[(target)]
            if target==0:
                return 1
            if i>=len(nums) or target<0:
                return 0

            totalWays=0

            for i in range(len(nums)):
                totalWays+= dfs(i,target-nums[i]) 
            
            memo[(target)] = totalWays
            return totalWays        
        
        return dfs(0,target)


      ### 2d - dp... this is my first dp solution by myself. so happy (~_~)

        dp = [[0 for _ in range(target+1)] for _ in range(len(nums)+1)]

        for i in range(len(nums)+1):
            dp[i][0]=1

        for i in reversed(range(len(nums))):
            for t in range(1,len(dp[0])):

                for k in range(len(nums)):
                    if t-nums[k]>=0:
                        dp[i][t]+=dp[i][t-nums[k]]
        
        
        return dp[0][target]

