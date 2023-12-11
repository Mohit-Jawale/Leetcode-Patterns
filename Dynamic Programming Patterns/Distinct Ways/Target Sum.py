## DFS + memo
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def dfs(i,target):
            
            if (i,target) in memo:
                return memo[(i,target)]

            if target==0 and i==len(nums):
                return 1

            if i>=len(nums):
                return 0

            totalExp = 0

            positiveSign = dfs(i+1,target+nums[i])
            negativeSign = dfs(i+1,target-nums[i])

            totalExp += (positiveSign + negativeSign)
            
            memo[(i,target)] = totalExp
            return totalExp


        return dfs(0,target)
        
 ### Below is 2d-dp solution.... This soltuion is copied from chat-gpt and modified I still dont get some of it

        n = len(nums)
        # Calculate the maximum possible sum of the numbers in nums
        max_sum = sum(nums)
        
        # Check if the target is out of bounds, there can't be any ways to achieve it
        if abs(target) > max_sum:
            return 0
        
        # Initialize a 2D DP array
        dp = [[0 for _ in range(target-max_sum,target+max_sum+1)] for _ in range(n + 1)]
        
        # Initialize the base case
        # When no numbers are considered, there's only one way to achieve a sum of 0 (doing nothing)
        dp[0][max_sum] = 1
        
        # Populate the DP array
        for i in range(1, len(dp)):
            for j in range(1,len(dp[0])):
                if dp[i - 1][j] > 0:
                    # Add the current number to the sum
                    dp[i][j + nums[i - 1]] += dp[i - 1][j]
                    # Subtract the current number from the sum
                    dp[i][j - nums[i - 1]] += dp[i - 1][j]
        
        # The answer is stored in dp[n][target + max_sum]
        return dp[n][target + max_sum]

