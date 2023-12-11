class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        totalSum = sum(nums)

        target = totalSum//2

        memo = {}

        if totalSum%2!=0:
            return False

        def dfs(i,target):

            if (i,target) in memo:
                return memo[(i,target)]
            
            if target == 0:
                return True
            if target<0 or i>=len(nums):
                return False


            taken = dfs(i+1,target-nums[i])
            skip = dfs(i+1,target)

            memo[(i,target)] = (taken or skip)
            

            return (taken or skip)


        return dfs(0,target)     
### 2dp -solution
### Here lots of things are gng on in building the solution
### observation 1-: in dfs->>i->>> is from 0 to n and target is from n to 0.
### that's why the i-1 in the dp solution if we reverse the row loop for bottom-up solution
### dp[0][0]== True we can deduce this by the base condition of dfs solution
### dp[i][target] is outside bcz if the target>=nums[i-1] condition is false we need to fill the row -1 value in it.

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        totalSum = sum(nums)

        target = totalSum//2

        if totalSum%2!=0:
            return False


        dp= [[False for _ in range(target+1)] for _ in range(len(nums)+1)]

        dp[0][0]=True

        for i in range(1,len(dp)):
            for target in range(1,len(dp[0])):

                dp[i][target] = dp[i - 1][target]
                if target>=nums[i-1]:
                    dp[i][target]= dp[i-1][target-nums[i-1]] or dp[i-1][target]

        return dp[-1][-1]              
