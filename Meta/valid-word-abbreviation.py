class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:


        ans = False
        i = 0
        j=0
        while j<len(abbr) and i<len(word):

            num = ""
            while j<len(abbr) and abbr[j].isnumeric():
                num+=abbr[j]
                if num=='0':
                    return False
                j+=1

            if num !="":
                i+=int(num)

            if (i<len(word) and j<len(abbr) )and word[i]==abbr[j]:
                i+=1
                j+=1
            else:
                break
        
        if i==len(word) and j==len(abbr):
            return True
        return ans 

            
                

        
        
