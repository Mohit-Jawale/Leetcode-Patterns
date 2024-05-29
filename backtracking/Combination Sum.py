class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []



        def dfs(i,combiSet,total):

            nonlocal ans

            if i>=len(candidates) or total>target:
                return
            if total == target:
                ans.append(combiSet)
                return
            
            for k in range(i,len(candidates)):
                temp = combiSet+[candidates[k]]
                dfs(k,temp,total+candidates[k])
                

        
        dfs(0,[],0)
        return ans
