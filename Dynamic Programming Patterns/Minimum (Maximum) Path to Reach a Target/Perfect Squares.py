
class Solution:
    def numSquares(self, n: int) -> int:

        perfectSq = [i for i in range(1,n+1) if int(sqrt(i))*int(sqrt(i)) == int(i)]

        memo = {}
        def dfs(total):

            if total>n:
                return float('inf')
            if total == n:
                return 0
            if total in memo:
                return memo[total]

            minSq = float('inf')

            for sq in perfectSq:
                minSq = min(dfs(total+sq)+1,minSq)
            
            memo[total] = minSq
            return minSq

        return dfs(0)

        dp = [float('inf')]*(n+1)
        dp[n]=0
        
        for total in reversed(range(len(dp)-1)):
    
            for sq in perfectSq:
                if total+sq<=n:
                    dp[total]= min(dp[total+sq]+1,dp[total])
                    
        return dp[0]

        

# class Solution:
#     def numSquares(self, n: int) -> int:

#         perfectSquares = [i for i in range(n,0,-1) if int(sqrt(i))*int(sqrt(i))==i]
#         memo = {}

#         def dfs(n):
#             if n==0:
#                 return 0
#             if n<0:
#                 return float('inf')
#             if n in memo:
#                 return memo[n]
#             minSQ = float('inf')

#             for i in perfectSquares:
 
#                 minSQ = min(minSQ,dfs(n-i)+1)

#             memo[n]= minSQ
#             return minSQ  

#         return dfs(n)            

# ### 2 dp

# class Solution:
#     def numSquares(self, n: int) -> int:

#         perfectSquares = [i for i in range(1,n+1) if int(sqrt(i))*int(sqrt(i))==i]

#         dp = [[0 for col in range(n+1)] for row in range(len(perfectSquares))]

#         for i in range(len(dp)):
#             for j in range(len(dp[0])):

#                 if i==0 or j==0:
#                     dp[i][j]=j
#                 elif j==0:
#                     continue
#                 elif j>=perfectSquares[i]:
#                      dp[i][j]= min(dp[i-1][j],dp[i][j-perfectSquares[i]]+1)
#                 else:
#                     dp[i][j]= dp[i-1][j]    

#         return dp[-1][-1]
