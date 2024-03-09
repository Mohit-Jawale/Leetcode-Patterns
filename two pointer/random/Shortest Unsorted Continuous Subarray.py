class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        wrong_postion = []

        currmax,currmin = -float('inf'),float('inf')

        for i in range(len(nums)):
            currmax = max(nums[i],currmax)
            if currmax !=nums[i]:
                wrong_postion.append(i)

        for i in reversed(range(len(nums))):
            currmin = min(nums[i],currmin)
            if currmin!=nums[i]:
                wrong_postion.append(i)

        return  max(wrong_postion)-min(wrong_postion)+1 if len(wrong_postion)!=0 else 0

        
