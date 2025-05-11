class Solution:
    def minCut(self, s: str) -> int:
        
        ### Tc o(N^3)

        # def check_palindrome(s1):

        #     if s1 == s1[::-1]:
        #         return True

        #     return False

        n = len(s)
        dp = [ [False for _ in range(n+1)] for _ in range(n+1)]

        for i in range(n): ### this is length one palindrome
            dp[i][i]=True
        
        for i in range(n-1): #### this is length of two palindrome

            if s[i]==s[i+1]:
                dp[i][i+1]=True
        
        for length in range(3,len(s)+1): ### remaining length if you draw the table you can see the traversal is diagonal
            i=0
            for j in range(length-1,len(s)):
                if s[i]==s[j] and dp[i+1][j-1]:
                    dp[i][j]=True
                i+=1
        

        memo = {}
        def palindrome_partioning(i):
            
            if i>=len(s):
                return -1
            
            total_cuts = float('inf')

            if i in memo:
                return memo[i]

            for k in range(i,len(s)):

                if dp[i][k]:
                   total_cuts = min(palindrome_partioning(k+1)+1,total_cuts)
            
            memo[i] = total_cuts
            return total_cuts


        return palindrome_partioning(0)    
        


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
        
