class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        alienDictOrder = {" ":-1}

        for i in range(len(order)):

            alienDictOrder[order[i]] = i
        
        j = 0
        for word in words[1:]:
            start = words[j]
            for i in range(max(len(start),len(word))):

                if i>=len(start):
                    start+=" "
                if i>=len(word):
                    word+=" "

                if alienDictOrder[start[i]]==alienDictOrder[word[i]]:
                    continue
                elif alienDictOrder[start[i]]<alienDictOrder[word[i]]:
                    break
                else:
                    return False
            j+=1
        
        return True
            




        
