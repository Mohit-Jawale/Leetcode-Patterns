### This question is from greedy section but it can be solved using the same complexity by 1 dp and intuition is also easy to understand
### At any index think about if including that element can increase the max continous sum at that point or we should add the prev sum.


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        dp = [0]*len(nums)
        ans = -float('inf')
        for index,value in enumerate(nums):

            ans = max(value,value+ans)
            dp[index]=ans
        
        return max(dp)    

        
