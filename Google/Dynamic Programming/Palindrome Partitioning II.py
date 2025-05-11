class Solution:
    def minCut(self, s: str) -> int:


        def check_palindrome(s1):

            if s1 == s1[::-1]:
                return True

            return False
        
        memo = {}
        def palindrome_partioning(i):
            
            if i>=len(s):
                return -1
            
            total_cuts = float('inf')

            if i in memo:
                return memo[i]

            for k in range(i,len(s)):


                if check_palindrome(s[i:k+1]):
                   total_cuts = min(palindrome_partioning(k+1)+1,total_cuts)
            
            memo[i] = total_cuts
            return total_cuts


        return palindrome_partioning(0)    
        
