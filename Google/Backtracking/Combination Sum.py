class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:


        ans = []

        def dfs(i,total,subset):

            if target<total:
                return

            if target == total:
                ans.append(subset[:])

            for k in range(i,len(candidates)):

                subset.append(candidates[k])
                dfs(k,total+candidates[k],subset)
                subset.pop()
        
        dfs(0,0,[])
        return ans


            
            
            
            
            

        
