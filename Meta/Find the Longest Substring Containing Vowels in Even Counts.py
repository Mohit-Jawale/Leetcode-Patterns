class Solution:
    def findTheLongestSubstring(self, s: str) -> int:


        vowels = "aeiou"

        lookup = {0:-1}

        mask = 0

        res = 0

        for index,value in enumerate(s):
            ### here adding 1 bcz 0000 ^ 0000 is not 0001
            print(lookup,res,mask)
            if value in vowels:
                mask = mask ^ (ord(value)-ord('a')+1)
              
            if mask in lookup:
                length = index-lookup[mask]
                res = max(length,res)
            else:
                lookup[mask]=index
        
        return res

