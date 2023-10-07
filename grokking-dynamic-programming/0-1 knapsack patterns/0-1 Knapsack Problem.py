https://www.educative.io/courses/grokking-dynamic-programming-a-deep-dive-using-python/solving-the-0-1-knapsack-problem

def find_knapsack(capacity, weights, values, n):
  
    dp = [[0 for j in range(capacity+1)] for i in range(len(weights)+1)]

    for i in range(len(dp)):
        for j in range(len(dp[0])):
            if i == 0 or j == 0:
                dp[i][j]=0
            elif weights[i-1]<=j:
                dp[i][j]= max(values[i-1]+dp[i-1][j-weights[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]

    return dp[-1][-1]                    
