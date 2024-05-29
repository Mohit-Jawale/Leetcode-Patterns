class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:


        ans = []
        candidates.sort()
        

        def dfs(i,combiSet,total):

                        
            if total == target:
                ans.append(combiSet)
                return
                
            if i>=len(candidates) or total>target:
                return

            

            for k in range(i,len(candidates)):
                if k>i and candidates[k-1]==candidates[k]:
                    continue
                temp = combiSet + [candidates[k]]
                dfs(k+1,temp,total+candidates[k])

                
        
        dfs(0,[],0)
        return ans

        
