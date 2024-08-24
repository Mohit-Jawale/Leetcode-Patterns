class Solution:
    def romanToInt(self, s: str) -> int:


        romanToInt = {

            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        doubles= {

            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900

        }

        ans = 0
        index = 0
        while index<len(s):
    
            if index+1<len(s) and s[index:index+2] in doubles:
                ans+=doubles[s[index:index+2]]
                index+=1
            elif s[index] in romanToInt:
                ans+=romanToInt[s[index]]

            index+=1
        
        return ans
