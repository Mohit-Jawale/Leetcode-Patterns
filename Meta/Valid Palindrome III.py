class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:

        if k == len(s):
            return True
        memo = {}
        
        def dfs(start,end,k):

            if start>end:
                return True

            if k == 0:
                return s[start:end+1] == s[start:end+1][::-1]
            
            if (start,end,k) in memo:
                return memo[(start,end,k)]
 
            if s[start]==s[end]:
                notremoved = dfs(start+1,end-1,k)
                memo[(start,end,k)] = notremoved
                return notremoved
            else:
                removed = dfs(start+1,end,k-1) or dfs(start,end-1,k-1)
                memo[(start,end,k)] = removed
                return removed
    
        
        return dfs(0,len(s)-1,k)
                
            
        
