class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        left,right = 0,0

        charCounter = Counter()
        ans = 0

        while right<len(s):
            charCounter[s[right]]+=1
            while len(charCounter)>2:
                
                if charCounter[s[left]]>0:
                    charCounter[s[left]]-=1
                if charCounter[s[left]] == 0:
                    del charCounter[s[left]]
                left+=1
            
            ans = max(ans,right-left+1)
            right+=1
        
        return ans



            


        
