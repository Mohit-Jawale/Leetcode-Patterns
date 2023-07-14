#the mean of k = 2 or anything is current window size - max_value should less than k if greater than shrink

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left, right = 0, 0
        ans = 0
        char_counter = Counter()

        while right < len(s):

            char_counter[s[right]]+=1 

            while ((right-left+1) - max(char_counter.values()))>k:

                char_counter[s[left]]-=1
                left+=1

            ans = max(ans,right-left+1)
            right+=1
        return ans     









        
