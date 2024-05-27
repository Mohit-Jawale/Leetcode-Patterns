class Solution:
    def maxVowels(self, s: str, k: int) -> int:

        vowels=set(('a','e','i','o','u'))

    
        left,right = 0,0

        ans = 0

        vowelCounter = 0

        while right<len(s):

            if s[right] in vowels:
                vowelCounter+=1

            while(right-left+1)>k:
                if s[left] in vowels:
                    vowelCounter-=1
                left+=1

            ans = max(vowelCounter,ans)
            right+=1

        return ans
            
            
                



        
        
