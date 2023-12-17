### DFS + memo
class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:

        memo = {}
        def dfs(i,j):
            
            if (i,j) in memo:
                return memo[(i,j)]

            if i+1==j:
                return 0

            totalMIN = float('inf')
            for k in range(i+1,j):
                totalMIN = min((values[i]*values[j]*values[k])+dfs(i,k)+dfs(k,j),totalMIN)

            memo[(i,j)] = totalMIN
            return totalMIN

        return dfs(0,len(values)-1)       

        
