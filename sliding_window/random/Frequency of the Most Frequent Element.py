class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        left,right = 0, 0
        windowSum = 0
        ans = 0

        while right<len(nums):
            windowSum+=nums[right]

            while (nums[right]*(right-left+1)-windowSum)>k:
                windowSum-=nums[left]
                left+=1

            ans= max(ans,right-left+1)

            right+=1

        return ans        

