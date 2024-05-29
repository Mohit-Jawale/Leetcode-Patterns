class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ans = [[]]


        def dfs(i,subset):
            nonlocal ans
            if i>=len(nums):
                return

            for k in range(i,len(nums)):
                temp = subset + [nums[k]]
                ans.append(temp)
                dfs(k+1,temp)
        

        dfs(0,[])
        return ans
             



        
