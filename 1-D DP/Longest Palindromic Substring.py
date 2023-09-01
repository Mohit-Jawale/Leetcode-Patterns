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




        


        
