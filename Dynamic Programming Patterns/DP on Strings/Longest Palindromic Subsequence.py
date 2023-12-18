### DF +memo
### the LPS is basically reverse of the str and LCS on the both string
### the longest palindromic subsequence of string is reverse of its own and LCS b/w them.--this is trick
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        memo = {}
        revstr = s[::-1]

        def dfs(i,j):

            if (i,j) in memo:
                return memo[(i,j)]

            if i>=len(s) or j>=len(s):
                return 0

            LPS = 0

            if s[i]==revstr[j]:
                LPS = dfs(i+1,j+1)+1

            else:
                LPS = max(dfs(i+1,j),dfs(i,j+1))

            memo[(i,j)] = LPS
            return LPS


        return dfs(0,0) 
        
