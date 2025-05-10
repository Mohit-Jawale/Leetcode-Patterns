class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        ##### text1 = "abcde", text2 = "ace" 
        #####           i                j

        ####LCS(i+1,j+1)+1 
        #### if max(LCS(i+1,j) LCS(i,j+1))

        # memo = {}

        # def LCS(i,j):

        #     if i>=len(text1) or j>=len(text2):
        #         return 0
            
        #     if (i,j) in memo:
        #         return memo[(i,j)]

        #     same,notSame = 0,0

        #     if text1[i]==text2[j]:
        #         same = LCS(i+1,j+1)+1
        #     else:
        #         notSame = max(LCS(i+1,j),LCS(i,j+1))
            
        #     memo[(i,j)] = max(same,notSame)

        #     return max(same,notSame)
        
        # return LCS(0,0)'
        m,n = len(text1), len(text2)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]


        for i in reversed(range(m)):
            for j in reversed(range(n)):

                if text1[i]==text2[j]:
                    dp[i][j] = dp[i+1][j+1]+1
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
                    
        return dp[0][0]





        
