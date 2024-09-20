class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        ### is i can make palindrome of any string
        ### there will be two case
        ### odd -> aab - > a:2 b:1 -> true
        ### even ->mnmn - > m:2:n:2
        ### len(odd)-> expected on all should be divisbile by 2
        #### len(even)-> all should be divisilbe by 2

        char_counter = Counter(s)
        count=len(char_counter)
        if len(s)%2!=0:
            count-=1

        for key,value in char_counter.items():
            
            if (char_counter[key]%2)==0:
                count-=1
        
        return True if count==0 else False
