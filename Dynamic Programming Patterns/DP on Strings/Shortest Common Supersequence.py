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
                    dp[i][j]= dp[i+1][j+1]+1
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])

        i,j=0,0
        lcs = ""
        while i<m and j<n:
                if str1[i]==str2[j]:
                    lcs+=str1[i]
                    i,j = i+1,j+1
                else:
                    if dp[i+1][j]>=dp[i][j+1]:
                        lcs+=str1[i]
                        i,j= i+1,j
                    else:
                        lcs+=str2[j]
                        i,j = i,j+1

        while i<m:
            lcs+=str1[i]
            i+=1
        while j<n:
            lcs+=str2[j]
            j+=1
   
        return(lcs)                    
