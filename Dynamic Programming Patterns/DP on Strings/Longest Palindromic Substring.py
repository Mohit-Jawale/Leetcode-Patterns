class Solution:
    def longestPalindrome(self, s: str) -> str:

        dp = [[False for j in range(len(s))] for i in range(len(s))]

        LPSub = s[0]

        ###Base Case 1 with one letter
        for i in range(len(s)):
            dp[i][i] = True
         
        
        ### Base Case 2 with two letter
        for i in range(len(s)-1):
            dp[i][i+1] = (s[i]==s[i+1])
            LPSub = s[i:i+2] if dp[i][i+1] else LPSub
        
        for length in range(3,len(s)+1):
            i = 0
            for j in range(length-1,len(s)):

                dp[i][j] = dp[i+1][j-1] and s[i]==s[j]

                LPSub = s[i:j+1] if dp[i][j] else LPSub
                
                i+=1

        return LPSub






        


        

class Solution:
    def longestPalindrome(self, s: str) -> str:

        def checkPalindrome(left,right):

            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return left+1,right-1

        ans = ""
        max_len = 0
        for i in range(len(s)):

            left,right = checkPalindrome(i,i)
            
            if max_len < (right-left+1):
                max_len = right-left+1
                ans = s[left:right+1]


            left,right = checkPalindrome(i,i+1)

            if max_len < (right-left+1):
                max_len = right-left+1
                ans = s[left:right+1]

        return ans   




        


        
