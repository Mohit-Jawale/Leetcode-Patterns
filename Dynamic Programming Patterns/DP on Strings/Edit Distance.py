class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        m,n = len(word1),len(word2)
        memo = {}

        def dfs(i,j):
            
            if (i,j) in memo:
                return memo[(i,j)]
            ### if one string is greater than the other string we need remaining operation 
            if i>=m:
                return n-j
            if j>=n:
                return m-i

            minOp = float('inf')

            if word1[i]==word2[j]:
                minOp = dfs(i+1,j+1)
            else:

                insertOp = dfs(i,j+1)+1

                deleteOp = dfs(i+1,j)+1

                replaceOp = dfs(i+1,j+1)+1

                minOp = min(minOp,insertOp,deleteOp,replaceOp)

            memo[(i,j)] = minOp
            return minOp

        return dfs(0,0)  
                       

        
