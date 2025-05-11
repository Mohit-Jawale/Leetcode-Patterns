class Solution:
    def longestPalindrome(self, s: str) -> str:

        def check_palindrome(i,j):

            while i>=0 and j<len(s):
                if s[i]==s[j]:
                    i-=1
                    j+=1
                else:
                    break
            return i+1,j-1

        max_len = 0
        LPS = ""

        for i in range(len(s)):


            p,q = check_palindrome(i,i)

            if q-p+1>max_len:
                max_len = q-p+1
                LPS = s[p:q+1]

            p,q = check_palindrome(i,i+1)

            if q-p+1>max_len:
                max_len = q-p+1
                LPS = s[p:q+1]
        return LPS



        
