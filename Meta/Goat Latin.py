class Solution:
    def toGoatLatin(self, sentence: str) -> str:

        ### rules 
        ### vowels-<ma
        ### else -> gma
        ### 'a'

        words = sentence.split(" ")
        ans = []

        for index,w in enumerate(words):

            if w[0] in ['a','A','e','E','I','i','o','O','u','U']:
                w = w+"ma"
                w = w+((index+1) * "a")
                ans.append(w)
            else:
                w = w + w[0] + "ma" 
                w = w+ ((index+1) * "a")
                ans.append(w[1:])

            
        
        return " ".join(ans)






        
