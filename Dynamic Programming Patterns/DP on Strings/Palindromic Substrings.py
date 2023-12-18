### This question has trick this can be done in dp way but this way is easier and intutive to understand
class Solution:
    def countSubstrings(self, s: str) -> int:

        def countPalindrome(left,right):
            
            count = 0
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
                count+=1

            return count    

        countPalindromeSubstring = 0

        for i in range(len(s)):
            left=right=i

            ##odd case
            countPalindromeSubstring+=countPalindrome(left,right)

            ## even case
            countPalindromeSubstring+=countPalindrome(left,right+1)

        return  countPalindromeSubstring   






        


