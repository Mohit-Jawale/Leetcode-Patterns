### DFS+ memo

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        memo = {}

        def dfs(index,prev_num):
            
            nonlocal memo

            if index == len(nums):
                return 0

            max_len = 0

            if index in memo:
                return memo[index]

            for i in range(index,len(nums)):

                if prev_num < nums[i]:
                    max_len = max(max_len,1+dfs(i+1,nums[i]))

            memo[index] = max_len

            return max_len

        return dfs(0,-float('inf'))        

### 1D 
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        LIS = [1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[j]>nums[i]:
                    LIS[i] = max(LIS[i],1+LIS[j])


        return max(LIS)        
                
