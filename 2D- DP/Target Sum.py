### DFS + memo
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def dfs(i,candidates):
            

            if i == len(nums):
                if candidates == target:
                    return 1
                else:
                    return 0    

            if (candidates,i) in dp:
                return dp[(candidates,i)]        


            left = dfs(i+1,candidates+nums[i])

            right = dfs(i+1,candidates-nums[i])

            dp[(candidates,i)] = left+right


            return left+right


        return dfs(0,0)    
