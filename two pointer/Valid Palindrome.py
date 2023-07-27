class Solution:
    def isPalindrome(self, s: str) -> bool:


        s = "".join(s.lower().split(' '))
        s = "".join([i for i in s if i.isalnum()])

        left, right = 0, len(s)-1
        ans = True

        while left<right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                ans = False
                break

        return ans 
