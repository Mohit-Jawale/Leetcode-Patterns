### need to understand what they are asking 
class Solution:
    def minInsertions(self, s: str) -> int:
        

        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        
        for i in range(len(s)):
            dp[i][i]= 1

        for i in reversed(range(len(s))):
            for j in range(i+1, len(s)):
         
                if s[i]==s[j]:
                    dp[i][j] = max(dp[i+1][j-1]+2,dp[i][j])
                else:
                    dp[i][j]= max(dp[i+1][j],dp[i][j-1])
        

        return len(s) - dp[0][len(s)-1]
