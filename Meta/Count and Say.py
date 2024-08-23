class Solution:
    def countAndSay(self, n: int) -> str:

        def RLE(s):
            rle = ""
            left,right = 0 ,0

            while right<len(s):
                if s[left]==s[right]:
                    right+=1
                else:
                    rle+=str(right-left)+str(s[left])
                    left=right
            rle+=str(right-left)+str(s[left])
            return rle


        def dfs(i):

            if i==1:
                return "1"
            
            return RLE(dfs(i-1))

        ans = dfs(n)
        return ans
     


                        



        
