### Observer how different the condition is then two pointer remember the difference

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = right = 0
        ans = 0
        char_counter = Counter()

        while right<len(s):
            char_counter[s[right]]+=1
            

            while char_counter[s[right]]>1:
                char_counter[s[left]]-=1
                left+=1

            ans = max(right-left+1,ans)
            right+=1

        return  ans       





        
