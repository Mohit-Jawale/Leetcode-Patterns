class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        ptr1,ptr2 = 0,0
        ans = ""
        lengthOfWord = len(word1) if len(word1)<=len(word2) else len(word2)

        for _ in range(lengthOfWord):
            ans+=word1[ptr1]
            ans+=word2[ptr2]
            ptr1+=1
            ptr2+=1
        
        if ptr1==len(word1):
            ans+=word2[ptr2:]
        else:
            ans+=word1[ptr1:]
        
        return ans

        
        

        





        
