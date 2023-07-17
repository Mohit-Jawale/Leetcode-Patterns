class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
 
        char_counter_t = Counter(t)
        char_counter_s = Counter()
        need,have = len(t), 0
        left, right = 0,0
        res,res_len= [-1,-1], float('inf')

        while right<len(s):
            char_right = s[right]
            char_counter_s[char_right]+=1
            if char_right in char_counter_t and char_counter_t[char_right]>=char_counter_s[char_right]:
                have+=1

            while have == need:
                char_left =s[left]
                if (right-left+1)<res_len:
                    res = [left,right]
                    res_len = right-left+1

                char_counter_s[char_left]-=1
                if char_left in char_counter_t and char_counter_t[char_left]>char_counter_s[char_left]:
                    have-=1
                left+=1

            right+=1

      
        left, right = res
        
        return s[left:right+1]  if res_len != float('inf') else ""     




        
