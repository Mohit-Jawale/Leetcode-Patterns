class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        dp =[[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]


        if len(s1)+len(s2)!=len(s3):
            return False

        dp[len(s1)][len(s2)]=1    

        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if i<len(s1) and s3[i+j]==s1[i] and dp[i+1][j]==True:
                    dp[i][j] = True
                if j<len(s2) and s3[i+j]==s2[j] and dp[i][j+1]==True:
                    dp[i][j] = True

        return dp[0][0]                
