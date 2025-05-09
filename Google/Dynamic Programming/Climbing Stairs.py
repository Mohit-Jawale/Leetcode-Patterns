class Solution:
    def climbStairs(self, n: int) -> int:


        ### total distanct ways to reach on top
        ###  n=2

        #####                          step4. top n==4
        ##########                 step3
        ############            step2 
        ####                step1
        ###.  bottom-step 0 ->

        #       Dfs(0)
        # dfs(1).                 dfs(2)
        # dfs(2)        dfs(3)
        # dfs(3) dfs(4). dfs(4). 
        # dfs(4)
        
        ### time comlexity
        ### O(2^n) ->> O(N) 
        #### O(N)

        # memo = {}


        # def totalWaysToReachTop(i):

        #     if i>n:
        #         return 0
        #     if i==n:
        #         return 1
            
        #     if i in memo:
        #         return memo[i]

        #     oneStep = totalWaysToReachTop(i+1)
        #     twoStep = totalWaysToReachTop(i+2)

        #     memo[i] = oneStep+twoStep

        #     return oneStep+twoStep
        
        # return totalWaysToReachTop(0)


        # dp = [0]*(n+2)
        # dp[n] = 1

        # for i in reversed(range(n)):

        #     dp[i] = dp[i+1]+dp[i+2]
        
        # return dp[0]

        next,next_to_next = 1,0
        curr = 0
        for i in reversed(range(n)):

            curr = next+next_to_next
            next_to_next = next
            next = curr
        
        return curr


        
