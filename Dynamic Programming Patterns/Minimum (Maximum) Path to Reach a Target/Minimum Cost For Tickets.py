class Solution:
    def mincostTickets(self, days, costs):
        def dfs(i):
            if i == len(days):
                return 0
            if memo[i] != float('inf'):
                return memo[i]

            ans = dfs(i + 1) + costs[0]
            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j += 1
            ans = min(ans, dfs(j) + costs[1]

            while j < len(days) and days[j] < days[i] + 30:
                j += 1
            ans = min(ans, dp(j) + costs[2])

            memo[i] = ans
            return ans

        memo = [float('inf')] * len(days)
        return dp(0)
