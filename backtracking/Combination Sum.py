class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        ans = []
        candidates.sort()


        def dfs(sum,combination,k):

            if sum>target:
                return
            if sum == target:
                ans.append(combination)  
                return

            for candidate in candidates[k:]:
                sum+=candidate
                nextCandidate = combination + [candidate]
                if sum>target:
                    break
                dfs(sum,nextCandidate,k)
                sum-=candidate
                k+=1


        dfs(0,[],0)
        return ans        


        
