class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:


        minNum = min(nums)
        indexMin = nums.index(minNum)
        left,right = indexMin-1,indexMin
        swapcount = 0
        while right!=0:
            nums[left],nums[right] = nums[right],nums[left]
            swapcount+=1
            right-=1
            left-=1
        
    
        maxNum = max(nums[::-1])
        indexMax = len(nums)-nums[::-1].index(maxNum)-1

        left,right = indexMax,indexMax+1
        while right!=len(nums):
            nums[left],nums[right] = nums[right],nums[left]
            swapcount+=1
            right+=1
            left+=1
        
        return swapcount
