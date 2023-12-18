### DFS + Memo
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}

        def dfs(i,j):

            if (i,j) in memo:
                return memo[(i,j)]
            if i>=len(text1) or j>=len(text2):
                return 0

            LCS = 0

            if text1[i]==text2[j]:
                LCS = dfs(i+1,j+1)+1

            else:
                LCS = max(dfs(i+1,j),dfs(i,j+1))

            memo[(i,j)] = LCS
            return LCS


        return dfs(0,0)    

                    
        
        
