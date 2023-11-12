class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = {}

        def dfs(k):

            if k>=len(nums)-1:
                return 0

            if k in memo:
                return memo[k]

            minDistance = float('inf')

            for i in range(1,nums[k]+1):
      
                minDistance = min(minDistance,dfs(k+i)+1)

            memo[k] = minDistance

            return minDistance

        return dfs(0)    
