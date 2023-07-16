class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        char_counter_1 = Counter(s1)
        char_counter_2 = Counter(s2[:len(s1)])
        matches = 0

        for i in range(0,26):
            char = chr(ord('a')+i)
            if char not in char_counter_1:
                char_counter_1[char]=0
            if char not in char_counter_2:    
                char_counter_2[char]=0
            if char_counter_1[char] == char_counter_2[char]:
                matches+=1

        left = 0
        right = len(s1)
        ans = False


        while right<len(s2):

            if matches==26:
                return True
    
            char_counter_2[s2[right]]+=1
            if char_counter_2[s2[right]]==char_counter_1[s2[right]]:
                matches+=1
            elif char_counter_2[s2[right]]==char_counter_1[s2[right]]+1: ### This step is most imp to understand it is like this if you increase
              ### the char in s2 counter by 1 and if that does match with s1 counter without actually incrementing by 1 then matches are reduce
                matches-=1    

            char_counter_2[s2[left]]-=1
            if char_counter_2[s2[left]]==char_counter_1[s2[left]]:
                matches+=1
            elif char_counter_2[s2[left]]==char_counter_1[s2[left]]-1:
                matches-=1   

            left+=1
            right+=1
            

        return matches==26        

               




        
        

           




             

        
