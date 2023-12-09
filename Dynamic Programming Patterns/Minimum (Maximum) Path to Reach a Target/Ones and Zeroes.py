### This is also good knapsack problem here the trick of "(m >= zeros and n >= ones)" is amazing and crucial.
### That trick is helping checking if the string we are going thorugh is vaild or not
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        def binary_count(binaryString):
            count_1 = binaryString.count('1')
            count_0 = binaryString.count('0')
            return (count_1,count_0)

        memo = {}
        def dfs(i,m,n):

            if i>=len(strs) or (m<0 or n<0):
                return 0
            if (i,m,n) in memo:
              return memo[(m,n)]

            ones,zeros = binary_count(strs[i])
            ### here if the string is not valid dont add it
            takenStr =  dfs(i+1,m-zeros,n-ones) + (m >= zeros and n >= ones)
            dropStr = dfs(i+1,m,n)

            memo[(i,m,n)] = max(takenStr,dropStr)
            return max(takenStr,dropStr)

        return dfs(0,m,n)
## 3-DP solution

class Solution:
    def findMaxForm(self, strs, m, n):
        # Function to count the number of 1s and 0s in a binary string
        def binary_count(binaryString):
            count_1 = binaryString.count('1')
            count_0 = binaryString.count('0')
            return count_0, count_1


        dp = [[[0 for _ in range(m+1)]for _ in range(n+1)]for _ in range(len(strs)+1)]

        for i in range(1,len(strs)+1):
            zeros,ones = binary_count(strs[i-1])
            for j in range(n+1):
                for k in range(m+1):
                    if zeros<=k and ones<=j:
                        dp[i][j][k]= max(dp[i-1][j-ones][k-zeros]+1,dp[i-1][j][k])
                    else:
                        dp[i][j][k]=dp[i-1][j][k]    
 
        return dp[-1][-1][-1]                


        

        
