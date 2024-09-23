class Solution:
    def multiply(self, num1: str, num2: str) -> str:


        if num1=="0" or num2 =="0":
            return "0"
        
        multiplication = [0]*(len(num1)+len(num2))


        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):

                mul = int(num1[i])*int(num2[j])

                p1 = i+j
                p2 = i+j+1

                sumCarry = mul+multiplication[p2]

                multiplication[p2] = sumCarry%10
                multiplication[p1] += sumCarry//10
        
      
        multiplication = "".join(map(str,multiplication))
        return multiplication.lstrip('0')




        
  
         
        
