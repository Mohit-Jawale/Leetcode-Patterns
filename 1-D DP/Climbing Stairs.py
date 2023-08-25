### This is DFS + Memo

class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def dfs(n):

            print(n)
            if n<0:
                return 0
            if n==0:
                return 1

            if n in memo:
                return memo[n]    

            memo[n]=dfs(n-1)+dfs(n-2)

            return memo[n]

        return dfs(n)
      
### This is  1-D dp 
### Here we are using var one and two instead of array

class Solution:
    def climbStairs(self, n: int) -> int:

        one,two = 1,1

        for i in range(n-1):
            temp = one+two
            one = two
            two = temp

        return two    
            
        
      
 

        
