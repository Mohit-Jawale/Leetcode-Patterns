class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:


        ans = [[]]
        nums.sort()

        def dfs(i,subset):
            
            nonlocal ans

            if i>=len(nums):
                return
            
            for k in range(i,len(nums)):
                if k>i and nums[k]==nums[k-1]:
                    continue
                temp = subset+[nums[k]]
                ans.append(temp)
                dfs(k+1,temp)
        
        dfs(0,[])
        return ans

            

                 
