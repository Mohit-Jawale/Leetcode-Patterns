class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left, right = 0, len(s)-1

        while left<right:
            if s[left]!=s[right]:
                lskip = s[left+1:right+1]
                rskip = s[left:right]
                return (lskip[::-1]==lskip) or (rskip[::-1]==rskip)

            else:
                left+=1
                right-=1

        return  True 
