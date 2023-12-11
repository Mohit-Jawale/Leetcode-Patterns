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
