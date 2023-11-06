class Solution:
    ### This problem talks about unique combinations like 1,1,2!= 2,1,1 thats why we have to use i
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = {}
        def dfs(k,amount):
            if amount == 0:
                return 1
            if (k,amount) in memo:
                return memo[(k,amount)]
            count = 0
            for i in range(k,len(coins)):
                if amount>=coins[i]:
                    count += dfs(i,amount-coins[i])
            memo[(k,amount)]=count
            return count  
        return dfs(0,amount)
                



class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [[0 for j in range(amount+1)] for _ in range(len(coins))]

        for i in range(len(coins)):
            for j in range(amount+1):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = 1 if j % coins[i] == 0 else 0
                elif j >= coins[i]:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(coins)-1][amount]
