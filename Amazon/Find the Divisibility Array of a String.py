class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:

        ans = [0]* len(word)
        prefix = 0
        for index,value in enumerate(word):
            print(prefix)
            prefix = 10*prefix + ord(value)-48
            prefix%=m
            if prefix == 0:
                ans[index]=1
        
        return ans
            
        
        return ans
            

        
