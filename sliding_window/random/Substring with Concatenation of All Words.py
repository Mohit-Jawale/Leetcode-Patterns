class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

 

            windowsize = len(words[0])
            maxWindowsize = windowsize*len(words)
            needCharCounter = Counter(words)
            res = []

            for left in range(len(s)-maxWindowsize+1):
                right = 0
                counterChar = Counter()
              
                
                while right < maxWindowsize:
                    word = s[left+right:left+right+windowsize]
                    
                    if word in needCharCounter:
                        counterChar[word]+=1
                        if counterChar[word]>needCharCounter[word]:
                            break
                    else:
                        break
                    right+=windowsize

                if right == maxWindowsize:
                    res.append(left)


            return res



            
            
        
        
