class Solution:
    def minWindow(self, s: str, t: str) -> str:

        charCounter_s = Counter()
        charCounter_t = Counter(t)

        need,have = len(t), 0

        right,left = 0,0

        res,res_len = [-1,-1], float('inf')

        while right<len(s):

            charCounter_s[s[right]]+=1

            if s[right] in charCounter_t and charCounter_t[s[right]]>=charCounter_s[s[right]]:
                have+=1
            
            while need==have:

                charCounter_s[s[left]]-=1

                if res_len>right-left+1:
                    res_len = right-left+1
                    res = [left,right]

                if s[left] in charCounter_t and charCounter_t[s[left]]>charCounter_s[s[left]]:
                    have-=1

                left+=1
            
            right+=1
        
        left,right = res

        return s[left:right+1] if res_len!=float('inf') else ""
            




        
