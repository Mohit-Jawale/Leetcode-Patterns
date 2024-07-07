### here the third for loop is going zigzag 
class Solution:
    def countSubstrings(self, s: str) -> int:
        

        count = 0

        dp = [ [ False for j in range(len(s))] for i in range(len(s)) ]

        ### Base case with length 1

        for i in range(len(s)):
            dp[i][i] = True
            count+=1
        
        ### Base case with length 2

        for i in range(len(s)-1):
            dp[i][i+1] = (s[i]==s[i+1])
            count+= dp[i][i+1]
        
        ### now we find out remaining length string 3,4 ....
        for length in range(3,len(s)+1):
            i = 0
            for j in range(length-1,len(s)):
                dp[i][j] = dp[i+1][j-1] and (s[i] == s[j])
                count+=dp[i][j]
                i+=1

        return count



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






        


