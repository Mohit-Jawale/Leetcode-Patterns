### DFS+memo gives MLE


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums_sum = sum(nums)

        if nums_sum%2!=0:
            return False
        memo = {}
        half_sum = nums_sum//2
      


        def dfs(k,total):

            nonlocal memo,half_sum

            if k == len(nums) or total>half_sum:
                return False
            if total == 0:
                return True    
            if (total,k) in memo:
                return memo[(total,k)]    

            left = dfs(k+1,total-nums[k])
            right = dfs(k+1,total)
            memo[(total,k)] = (right or left)

            return (right or left)


        return dfs(0,half_sum)    

                    


#### 1DP solution

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        dp = set()
        dp.add(0)
        if total%2 !=0:
            return False

        for i in range(len(nums)-1,-1,-1):
            nextDP = set()
            for j in dp:
                nextDP.add(j+nums[i])
                nextDP.add(j)
            dp = nextDP   


        return True if total//2 in dp else False 

