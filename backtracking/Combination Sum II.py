class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        ans = []
        visited = set()


        def dfs(sum,k,combination):
            
            if sum>target:
                return

            if sum == target:
                ans.append(combination)
                return 

            for candidate in candidates[k:]:
                nextCandidate = combination+[candidate] 
                if tuple(nextCandidate) in visited:
                    k+=1
                    continue
                visited.add(tuple(nextCandidate))
                sum+=candidate
                dfs(sum,k+1,nextCandidate)
                sum-=candidate
                k+=1

        dfs(0,0,[])
        return ans               

        
        
