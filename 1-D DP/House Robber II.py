class Solution:
    def rob(self, nums: List[int]) -> int:
        
        @lru_cache(None)
        def dfs(k,robbedFirst):
            
            if k == len(nums)-1 and robbedFirst:
                return 0

            if k>=len(nums):
                return 0
            
 
            rob_this = dfs(k+2,robbedFirst)+nums[k]
            skip_this = dfs(k+1,robbedFirst)

            return max(rob_this,skip_this)


            
        return max(dfs(1,False),nums[0]+dfs(2,True))   
