class Solution:
    def numTeams(self, rating: List[int]) -> int:


        memo = {}
        def dfs(i,prev,validLen):
            
            if validLen == 3:
                return 1

            if i>=len(rating):
                return 0

            if (i,prev,validLen) in memo:
                return memo[i,prev,validLen]
            
            totalTeams = 0

            for k in range(i,len(rating)):

                if rating[k]>prev:
                   totalTeams+=dfs(k+1,rating[k],validLen+1)
                
            memo[i,prev,validLen] = totalTeams

            return totalTeams
        

        increasingCount = dfs(0,-float('inf'),0)
        rating  = rating[::-1]
        memo = {}
        decreasingCount = dfs(0,-float('inf'),0)

        return (increasingCount + decreasingCount)
