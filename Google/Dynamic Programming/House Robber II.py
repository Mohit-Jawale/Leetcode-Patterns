class Solution:
    def rob(self, nums: List[int]) -> int:

        ### [1,2,3,1]

        if len(nums)==1:
            return nums[0]

        memo = {}

        def getMaxMoney(i,n):

            if i>=n:
                return 0
            if i in memo:
                return memo[i]
            
            memo[i] = max(getMaxMoney(i+2,n)+nums[i],getMaxMoney(i+1,n))

            return memo[i]
        
        option1 = getMaxMoney(0,len(nums)-1)
        memo = {}
        option2 = getMaxMoney(1,len(nums))

        return max(option1,option2)

        
