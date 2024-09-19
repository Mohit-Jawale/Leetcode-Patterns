class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x<0:
            return False
        
        temp = x
        reversed_num = 0

        while temp!=0:

            digit = temp%10
            reversed_num = 10*reversed_num+digit
            temp = temp//10
        
        return reversed_num==x







        



        
