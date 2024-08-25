class Solution:
    def addStrings(self, num1: str, num2: str) -> str:


        if len(num1)<len(num2):
            num1,num2 = num2,num1
        

        m,n = len(num1)-1,len(num2)-1
        ans = []
        carry = 0

        while m>=0 and n>=0:

            num = int(num1[m])+int(num2[n]) + carry
            carry = num//10
            ans.append(str(num%10))
            m-=1
            n-=1
        
        if n<0:
            while m>=0:
                num = int(num1[m])+carry
                carry = num//10
                ans.append(str(num%10))
                m-=1

        ### overflow
        if carry>0:
            ans.append(str(carry))
            
        ans.reverse()
        num = "".join(ans)
        return num
        


        



        
