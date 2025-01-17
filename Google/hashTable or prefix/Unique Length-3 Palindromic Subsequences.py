class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:


        first_occurence = {}
        last_occurence = {}

        for i in range(len(s)):
            if s[i] not in first_occurence:
                first_occurence[s[i]]=i
        
        for j in reversed(range(len(s))):
            if s[j] not in last_occurence:
                last_occurence[s[j]]=j
        

        
        unique_count = 0

        for i in range(0,26):

            char = chr(97+i)

            unique_palindrome = set()

            if char not in first_occurence or char not in last_occurence:
                continue
            
            for j in range(first_occurence[char]+1,last_occurence[char]):

                unique_palindrome.add(s[j])

            unique_count+=len(unique_palindrome)
        
        return unique_count
            

        
        


        
