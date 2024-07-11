### DF +memo
### the LPS is basically reverse of the str and LCS on the both string
### the longest palindromic subsequence of string is reverse of its own and LCS b/w them.--this is trick
        memo = {}

        def dfs(i,j):

            if i==j:
                return 1
            if i>j:
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            
            lps = 0
            
            if s[i]==s[j]:
                lps = max(dfs(i+1,j-1)+2,lps)
            else:
                lps = max(dfs(i,j-1),dfs(i+1,j))
            
            memo[(i,j)] = lps
            return lps
        
        return dfs(0,len(s)-1)


### 2D - dp

        dp = [[0 for _ in range(len(s)+1)] for _ in range(len(s)+1)]
        
        for i in range(len(s)):
            dp[i][i]= 1

        for i in reversed(range(len(s))):
            for j in range(i+1, len(s)):
         
                if s[i]==s[j]:
                    dp[i][j] = max(dp[i+1][j-1]+2,dp[i][j])
                else:
                    dp[i][j]= max(dp[i+1][j],dp[i][j-1])
        

        return dp[0][len(s)-1]

        
