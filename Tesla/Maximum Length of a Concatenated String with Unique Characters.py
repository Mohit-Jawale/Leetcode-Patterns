class Solution:
    def maxLength(self, arr: List[str]) -> int:

        def get_new_bit(bit,curr):
           
            for c in curr:
               if 1<<(ord(c)-ord('a')) & bit : return -1
               bit |= 1<< (ord(c)-ord('a'))
            return bit

        @lru_cache(None)
        def dfs(i,bit):
            
            if i>=len(arr):
                return 0 
            ans = 0

            for s in arr[i:]:
                new_bit = get_new_bit(bit,s)
                if new_bit== -1: continue
                ans = max(ans,dfs(i+1,new_bit)+len(s))
            
            return ans


        return dfs(0,0)
