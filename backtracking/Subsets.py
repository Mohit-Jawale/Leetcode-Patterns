class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        ans = []
        ans.append([])
        
        def dfs(k,subset):

            nonlocal ans
            if k==len(nums):
                return

            for num in nums[k:]:
                temp = subset+[num]
                ans.append(temp)
                dfs(k+1,temp)
                k+=1


        dfs(0,[])
        return ans
