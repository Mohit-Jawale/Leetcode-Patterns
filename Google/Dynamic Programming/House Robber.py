class Solution:
    def rob(self, nums: List[int]) -> int:


        ### nums = [1,2,3,1]

        #### this sound like maxization problem
        ### take or skip
        #### O(2^n)->>> dfs+memo
        ####     dfs(0,0)
        #### dfs(i+2=2,1).                   dfs(i+1=1,0)
        ####                                  dfs(i+2=3,2). dfs(i+1=2,)
        ####dfs(i+2>n,4)-> base condtion  dfs(i+1=3,2)
        # memo = {}

        # def maxAmountOfMoney(i):

        #     if i>=len(nums):
        #         return 0
            
        #     if i in memo:
        #         return memo[i]
            
        #     take = maxAmountOfMoney(i+2)+ nums[i]
        #     skip = maxAmountOfMoney(i+1) 

        #     memo[i] = max(take,skip)
        #     return max(take,skip)
        
        # return maxAmountOfMoney(0)

        # n = len(nums)
        # dp = [-float('inf')]*(n+2)

        # dp[n]=0
        # dp[n+1]=0

        # for i in reversed(range(n)):

        #     dp[i] = max(dp[i+2]+nums[i],dp[i+1])
        
        # return dp[0]

        n = len(nums)
        next_to_next = 0
        next = 0
        curr = 0
        for i in reversed(range(n)):
            
            curr = max(next,next_to_next+nums[i])
            next_to_next = next
            next = curr
        
        return curr













        
