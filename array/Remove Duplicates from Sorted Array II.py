
### This solution is intuitive with two pointer techique but rather than 

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        left,right = 0, 0 
        count = 0
        while right<=len(nums)-1:
            if count<2 or nums[left-2]<nums[right]:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right+=1
                count+=1
            else:
                right+=1

        return count



