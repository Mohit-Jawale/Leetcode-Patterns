### There are multiple concepts involved like LCS,printing LCS, and modified LCS
### This is good problem to understand lots of concpets related to LCS
### If lost while reading the solution print the LCS table and trace the LCS from 0,0 
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        
        m,n = len(str1),len(str2)

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in reversed(range(m)):
            for j in reversed(range(n)):
                if str1[i]==str2[j]:
                    dp[i][j] = max(dp[i+1][j+1]+1,dp[i][j])
                else:
                    dp[i][j] = max(dp[i+1][j],dp[i][j+1])
        
        
        i,j = 0,0
        shortestCommonSupersequence = ""

        while i<m and j<n:

            if str1[i]==str2[j]:
                shortestCommonSupersequence+=str1[i]
                i,j = i+1,j+1
            else:
                ### in actaully LCS we dont care if they are not equal we dont add them in soln
                ### but we need to add here because the order matters
                if dp[i][j+1]>=dp[i+1][j]:
                    shortestCommonSupersequence+=str2[j]
                    i,j = i,j+1
                else:
                    shortestCommonSupersequence+=str1[i]
                    i,j = i+1,j
        
        
        shortestCommonSupersequence = shortestCommonSupersequence+str1[i:]+str2[j:]

        return shortestCommonSupersequence
                  
