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
