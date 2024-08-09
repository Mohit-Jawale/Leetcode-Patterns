class Solution:
    def minSwaps(self, nums: List[int]) -> int:


        maxWindowOnes = -float('inf')

        left,right = 0,0

        ones,zeros = 0,0

        totalOnes = nums.count(1)
        N = len(nums)

        while right<(2*len(nums)):

            if nums[right%N]==1:
                ones+=1
            elif nums[right%N]==0:
                zeros+=1
            
            while (right-left+1)>totalOnes:
                if nums[left%N]==1:
                    ones-=1
                elif nums[left%N]==0:
                    zeros-=1
                left+=1
            
            maxWindowOnes = max(maxWindowOnes,ones)
            right+=1
        
        return totalOnes - maxWindowOnes



        
