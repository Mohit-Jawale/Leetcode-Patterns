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
        
 ### Below is 2d-dp solution.

        totalSum = sum(nums)

        if totalSum<target:
            return 0

        dp = [[0 for _ in range(target-totalSum,target+totalSum+1)] for _ in range(len(nums)+1)]

        ## if you draw table you will know the index starts with negative number
        dp[len(nums)][0+totalSum]=1


        for i in reversed(range(len(nums))):
            for j in range(-totalSum,totalSum+1):## This is maxlimit
                j = j + totalSum
     
                positiveSign = j + nums[i]
                negativeSign = j - nums[i]

                if positiveSign >= 0 and positiveSign<= (2*totalSum):
                    dp[i][j]+=dp[i+1][positiveSign]
                if negativeSign >= 0 and negativeSign<= (2*totalSum):
                    dp[i][j]+=dp[i+1][negativeSign] 


        return dp[0][target+totalSum]    

