class Solution:
    def compressedString(self, word: str) -> str:

        left,right = 0,0
        comp = ""
        ### when we have to do back update its wise to make right==len(word)
        while right<=len(word):

            if right==left:
                right+=1
                continue
            
            if right!=len(word) and word[right]==word[left]:
                right+=1
            else:
                prefix_len = right-left
                if prefix_len<9:
                    comp += str(prefix_len)+word[left]
                    left=right
                else:
                    while prefix_len>=9:
                        
                        if prefix_len>=9:
                            comp +=str(9)+word[left]                

                        prefix_len = prefix_len-9

                    if prefix_len!=0:
                        comp +=str(prefix_len)+word[left]
                    left=right
        
        return comp
            
            
            
            

        
