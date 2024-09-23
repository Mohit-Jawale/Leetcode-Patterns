class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        ans = [0]*(len(digits)+1)
        carry = 0

        for i in reversed(range(len(digits))):
            
            p2 = i
            p1 = i+1
            
            if i==len(digits)-1:
                add = digits[i]+carry+1
            else:
                add = digits[i]+carry

            ans[p1] = add%10
            
            ans[p2] = add//10
            carry = add//10


        return ans if ans[0]!=0 else ans[1:]

          

            



        
