class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        ### this is grt question -> why?
        ### how are u handling leading zero
        ### that is classic problem were u can miss case if nested loop might head of the 
        #### outer u need to put condition to check
        #### when u are skiping steps then make sure the edge case is not false
        ### their is chance of u going out of bound
        
        i , j = 0 ,0

        while i<len(word) and j<len(abbr):

            if word[i] == abbr[j]:
                i+=1
                j+=1
            else:
                if abbr[j].isdigit():
                    num = ""
                    while j<len(abbr) and abbr[j].isdigit():
                        if num == "" and abbr[j] =='0': ### this is to check leading zero
                            return False
                        num+=abbr[j]
                        j+=1
                    i+=int(num)
                else:
                    return False
        

        return True if j==len(abbr) and i==len(word) else False
                    
                
        
