### DFS+memo
### you ca use 0/1 knapsack appraoch but you need to maintain seperate varioable for brach merging

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        memo = {}
        count = 0

        def dfs(i,prev):

            
            if (i,prev) in memo:
                return memo[(i,prev)]

            if i>=len(nums):
                return 0,1

            include = 0
            includeWays = 0
            if prev<nums[i]:
                include,includeWays = dfs(i+1,nums[i])
                include+=1
            skip,skipWays = dfs(i+1,prev)
          
            if include == skip:
                maxWays = includeWays+skipWays
                maxLen = include
            elif include>skip:
                maxWays = includeWays
                maxLen = include
            else:
                maxWays = skipWays
                maxLen = skip        

            memo[(i,prev)] = maxLen,maxWays

            return memo[(i,prev)]

        LIS,count = dfs(0,-float('inf'))  
        return count  


        
