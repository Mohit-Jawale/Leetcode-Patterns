class Solution:
    def myPow(self, x: float, n: int) -> float:


        if n==0:
            return 1
        if n<0:
            n = (-1)*n
            x = 1/x

        ans = 1

        while n!=0:
            #### there if 2^5 - > then u side 2 first if its odd then calculate 2^4
            ### and in last when n==1 multiple the remaining 2

            if n%2==1:
                ans*=x
                n=n-1

            x*=x
            n = n//2

        return ans    
