class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        

        ##[9,9]

        curr_total = digits[-1]+1
        carry = curr_total//10
        num = curr_total%10
        i=len(digits)-2
        digits[-1] = num

        while carry!=0 and i>=0:

            curr_total = digits[i]+carry
            num = curr_total%10
            carry = curr_total//10
            digits[i]= num
            i-=1

        if carry:
            digits = [carry]+digits

        return digits
