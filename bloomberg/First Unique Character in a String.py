class Solution:
    def firstUniqChar(self, s: str) -> int:

        charCounter = Counter(s)

        for index,char in enumerate(s):

            if char in charCounter and charCounter[char]==1:
                return index
        

        return -1

        
