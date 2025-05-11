class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        

        ### O(n*m*k)
        memo = {}

        def matchWords(i):
            
            if i>len(s):
                return False

            if i==len(s):
                return True
            
            if i in memo:
                return memo[i]

            for word in wordDict:

                if s[i:i+len(word)] == word:

                    if matchWords(len(word)+i):
                        memo[i]=True
                        return True
            memo[i]=False
            return False
        

        return matchWords(0)

            
        
