class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:



        candidates.sort()
        ans = []


        def dfs(i,total,subset):

            if total>target:
                return
            if i>len(candidates):
                return

            if total==target:
                ans.append(subset[:])
            

            for k in range(i,len(candidates)):

                if k>i and candidates[k-1]==candidates[k]:
                    continue

                subset.append(candidates[k])

                dfs(k+1,total+candidates[k],subset)

                subset.pop()
        
        dfs(0,0,[])
        return ans
            


        
